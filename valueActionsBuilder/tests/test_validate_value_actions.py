#!/usr/bin/env python3
"""
Pruebas automatizadas de unidad e integración para validate_value_actions.py.
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

# Ajustar importación
SCRIPT_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from validate_value_actions import validate_value_actions_file

SAMPLE_VALID_MD = """# Inventario de Acciones de Valor

## 2. Inventario de Acciones de Valor
| ID Acción | Acción Propuesta | Palanca EERR | Cruce CAME | Proceso Primario | Procesos Afectados | Impacto |
|---|---|---|---|---|---|---|
| `AV-01` | Desplegar app móvil | Crear | DO (D1 + O1) | Distribución | Facturación | Trazabilidad |
| `AV-02` | Eliminar papel | Eliminar | DO (D2 + O1) | Despacho | Archivo | Sin costos de papel |
| `AV-03` | Reducir esperas | Reducir | DO (D3 + O2) | Recepción | Almacén | Menor tiempo ciclo |
| `AV-04` | Incrementar stock real | Incrementar | FO (F1 + O2) | Inventario | Ventas | Mayor exactitud |

## 3. Matriz del Filtro de Restricciones Operativas
| ID Acción | Plazos y Tiempos | Costos y Presupuesto | Dependencia TI | Resistencia al Cambio | Dictamen | Mitigación Requerida |
|---|---|---|---|---|---|---|
| `AV-01` | 8 semanas | Medio | Estándar API | Media | APROBADA CON MITIGACIÓN | Talleres presenciales de capacitación |
| `AV-02` | Inmediato | Bajo | No requiere | Baja | APROBADA | N/A |
| `AV-03` | 3 semanas | Bajo | Parámetros ERP | Baja | APROBADA | N/A |
| `AV-04` | 6 semanas | Medio | Conector base | Baja | APROBADA | N/A |
"""

SAMPLE_INVALID_EERR_MD = """# Inventario
| ID Acción | Acción | Palanca EERR | Cruce CAME | Proceso Primario | Procesos Afectados |
|---|---|---|---|---|---|
| `AV-01` | Desplegar portal | Inventar | DO (D1 + O1) | Ventas | TI |

| ID Acción | Plazos | Costos | Dependencia TI | Resistencia | Dictamen | Mitigación |
|---|---|---|---|---|---|---|
| `AV-01` | 4 semanas | Bajo | Factible | Baja | APROBADA | N/A |
"""

SAMPLE_MISSING_MITIGATION_MD = """# Inventario
| ID Acción | Acción | Palanca EERR | Cruce CAME | Proceso Primario | Procesos Afectados |
|---|---|---|---|---|---|
| `AV-01` | Desplegar portal | Crear | DO (D1 + O1) | Ventas | TI |

| ID Acción | Plazos | Costos | Dependencia TI | Resistencia | Dictamen | Mitigación |
|---|---|---|---|---|---|---|
| `AV-01` | 4 semanas | Bajo | Factible | Alta | APROBADA CON MITIGACIÓN | N/A |
"""

SAMPLE_MISSING_CONSTRAINT_MD = """# Inventario
| ID Acción | Acción | Palanca EERR | Cruce CAME | Proceso Primario | Procesos Afectados |
|---|---|---|---|---|---|
| `AV-01` | Desplegar portal | Crear | DO (D1 + O1) | Ventas | TI |

| ID Acción | Plazos | Costos | Dictamen | Mitigación |
|---|---|---|---|---|
| `AV-01` | 4 semanas | Bajo | APROBADA | N/A |
"""

class TestValueActionsValidator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = Path(__file__).resolve().parent / "temp_test_files"
        self.temp_dir.mkdir(exist_ok=True)

    def tearDown(self):
        for f in self.temp_dir.glob("*"):
            try:
                f.unlink()
            except Exception:
                pass
        try:
            self.temp_dir.rmdir()
        except Exception:
            pass

    def test_canonical_template(self):
        template_path = Path(__file__).resolve().parent.parent / "templates" / "value_actions_template.md"
        result = validate_value_actions_file(template_path)
        self.assertTrue(result["valid"], f"Template canonical failed: {result['errors']}")
        self.assertEqual(result["actions_found"], 4)
        self.assertEqual(len(result["errors"]), 0)

    def test_valid_custom_content(self):
        test_file = self.temp_dir / "valid.md"
        test_file.write_text(SAMPLE_VALID_MD, encoding="utf-8")
        result = validate_value_actions_file(test_file)
        self.assertTrue(result["valid"], f"Valid content failed: {result['errors']}")
        self.assertEqual(result["actions_found"], 4)
        self.assertEqual(result["eerr_breakdown"]["crear"], 1)
        self.assertEqual(result["eerr_breakdown"]["eliminar"], 1)
        self.assertEqual(result["eerr_breakdown"]["reducir"], 1)
        self.assertEqual(result["eerr_breakdown"]["incrementar"], 1)
        self.assertIn("AV-01", result["mitigated_actions"])

    def test_invalid_eerr_lever(self):
        test_file = self.temp_dir / "invalid_eerr.md"
        test_file.write_text(SAMPLE_INVALID_EERR_MD, encoding="utf-8")
        result = validate_value_actions_file(test_file)
        self.assertFalse(result["valid"])
        self.assertTrue(any("Palanca EERR inválida" in err for err in result["errors"]))

    def test_missing_mitigation_error(self):
        test_file = self.temp_dir / "missing_mitigation.md"
        test_file.write_text(SAMPLE_MISSING_MITIGATION_MD, encoding="utf-8")
        result = validate_value_actions_file(test_file)
        self.assertFalse(result["valid"])
        self.assertTrue(any("no define una medida de mitigación concreta" in err for err in result["errors"]))

    def test_missing_mandatory_constraints(self):
        test_file = self.temp_dir / "missing_constraint.md"
        test_file.write_text(SAMPLE_MISSING_CONSTRAINT_MD, encoding="utf-8")
        result = validate_value_actions_file(test_file)
        self.assertFalse(result["valid"])
        self.assertTrue(any("carece de columnas obligatorias" in err for err in result["errors"]))

    def test_missing_came_trace(self):
        sample_missing_came = """# Inventario
| ID Acción | Acción | Palanca EERR | Cruce CAME | Proceso Primario | Procesos Afectados |
|---|---|---|---|---|---|
| `AV-01` | Desplegar portal | Crear | Sin Cruce | Ventas | TI |

| ID Acción | Plazos | Costos | Dependencia TI | Resistencia | Dictamen | Mitigación |
|---|---|---|---|---|---|---|
| `AV-01` | 4 semanas | Bajo | Factible | Baja | APROBADA | N/A |
"""
        test_file = self.temp_dir / "missing_came.md"
        test_file.write_text(sample_missing_came, encoding="utf-8")
        result = validate_value_actions_file(test_file)
        self.assertFalse(result["valid"])
        self.assertTrue(any("No especifica un cruce CAME válido" in err for err in result["errors"]))

    def test_id_mismatch_eerr_and_filter(self):
        sample_mismatch = """# Inventario
| ID Acción | Acción | Palanca EERR | Cruce CAME | Proceso Primario | Procesos Afectados |
|---|---|---|---|---|---|
| `AV-01` | Desplegar portal | Crear | DO (D1 + O1) | Ventas | TI |
| `AV-02` | Eliminar formularios | Eliminar | DO (D2 + O1) | Ventas | TI |

| ID Acción | Plazos | Costos | Dependencia TI | Resistencia | Dictamen | Mitigación |
|---|---|---|---|---|---|---|
| `AV-01` | 4 semanas | Bajo | Factible | Baja | APROBADA | N/A |
"""
        test_file = self.temp_dir / "mismatch.md"
        test_file.write_text(sample_mismatch, encoding="utf-8")
        result = validate_value_actions_file(test_file)
        self.assertFalse(result["valid"])
        self.assertTrue(any("Acciones en tabla EERR ausentes en el Filtro de Restricciones: AV-02" in err for err in result["errors"]))

    def test_empty_and_nonexistent_file(self):
        empty_file = self.temp_dir / "empty.md"
        empty_file.write_text("", encoding="utf-8")
        res_empty = validate_value_actions_file(empty_file)
        self.assertFalse(res_empty["valid"])
        self.assertTrue(any("está vacío" in err for err in res_empty["errors"]))

        non_existent = self.temp_dir / "does_not_exist.md"
        res_none = validate_value_actions_file(non_existent)
        self.assertFalse(res_none["valid"])
        self.assertTrue(any("no existe" in err for err in res_none["errors"]))

    def test_canonical_deliverable(self):
        deliverable_path = Path(__file__).resolve().parent.parent / "acciones_valor.md"
        result = validate_value_actions_file(deliverable_path)
        self.assertTrue(result["valid"], f"Deliverable validation failed: {result['errors']}")
        self.assertEqual(result["actions_found"], 4)
        self.assertEqual(result["eerr_breakdown"]["crear"], 1)
        self.assertEqual(result["eerr_breakdown"]["eliminar"], 1)
        self.assertEqual(result["eerr_breakdown"]["reducir"], 1)
        self.assertEqual(result["eerr_breakdown"]["incrementar"], 1)
        self.assertEqual(len(result["errors"]), 0)

    def test_cli_execution_and_json(self):
        template_path = Path(__file__).resolve().parent.parent / "templates" / "value_actions_template.md"
        script_path = SCRIPT_DIR / "validate_value_actions.py"
        cmd = [sys.executable, str(script_path), str(template_path), "--json"]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0)
        data = json.loads(proc.stdout)
        self.assertTrue(data["valid"])
        self.assertEqual(data["actions_found"], 4)

if __name__ == "__main__":
    unittest.main()


