#!/usr/bin/env python3
"""Pruebas unitarias para scripts/validate_stakeholders.py."""

import tempfile
import unittest
from pathlib import Path
import sys

# Importar el validador desde el directorio hermano scripts/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from validate_stakeholders import validate_stakeholder_file, extract_table, extract_all_tables


class TestValidateStakeholders(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.base_path = Path(self.temp_dir.name)

    def test_non_existent_file(self):
        fake_path = self.base_path / "non_existent.md"
        errors = validate_stakeholder_file(fake_path)
        self.assertTrue(any("El archivo no existe" in e for e in errors))

    def test_empty_file(self):
        empty_file = self.base_path / "empty.md"
        empty_file.write_text("", encoding="utf-8")
        errors = validate_stakeholder_file(empty_file)
        self.assertTrue(any("vacío" in e for e in errors))

    def test_missing_mandatory_sections(self):
        incomplete_file = self.base_path / "incomplete.md"
        incomplete_file.write_text("# Documento sin secciones requeridas", encoding="utf-8")
        errors = validate_stakeholder_file(incomplete_file)
        self.assertTrue(any("Sección obligatoria faltante" in e for e in errors))

    def test_missing_triple_column_in_table(self):
        bad_table_file = self.base_path / "bad_table.md"
        bad_table_content = """
## 1. Encuadre y Alcance del Proceso
Proceso de Prueba.

## 2. Matriz Principal de Partes Interesadas
Principio de bidireccionalidad: ¿cómo nos afecta el stakeholder y cómo el proceso le afecta?
| ID | Stakeholder / Actor | Rol en el Proceso |
|---|---|---|
| STK-01 | Operario | Ejecutor |

## 3. Matriz de Prominencia / Mendelow
Poder vs Interes

## 4. Análisis de Tensiones y Conflictos
Tensiones

## 5. Conclusiones e Insumos Críticos para el Rediseño TO-BE
FODA y CAME
"""
        bad_table_file.write_text(bad_table_content, encoding="utf-8")
        errors = validate_stakeholder_file(bad_table_file)
        self.assertTrue(any("Columna 1: Resultados" in e for e in errors))
        self.assertTrue(any("Columna 2: Expectativas" in e for e in errors))
        self.assertTrue(any("Columna 3: Obstáculos y Riesgos" in e for e in errors))

    def test_empty_cells_in_required_columns(self):
        empty_cells_file = self.base_path / "empty_cells.md"
        empty_cells_content = """
## 1. Encuadre y Alcance del Proceso
Proceso X

## 2. Matriz Principal de Partes Interesadas
Bidireccionalidad: ¿cómo nos afecta este stakeholder?
| ID | Stakeholder / Actor | Categoría y Nivel | Rol en el Proceso | 1. Resultados | 2. Expectativas | 3. Obstáculos y Riesgos | Evidencia |
|---|---|---|---|---|---|---|---|
| STK-01 | Operarios | Interno - Operativo | Tareas | | Entrega rápida | Fricción | EV-01 |

## 3. Matriz de Prominencia / Mendelow
Gestionar de cerca

## 4. Análisis de Tensiones y Conflictos
Tensión A

## 5. Conclusiones e Insumos Críticos para el Rediseño TO-BE
FODA Debilidades y CAME EERR
"""
        empty_cells_file.write_text(empty_cells_content, encoding="utf-8")
        errors = validate_stakeholder_file(empty_cells_file)
        self.assertTrue(any("Fila 1 tiene vacía o incompleta la celda" in e for e in errors))

    def test_missing_taxonomy_category(self):
        missing_cat_file = self.base_path / "missing_cat.md"
        # Tiene operarios, supervisores, gerencia, cliente y proveedor, pero NO regulador
        missing_cat_content = """
## 1. Encuadre y Alcance del Proceso
Proceso Y

## 2. Matriz Principal de Partes Interesadas
Bidireccionalidad: análisis bidireccional
| ID | Stakeholder / Actor | Categoría y Nivel | Rol en el Proceso | 1. Resultados | 2. Expectativas | 3. Obstáculos y Riesgos | Evidencia |
|---|---|---|---|---|---|---|---|
| STK-01 | Operarios | Interno - Nivel Operativo | Tareas | Res 1 | Exp 1 | Obs 1 | EV-01 |
| STK-02 | Supervisores | Interno - Supervisión | Control | Res 2 | Exp 2 | Obs 2 | EV-02 |
| STK-03 | Gerencia | Interno - Gerencia | Decisión | Res 3 | Exp 3 | Obs 3 | EV-03 |
| STK-04 | Clientes | Externo - Cliente | Receptor | Res 4 | Exp 4 | Obs 4 | EV-04 |
| STK-05 | Proveedores | Externo - Proveedor | Insumos | Res 5 | Exp 5 | Obs 5 | EV-05 |

## 3. Matriz de Prominencia / Mendelow
Poder e Interes

## 4. Análisis de Tensiones y Conflictos
Tensiones

## 5. Conclusiones e Insumos Críticos para el Rediseño TO-BE
FODA y CAME
"""
        missing_cat_file.write_text(missing_cat_content, encoding="utf-8")
        errors = validate_stakeholder_file(missing_cat_file)
        self.assertTrue(any("Externo - Regulador / Control" in e for e in errors))

    def test_canonical_template_passes_validation(self):
        template_path = Path(__file__).resolve().parent.parent / "templates" / "stakeholder_matrix_template.md"
        errors = validate_stakeholder_file(template_path)
        self.assertEqual(errors, [], f"La plantilla oficial tiene errores de validación: {errors}")

    def test_multi_table_document_selects_stakeholder_table(self):
        """Verifica que un documento con tabla auxiliar previa no confunda al validador."""
        multi_table_file = self.base_path / "multi_table.md"
        multi_table_content = """
## 1. Encuadre y Alcance del Proceso
| Parámetro | Detalle |
|---|---|
| Proceso Analizado | Despacho Farmacéutico |
| Líder del Proceso | Jefe de Farmacia |

## 2. Matriz Principal de Partes Interesadas
Análisis de bidireccionalidad: ¿cómo nos afecta este stakeholder en el proceso y cómo le afecta el proceso a él?

| ID | Stakeholder / Actor | Rol en el Proceso | 1. Resultados Esperados | 2. Expectativas Cualitativas | 3. Obstáculos Percibidos | Evidencia |
|---|---|---|---|---|---|---|
| STK-01 | Operarios de Depósito | Preparación | Órdenes listas | Ergonomía | Planillas papel | EV-01 |
| STK-02 | Supervisores de Turno | Control | Panel de avance | Predictibilidad | Ceguera operativa | EV-02 |
| STK-03 | Gerencia General | Dirección | Informes de costo | Datos confiables | Desfase 48h | EV-03 |
| STK-04 | Clientes Finales | Receptores | Pedido a tiempo | Trazabilidad | Falta de aviso | EV-04 |
| STK-05 | Proveedores de Transporte | Distribución | Hojas de ruta | Espera mínima | Demoras en muelle | EV-05 |
| STK-06 | Regulador Sanitario | Fiscalización | Guías conformes | Transparencia | Archivo físico | EV-06 |

## 3. Matriz de Prominencia / Mendelow
Poder vs Interés de Mendelow

## 4. Análisis de Tensiones y Conflictos
Tensiones operativas

## 5. Conclusiones e Insumos Críticos para el Rediseño TO-BE
Conexión con FODA (Debilidades y Amenazas) y CAME EERR (Eliminar, Reducir, Incrementar, Crear).
"""
        multi_table_file.write_text(multi_table_content, encoding="utf-8")
        errors = validate_stakeholder_file(multi_table_file)
        self.assertEqual(errors, [], f"Falló la extracción en documento multi-tabla: {errors}")

    def test_catedra_headers_and_roles_pass(self):
        """Verifica que un documento con cabeceras y roles exactos de la cátedra GMP pase sin errores."""
        catedra_file = self.base_path / "catedra_case.md"
        catedra_content = """
## 1. Encuadre y Alcance del Proceso
- Proceso: Gestión de la Trayectoria, Formación Integral y Graduación del Estudiante
- Límites: Desde admisión hasta entrega del diploma

## 2. Matriz Principal de Partes Interesadas
Análisis bidireccionalidad: En lugar de analizar cómo el stakeholder afecta al proceso en análisis,
deben preguntarse: ¿Cómo nos afecta este stakeholder en la ejecución de este proceso en particular,
y cómo afecta este proceso al stakeholder?

| Identificación del Stakeholder | RESULTADOS (¿Qué reciben?) | EXPECTATIVAS (¿Qué esperan?) | OBSTÁCULOS (¿Qué podría fallar?) |
|---|---|---|---|
| Estudiantes (Cliente / Destinatario) | Título académico oficial y desarrollo de competencias técnicas/blandas. | Que la educación sea práctica, actualizada y en un entorno inclusivo. | • Obstáculos: Procesos administrativos lentos.<br>• Riesgos: Contenidos desfasados del mundo real. |
| Docentes (Personal Operativo Académico) | Recursos para la enseñanza, compensación justa y reconocimiento. | Claridad en los procesos, soporte técnico y libertad para innovar en el aula. | • Obstáculos: Sobrecarga de tareas burocráticas.<br>• Riesgos: Falta de soporte técnico ante nuevas tecnologías. |
| Directores de Carrera (Mandos Medios / Supervisión) | Indicadores de retención y seguimiento académico. | Herramientas ágiles y procesos sin fricciones. | • Obstáculos: Información dispersa en silos.<br>• Riesgos: Deserción estudiantil temprana. |
| Dueños Universidad (Directorio / Gerencia) | Rentabilidad (ROI), cumplimiento de metas de matrícula y valorización de marca. | Una operación eficiente, procesos transparentes y crecimiento sostenible. | • Obstáculos: Ineficiencias operativas en el día a día.<br>• Riesgos: Procesos con vacíos legales o fallas de control. |
| Empresas y Mercado (Socios / Empleadores) | Perfiles profesionales competentes y convenios de pasantías efectivos. | Que los alumnos tengan habilidades de día 1 y se adapten rápido. | • Obstáculos: Brecha de competencias visible.<br>• Riesgos: Pérdida de convenios clave con la industria. |
| Entes reguladores (Control / Fiscalización) | Reportes de cumplimiento, estadísticas de calidad y transparencia. | Procesos auditables, trazabilidad de la información y rigor académico. | • Obstáculos: Dificultad para recopilar evidencia.<br>• Riesgos: Incumplimiento de estándares de calidad obligatorios. |

## 3. Matriz de Prominencia / Mendelow
Poder e Interés de Mendelow

## 4. Análisis de Tensiones y Conflictos
Tensiones inter-actor

## 5. Conclusiones e Insumos Críticos para el Rediseño TO-BE
Insumos para FODA (Debilidades y Amenazas) y CAME EERR.
"""
        catedra_file.write_text(catedra_content, encoding="utf-8")
        errors = validate_stakeholder_file(catedra_file)
        self.assertEqual(errors, [], f"Falló el caso oficial de cátedra: {errors}")

    def test_missing_bidirectionality_fails(self):
        """Verifica que si no se menciona el principio de bidireccionalidad se reporte el error."""
        no_bidi_file = self.base_path / "no_bidi.md"
        no_bidi_content = """
## 1. Encuadre y Alcance del Proceso
Proceso

## 2. Matriz Principal de Partes Interesadas
| ID | Stakeholder / Actor | 1. Resultados | 2. Expectativas | 3. Obstáculos y Riesgos |
|---|---|---|---|---|
| STK-01 | Operarios de Depósito | Res | Exp | Obs |
| STK-02 | Supervisores | Res | Exp | Obs |
| STK-03 | Gerencia | Res | Exp | Obs |
| STK-04 | Clientes | Res | Exp | Obs |
| STK-05 | Proveedores | Res | Exp | Obs |
| STK-06 | Regulador | Res | Exp | Obs |

## 3. Matriz de Prominencia / Mendelow
Poder vs Interes

## 4. Análisis de Tensiones y Conflictos
Tensiones

## 5. Conclusiones e Insumos Críticos para el Rediseño TO-BE
FODA y CAME EERR
"""
        no_bidi_file.write_text(no_bidi_content, encoding="utf-8")
        errors = validate_stakeholder_file(no_bidi_file)
        self.assertTrue(any("bidireccionalidad" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
