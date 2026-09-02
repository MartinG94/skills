# -*- coding: utf-8 -*-
"""
BPMN-IR Transformer CLI & Library
Transforma especificaciones JSON de BPMN-IR a OMG BPMN 2.0 XML y codigo Mermaid.js.
"""

import sys
import os
import json
import argparse
import xml.etree.ElementTree as ET
from typing import Dict, List, Any, Optional, Tuple, Set


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

    def validate(self, process: List[Dict[str, Any]], is_top_level: bool = True) -> Set[str]:
        seen_ids = set()
        start_events = 0

        for element in process:
            elem_id = element.get("id")
            elem_type = element.get("type")

            if not elem_id or not elem_type:
                raise BPMNValidationError(f"Element missing id or type: {element}")

            if elem_id in seen_ids:
                raise BPMNValidationError(f"Duplicate element ID: '{elem_id}'")
            seen_ids.add(elem_id)

            if elem_type in self.SUPPORTED_TASKS:
                if "label" not in element:
                    raise BPMNValidationError(f"Task '{elem_id}' missing required 'label'")

            elif elem_type in self.SUPPORTED_EVENTS:
                if is_top_level and elem_type == "startEvent":
                    start_events += 1

            elif elem_type == "exclusiveGateway":
                if "branches" not in element or not isinstance(element["branches"], list):
                    raise BPMNValidationError(f"Exclusive gateway '{elem_id}' requires 'branches' list")
                if len(element["branches"]) < 2:
                    raise BPMNValidationError(f"Exclusive gateway '{elem_id}' requires at least 2 branches")
                for branch in element["branches"]:
                    if "condition" not in branch or "path" not in branch:
                        raise BPMNValidationError(f"Branch in gateway '{elem_id}' missing 'condition' or 'path'")
                    sub_ids = self.validate(branch["path"], is_top_level=False)
                    seen_ids.update(sub_ids)

            elif elem_type == "inclusiveGateway":
                if "branches" not in element or not isinstance(element["branches"], list):
                    raise BPMNValidationError(f"Inclusive gateway '{elem_id}' requires 'branches' list")
                for branch in element["branches"]:
                    if "path" not in branch:
                        raise BPMNValidationError(f"Branch in inclusive gateway '{elem_id}' missing 'path'")
                    sub_ids = self.validate(branch["path"], is_top_level=False)
                    seen_ids.update(sub_ids)

            elif elem_type == "parallelGateway":
                if "branches" not in element or not isinstance(element["branches"], list):
                    raise BPMNValidationError(f"Parallel gateway '{elem_id}' requires 'branches' list")
                if len(element["branches"]) < 2:
                    raise BPMNValidationError(f"Parallel gateway '{elem_id}' requires at least 2 parallel branches")
                for branch in element["branches"]:
                    if not isinstance(branch, list) or len(branch) == 0:
                        raise BPMNValidationError(f"Parallel gateway '{elem_id}' contains empty branch (AP-08 violation)")
                    sub_ids = self.validate(branch, is_top_level=False)
                    seen_ids.update(sub_ids)
            else:
                raise BPMNValidationError(f"Unknown element type: '{elem_type}' in element '{elem_id}'")

        if is_top_level:
            if start_events != 1:
                raise BPMNValidationError(f"Process must contain exactly 1 top-level startEvent, found {start_events}")
            if not self._check_any_end_event(process):
                raise BPMNValidationError("Process must contain at least one reachable endEvent (AP-06/AP-12 violation)")

        return seen_ids

    def _check_any_end_event(self, elements: List[Dict[str, Any]]) -> bool:
        for elem in elements:
            if elem.get("type") == "endEvent":
                return True
            if elem.get("type") in ("exclusiveGateway", "inclusiveGateway"):
                for b in elem.get("branches", []):
                    if self._check_any_end_event(b.get("path", [])):
                        return True
            if elem.get("type") == "parallelGateway":
                for b in elem.get("branches", []):
                    if self._check_any_end_event(b):
                        return True
        return False


class BPMNProcessTransformer:
    """Transforma el arbol JSON anidado en un grafo plano de flowNodes y sequenceFlows."""

    def transform(self, process: List[Dict[str, Any]], parent_next_id: Optional[str] = None) -> Dict[str, Any]:
        elements: List[Dict[str, Any]] = []
        flows: List[Dict[str, Any]] = []

        def add_flow(source_ref: str, target_ref: str, flow_id: Optional[str] = None, condition: Optional[str] = None):
            for fl in flows:
                if fl["sourceRef"] == source_ref and fl["targetRef"] == target_ref:
                    return
            fid = flow_id or f"flow_{source_ref}_{target_ref}"
            flows.append({
                "id": fid,
                "sourceRef": source_ref,
                "targetRef": target_ref,
                "condition": condition
            })

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
                        "label": f"Join {elem.get('label', '')}",
                        "lane": elem.get("lane", "Lane_Default")
                    })

                for branch in elem.get("branches", []):
                    b_path = branch.get("path", [])
                    b_next = branch.get("next")
                    b_cond = branch.get("condition")

                    if not b_path:
                        target = b_next or next_elem_id
                        if target:
                            add_flow(elem["id"], target, condition=b_cond)
                    else:
                        sub_target = b_next or join_id or next_elem_id
                        sub_res = self.transform(b_path, sub_target)
                        elements.extend(sub_res["elements"])
                        flows.extend(sub_res["flows"])
                        first_b_elem = sub_res["elements"][0]
                        add_flow(elem["id"], first_b_elem["id"], condition=b_cond)

                if join_id and next_elem_id:
                    add_flow(join_id, next_elem_id)

            elif elem_type == "inclusiveGateway":
                join_id = f"{elem['id']}_join" if elem.get("has_join") else None
                if join_id:
                    elements.append({
                        "id": join_id,
                        "type": "inclusiveGateway",
                        "label": f"Join {elem.get('label', '')}",
                        "lane": elem.get("lane", "Lane_Default")
                    })

                for branch in elem.get("branches", []):
                    b_path = branch.get("path", [])
                    b_next = branch.get("next")
                    b_cond = branch.get("condition")
                    is_def = branch.get("is_default", False)

                    if not b_path:
                        target = b_next or next_elem_id
                        if target:
                            fid = f"flow_{elem['id']}_{target}"
                            add_flow(elem["id"], target, flow_id=fid, condition=b_cond)
                            if is_def:
                                transformed["default_flow"] = fid
                    else:
                        sub_target = b_next or join_id or next_elem_id
                        sub_res = self.transform(b_path, sub_target)
                        elements.extend(sub_res["elements"])
                        flows.extend(sub_res["flows"])
                        first_b_elem = sub_res["elements"][0]
                        fid = f"flow_{elem['id']}_{first_b_elem['id']}"
                        add_flow(elem["id"], first_b_elem["id"], flow_id=fid, condition=b_cond)
                        if is_def:
                            transformed["default_flow"] = fid

                if join_id and next_elem_id:
                    add_flow(join_id, next_elem_id)

            elif elem_type == "parallelGateway":
                join_id = f"{elem['id']}_join"
                elements.append({
                    "id": join_id,
                    "type": "parallelGateway",
                    "label": "Join Sincronizacion",
                    "lane": elem.get("lane", "Lane_Default")
                })

                for branch in elem.get("branches", []):
                    sub_res = self.transform(branch, join_id)
                    elements.extend(sub_res["elements"])
                    flows.extend(sub_res["flows"])
                    first_b_elem = sub_res["elements"][0]
                    last_b_elem = sub_res["elements"][-1]
                    add_flow(elem["id"], first_b_elem["id"])
                    add_flow(last_b_elem["id"], join_id)

                if next_elem_id:
                    add_flow(join_id, next_elem_id)

            elif elem_type != "endEvent" and next_elem_id:
                add_flow(elem["id"], next_elem_id)

        unique_elements = []
        seen = set()
        for el in elements:
            if el["id"] not in seen:
                seen.add(el["id"])
                unique_elements.append(el)

        return {"elements": unique_elements, "flows": flows}


class BPMNXMLGenerator:
    """Genera documento XML compatible con estandar OMG BPMN 2.0."""

    def generate_xml(self, transformed_data: Dict[str, Any], process_id: str = "Process_Main", process_name: str = "Proceso de Negocio") -> str:
        root = ET.Element("bpmn:definitions")
        root.set("xmlns:bpmn", "http://www.omg.org/spec/BPMN/20100524/MODEL")
        root.set("xmlns:bpmndi", "http://www.omg.org/spec/BPMN/20100524/DI")
        root.set("xmlns:dc", "http://www.omg.org/spec/DD/20100524/DC")
        root.set("xmlns:di", "http://www.omg.org/spec/DD/20100524/DI")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("id", f"Definitions_{process_id}")
        root.set("targetNamespace", "http://bpmn.io/schema/bpmn")
        root.set("exporter", "Antigravity BPMN-IR Engine")
        root.set("exporterVersion", "2.1")

        # Collaboration
        collab = ET.SubElement(root, "bpmn:collaboration")
        collab.set("id", f"Collab_{process_id}")
        participant = ET.SubElement(collab, "bpmn:participant")
        participant.set("id", f"Participant_{process_id}")
        participant.set("name", process_name)
        participant.set("processRef", process_id)

        # Process
        proc = ET.SubElement(root, "bpmn:process")
        proc.set("id", process_id)
        proc.set("name", process_name)
        proc.set("isExecutable", "true")

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
                sf.set("name", fl["condition"])

        ET.indent(root, space="  ", level=0)
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode")


class BPMNMermaidGenerator:
    """Genera representacion Mermaid.js limpia con agrupacion por Lanes y estilos."""

    def generate_mermaid(self, transformed_data: Dict[str, Any], process_name: str = "Proceso Principal") -> str:
        lines = ["flowchart TB"]
        lines.append(f'    subgraph Pool_Main ["Pool: {process_name}"]')

        lanes = {}
        for elem in transformed_data["elements"]:
            lname = elem.get("lane", "Lane_Default")
            if lname not in lanes:
                lanes[lname] = []
            lanes[lname].append(elem)

        for lane_name, elems in lanes.items():
            clean_lane_label = lane_name.replace("Lane_", "").replace("_", " ")
            lines.append(f'        subgraph {lane_name} ["Lane: {clean_lane_label}"]')
            for elem in elems:
                eid = elem["id"]
                etype = elem["type"]
                label = elem.get("label", eid).replace('"', "'")

                if etype == "startEvent":
                    lines.append(f'            {eid}(("Inicio: {label}"))')
                elif etype == "endEvent":
                    lines.append(f'            {eid}((("Fin: {label}")))')
                elif etype in ("exclusiveGateway", "inclusiveGateway"):
                    lines.append(f'            {eid}{{"{label}?"}}')
                elif etype == "parallelGateway":
                    lines.append(f'            {eid}{{"(+) {label}"}}')
                elif etype == "intermediateCatchEvent":
                    lines.append(f'            {eid}(("Espera: {label}"))')
                elif etype == "intermediateThrowEvent":
                    lines.append(f'            {eid}(("Emite: {label}"))')
                else:
                    lines.append(f'            {eid}["{label}"]')
            lines.append("        end\n")

        lines.append("    end\n")

        lines.append("    %% Flujos de Secuencia Internos")
        for fl in transformed_data["flows"]:
            s = fl["sourceRef"]
            t = fl["targetRef"]
            cond = fl.get("condition")
            if cond:
                lines.append(f"    {s} -->|{cond}| {t}")
            else:
                lines.append(f"    {s} --> {t}")

        lines.append("\n    %% Estilos de Nodos")
        lines.append("    classDef startEvent fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#155724;")
        lines.append("    classDef endEvent fill:#f8d7da,stroke:#dc3545,stroke-width:2px,color:#721c24;")
        lines.append("    classDef gateway fill:#fff3cd,stroke:#ffc107,stroke-width:2px,color:#856404;")
        lines.append("    classDef userTask fill:#e7f3fe,stroke:#0d6efd,stroke-width:1.5px,color:#084298;")
        lines.append("    classDef autoTask fill:#e2e3e5,stroke:#6c757d,stroke-width:1.5px,color:#383d41;")

        start_ids = [e["id"] for e in transformed_data["elements"] if e["type"] == "startEvent"]
        end_ids = [e["id"] for e in transformed_data["elements"] if e["type"] == "endEvent"]
        gw_ids = [e["id"] for e in transformed_data["elements"] if "Gateway" in e["type"]]
        user_ids = [e["id"] for e in transformed_data["elements"] if e["type"] in ("userTask", "manualTask")]
        auto_ids = [e["id"] for e in transformed_data["elements"] if e["type"] in ("serviceTask", "sendTask", "receiveTask", "scriptTask", "businessRuleTask")]

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
    parser = argparse.ArgumentParser(description="Transformador de BPMN-IR a XML BPMN 2.0 y Mermaid.js")
    parser.add_argument("input_file", help="Ruta al archivo JSON de BPMN-IR")
    parser.add_argument("--format", choices=["xml", "mermaid", "both"], default="both", help="Formato de salida")
    parser.add_argument("--output", help="Ruta de archivo para guardar el resultado")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Archivo no encontrado: {args.input_file}", file=sys.stderr)
        sys.exit(1)

    with open(args.input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "process" not in data or not isinstance(data["process"], list):
        print("Error: El JSON debe contener la clave raiz 'process' con una lista de elementos.", file=sys.stderr)
        sys.exit(1)

    validator = BPMNValidator()
    try:
        validator.validate(data["process"])
        print("[OK] Validacion BPMN-IR completada sin errores.", file=sys.stderr)
    except BPMNValidationError as e:
        print(f"[ERROR] Fallo de validacion BPMN-IR: {e}", file=sys.stderr)
        sys.exit(2)

    transformer = BPMNProcessTransformer()
    transformed = transformer.transform(data["process"])

    output_parts = []
    if args.format in ("mermaid", "both"):
        mermaid_gen = BPMNMermaidGenerator()
        m_code = mermaid_gen.generate_mermaid(transformed)
        output_parts.append("```mermaid\n" + m_code + "\n```")

    if args.format in ("xml", "both"):
        xml_gen = BPMNXMLGenerator()
        x_code = xml_gen.generate_xml(transformed)
        output_parts.append("```xml\n" + x_code + "\n```")

    result_text = "\n\n".join(output_parts)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as out_f:
            out_f.write(result_text)
        print(f"[OK] Resultado exportado a: {args.output}", file=sys.stderr)
    else:
        print(result_text)


if __name__ == "__main__":
    main()
