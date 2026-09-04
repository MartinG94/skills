import json
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from bpmn_ir_transformer import (
    BPMNMermaidGenerator,
    BPMNProcessTransformer,
    BPMNValidationError,
    BPMNValidator,
    BPMNXMLGenerator,
)


ROOT = Path(__file__).resolve().parents[1]


class BPMNIRTests(unittest.TestCase):
    def setUp(self):
        self.validator = BPMNValidator()

    def test_example_is_valid_and_xml_is_non_executable(self):
        data = json.loads(
            (ROOT / "templates" / "bpmn_process_ir_example.json").read_text(
                encoding="utf-8"
            )
        )
        process_source = self.validator.validate_document(data)
        graph = BPMNProcessTransformer().transform(process_source)
        self.validator.validate_flat_graph(graph, process_id=data["id"])
        xml = BPMNXMLGenerator().generate_xml(
            graph, process_id=data["id"], process_name=data["name"]
        )
        root = ET.fromstring(xml)
        namespace = {"bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL"}
        process = root.find("bpmn:process", namespace)
        self.assertIsNotNone(process)
        self.assertEqual(process.attrib["isExecutable"], "false")
        self.assertEqual(process.attrib["id"], data["id"])
        self.assertEqual(process.attrib["name"], data["name"])

    def test_duplicate_id_across_branches_is_rejected(self):
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "exclusiveGateway",
                "id": "gw",
                "has_join": False,
                "branches": [
                    {
                        "condition": "A",
                        "path": [{"type": "task", "id": "same", "label": "Uno"}],
                    },
                    {
                        "condition": "B",
                        "path": [{"type": "task", "id": "same", "label": "Dos"}],
                    },
                ],
            },
            {"type": "endEvent", "id": "end", "label": "Fin"},
        ]
        with self.assertRaisesRegex(BPMNValidationError, "Duplicate element ID"):
            self.validator.validate(process)

    def test_unknown_branch_target_is_rejected(self):
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "exclusiveGateway",
                "id": "gw",
                "has_join": False,
                "branches": [
                    {"condition": "A", "path": [], "next": "missing"},
                    {"condition": "B", "path": []},
                ],
            },
            {"type": "endEvent", "id": "end", "label": "Fin"},
        ]
        with self.assertRaisesRegex(BPMNValidationError, "unknown IDs"):
            self.validator.validate(process)

    def test_end_inside_parallel_branch_is_rejected(self):
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "parallelGateway",
                "id": "fork",
                "branches": [
                    [{"type": "task", "id": "a", "label": "A"}],
                    [{"type": "endEvent", "id": "early_end", "label": "Fin"}],
                ],
            },
            {"type": "endEvent", "id": "end", "label": "Fin general"},
        ]
        with self.assertRaisesRegex(BPMNValidationError, "Parallel branch contains"):
            self.validator.validate(process)

    def test_distinct_conditions_to_same_target_are_preserved(self):
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "exclusiveGateway",
                "id": "gw",
                "has_join": False,
                "branches": [
                    {"condition": "A", "path": []},
                    {"condition": "B", "path": []},
                ],
            },
            {"type": "endEvent", "id": "end", "label": "Fin"},
        ]
        self.validator.validate(process)
        graph = BPMNProcessTransformer().transform(process)
        flows = [flow for flow in graph["flows"] if flow["sourceRef"] == "gw"]
        self.assertEqual([flow["condition"] for flow in flows], ["A", "B"])
        self.assertEqual(len({flow["id"] for flow in flows}), 2)
        self.validator.validate_flat_graph(graph)

    def test_empty_join_branch_reaches_the_join(self):
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "exclusiveGateway",
                "id": "gw",
                "has_join": True,
                "branches": [
                    {"condition": "A", "path": []},
                    {
                        "condition": "B",
                        "path": [{"type": "task", "id": "work", "label": "Trabajar"}],
                    },
                ],
            },
            {"type": "endEvent", "id": "end", "label": "Fin"},
        ]
        self.validator.validate(process)
        graph = BPMNProcessTransformer().transform(process)
        edges = {(flow["sourceRef"], flow["targetRef"]) for flow in graph["flows"]}
        self.assertIn(("gw", "gw_join"), edges)
        self.assertNotIn(("gw", "end"), edges)
        self.validator.validate_flat_graph(graph)

    def test_nested_gateway_in_parallel_has_no_outer_join_bypass(self):
        nested = {
            "type": "exclusiveGateway",
            "id": "choice",
            "has_join": True,
            "branches": [
                {"condition": "A", "path": []},
                {"condition": "B", "path": []},
            ],
        }
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "parallelGateway",
                "id": "fork",
                "branches": [
                    [nested],
                    [{"type": "task", "id": "other", "label": "Otra tarea"}],
                ],
            },
            {"type": "endEvent", "id": "end", "label": "Fin"},
        ]
        self.validator.validate(process)
        graph = BPMNProcessTransformer().transform(process)
        choice_targets = {
            flow["targetRef"] for flow in graph["flows"] if flow["sourceRef"] == "choice"
        }
        self.assertEqual(choice_targets, {"choice_join"})
        self.assertIn(
            ("choice_join", "fork_join"),
            {(flow["sourceRef"], flow["targetRef"]) for flow in graph["flows"]},
        )
        self.validator.validate_flat_graph(graph)

    def test_nested_gateway_in_parallel_cannot_escape_with_next(self):
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "parallelGateway",
                "id": "fork",
                "branches": [
                    [
                        {
                            "type": "exclusiveGateway",
                            "id": "choice",
                            "has_join": False,
                            "branches": [
                                {"condition": "A", "path": [], "next": "finish"},
                                {"condition": "B", "path": []},
                            ],
                        }
                    ],
                    [{"type": "task", "id": "work", "label": "Trabajar"}],
                ],
            },
            {"type": "endEvent", "id": "finish", "label": "Fin"},
        ]
        with self.assertRaisesRegex(BPMNValidationError, "inside a parallel branch"):
            self.validator.validate(process)

    def test_runtime_rejects_schema_type_mismatches(self):
        invalid_models = [
            [
                {"type": "startEvent", "id": "start", "label": "Inicio"},
                {"type": "exclusiveGateway", "id": "gw", "branches": []},
                {"type": "endEvent", "id": "end", "label": "Fin"},
            ],
            [
                {"type": "startEvent", "id": "start", "label": "Inicio"},
                {
                    "type": "inclusiveGateway",
                    "id": "gw",
                    "label": 12,
                    "has_join": False,
                    "branches": [
                        {"condition": "A", "path": []},
                        {"path": [], "is_default": "false"},
                    ],
                },
                {"type": "endEvent", "id": "end", "label": "Fin"},
            ],
            [
                {"type": "startEvent", "id": "start", "label": "Inicio"},
                {"type": ["task"], "id": "bad_type", "label": "Tarea"},
                {"type": "endEvent", "id": "end", "label": "Fin"},
            ],
            [
                {
                    "type": "startEvent",
                    "id": "start",
                    "label": "Inicio",
                    "eventDefinition": ["messageEventDefinition"],
                },
                {"type": "endEvent", "id": "end", "label": "Fin"},
            ],
            [
                {"type": "startEvent", "id": "start", "label": "Inicio"},
                {
                    "type": "exclusiveGateway",
                    "id": "gw",
                    "has_join": False,
                    "branches": [
                        {"condition": "A", "path": [], "next": 0},
                        {"is_default": True, "path": []},
                    ],
                },
                {"type": "endEvent", "id": "end", "label": "Fin"},
            ],
            [
                {"type": "startEvent", "id": "start", "label": "Inicio"},
                {
                    "type": "exclusiveGateway",
                    "id": "gw",
                    "has_join": False,
                    "branches": [
                        {"condition": "A", "path": []},
                        {"condition": 0, "path": [], "is_default": True},
                    ],
                },
                {"type": "endEvent", "id": "end", "label": "Fin"},
            ],
        ]
        for process in invalid_models:
            with self.subTest(process=process):
                with self.assertRaises(BPMNValidationError):
                    self.validator.validate(process)

    def test_exclusive_gateway_supports_one_default_branch(self):
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "exclusiveGateway",
                "id": "choice",
                "has_join": False,
                "branches": [
                    {"condition": "Coincide", "path": []},
                    {"is_default": True, "path": []},
                ],
            },
            {"type": "endEvent", "id": "end", "label": "Fin"},
        ]
        self.validator.validate(process)
        graph = BPMNProcessTransformer().transform(process)
        self.validator.validate_flat_graph(graph)
        gateway = next(item for item in graph["elements"] if item["id"] == "choice")
        default_flow = next(flow for flow in graph["flows"] if flow["id"] == gateway["default_flow"])
        self.assertIsNone(default_flow["condition"])
        mermaid = BPMNMermaidGenerator().generate_mermaid(graph)
        self.assertIn("-->|por defecto| N_end", mermaid)
        xml = BPMNXMLGenerator().generate_xml(graph)
        root = ET.fromstring(xml)
        namespace = {"bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL"}
        xml_gateway = root.find(".//bpmn:exclusiveGateway", namespace)
        self.assertEqual(xml_gateway.attrib["default"], gateway["default_flow"])

    def test_start_event_must_be_first_and_have_no_incoming_flow(self):
        out_of_order = [
            {"type": "task", "id": "before", "label": "Preparar"},
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {"type": "endEvent", "id": "finish", "label": "Fin"},
        ]
        with self.assertRaisesRegex(BPMNValidationError, "must be the first"):
            self.validator.validate(out_of_order)

        loop_to_start = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "exclusiveGateway",
                "id": "choice",
                "has_join": False,
                "branches": [
                    {"condition": "Reintentar", "path": [], "next": "start"},
                    {"condition": "Finalizar", "path": []},
                ],
            },
            {"type": "endEvent", "id": "finish", "label": "Fin"},
        ]
        self.validator.validate(loop_to_start)
        graph = BPMNProcessTransformer().transform(loop_to_start)
        with self.assertRaisesRegex(BPMNValidationError, "cannot have incoming"):
            self.validator.validate_flat_graph(graph)

    def test_timer_definition_is_rejected_on_end_event(self):
        process = [
            {"type": "startEvent", "id": "start", "label": "Inicio"},
            {
                "type": "endEvent",
                "id": "end",
                "label": "Fin",
                "eventDefinition": "timerEventDefinition",
            },
        ]
        with self.assertRaisesRegex(BPMNValidationError, "Unsupported eventDefinition"):
            self.validator.validate(process)

    def test_generated_xml_ids_cannot_collide(self):
        cases = [
            (
                "Process_Main",
                [
                    {"type": "startEvent", "id": "Process_Main", "label": "Inicio"},
                    {"type": "endEvent", "id": "end", "label": "Fin"},
                ],
            ),
            (
                "Process_Main",
                [
                    {
                        "type": "startEvent",
                        "id": "s",
                        "label": "Inicio",
                        "eventDefinition": "timerEventDefinition",
                    },
                    {"type": "task", "id": "timerEventDefinition_s", "label": "Tarea"},
                    {"type": "endEvent", "id": "end", "label": "Fin"},
                ],
            ),
            (
                "Process_Main",
                [
                    {"type": "startEvent", "id": "start", "label": "Inicio", "lane": "Lane_X"},
                    {"type": "task", "id": "Lane_X", "label": "Tarea"},
                    {"type": "endEvent", "id": "end", "label": "Fin"},
                ],
            ),
            (
                "Process_Main",
                [
                    {
                        "type": "startEvent",
                        "id": "start",
                        "label": "Inicio",
                        "lane": "LaneSet_Process_Main",
                    },
                    {"type": "endEvent", "id": "finish", "label": "Fin"},
                ],
            ),
            (
                "Process_Main",
                [
                    {
                        "type": "startEvent",
                        "id": "s",
                        "label": "Inicio",
                        "eventDefinition": "timerEventDefinition",
                        "lane": "timerEventDefinition_s",
                    },
                    {"type": "endEvent", "id": "finish", "label": "Fin"},
                ],
            ),
        ]
        for process_id, process in cases:
            with self.subTest(process=process):
                self.validator.validate(process)
                graph = BPMNProcessTransformer().transform(process)
                with self.assertRaisesRegex(BPMNValidationError, "generated XML namespace"):
                    self.validator.validate_flat_graph(graph, process_id=process_id)

    def test_flow_ids_are_unambiguous_for_underscored_node_ids(self):
        process = [
            {"type": "startEvent", "id": "a_b", "label": "Inicio"},
            {"type": "task", "id": "c", "label": "Uno"},
            {"type": "task", "id": "a", "label": "Dos"},
            {"type": "task", "id": "b_c", "label": "Tres"},
            {"type": "endEvent", "id": "end", "label": "Fin"},
        ]
        self.validator.validate(process)
        graph = BPMNProcessTransformer().transform(process)
        self.assertEqual(len(graph["flows"]), len({flow["id"] for flow in graph["flows"]}))
        self.validator.validate_flat_graph(graph)

    def test_mermaid_preserves_root_identity_defaults_and_event_kind_safely(self):
        data = {
            "id": "Quoted_Process",
            "name": 'Atender "consulta"\r\nen línea',
            "process": [
                {
                    "type": "startEvent",
                    "id": "start",
                    "label": "Consulta recibida",
                    "eventDefinition": "timerEventDefinition",
                },
                {
                    "type": "intermediateCatchEvent",
                    "id": "message_received",
                    "label": "Respuesta recibida",
                    "eventDefinition": "messageEventDefinition",
                },
                {
                    "type": "inclusiveGateway",
                    "id": "choice",
                    "has_join": False,
                    "branches": [
                        {"condition": "Resolver", "path": []},
                        {"is_default": True, "path": []},
                    ],
                },
                {"type": "endEvent", "id": "end", "label": "Consulta cerrada"},
            ],
        }
        process = self.validator.validate_document(data)
        graph = BPMNProcessTransformer().transform(process)
        self.validator.validate_flat_graph(graph, process_id=data["id"])
        mermaid = BPMNMermaidGenerator().generate_mermaid(
            graph, process_id=data["id"], process_name=data["name"]
        )
        self.assertIn('subgraph P_Quoted_Process ["Pool: Atender \'consulta\'  en línea"]', mermaid)
        self.assertIn('N_start(("Consulta recibida (temporizador)"))', mermaid)
        self.assertIn('N_message_received(("Respuesta recibida (mensaje)"))', mermaid)
        self.assertIn("-->|por defecto| N_end", mermaid)
        self.assertNotIn("\r", mermaid)
        self.assertNotIn("\n            end", mermaid)

    def test_cli_emits_each_documented_format(self):
        script = ROOT / "scripts" / "bpmn_ir_transformer.py"
        example = ROOT / "templates" / "bpmn_process_ir_example.json"
        for output_format in ("mermaid", "xml", "both"):
            with self.subTest(output_format=output_format):
                result = subprocess.run(
                    [
                        sys.executable,
                        str(script),
                        str(example),
                        "--format",
                        output_format,
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("[OK]", result.stderr)
                if output_format == "mermaid":
                    self.assertTrue(result.stdout.startswith("flowchart TB"))
                elif output_format == "xml":
                    ET.fromstring(result.stdout)
                else:
                    self.assertIn("```mermaid", result.stdout)
                    self.assertIn("```xml", result.stdout)


if __name__ == "__main__":
    unittest.main()
