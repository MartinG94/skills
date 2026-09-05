import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from validate_requirements_semantics import validate_semantics


def valid_register():
    return {
        "metadata": {"product": "Portal", "artifact_kind": "registro_requisitos", "version": "1"},
        "sources": [{"id": "SRC-01", "title": "Minuta", "type": "minuta"}],
        "functional_requirements": [
            {
                "id": "RF-01",
                "level": "global",
                "statement": "Consultar estado",
                "origin": "explicito",
                "evidence": [{"source_id": "SRC-01", "locator": "p. 1"}],
                "status": "pendiente_validacion",
            }
        ],
        "non_functional_requirements": [],
        "business_rules": [],
        "assumptions": [],
        "constraints": [],
        "dependencies": [],
        "open_items": [],
        "conflicts": [],
        "coverage_control": {
            "reviewed_source_ids": ["SRC-01"],
            "pending_source_ids": [],
            "derived_pending_ids": [],
            "blocking_tbd_ids": [],
        },
    }


class RequirementsSemanticTests(unittest.TestCase):
    def test_valid_register(self):
        self.assertEqual(validate_semantics(valid_register()), [])

    def test_duplicate_and_unknown_evidence_source(self):
        data = valid_register()
        duplicate = copy.deepcopy(data["functional_requirements"][0])
        duplicate["evidence"][0]["source_id"] = "SRC-99"
        data["functional_requirements"].append(duplicate)
        errors = validate_semantics(data)
        self.assertTrue(any("duplicate id" in error for error in errors))
        self.assertTrue(any("unknown source" in error for error in errors))

    def test_detailed_requirement_requires_existing_global_parent(self):
        data = valid_register()
        data["functional_requirements"].append(
            {
                "id": "RF-01.1",
                "level": "detallado",
                "parent_id": "RF-99",
                "statement": "Ver detalle",
                "origin": "explicito",
                "evidence": [{"source_id": "SRC-01", "locator": "p. 1"}],
                "status": "pendiente_validacion",
            }
        )
        self.assertTrue(any("unknown functional requirement" in e for e in validate_semantics(data)))

    def test_targets_and_coverage_must_resolve(self):
        data = valid_register()
        data["open_items"] = [
            {
                "id": "OPEN-01",
                "target_ids": ["RF-99"],
                "question": "¿Cuál?",
                "blocking": True,
                "status": "abierto",
            }
        ]
        data["coverage_control"]["blocking_tbd_ids"] = ["OPEN-01"]
        errors = validate_semantics(data)
        self.assertTrue(any("unknown artifact" in error for error in errors))

    def test_derived_artifact_must_be_pending_and_listed(self):
        data = valid_register()
        requirement = data["functional_requirements"][0]
        requirement["origin"] = "derivado"
        requirement["derivation"] = "Consecuencia necesaria"
        requirement["evidence"].append({"source_id": "SRC-01", "locator": "p. 2"})
        requirement["status"] = "confirmado"
        errors = validate_semantics(data)
        self.assertTrue(any("must remain pendiente_validacion" in error for error in errors))
        self.assertTrue(any("missing 'RF-01'" in error for error in errors))

    def test_hypothesis_tbd_conflict_and_global_parent_are_guarded(self):
        data = valid_register()
        data["functional_requirements"][0]["parent_id"] = "RF-01"
        data["functional_requirements"][0]["status"] = "TBD"
        data["assumptions"] = [
            {
                "id": "SUP-01",
                "statement": "Se usará un canal",
                "basis": "hipotesis_analista",
                "validation_question": "¿Qué canal?",
                "status": "confirmado",
            }
        ]
        data["conflicts"] = [
            {
                "id": "CONF-01",
                "target_ids": [],
                "statements": [
                    {
                        "statement": "Versión A",
                        "evidence": {"source_id": "SRC-01", "locator": "p. 1"},
                    },
                    {
                        "statement": "Versión B",
                        "evidence": {"source_id": "SRC-01", "locator": "p. 2"},
                    },
                ],
                "decision_question": "¿Cuál versión?",
                "status": "pendiente",
            }
        ]
        errors = validate_semantics(data)
        self.assertTrue(any("global requirement cannot have a parent" in e for e in errors))
        self.assertTrue(any("analyst hypothesis" in e for e in errors))
        self.assertTrue(any("at least one artifact" in e for e in errors))
        self.assertTrue(any("TBD requires" in e for e in errors))

    def test_tbd_with_linked_open_item_is_valid(self):
        data = valid_register()
        data["functional_requirements"][0]["status"] = "TBD"
        data["open_items"] = [
            {
                "id": "OPEN-01",
                "target_ids": ["RF-01"],
                "question": "¿Cuál es el alcance?",
                "blocking": True,
                "status": "abierto",
            }
        ]
        data["coverage_control"]["blocking_tbd_ids"] = ["OPEN-01"]
        self.assertEqual(validate_semantics(data), [])

    def test_derived_detail_with_two_evidence_entries_is_valid(self):
        data = valid_register()
        data["functional_requirements"].append(
            {
                "id": "RF-01.1",
                "level": "detallado",
                "parent_id": "RF-01",
                "statement": "Consultar detalle",
                "origin": "derivado",
                "derivation": "Dos fragmentos obligan a distinguir el detalle",
                "evidence": [
                    {"source_id": "SRC-01", "locator": "p. 1"},
                    {"source_id": "SRC-01", "locator": "p. 2"},
                ],
                "status": "pendiente_validacion",
            }
        )
        data["coverage_control"]["derived_pending_ids"] = ["RF-01.1"]
        self.assertEqual(validate_semantics(data), [])

    def test_derived_artifact_requires_distinct_evidence_locations(self):
        data = valid_register()
        requirement = data["functional_requirements"][0]
        requirement["origin"] = "derivado"
        requirement["derivation"] = "Consecuencia necesaria"
        requirement["evidence"][0]["excerpt"] = "Fragmento A"
        duplicate_location = copy.deepcopy(requirement["evidence"][0])
        duplicate_location["excerpt"] = "Fragmento B"
        requirement["evidence"].append(duplicate_location)
        data["coverage_control"]["derived_pending_ids"] = ["RF-01"]
        errors = validate_semantics(data)
        self.assertTrue(any("distinct evidence locations" in error for error in errors))

    def test_unlisted_blocking_open_item_is_rejected(self):
        data = valid_register()
        data["functional_requirements"][0]["status"] = "TBD"
        data["open_items"] = [
            {
                "id": "OPEN-01",
                "target_ids": ["RF-01"],
                "question": "¿Cuál es el alcance?",
                "blocking": True,
                "status": "abierto",
            }
        ]
        errors = validate_semantics(data)
        self.assertTrue(any("missing 'OPEN-01'" in error for error in errors))

    def test_cli_exit_codes_for_valid_and_invalid_registers(self):
        script = Path(__file__).with_name("validate_requirements_semantics.py")
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "requirements.json"
            fixture.write_text(json.dumps(valid_register()), encoding="utf-8")
            valid = subprocess.run(
                [sys.executable, str(script), str(fixture)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(valid.returncode, 0, valid.stderr)

            invalid_data = valid_register()
            invalid_data["functional_requirements"][0]["status"] = "TBD"
            fixture.write_text(json.dumps(invalid_data), encoding="utf-8")
            invalid = subprocess.run(
                [sys.executable, str(script), str(fixture)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(invalid.returncode, 2, invalid.stderr)
            self.assertIn("TBD requires a linked unresolved open item", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
