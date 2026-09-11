#!/usr/bin/env python3
"""
Pruebas automatizadas del validador de Cadena de Valor Virtual (validate_virtual_value_chain.py).
"""

import os
import subprocess
import sys
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR_SCRIPT = SKILL_ROOT / "scripts" / "validate_organization_analysis.py"
EXAMPLE_FILE = SKILL_ROOT / "examples" / "bio_trace_cadena_virtual.md"

sys.path.insert(0, str(SKILL_ROOT / "scripts"))
from validate_organization_analysis import validate_content


class TestValidateOrganizationAnalysis(unittest.TestCase):
    def setUp(self):
        self.assertTrue(EXAMPLE_FILE.exists(), f"El archivo de ejemplo {EXAMPLE_FILE} debe existir.")
        self.example_content = EXAMPLE_FILE.read_text(encoding="utf-8")

    def test_valid_example(self):
        """Verifica que el caso de estudio oficial pase todas las validaciones sin errores."""
        res = validate_content(self.example_content, filename=str(EXAMPLE_FILE))
        self.assertTrue(res["valid"], f"Se esperaba válido pero falló con: {res['errors']}")
        self.assertEqual(len(res["errors"]), 0)
        self.assertEqual(len(res["metrics"]["stages_found"]), 5)
        self.assertTrue(res["metrics"]["has_cross_matrix"])
        self.assertTrue(res["metrics"]["has_sdl_analysis"])
        self.assertTrue(res["metrics"]["has_bottleneck"])

    def test_missing_stage(self):
        """Verifica que omitir una de las 5 etapas canónicas genere un error crítico."""
        # Remover la fila de Sintetizar
        tampered = "\n".join(
            line for line in self.example_content.splitlines()
            if not ("Sintetizar" in line or "Synthesize" in line)
        )
        res = validate_content(tampered, filename="tampered.md")
        self.assertFalse(res["valid"])
        self.assertTrue(any("sintetizar" in err.lower() for err in res["errors"]))

    def test_invalid_maturity_phase(self):
        """Verifica que una fase de madurez no reconocida genere un error."""
        tampered = self.example_content.replace("Fase 1: Visibilidad", "Fase 99: Fase Desconocida")
        res = validate_content(tampered, filename="invalid_phase.md")
        self.assertFalse(res["valid"])
        self.assertTrue(any("fase de madurez inválida" in err.lower() for err in res["errors"]))

    def test_missing_required_section(self):
        """Verifica que omitir una sección requerida (ej. Sección 3) invalide el entregable."""
        tampered = self.example_content.replace(
            "## 3. Diagnóstico de Madurez y Evolución Digital",
            "## 3. Notas Varias del Proceso"
        )
        res = validate_content(tampered, filename="missing_section.md")
        self.assertFalse(res["valid"])
        self.assertTrue(any("sección obligatoria 3" in err.lower() for err in res["errors"]))

    def test_empty_data_fields(self):
        """Verifica que celdas de datos vacías en la matriz canónica sean rechazadas."""
        # Remplazar atributos técnicos por vacío
        tampered = self.example_content.replace(
            "`id_lote`, `temp_celsius`, `timestamp_utc`, `gps_lat_long`, `id_vehiculo`, `id_chofer`, `firma_digital_base64`",
            "   "
        )
        res = validate_content(tampered, filename="empty_data.md")
        self.assertFalse(res["valid"])
        self.assertTrue(any("datos clave involucrados" in err.lower() for err in res["errors"]))

    def test_cli_invocation(self):
        """Verifica la ejecución por línea de comandos vía subproceso."""
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "utf-8"
        cmd = [sys.executable, str(VALIDATOR_SCRIPT), str(EXAMPLE_FILE), "--json"]
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=env)
        self.assertEqual(proc.returncode, 0, f"Error en CLI: {proc.stderr}")
        self.assertIn('"valid": true', proc.stdout)


if __name__ == "__main__":
    unittest.main()
