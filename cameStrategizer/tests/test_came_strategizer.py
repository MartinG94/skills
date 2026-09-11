#!/usr/bin/env python3
"""Suite de pruebas unitarias exhaustivas para la skill cameStrategizer y el validador validate_came.py."""

import sys
import unittest
from pathlib import Path

# Agregar scripts al path para importar validate_came
scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

from validate_came import (
    classify_quadrant_type,
    extract_declared_foda_factors,
    extract_factors_from_cell,
    infer_quadrant_from_factors,
    is_came_strategy_table_header,
    parse_markdown_table_rows,
    split_markdown_cells,
    validate_came_content,
)


class TestCAMEClassification(unittest.TestCase):
    """Pruebas para la clasificación de cuadrantes y extracción de factores."""

    def test_classify_quadrant_exact(self):
        self.assertEqual(classify_quadrant_type("FO"), "FO")
        self.assertEqual(classify_quadrant_type("FA"), "FA")
        self.assertEqual(classify_quadrant_type("DO"), "DO")
        self.assertEqual(classify_quadrant_type("DA"), "DA")

    def test_classify_quadrant_aliases(self):
        self.assertEqual(classify_quadrant_type("**FO (Ofensiva)**"), "FO")
        self.assertEqual(classify_quadrant_type("FA (Defensiva)"), "FA")
        self.assertEqual(classify_quadrant_type("DO (Reorientación)"), "DO")
        self.assertEqual(classify_quadrant_type("DA (Supervivencia)"), "DA")
        self.assertEqual(classify_quadrant_type("reorientacion"), "DO")
        self.assertEqual(classify_quadrant_type("corregir-afrontar"), "DA")
        self.assertEqual(classify_quadrant_type("EST-FO-01"), "FO")
        self.assertEqual(classify_quadrant_type("EST-DA-04"), "DA")

    def test_substring_collision_prevention(self):
        """Verifica que palabras del español con 'da', 'do', 'fa', 'fo' no sean clasificadas como cuadrantes."""
        self.assertIsNone(classify_quadrant_type("Estrategia orientada a oportunidades"))
        self.assertIsNone(classify_quadrant_type("Estrategia de Crecimiento Rápido"))
        self.assertIsNone(classify_quadrant_type("Fase 1: Implementación"))
        self.assertIsNone(classify_quadrant_type("Foco de inversión prioritario"))
        self.assertIsNone(classify_quadrant_type("Medida adoptada para el personal"))

    def test_infer_quadrant_from_factors(self):
        self.assertEqual(infer_quadrant_from_factors(["F1"], ["O1"]), "FO")
        self.assertEqual(infer_quadrant_from_factors(["F1", "F2"], ["A1"]), "FA")
        self.assertEqual(infer_quadrant_from_factors(["D1"], ["O2", "O3"]), "DO")
        self.assertEqual(infer_quadrant_from_factors(["D2"], ["A2"]), "DA")
        # Incompatible factors do not infer a quadrant
        self.assertIsNone(infer_quadrant_from_factors(["F1"], ["D1"]))
        self.assertIsNone(infer_quadrant_from_factors(["O1"], ["A1"]))

    def test_extract_factors(self):
        internal, external = extract_factors_from_cell("F1 x O2")
        self.assertEqual(internal, ["F1"])
        self.assertEqual(external, ["O2"])

        internal, external = extract_factors_from_cell("[D2 + O1]")
        self.assertEqual(internal, ["D2"])
        self.assertEqual(external, ["O1"])

        internal, external = extract_factors_from_cell("F1, F2 x A1, A2")
        self.assertEqual(internal, ["F1", "F2"])
        self.assertEqual(external, ["A1", "A2"])

    def test_non_standard_factor_ids(self):
        """Verifica que factores con guiones, guiones bajos o puntos sean detectados."""
        internal, external = extract_factors_from_cell("F-1 x O-2")
        self.assertEqual(internal, ["F-1"])
        self.assertEqual(external, ["O-2"])

        internal, external = extract_factors_from_cell("F_1 x O_1")
        self.assertEqual(internal, ["F_1"])
        self.assertEqual(external, ["O_1"])

        internal, external = extract_factors_from_cell("F.1 x O.1")
        self.assertEqual(internal, ["F.1"])
        self.assertEqual(external, ["O.1"])

        internal, external = extract_factors_from_cell("F_tech_01 x O_market_02")
        self.assertEqual(internal, ["F_TECH_01"])
        self.assertEqual(external, ["O_MARKET_02"])

        internal, external = extract_factors_from_cell("D-RRHH-02 x A-EXT-01")
        self.assertEqual(internal, ["D-RRHH-02"])
        self.assertEqual(external, ["A-EXT-01"])


class TestMarkdownTableParsing(unittest.TestCase):
    """Pruebas para el parser de tablas y discriminación de encabezados."""

    def test_split_markdown_cells_with_escaped_pipe(self):
        line = "| EST-FO-01 | FO | F1 x O1 | Enunciado | Acción \\| Detalle | Proc | Alin |"
        cells = split_markdown_cells(line)
        self.assertEqual(len(cells), 7)
        self.assertEqual(cells[4], "Acción | Detalle")

    def test_is_came_strategy_table_header(self):
        # Header de FODA debe ser descartado
        self.assertFalse(is_came_strategy_table_header(["ID Factor", "Tipo", "Denominación Corta", "Descripción"]))
        # Header de matriz conceptual 2x2 debe ser descartado
        self.assertFalse(is_came_strategy_table_header(["Matriz CAME", "Oportunidades (O)", "Amenazas (A)"]))
        self.assertFalse(is_came_strategy_table_header(["Análisis Interno \\ Externo", "Oportunidades", "Amenazas"]))
        # Header de tabla EERR debe ser descartado
        self.assertFalse(is_came_strategy_table_header(["ID Acción", "Acción de Valor", "Clasificación EERR", "Cruce CAME"]))
        # Headers legítimos de CAME deben ser aceptados
        self.assertTrue(is_came_strategy_table_header(["ID Estrategia", "Tipo CAME", "Cruce de Factores (IDs)", "Enunciado"]))
        self.assertTrue(is_came_strategy_table_header(["ID", "Cruce", "Enunciado", "Acción"]))
        self.assertTrue(is_came_strategy_table_header(["N°", "Cuadrante", "Factores Cruzados", "Propuesta"]))


class TestCAMEValidationRules(unittest.TestCase):
    """Pruebas para las reglas de oro de cátedra del CAME."""

    def test_empty_content(self):
        result = validate_came_content("")
        self.assertFalse(result["valid"])
        self.assertTrue(any("vacío" in e for e in result["errors"]))

    def test_missing_quadrants(self):
        content = """
| ID Estrategia | Tipo CAME | Cruce de Factores (IDs) | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO | F1 x O1 | Apalancar flota | Desplegar app |
"""
        result = validate_came_content(content)
        self.assertFalse(result["valid"])
        self.assertTrue(any("FA" in e for e in result["errors"]))
        self.assertTrue(any("DO" in e for e in result["errors"]))
        self.assertTrue(any("DA" in e for e in result["errors"]))

    def test_incompatible_factors(self):
        # FO que cruza D1 x O1 (D1 es debilidad, no fortaleza)
        content = """
| ID Estrategia | Tipo CAME | Cruce de Factores (IDs) | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO | D1 x O1 | Enunciado | Acción |
| EST-FA-01 | FA | F1 x A1 | Enunciado | Acción |
| EST-DO-01 | DO | D1 x O2 | Enunciado | Acción |
| EST-DA-01 | DA | D2 x A2 | Enunciado | Acción |
"""
        result = validate_came_content(content)
        self.assertFalse(result["valid"])
        self.assertTrue(any("clasificada como FO pero cruza el factor interno 'D1'" in e for e in result["errors"]))

    def test_complete_valid_matrix(self):
        content = """
# Matriz CAME

| ID Estrategia | Tipo CAME | Cruce de Factores (IDs) | Descripción de Factores | Enunciado Estratégico de Intervención | Acción de Mejora Concreta Derivada |
|---|---|---|---|---|---|
| `EST-FO-01` | **FO (Ofensiva)** | `F1 x O1` | Flota x Demanda | Apalancar capacidad de flota certificada | Desplegar servicio pharma con telemetría |
| `EST-FA-01` | **FA (Defensiva)** | `F1 x A1` | Flota x Competidores | Blindar posicionamiento ante rivales | Certificar ISO 9001 en distribución |
| `EST-DO-01` | **DO (Reorientación)** | `D1 x O2` | Papel x Móvil | Erradicar rendición en papel | Desplegar app móvil con firma digital |
| `EST-DA-01` | **DA (Supervivencia)** | `D2 x A2` | Silos TI x Regulación | Blindar registros ante auditorías | Integrar base centralizada de trazabilidad |
"""
        result = validate_came_content(content)
        self.assertTrue(result["valid"], f"Errores encontrados: {result['errors']}")
        self.assertEqual(result["total_strategies"], 4)
        self.assertEqual(result["quadrant_counts"]["FO"], 1)
        self.assertEqual(result["quadrant_counts"]["FA"], 1)
        self.assertEqual(result["quadrant_counts"]["DO"], 1)
        self.assertEqual(result["quadrant_counts"]["DA"], 1)

    def test_coexistence_with_2x2_matrix(self):
        """Verifica que una matriz 2x2 conceptual no cause errores al coexistir con la tabla formal."""
        content = """
# Matriz CAME

## 2. Matriz Conceptual CAME
| CAME Cuadrantes | Oportunidades (O) | Amenazas (A) |
|---|---|---|
| Fortalezas (F) | FO Ofensiva: F1 x O1 | FA Defensiva: F1 x A1 |
| Debilidades (D) | DO Reorientación: D1 x O1 | DA Supervivencia: D1 x A1 |

## 3. Matriz CAME Formal
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO | F1 x O1 | Enunciado | Acción |
| EST-FA-01 | FA | F1 x A1 | Enunciado | Acción |
| EST-DO-01 | DO | D1 x O1 | Enunciado | Acción |
| EST-DA-01 | DA | D1 x A1 | Enunciado | Acción |
"""
        result = validate_came_content(content)
        self.assertTrue(result["valid"], f"Errores encontrados: {result['errors']}")
        self.assertEqual(result["total_strategies"], 4)

    def test_table_without_type_column_infers_quadrants(self):
        """Verifica que si la columna 'Tipo CAME' no existe, el cuadrante se deduzca de los factores."""
        content = """
| ID Estrategia | Cruce de Factores | Enunciado Estratégico | Acción Concreta |
|---|---|---|---|
| EST-01 | F1 x O1 | Enunciado FO | Acción FO |
| EST-02 | F1 x A1 | Enunciado FA | Acción FA |
| EST-03 | D1 x O1 | Enunciado DO | Acción DO |
| EST-04 | D1 x A1 | Enunciado DA | Acción DA |
"""
        result = validate_came_content(content)
        self.assertTrue(result["valid"], f"Errores encontrados: {result['errors']}")
        self.assertEqual(result["quadrant_counts"]["FO"], 1)
        self.assertEqual(result["quadrant_counts"]["FA"], 1)
        self.assertEqual(result["quadrant_counts"]["DO"], 1)
        self.assertEqual(result["quadrant_counts"]["DA"], 1)

    def test_table_with_internal_divider_rows(self):
        """Verifica que filas con un solo valor (encabezados de cuadrante) no provoquen fallos."""
        content = """
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| **Estrategias Ofensivas (FO)** | | | | |
| EST-FO-01 | FO | F1 x O1 | Enunciado FO | Acción FO |
| **Estrategias Defensivas (FA)** | | | | |
| EST-FA-01 | FA | F1 x A1 | Enunciado FA | Acción FA |
| **Estrategias de Reorientación (DO)** | | | | |
| EST-DO-01 | DO | D1 x O1 | Enunciado DO | Acción DO |
| **Estrategias de Supervivencia (DA)** | | | | |
| EST-DA-01 | DA | D1 x A1 | Enunciado DA | Acción DA |
"""
        result = validate_came_content(content)
        self.assertTrue(result["valid"], f"Errores encontrados: {result['errors']}")
        self.assertEqual(result["total_strategies"], 4)

    def test_declared_factors_traceability(self):
        """Verifica la detección y advertencia de factores no declarados en Sección 1."""
        content = """
# Matriz CAME

## 1. Registro de Factores FODA de Entrada
| ID Factor | Tipo | Denominación Corta | Descripción |
|---|---|---|---|
| F1 | Fortaleza | Capacidad | Descripción |
| D1 | Debilidad | Falla | Descripción |
| O1 | Oportunidad | Mercado | Descripción |
| A1 | Amenaza | Riesgo | Descripción |

## 3. Matriz CAME Consolidada
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO | F1 x O1 | Enunciado FO | Acción FO |
| EST-FA-01 | FA | F1 x A1 | Enunciado FA | Acción FA |
| EST-DO-01 | DO | D1 x O1 | Enunciado DO | Acción DO |
| EST-DA-01 | DA | D1 x A1 | Enunciado DA | Acción DA |
| EST-FO-02 | FO | F8 x O1 | Cruce con F8 no declarado | Acción FO |
"""
        result = validate_came_content(content)
        self.assertTrue(result["valid"])
        self.assertTrue(any("F8" in w and "no fue declarado" in w for w in result["warnings"]))

    def test_validate_came_example_file(self):
        """Valida que el archivo de ejemplo came_example.md sea 100% conforme."""
        example_path = Path(__file__).parent.parent / "examples" / "came_example.md"
        content = example_path.read_text(encoding="utf-8")
        result = validate_came_content(content, filename=example_path.name)
        self.assertTrue(result["valid"], f"came_example.md falló validación: {result['errors']}")
        self.assertEqual(result["total_strategies"], 8)
        self.assertEqual(result["quadrant_counts"]["FO"], 2)
        self.assertEqual(result["quadrant_counts"]["FA"], 2)
        self.assertEqual(result["quadrant_counts"]["DO"], 2)
        self.assertEqual(result["quadrant_counts"]["DA"], 2)


if __name__ == "__main__":
    unittest.main()
