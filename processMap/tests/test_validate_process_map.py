#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias completas para validate_process_map.py (processMap skill v2.0).
Valida la arquitectura de 3 niveles, el diagrama Mermaid, la matriz multicriterio de los 5 factores y la selección del proceso crítico con su justificación.
"""

import os
import sys
import tempfile
import unittest
import json
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from validate_process_map import validate_process_map_file, extract_weights

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
        self.assertEqual(res["stats"]["critical_process_selected"], "PO-02")
        self.assertTrue(res["stats"]["critical_process_justified"])
        self.assertGreaterEqual(res["stats"]["evaluated_candidates_count"], 2)

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
| PO-01 | Operativo 1 |
| PS-01 | Soporte 1 |
## 4. Matriz Multicriterio de Selección Ponderada
| ID | Proceso | C1 | C2 | C3 | C4 | C5 | Sp | Rank |
|---|---|---|---|---|---|---|---|---|
| PO-01 | Proceso 1 | 4 | 4 | 4 | 4 | 4 | 4.00 | #1 |
| PO-02 | Proceso 2 | 3 | 3 | 3 | 3 | 3 | 3.00 | #2 |
## 5. Proceso Crítico Seleccionado y Justificación
PO-01 seleccionado. Justificación amplia con más de ochenta palabras detallando las causas raíz, problemas operativos, reclamos continuos de clientes y alineación con la estrategia institucional y metas SMART aprobadas por la gerencia general de la empresa.
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
flowchart TD
    subgraph ESTRATEGICOS
        PE01[PE-01: Direccion]
    end
```
## 3. Inventario Estructurado de Procesos
| ID | Nombre |
|---|---|
| PE-01 | Planificación |
## 4. Matriz Multicriterio de Selección Ponderada
| ID | Proceso | C1 | C2 | C3 | C4 | C5 | Sp |
|---|---|---|---|---|---|---|---|
| PE-01 | Planificación | 4 | 4 | 4 | 4 | 4 | 4.00 |
## 5. Proceso Crítico Seleccionado y Justificación
PE-01 justificado con suficiente extensión y sustento multifactorial en estrategia y costos.
"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(content_only_pe)
            temp_path = f.name

        try:
            res = validate_process_map_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertTrue(any("Procesos Operativos" in err or "Procesos de Soporte" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_weights_sum_validation(self):
        """Verifica que se detecten pesos cuya suma difiera de 1.00."""
        text = """## 4. Matriz Multicriterio de Selección Ponderada
| Código | Factor | Peso | Porcentaje |
|---|---|---|---|
| C1 | Estrategia | 0.30 | 30% |
| C2 | Tendencias | 0.30 | 30% |
| C3 | Problemas | 0.30 | 30% |
| C4 | Cliente | 0.30 | 30% |
| C5 | Producto | 0.30 | 30% |
"""
        weights, src = extract_weights(text)
        self.assertEqual(src, "tabla_ponderacion")
        self.assertAlmostEqual(sum(weights.values()), 1.50)

    def test_invalid_score_calculation(self):
        """Verifica error cuando el cálculo matemático reportado no coincide con sum(w_i * C_i)."""
        valid_template_copy = EXAMPLE_PATH.read_text(encoding="utf-8")
        # Modificar el puntaje de PO-01 a un valor matemáticamente falso (ej. 1.00 en vez de 3.65)
        bad_calculation_content = valid_template_copy.replace("| **3.65** |", "| **1.00** |")

        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(bad_calculation_content)
            temp_path = f.name

        try:
            res = validate_process_map_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertTrue(any("Inconsistencia matemática" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_missing_critical_process_selection(self):
        """Verifica error si la Sección 5 no declara el código del proceso crítico."""
        valid_template_copy = EXAMPLE_PATH.read_text(encoding="utf-8")
        # Remover la mención a PO-02 de la sección 5
        no_selection_content = valid_template_copy.replace("PO-02: Gestión de la Enseñanza-Aprendizaje", "Proceso no especificado")
        no_selection_content = no_selection_content.replace("`PO-02`", "el proceso")

        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(no_selection_content)
            temp_path = f.name

        try:
            res = validate_process_map_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertTrue(any("No se declaró explícitamente el código del Proceso Crítico" in err for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_insufficient_justification(self):
        """Verifica error si la justificación técnica es demasiado breve o vacía."""
        valid_template_copy = EXAMPLE_PATH.read_text(encoding="utf-8")
        # Truncar la sección 5 a una sola frase sin desarrollo
        sec5_pos = valid_template_copy.find("## 5.")
        short_justification_content = valid_template_copy[:sec5_pos] + "## 5. Proceso Crítico Seleccionado y Justificación\nPO-02 elegido porque es importante.\n"

        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
            f.write(short_justification_content)
            temp_path = f.name

        try:
            res = validate_process_map_file(temp_path)
            self.assertFalse(res["valid"])
            self.assertTrue(any("justificación técnica" in err.lower() for err in res["errors"]))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

if __name__ == "__main__":
    unittest.main()
