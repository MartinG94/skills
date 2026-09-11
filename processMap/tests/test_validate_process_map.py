#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para validate_process_map.py (processMap skill).
"""

import os
import sys
import tempfile
import unittest
import subprocess
import json
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from validate_process_map import validate_process_map_file

EXAMPLE_PATH = SKILL_ROOT / "examples" / "mapa_procesos_ejemplo.md"

class TestProcessMapValidator(unittest.TestCase):

    def test_canonical_example_is_valid(self):
        """Verifica que el ejemplo canónico de cátedra supere todas las validaciones."""
        self.assertTrue(EXAMPLE_PATH.exists(), f"No se encontró el ejemplo en {EXAMPLE_PATH}")
        res = validate_process_map_file(str(EXAMPLE_PATH))
        self.assertTrue(res["valid"], f"El ejemplo falló la validación: {res['errors']}")
        self.assertEqual(res["stats"]["sections_found"], 5)
        self.assertTrue(res["stats"]["has_mermaid_diagram"])
        self.assertGreaterEqual(res["stats"]["strategic_processes_count"], 2)
        self.assertGreaterEqual(res["stats"]["operational_processes_count"], 2)
        self.assertGreaterEqual(res["stats"]["support_processes_count"], 2)
        self.assertTrue(res["stats"]["customer_requirements_detected"])
        self.assertTrue(res["stats"]["customer_satisfaction_detected"])

    def test_nonexistent_file(self):
        """Verifica el manejo de archivos inexistentes."""
        res = validate_process_map_file("ruta/inexistente/mapa_procesos.md")
        self.assertFalse(res["valid"])
        self.assertTrue(any("no existe" in err for err in res["errors"]))

    def test_missing_sections(self):
        """Verifica error si faltan secciones canónicas obligatorias."""
        incomplete_content = """# Mapa de Procesos
## 1. Identificación y Encuadre Institucional
Organización ABC.
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(incomplete_content)
            temp_path = f.name

        try:
            res = validate_process_map_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertLess(res["stats"]["sections_found"], 5)
            self.assertTrue(any("Sección obligatoria" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_missing_mermaid_diagram(self):
        """Verifica error si falta el bloque de diagrama Mermaid."""
        content_no_mermaid = """# Mapa de Procesos
## 1. Identificación y Encuadre Institucional
Datos de la organización.
## 2. Diagrama Visual del Mapa de Procesos
Texto descriptivo sin bloque mermaid.
## 3. Inventario Estructurado de Procesos
| ID | Nombre |
|---|---|
| PE-01 | Estratégico 1 |
| PE-02 | Estratégico 2 |
| PO-01 | Operativo 1 |
| PO-02 | Operativo 2 |
| PS-01 | Soporte 1 |
| PS-02 | Soporte 2 |
## 4. Matriz de Relaciones Sistémicas
Relaciones descritas.
## 5. Insumos para la Selección del Proceso Crítico
Candidatos identificados.
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(content_no_mermaid)
            temp_path = f.name

        try:
            res = validate_process_map_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertTrue(any("Mermaid" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_insufficient_process_categories(self):
        """Verifica error si falta alguna de las 3 categorías canónicas (PE, PO, PS)."""
        content_only_pe = """# Mapa de Procesos
## 1. Identificación y Encuadre Institucional
Datos.
## 2. Diagrama Visual del Mapa de Procesos
```mermaid
flowchart LR
    REQ --> PE01 --> SAT
```
## 3. Inventario Estructurado de Procesos
| ID | Nombre |
|---|---|
| PE-01 | Estratégico 1 |
| PE-02 | Estratégico 2 |
## 4. Matriz de Relaciones Sistémicas
Tabla.
## 5. Insumos para la Selección del Proceso Crítico
Candidatos.
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(content_only_pe)
            temp_path = f.name

        try:
            res = validate_process_map_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertTrue(any("PO-XX" in err for err in res["errors"]))
            self.assertTrue(any("PS-XX" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_cli_execution_json(self):
        """Verifica la ejecución por línea de comandos y emisión de JSON válido."""
        script_path = SKILL_ROOT / "scripts" / "validate_process_map.py"
        cmd = [sys.executable, str(script_path), str(EXAMPLE_PATH), "--json"]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0)
        data = json.loads(proc.stdout)
        self.assertTrue(data["valid"])
        self.assertEqual(data["stats"]["sections_found"], 5)

if __name__ == "__main__":
    unittest.main()
