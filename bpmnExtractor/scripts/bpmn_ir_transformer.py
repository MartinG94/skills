# -*- coding: utf-8 -*-
"""Valida y renderiza el subconjunto documentado de BPMN-IR.

La salida XML es un modelo BPMN 2.0 no ejecutable y sin BPMNDI. Este modulo no
pretende sustituir un modelador BPMN ni validar conformidad completa con OMG.
"""

import sys
import os
import json
import argparse
import re
import xml.etree.ElementTree as ET
from collections import defaultdict, deque
from typing import Dict, List, Any, Optional, Set


class BPMNValidationError(Exception):
    pass


class BPMNValidator:
    SUPPORTED_TASKS = {
        "task", "userTask", "serviceTask", "sendTask",
        "receiveTask", "businessRuleTask", "manualTask", "scriptTask"
    }
    SUPPORTED_EVENTS = {
        "startEvent", "endEvent", "intermediateThrowEvent", "intermediateCatchEvent"
    }
    SUPPORTED_GATEWAYS = {
        "exclusiveGateway", "inclusiveGateway", "parallelGateway"
    }
    SUPPORTED_EVENT_DEFINITIONS = {
        "timerEventDefinition", "messageEventDefinition"
    }
    EVENT_DEFINITIONS_BY_TYPE = {
        "startEvent": SUPPORTED_EVENT_DEFINITIONS,
        "intermediateCatchEvent": SUPPORTED_EVENT_DEFINITIONS,
        "intermediateThrowEvent": {"messageEventDefinition"},
        "endEvent": {"messageEventDefinition"},
    }

    SAFE_ID = re.compile(r"^[A-Za-z_][A-Za-z0-9_.-]*$")

    def validate_document(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Validate the root contract and nested process, returning the process list."""
        if not isinstance(data, dict):
            raise BPMNValidationError("The BPMN-IR document must be an object")
        extras = set(data) - {"id", "name", "process"}
        if extras:
            raise BPMNValidationError(
                "Unsupported root properties: " + ", ".join(sorted(extras))
            )
        process_id = data.get("id")
        process_name = data.get("name")
        if not isinstance(process_id, str) or not self.SAFE_ID.fullmatch(process_id):
            raise BPMNValidationError("Root 'id' is required and must be a safe identifier")
        if not isinstance(process_name, str) or not process_name.strip():
            raise BPMNValidationError("Root 'name' is required and must be non-empty")
        process = data.get("process")
        self.validate(process)
        return process

    def validate(self, process: List[Dict[str, Any]]) -> Set[str]:
        """Validate the nested source model and return all explicit element IDs."""
        if not isinstance(process, list) or not process:
            raise BPMNValidationError("'process' must be a non-empty list")

        seen_ids: Set[str] = set()
        next_refs: Set[str] = set()
        generated_ids: Set[str] = set()
        start_events = self._validate_elements(
            process, seen_ids, next_refs, generated_ids, top_level=True, in_parallel=False
        )

        if start_events != 1:
            raise BPMNValidationError(
                f"Process must contain exactly 1 top-level startEvent, found {start_events}"
            )

        collisions = generated_ids & seen_ids
        if collisions:
            raise BPMNValidationError(
                "Explicit IDs collide with generated join IDs: " + ", ".join(sorted(collisions))
            )

        missing_refs = next_refs - seen_ids
        if missing_refs:
            raise BPMNValidationError(
                "Branch 'next' references unknown IDs: " + ", ".join(sorted(missing_refs))
            )

        if not any(self._contains_type(process, "endEvent")):
            raise BPMNValidationError("Process must contain at least one endEvent")
        return seen_ids

    def _validate_elements(
        self,
        elements: List[Dict[str, Any]],
        seen_ids: Set[str],
        next_refs: Set[str],
        generated_ids: Set[str],
        *,
        top_level: bool,
        in_parallel: bool,
    ) -> int:
        start_events = 0
        for element_index, element in enumerate(elements):
            if not isinstance(element, dict):
                raise BPMNValidationError(f"Element must be an object: {element!r}")
            elem_id = element.get("id")
            elem_type = element.get("type")
            if not elem_id or not elem_type:
                raise BPMNValidationError(f"Element missing id or type: {element}")
            if not isinstance(elem_id, str) or not self.SAFE_ID.fullmatch(elem_id):
                raise BPMNValidationError(f"Unsafe element ID: '{elem_id}'")
            if not isinstance(elem_type, str):
                raise BPMNValidationError(
                    f"Element type must be a string in '{elem_id}': {elem_type!r}"
                )
            if elem_id in seen_ids:
                raise BPMNValidationError(f"Duplicate element ID: '{elem_id}'")
            seen_ids.add(elem_id)

            lane = element.get("lane")
            if lane is not None and (
                not isinstance(lane, str) or not self.SAFE_ID.fullmatch(lane)
            ):
                raise BPMNValidationError(f"Unsafe lane ID in '{elem_id}': {lane!r}")

            if elem_type in self.SUPPORTED_TASKS:
                self._reject_extra(element, {"type", "id", "label", "lane"}, elem_id)
                self._require_label(element)
                continue

            if elem_type in self.SUPPORTED_EVENTS:
                self._reject_extra(
                    element, {"type", "id", "label", "eventDefinition", "lane"}, elem_id
                )
                self._require_label(element)
                event_definition = element.get("eventDefinition")
                if event_definition is not None and (
                    not isinstance(event_definition, str)
                    or event_definition not in self.EVENT_DEFINITIONS_BY_TYPE[elem_type]
                ):
                    raise BPMNValidationError(
                        f"Unsupported eventDefinition for {elem_type} '{elem_id}': {event_definition!r}"
                    )
                if elem_type == "startEvent":
                    if not top_level:
                        raise BPMNValidationError(
                            f"Nested startEvent '{elem_id}' is outside the supported IR"
                        )
                    if element_index != 0:
                        raise BPMNValidationError(
                            f"Top-level startEvent '{elem_id}' must be the first process element"
                        )
                    start_events += 1
                if in_parallel and elem_type == "endEvent":
                    raise BPMNValidationError(
                        f"Parallel branch contains endEvent '{elem_id}' before its generated join"
                    )
                continue

            if elem_type not in self.SUPPORTED_GATEWAYS:
                raise BPMNValidationError(
                    f"Unknown element type: '{elem_type}' in element '{elem_id}'"
                )

            branches = element.get("branches")
            if not isinstance(branches, list) or len(branches) < 2:
                raise BPMNValidationError(
                    f"Gateway '{elem_id}' requires at least 2 branches"
                )

            if elem_type in ("exclusiveGateway", "inclusiveGateway"):
                self._reject_extra(
                    element,
                    {"type", "id", "label", "has_join", "branches", "lane"},
                    elem_id,
                )
                if "label" in element and not isinstance(element["label"], str):
                    raise BPMNValidationError(f"Gateway '{elem_id}' label must be a string")
                if not isinstance(element.get("has_join"), bool):
                    raise BPMNValidationError(
                        f"Gateway '{elem_id}' requires boolean 'has_join'"
                    )
                if element["has_join"]:
                    generated_ids.add(f"{elem_id}_join")
                defaults = 0
                conditions: Set[str] = set()
                for branch in branches:
                    if not isinstance(branch, dict) or not isinstance(branch.get("path"), list):
                        raise BPMNValidationError(
                            f"Branch in gateway '{elem_id}' requires a list 'path'"
                        )
                    allowed_branch_keys = {"condition", "path", "next", "is_default"}
                    self._reject_extra(branch, allowed_branch_keys, f"{elem_id} branch")
                    if "is_default" in branch and not isinstance(branch["is_default"], bool):
                        raise BPMNValidationError(
                            f"Gateway '{elem_id}' branch 'is_default' must be boolean"
                        )
                    condition = branch.get("condition")
                    is_default = branch.get("is_default", False)
                    if "condition" in branch and (
                        not isinstance(condition, str) or not condition.strip()
                    ):
                        raise BPMNValidationError(
                            f"Gateway '{elem_id}' branch 'condition' must be a non-empty string"
                        )
                    if is_default and condition is not None:
                        raise BPMNValidationError(
                            f"Gateway '{elem_id}' default branch cannot also declare a condition"
                        )
                    if not is_default and (
                        not isinstance(condition, str) or not condition.strip()
                    ):
                        raise BPMNValidationError(
                            f"Gateway '{elem_id}' has a non-default branch without condition"
                        )
                    if condition:
                        normalized = condition.strip().casefold()
                        if normalized in conditions:
                            raise BPMNValidationError(
                                f"Gateway '{elem_id}' repeats condition '{condition}'"
                            )
                        conditions.add(normalized)
                    if is_default:
                        defaults += 1
                    next_id = branch.get("next")
                    if next_id is not None:
                        if not isinstance(next_id, str) or not self.SAFE_ID.fullmatch(next_id):
                            raise BPMNValidationError(
                                f"Invalid branch 'next' in '{elem_id}': {next_id!r}"
                            )
                        if in_parallel:
                            raise BPMNValidationError(
                                f"Gateway '{elem_id}' cannot use branch 'next' inside a parallel branch"
                            )
                        next_refs.add(next_id)
                    start_events += self._validate_elements(
                        branch["path"], seen_ids, next_refs, generated_ids,
                        top_level=False, in_parallel=in_parallel
                    )
                if defaults > 1:
                    raise BPMNValidationError(
                        f"Gateway '{elem_id}' has more than one default branch"
                    )
            else:
                self._reject_extra(
                    element, {"type", "id", "label", "branches", "lane"}, elem_id
                )
                if "label" in element and not isinstance(element["label"], str):
                    raise BPMNValidationError(f"Gateway '{elem_id}' label must be a string")
                generated_ids.add(f"{elem_id}_join")
                for branch in branches:
                    if not isinstance(branch, list) or not branch:
                        raise BPMNValidationError(
                            f"Parallel gateway '{elem_id}' contains an empty branch"
                        )
                    start_events += self._validate_elements(
                        branch, seen_ids, next_refs, generated_ids,
                        top_level=False, in_parallel=True
                    )
        return start_events

    @staticmethod
    def _require_label(element: Dict[str, Any]) -> None:
        if not isinstance(element.get("label"), str) or not element["label"].strip():
            raise BPMNValidationError(
                f"Element '{element.get('id')}' requires a non-empty label"
            )

    @staticmethod
    def _reject_extra(value: Dict[str, Any], allowed: Set[str], context: str) -> None:
        extras = set(value) - allowed
        if extras:
            raise BPMNValidationError(
                f"Unsupported properties in '{context}': {', '.join(sorted(extras))}"
            )

    def _contains_type(self, elements: List[Dict[str, Any]], wanted: str):
        for element in elements:
            yield element.get("type") == wanted
            if element.get("type") in ("exclusiveGateway", "inclusiveGateway"):
                for branch in element.get("branches", []):
                    yield from self._contains_type(branch.get("path", []), wanted)
            elif element.get("type") == "parallelGateway":
                for branch in element.get("branches", []):
                    yield from self._contains_type(branch, wanted)

    def validate_flat_graph(
        self, transformed_data: Dict[str, Any], process_id: str = "Process_Main"
    ) -> None:
        """Validate references and reachability after the tree is flattened."""
        elements = transformed_data.get("elements", [])
        flows = transformed_data.get("flows", [])
        element_ids = [element["id"] for element in elements]
        if len(element_ids) != len(set(element_ids)):
            duplicates = sorted({item for item in element_ids if element_ids.count(item) > 1})
            raise BPMNValidationError(
                "Duplicate flattened element IDs: " + ", ".join(duplicates)
            )

        flow_ids = [flow["id"] for flow in flows]
        if len(flow_ids) != len(set(flow_ids)):
            duplicates = sorted({item for item in flow_ids if flow_ids.count(item) > 1})
            raise BPMNValidationError("Duplicate flow IDs: " + ", ".join(duplicates))

        lane_ids = {element.get("lane", "Lane_Default") for element in elements}
        event_definition_ids = {
            f"{element['eventDefinition']}_{element['id']}"
            for element in elements
            if element.get("eventDefinition")
        }
        structural_ids = [
            process_id,
            f"Definitions_{process_id}",
            f"LaneSet_{process_id}",
        ]
        rendered_ids = (
            element_ids
            + flow_ids
            + list(lane_ids)
            + list(event_definition_ids)
            + structural_ids
        )
        if len(rendered_ids) != len(set(rendered_ids)):
            duplicates = sorted(
                {item for item in rendered_ids if rendered_ids.count(item) > 1}
            )
            raise BPMNValidationError(
                "IDs collide in the generated XML namespace: " + ", ".join(duplicates)
            )

        known = set(element_ids)
        outgoing = defaultdict(set)
        incoming = defaultdict(set)
        for flow in flows:
            source = flow["sourceRef"]
            target = flow["targetRef"]
            if source not in known or target not in known:
                raise BPMNValidationError(
                    f"Flow '{flow['id']}' references unknown nodes: {source} -> {target}"
                )
            outgoing[source].add(target)
            incoming[target].add(source)

        starts = [element["id"] for element in elements if element["type"] == "startEvent"]
        ends = {element["id"] for element in elements if element["type"] == "endEvent"}
        starts_with_incoming = [start for start in starts if incoming.get(start)]
        if starts_with_incoming:
            raise BPMNValidationError(
                "startEvent cannot have incoming sequence flows: "
                + ", ".join(sorted(starts_with_incoming))
            )
        reachable = self._walk(starts, outgoing)
        unreachable = known - reachable
        if unreachable:
            raise BPMNValidationError(
                "Unreachable elements: " + ", ".join(sorted(unreachable))
            )
        reachable_ends = ends & reachable
        if not reachable_ends:
            raise BPMNValidationError("No endEvent is reachable from the startEvent")
        can_reach_end = self._walk(reachable_ends, incoming)
        trapped = reachable - can_reach_end
        if trapped:
            raise BPMNValidationError(
                "Elements without a path to an endEvent: " + ", ".join(sorted(trapped))
            )

    @staticmethod
    def _walk(starts, adjacency):
        visited = set(starts)
        queue = deque(starts)
        while queue:
            current = queue.popleft()
            for target in adjacency.get(current, set()):
                if target not in visited:
                    visited.add(target)
                    queue.append(target)
        return visited


class BPMNProcessTransformer:
    """Transforma el arbol JSON anidado en un grafo plano de flowNodes y sequenceFlows."""

    def transform(self, process: List[Dict[str, Any]], parent_next_id: Optional[str] = None) -> Dict[str, Any]:
        elements: List[Dict[str, Any]] = []
        flows: List[Dict[str, Any]] = []

        def add_flow(source_ref: str, target_ref: str, flow_id: Optional[str] = None, condition: Optional[str] = None):
            base_id = flow_id or (
                f"flow_{len(source_ref)}_{source_ref}_{len(target_ref)}_{target_ref}"
            )
            used_ids = {flow["id"] for flow in flows}
            fid = base_id
            suffix = 2
            while fid in used_ids:
                fid = f"{base_id}_{suffix}"
                suffix += 1
            flows.append({
                "id": fid,
                "sourceRef": source_ref,
                "targetRef": target_ref,
                "condition": condition
            })
            return fid

        for index, elem in enumerate(process):
            next_elem_id = process[index + 1]["id"] if index < len(process) - 1 else parent_next_id

            transformed = {
                "id": elem["id"],
                "type": elem["type"],
                "label": elem.get("label"),
                "lane": elem.get("lane", "Lane_Default"),
                "eventDefinition": elem.get("eventDefinition")
            }
            elements.append(transformed)

            elem_type = elem["type"]

            if elem_type == "exclusiveGateway":
                join_id = f"{elem['id']}_join" if elem.get("has_join") else None
                if join_id:
                    elements.append({
                        "id": join_id,
                        "type": "exclusiveGateway",
                        "label": None,
                        "lane": elem.get("lane", "Lane_Default")
                    })

                for branch in elem.get("branches", []):
                    b_path = branch.get("path", [])
                    b_next = branch.get("next")
                    b_cond = branch.get("condition")
                    is_def = branch.get("is_default", False)

                    if not b_path:
                        target = b_next or join_id or next_elem_id
                        if target:
                            fid = add_flow(elem["id"], target, condition=b_cond)
                            if is_def:
                                transformed["default_flow"] = fid
                    else:
                        sub_target = b_next or join_id or next_elem_id
                        sub_res = self.transform(b_path, sub_target)
                        elements.extend(sub_res["elements"])
                        flows.extend(sub_res["flows"])
                        first_b_elem = sub_res["elements"][0]
                        fid = add_flow(elem["id"], first_b_elem["id"], condition=b_cond)
                        if is_def:
                            transformed["default_flow"] = fid

                if join_id and next_elem_id:
                    add_flow(join_id, next_elem_id)

            elif elem_type == "inclusiveGateway":
                join_id = f"{elem['id']}_join" if elem.get("has_join") else None
                if join_id:
                    elements.append({
                        "id": join_id,
                        "type": "inclusiveGateway",
                        "label": None,
                        "lane": elem.get("lane", "Lane_Default")
                    })

                for branch in elem.get("branches", []):
                    b_path = branch.get("path", [])
                    b_next = branch.get("next")
                    b_cond = branch.get("condition")
                    is_def = branch.get("is_default", False)

                    if not b_path:
                        target = b_next or join_id or next_elem_id
                        if target:
                            fid = add_flow(elem["id"], target, condition=b_cond)
                            if is_def:
                                transformed["default_flow"] = fid
                    else:
                        sub_target = b_next or join_id or next_elem_id
                        sub_res = self.transform(b_path, sub_target)
                        elements.extend(sub_res["elements"])
                        flows.extend(sub_res["flows"])
                        first_b_elem = sub_res["elements"][0]
                        fid = add_flow(elem["id"], first_b_elem["id"], condition=b_cond)
                        if is_def:
                            transformed["default_flow"] = fid

                if join_id and next_elem_id:
                    add_flow(join_id, next_elem_id)

            elif elem_type == "parallelGateway":
                join_id = f"{elem['id']}_join"
                elements.append({
                    "id": join_id,
                    "type": "parallelGateway",
                    "label": None,
                    "lane": elem.get("lane", "Lane_Default")
                })

                for branch in elem.get("branches", []):
                    sub_res = self.transform(branch, join_id)
                    elements.extend(sub_res["elements"])
                    flows.extend(sub_res["flows"])
                    first_b_elem = sub_res["elements"][0]
                    add_flow(elem["id"], first_b_elem["id"])

                if next_elem_id:
                    add_flow(join_id, next_elem_id)

            elif elem_type != "endEvent" and next_elem_id:
                add_flow(elem["id"], next_elem_id)

        # Preserve duplicates so the post-transform validator can report them.
        return {"elements": elements, "flows": flows}


class BPMNXMLGenerator:
    """Generate non-executable BPMN model XML for the supported subset."""

    def generate_xml(self, transformed_data: Dict[str, Any], process_id: str = "Process_Main", process_name: str = "Proceso de Negocio") -> str:
        root = ET.Element("bpmn:definitions")
        root.set("xmlns:bpmn", "http://www.omg.org/spec/BPMN/20100524/MODEL")
        root.set("id", f"Definitions_{process_id}")
        root.set("targetNamespace", "urn:bpmn-extractor:model")
        root.set("exporter", "bpmn-extractor")
        root.set("exporterVersion", "3.0")

        # Process
        proc = ET.SubElement(root, "bpmn:process")
        proc.set("id", process_id)
        proc.set("name", process_name)
        proc.set("isExecutable", "false")
        documentation = ET.SubElement(proc, "bpmn:documentation")
        documentation.text = (
            "Non-executable semantic model. BPMNDI, collaborations, message flows "
            "and engine expressions are outside this generator's supported subset."
        )

        # Segregate lanes
        lanes = {}
        for elem in transformed_data["elements"]:
            lane_name = elem.get("lane", "Lane_Default")
            if lane_name not in lanes:
                lanes[lane_name] = []
            lanes[lane_name].append(elem["id"])

        if len(lanes) > 0:
            lane_set = ET.SubElement(proc, "bpmn:laneSet")
            lane_set.set("id", f"LaneSet_{process_id}")
            for lane_name, elem_ids in lanes.items():
                lane = ET.SubElement(lane_set, "bpmn:lane")
                lane.set("id", lane_name)
                lane.set("name", lane_name.replace("Lane_", "").replace("_", " "))
                for eid in elem_ids:
                    ref = ET.SubElement(lane, "bpmn:flowNodeRef")
                    ref.text = eid

        # Add Flow Nodes
        for elem in transformed_data["elements"]:
            tag = f"bpmn:{elem['type']}"
            node = ET.SubElement(proc, tag)
            node.set("id", elem["id"])
            if elem.get("label"):
                node.set("name", elem["label"])
            if "default_flow" in elem:
                node.set("default", elem["default_flow"])

            for fl in transformed_data["flows"]:
                if fl["targetRef"] == elem["id"]:
                    inc = ET.SubElement(node, "bpmn:incoming")
                    inc.text = fl["id"]
                if fl["sourceRef"] == elem["id"]:
                    out = ET.SubElement(node, "bpmn:outgoing")
                    out.text = fl["id"]

            if elem.get("eventDefinition"):
                ev_tag = f"bpmn:{elem['eventDefinition']}"
                ev_node = ET.SubElement(node, ev_tag)
                ev_node.set("id", f"{elem['eventDefinition']}_{elem['id']}")

        # Add Sequence Flows
        for fl in transformed_data["flows"]:
            sf = ET.SubElement(proc, "bpmn:sequenceFlow")
            sf.set("id", fl["id"])
            sf.set("sourceRef", fl["sourceRef"])
            sf.set("targetRef", fl["targetRef"])
            if fl.get("condition"):
                # Conditions are human-readable labels, not executable expressions.
                sf.set("name", fl["condition"])

        ET.indent(root, space="  ", level=0)
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode")


class BPMNMermaidGenerator:
    """Generate a Mermaid preview; this is not BPMN interchange notation."""

    def generate_mermaid(
        self,
        transformed_data: Dict[str, Any],
        process_id: str = "Process_Main",
        process_name: str = "Proceso Principal",
    ) -> str:
        safe_process_name = (
            process_name.replace('"', "'").replace("\r", " ").replace("\n", " ")
        )
        lines = ["flowchart TB"]
        lines.append(f'    subgraph P_{process_id} ["Pool: {safe_process_name}"]')

        lanes = {}
        for elem in transformed_data["elements"]:
            lname = elem.get("lane", "Lane_Default")
            if lname not in lanes:
                lanes[lname] = []
            lanes[lname].append(elem)

        for lane_name, elems in lanes.items():
            clean_lane_label = lane_name.replace("Lane_", "").replace("_", " ")
            lines.append(f'        subgraph L_{lane_name} ["Lane: {clean_lane_label}"]')
            for elem in elems:
                eid = elem["id"]
                mermaid_eid = f"N_{eid}"
                etype = elem["type"]
                label = (
                    (elem.get("label") or eid)
                    .replace('"', "'")
                    .replace("\r", " ")
                    .replace("\n", " ")
                )
                event_suffix = {
                    "timerEventDefinition": "temporizador",
                    "messageEventDefinition": "mensaje",
                }.get(elem.get("eventDefinition"))
                if event_suffix:
                    label = f"{label} ({event_suffix})"

                if etype == "startEvent":
                    lines.append(f'            {mermaid_eid}(("{label}"))')
                elif etype == "endEvent":
                    lines.append(f'            {mermaid_eid}((("{label}")))')
                elif etype in ("exclusiveGateway", "inclusiveGateway"):
                    symbol = "XOR" if etype == "exclusiveGateway" else "OR"
                    lines.append(f'            {mermaid_eid}{{"{symbol}"}}')
                elif etype == "parallelGateway":
                    lines.append(f'            {mermaid_eid}{{"AND"}}')
                elif etype == "intermediateCatchEvent":
                    lines.append(f'            {mermaid_eid}(("{label}"))')
                elif etype == "intermediateThrowEvent":
                    lines.append(f'            {mermaid_eid}(("{label}"))')
                else:
                    lines.append(f'            {mermaid_eid}["{label}"]')
            lines.append("        end\n")

        lines.append("    end\n")

        lines.append("    %% Flujos de Secuencia Internos")
        default_flows = {
            elem["default_flow"]
            for elem in transformed_data["elements"]
            if elem.get("default_flow")
        }
        for fl in transformed_data["flows"]:
            s = f"N_{fl['sourceRef']}"
            t = f"N_{fl['targetRef']}"
            cond = fl.get("condition")
            if cond:
                safe_condition = (
                    str(cond).replace("|", "/").replace("\r", " ").replace("\n", " ")
                )
                lines.append(f"    {s} -->|{safe_condition}| {t}")
            elif fl["id"] in default_flows:
                lines.append(f"    {s} -->|por defecto| {t}")
            else:
                lines.append(f"    {s} --> {t}")

        lines.append("\n    %% Estilos de Nodos")
        lines.append("    classDef startEvent fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#155724;")
        lines.append("    classDef endEvent fill:#f8d7da,stroke:#dc3545,stroke-width:2px,color:#721c24;")
        lines.append("    classDef gateway fill:#fff3cd,stroke:#ffc107,stroke-width:2px,color:#856404;")
        lines.append("    classDef userTask fill:#e7f3fe,stroke:#0d6efd,stroke-width:1.5px,color:#084298;")
        lines.append("    classDef autoTask fill:#e2e3e5,stroke:#6c757d,stroke-width:1.5px,color:#383d41;")

        start_ids = [f"N_{e['id']}" for e in transformed_data["elements"] if e["type"] == "startEvent"]
        end_ids = [f"N_{e['id']}" for e in transformed_data["elements"] if e["type"] == "endEvent"]
        gw_ids = [f"N_{e['id']}" for e in transformed_data["elements"] if "Gateway" in e["type"]]
        user_ids = [f"N_{e['id']}" for e in transformed_data["elements"] if e["type"] in ("userTask", "manualTask")]
        auto_ids = [f"N_{e['id']}" for e in transformed_data["elements"] if e["type"] in ("serviceTask", "sendTask", "receiveTask", "scriptTask", "businessRuleTask")]

        if start_ids:
            lines.append(f"    class {','.join(start_ids)} startEvent;")
        if end_ids:
            lines.append(f"    class {','.join(end_ids)} endEvent;")
        if gw_ids:
            lines.append(f"    class {','.join(gw_ids)} gateway;")
        if user_ids:
            lines.append(f"    class {','.join(user_ids)} userTask;")
        if auto_ids:
            lines.append(f"    class {','.join(auto_ids)} autoTask;")

        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Validador y renderer del subconjunto BPMN-IR documentado"
    )
    parser.add_argument("input_file", help="Ruta al archivo JSON de BPMN-IR")
    parser.add_argument(
        "--format", choices=["xml", "mermaid", "both"], default="mermaid",
        help="Formato de salida; 'both' solo cuando se necesitan ambos renderings"
    )
    parser.add_argument("--output", help="Ruta de archivo para guardar el resultado")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Archivo no encontrado: {args.input_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[ERROR] No se pudo leer BPMN-IR: {exc}", file=sys.stderr)
        sys.exit(1)

    validator = BPMNValidator()
    try:
        process = validator.validate_document(data)
        print("[OK] Validacion BPMN-IR completada sin errores.", file=sys.stderr)
    except BPMNValidationError as e:
        print(f"[ERROR] Fallo de validacion BPMN-IR: {e}", file=sys.stderr)
        sys.exit(2)

    transformer = BPMNProcessTransformer()
    transformed = transformer.transform(process)
    try:
        validator.validate_flat_graph(transformed, process_id=data["id"])
        print("[OK] Validacion del grafo aplanado completada sin errores.", file=sys.stderr)
    except BPMNValidationError as e:
        print(f"[ERROR] Fallo de validacion del grafo: {e}", file=sys.stderr)
        sys.exit(2)

    mermaid_code = None
    xml_code = None
    if args.format in ("mermaid", "both"):
        mermaid_code = BPMNMermaidGenerator().generate_mermaid(
            transformed, process_id=data["id"], process_name=data["name"]
        )
    if args.format in ("xml", "both"):
        xml_code = BPMNXMLGenerator().generate_xml(
            transformed, process_id=data["id"], process_name=data["name"]
        )

    if args.format == "mermaid":
        result_text = mermaid_code
    elif args.format == "xml":
        result_text = xml_code
    else:
        result_text = (
            "```mermaid\n" + mermaid_code + "\n```\n\n"
            "```xml\n" + xml_code + "\n```"
        )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as out_f:
            out_f.write(result_text)
        print(f"[OK] Resultado exportado a: {args.output}", file=sys.stderr)
    else:
        print(result_text)


if __name__ == "__main__":
    main()
