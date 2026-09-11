#!/usr/bin/env python3
"""
test_validate_selection.py - Pruebas unitarias automatizadas para validate_selection.py
"""

import sys
import unittest
from pathlib import Path
import tempfile

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from validate_selection import parse_selection_file

VALID_SAMPLE_MD = r"""# Matriz de Selección Ponderada del Proceso Crítico (GMP Etapa 1)

## 1. Encuadre Organizacional y Contexto Estratégico
- **Organización / Empresa:** FrigoSur Logística S.A.
- **Sector / Industria:** Logística de Cadena de Frío
- **Misión:** Garantizar la integridad térmica de productos farmacéuticos y alimenticios.
- **Visión:** Ser el operador logístico líder en confiabilidad y trazabilidad.
- **Propuesta de Valor:** Distribución certificada con visibilidad en tiempo real.
- **Objetivos Estratégicos:**
  - **OE-1:** Reducir reclamos por temperatura a cero.
  - **OE-2:** Ampliar cobertura nacional en 20%.
- **Propósito de la Intervención GMP:** Optimizar la entrega y eliminar mermas operativas.

---

## 2. Inventario de Procesos Candidatos
| ID | Proceso Candidato | Tipo de Proceso | Evento Disparador (Inicio) | Resultado Entregado (Fin) | Responsable / Área Líder |
|:---:|:---|:---:|:---|:---|:---|
| **P1** | Recepción y Almacenamiento | Clave | Arribo de camión de proveedor | Mercadería estibada en cámara | Operaciones |
| **P2** | Preparación y Despacho | Clave | Orden de pedido aprobada | Pedido entregado conforme al cliente | Logística |
| **P3** | Compras de Insumos | Soporte | Solicitud de reposición | Insumos recibidos | Compras |
| **P4** | Facturación y Cobranzas | Soporte | Remito conformado | Cobro registrado | Administración |

---

## 3. Factores de Evaluación Normativos de Cátedra y Ponderación
| Código | Factor de Cátedra | Peso ($w_i$) | Porcentaje | Justificación del Peso en el Negocio |
|:---:|:---|:---:|:---|:---|
| **C1** | Impacto / Alineación con la Estrategia | `0.25` | 25% | Prioriza objetivos estratégicos |
| **C2** | Tendencias del Entorno / SDL | `0.20` | 20% | Co-creación y servitización |
| **C3** | Problemas Identificados (Costos, Fallas) | `0.25` | 25% | Urgencia por mermas y cuellos de botella |
| **C4** | Cliente (Experiencia y Satisfacción) | `0.20` | 20% | Impacto en SLAs |
| **C5** | Producto / Servicio Central | `0.10` | 10% | Core business |
| **Total** | **Suma de Ponderaciones ($\sum w_i$)** | **`1.00`** | **100%** | **Cierre estricto** |

---

## 4. Matriz Multicriterio de Selección Ponderada
| ID | Proceso Candidato | C1: Estrategia ($w=0.25$) | C2: Tendencias/SDL ($w=0.20$) | C3: Problemas/Costos ($w=0.25$) | C4: Cliente ($w=0.20$) | C5: Producto ($w=0.10$) | Puntaje Ponderado Total ($S_p$) | Ranking | Decisión Metodológica |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | **SELECCIONADO (Proceso Crítico)** |
| **P1** | Recepción y Almacenamiento | 4 | 3 | 4 | 3 | 4 | 3.60 | #2 | No Seleccionado |
| **P4** | Facturación y Cobranzas | 3 | 3 | 3 | 3 | 2 | 2.90 | #3 | No Seleccionado |
| **P3** | Compras de Insumos | 3 | 2 | 3 | 1 | 3 | 2.40 | #4 | No Seleccionado |

---

## 5. Justificación Cualitativa y Cuantitativa del Proceso Seleccionado
Preparación y Despacho obtiene 4.80 puntos por concentrar el 75% de los reclamos de clientes.

---

## 6. Análisis Comparativo y Razones de Descarte Relativo
Los demás procesos presentan menor impacto directo en la satisfacción del cliente final.

---

## 7. Delimitación de Fronteras y Handoff a Etapa 2 de GMP
- **Proceso Seleccionado:** Preparación y Despacho
- **Disparador:** Pedido confirmado
- **Entregable:** Mercadería entregada
"""

class TestValidateSelection(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.valid_file = Path(self.temp_dir.name) / "seleccion_proceso.md"
        self.valid_file.write_text(VALID_SAMPLE_MD, encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_valid_file_passes(self):
        success, res = parse_selection_file(self.valid_file)
        self.assertTrue(success, f"Debería ser válido pero falló con: {res.get('errors')}")
        self.assertEqual(len(res["candidates"]), 4)
        self.assertIsNotNone(res["winner"])
        self.assertEqual(res["winner"]["id"], "P2")
        self.assertAlmostEqual(res["winner"]["declared_score"], 4.80, places=2)

    def test_missing_required_section_fails(self):
        bad_md = VALID_SAMPLE_MD.replace("## 5. Justificación", "## Sección Modificada")
        bad_file = Path(self.temp_dir.name) / "bad_section.md"
        bad_file.write_text(bad_md, encoding="utf-8")
        
        success, res = parse_selection_file(bad_file)
        self.assertFalse(success)
        self.assertTrue(any("Faltan secciones requeridas" in err for err in res["errors"]))

    def test_invalid_weights_sum_fails(self):
        bad_md = VALID_SAMPLE_MD.replace("| `0.10` | 10% | Core business |", "| `0.30` | 30% | Core business |")
        bad_file = Path(self.temp_dir.name) / "bad_weights.md"
        bad_file.write_text(bad_md, encoding="utf-8")
        
        success, res = parse_selection_file(bad_file)
        self.assertFalse(success)
        self.assertTrue(any("suma de ponderaciones" in err.lower() for err in res["errors"]))

    def test_score_out_of_range_fails(self):
        bad_md = VALID_SAMPLE_MD.replace(
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | **SELECCIONADO (Proceso Crítico)** |",
            "| **P2** | Preparación y Despacho | 6 | 4 | 5 | 5 | 5 | 5.05 | #1 | **SELECCIONADO (Proceso Crítico)** |"
        )
        bad_file = Path(self.temp_dir.name) / "bad_range.md"
        bad_file.write_text(bad_md, encoding="utf-8")

        success, res = parse_selection_file(bad_file)
        self.assertFalse(success)
        self.assertTrue(any("fuera de rango" in err.lower() for err in res["errors"]))
        # Verificar que no haya mensajes de error duplicados para la misma fila/criterio
        c1_errors = [err for err in res["errors"] if "C1=6.0" in err]
        self.assertEqual(len(c1_errors), 1, "El mensaje de calificación fuera de rango no debe duplicarse")

    def test_score_not_integer_fails(self):
        bad_md = VALID_SAMPLE_MD.replace(
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | **SELECCIONADO (Proceso Crítico)** |",
            "| **P2** | Preparación y Despacho | 4.5 | 4 | 5 | 5 | 5 | 4.68 | #1 | **SELECCIONADO (Proceso Crítico)** |"
        )
        bad_file = Path(self.temp_dir.name) / "bad_float_score.md"
        bad_file.write_text(bad_md, encoding="utf-8")

        success, res = parse_selection_file(bad_file)
        self.assertFalse(success)
        self.assertTrue(any("entero discreto" in err.lower() for err in res["errors"]))

    def test_calculation_error_fails(self):
        bad_md = VALID_SAMPLE_MD.replace(
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | **SELECCIONADO (Proceso Crítico)** |",
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 3.10 | #1 | **SELECCIONADO (Proceso Crítico)** |"
        )
        bad_file = Path(self.temp_dir.name) / "bad_math.md"
        bad_file.write_text(bad_md, encoding="utf-8")

        success, res = parse_selection_file(bad_file)
        self.assertFalse(success)
        self.assertTrue(any("error de cálculo" in err.lower() for err in res["errors"]))

    def test_no_process_selected_fails(self):
        bad_md = VALID_SAMPLE_MD.replace("**SELECCIONADO (Proceso Crítico)**", "No Seleccionado")
        bad_file = Path(self.temp_dir.name) / "no_winner.md"
        bad_file.write_text(bad_md, encoding="utf-8")

        success, res = parse_selection_file(bad_file)
        self.assertFalse(success)
        self.assertTrue(any("no se ha marcado ningún proceso" in err.lower() for err in res["errors"]))

    def test_multiple_processes_selected_fails(self):
        bad_md = VALID_SAMPLE_MD.replace(
            "| **P1** | Recepción y Almacenamiento | 4 | 3 | 4 | 3 | 4 | 3.60 | #2 | No Seleccionado |",
            "| **P1** | Recepción y Almacenamiento | 4 | 3 | 4 | 3 | 4 | 3.60 | #2 | **SELECCIONADO (Proceso Crítico)** |"
        )
        bad_file = Path(self.temp_dir.name) / "multiple_winners.md"
        bad_file.write_text(bad_md, encoding="utf-8")

        success, res = parse_selection_file(bad_file)
        self.assertFalse(success)
        self.assertTrue(any("se encontraron 2 procesos marcados como seleccionados" in err.lower() for err in res["errors"]))

    def test_winner_with_lower_score_fails(self):
        bad_md = VALID_SAMPLE_MD.replace(
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | **SELECCIONADO (Proceso Crítico)** |",
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | No Seleccionado |"
        ).replace(
            "| **P3** | Compras de Insumos | 3 | 2 | 3 | 1 | 3 | 2.40 | #4 | No Seleccionado |",
            "| **P3** | Compras de Insumos | 3 | 2 | 3 | 1 | 3 | 2.40 | #4 | **SELECCIONADO (Proceso Crítico)** |"
        )
        bad_file = Path(self.temp_dir.name) / "wrong_winner.md"
        bad_file.write_text(bad_md, encoding="utf-8")

        success, res = parse_selection_file(bad_file)
        self.assertFalse(success)
        self.assertTrue(any("inferior al máximo" in err.lower() for err in res["errors"]))

    def test_tie_breaking_wrong_winner_fails(self):
        # P1 y P2 empatan en 4.25 (P1: C3=5, C1=4; P2: C3=4, C1=5). P1 debe ganar por C3.
        # Si se selecciona erróneamente P2, debe fallar.
        tie_md = VALID_SAMPLE_MD.replace(
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | **SELECCIONADO (Proceso Crítico)** |\n| **P1** | Recepción y Almacenamiento | 4 | 3 | 4 | 3 | 4 | 3.60 | #2 | No Seleccionado |",
            "| **P1** | Recepción y Almacenamiento | 4 | 4 | 5 | 4 | 4 | 4.25 | #1 | No Seleccionado |\n| **P2** | Preparación y Despacho | 5 | 4 | 4 | 4 | 4 | 4.25 | #2 | **SELECCIONADO (Proceso Crítico)** |"
        )
        bad_tie_file = Path(self.temp_dir.name) / "bad_tie.md"
        bad_tie_file.write_text(tie_md, encoding="utf-8")

        success, res = parse_selection_file(bad_tie_file)
        self.assertFalse(success)
        self.assertTrue(any("pierde el desempate jerárquico normativo" in err.lower() for err in res["errors"]))

    def test_tie_breaking_correct_winner_passes(self):
        # P1 y P2 empatan en 4.25. P1 es seleccionado correctamente por tener mayor C3 (5 > 4).
        tie_md = VALID_SAMPLE_MD.replace(
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | **SELECCIONADO (Proceso Crítico)** |\n| **P1** | Recepción y Almacenamiento | 4 | 3 | 4 | 3 | 4 | 3.60 | #2 | No Seleccionado |",
            "| **P1** | Recepción y Almacenamiento | 4 | 4 | 5 | 4 | 4 | 4.25 | #1 | **SELECCIONADO (Proceso Crítico)** |\n| **P2** | Preparación y Despacho | 5 | 4 | 4 | 4 | 4 | 4.25 | #2 | No Seleccionado |"
        )
        good_tie_file = Path(self.temp_dir.name) / "good_tie.md"
        good_tie_file.write_text(tie_md, encoding="utf-8")

        success, res = parse_selection_file(good_tie_file)
        self.assertTrue(success, f"El desempate correcto debió pasar: {res.get('errors')}")
        self.assertIsNotNone(res.get("tie_resolution"))
        self.assertIn("Empate resuelto por criterio normativo", res["tie_resolution"])

    def test_comma_decimal_separator_passes(self):
        # Validar compatibilidad con formato en español (coma como separador decimal: 4,80 y 0,25)
        comma_md = VALID_SAMPLE_MD.replace("4.80", "4,80").replace("3.60", "3,60").replace("2.90", "2,90").replace("2.40", "2,40")
        comma_file = Path(self.temp_dir.name) / "comma_sample.md"
        comma_file.write_text(comma_md, encoding="utf-8")

        success, res = parse_selection_file(comma_file)
        self.assertTrue(success, f"Debería admitir comas decimales pero falló: {res.get('errors')}")
        self.assertAlmostEqual(res["winner"]["expected_score"], 4.80, places=2)

    def test_unfilled_placeholders_fails(self):
        # Validar detección de placeholders sin completar en el texto
        ph_md = VALID_SAMPLE_MD.replace("FrigoSur Logística S.A.", "[Nombre de la Organización]")
        ph_file = Path(self.temp_dir.name) / "placeholder_sample.md"
        ph_file.write_text(ph_md, encoding="utf-8")

        success, res = parse_selection_file(ph_file)
        self.assertFalse(success)
        self.assertTrue(any("placeholders sin completar" in err.lower() for err in res["errors"]))

    def test_custom_weights_table_passes(self):
        # Ponderaciones personalizadas en la tabla: C1=0.30, C2=0.15, C3=0.30, C4=0.15, C5=0.10 (Suma = 1.00)
        custom_weights_md = VALID_SAMPLE_MD.replace(
            "| **C1** | Impacto / Alineación con la Estrategia | `0.25` | 25% | Prioriza objetivos estratégicos |",
            "| **C1** | Impacto / Alineación con la Estrategia | `0.30` | 30% | Prioriza objetivos estratégicos |"
        ).replace(
            "| **C2** | Tendencias del Entorno / SDL | `0.20` | 20% | Co-creación y servitización |",
            "| **C2** | Tendencias del Entorno / SDL | `0.15` | 15% | Co-creación y servitización |"
        ).replace(
            "| **C3** | Problemas Identificados (Costos, Fallas) | `0.25` | 25% | Urgencia por mermas y cuellos de botella |",
            "| **C3** | Problemas Identificados (Costos, Fallas) | `0.30` | 30% | Urgencia por mermas y cuellos de botella |"
        ).replace(
            "| **C4** | Cliente (Experiencia y Satisfacción) | `0.20` | 20% | Impacto en SLAs |",
            "| **C4** | Cliente (Experiencia y Satisfacción) | `0.15` | 15% | Impacto en SLAs |"
        ).replace(
            # Recalcular P2: 0.30*5 + 0.15*4 + 0.30*5 + 0.15*5 + 0.10*5 = 1.5 + 0.6 + 1.5 + 0.75 + 0.5 = 4.85
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.80 | #1 | **SELECCIONADO (Proceso Crítico)** |",
            "| **P2** | Preparación y Despacho | 5 | 4 | 5 | 5 | 5 | 4.85 | #1 | **SELECCIONADO (Proceso Crítico)** |"
        ).replace(
            # Recalcular P1: 0.30*4 + 0.15*3 + 0.30*4 + 0.15*3 + 0.10*4 = 1.2 + 0.45 + 1.2 + 0.45 + 0.4 = 3.70
            "| **P1** | Recepción y Almacenamiento | 4 | 3 | 4 | 3 | 4 | 3.60 | #2 | No Seleccionado |",
            "| **P1** | Recepción y Almacenamiento | 4 | 3 | 4 | 3 | 4 | 3.70 | #2 | No Seleccionado |"
        ).replace(
            # Recalcular P4: 0.30*3 + 0.15*3 + 0.30*3 + 0.15*3 + 0.10*2 = 0.9 + 0.45 + 0.9 + 0.45 + 0.2 = 2.90
            "| **P4** | Facturación y Cobranzas | 3 | 3 | 3 | 3 | 2 | 2.90 | #3 | No Seleccionado |",
            "| **P4** | Facturación y Cobranzas | 3 | 3 | 3 | 3 | 2 | 2.90 | #3 | No Seleccionado |"
        ).replace(
            # Recalcular P3: 0.30*3 + 0.15*2 + 0.30*3 + 0.15*1 + 0.10*3 = 0.9 + 0.3 + 0.9 + 0.15 + 0.3 = 2.55
            "| **P3** | Compras de Insumos | 3 | 2 | 3 | 1 | 3 | 2.40 | #4 | No Seleccionado |",
            "| **P3** | Compras de Insumos | 3 | 2 | 3 | 1 | 3 | 2.55 | #4 | No Seleccionado |"
        )
        cw_file = Path(self.temp_dir.name) / "custom_weights.md"
        cw_file.write_text(custom_weights_md, encoding="utf-8")

        success, res = parse_selection_file(cw_file)
        self.assertTrue(success, f"Pesos personalizados válidos fallaron: {res.get('errors')}")
        self.assertEqual(res["weights"]["C1"], 0.30)
        self.assertAlmostEqual(res["winner"]["expected_score"], 4.85, places=2)

if __name__ == "__main__":
    unittest.main()
