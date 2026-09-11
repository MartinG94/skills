#!/usr/bin/env python3
"""Pruebas unitarias completas para scripts/validate_foda.py de fodaProcess."""

import sys
import unittest
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CURRENT_DIR))

from validate_foda import (
    parse_foda_markdown,
    validate_file,
    validate_foda_structure,
)


class TestFodaValidator(unittest.TestCase):
    def setUp(self):
        self.template_path = CURRENT_DIR.parent / "templates" / "foda_process_template.md"

    def test_template_is_valid(self):
        """Verifica que la plantilla institucional oficial cumpla 100% las reglas de cátedra."""
        self.assertTrue(self.template_path.exists(), "La plantilla institucional no existe.")
        res = validate_file(self.template_path)
        self.assertEqual(len(res.errors), 0, f"Errores encontrados en plantilla: {res.errors}")
        self.assertTrue(res.is_valid)
        self.assertEqual(len(res.factors["fortalezas"]), 6)
        self.assertEqual(len(res.factors["debilidades"]), 6)
        self.assertEqual(len(res.factors["oportunidades"]), 6)
        self.assertEqual(len(res.factors["amenazas"]), 6)

    def test_valid_minimal_matrix(self):
        """Verifica una matriz mínima válida con 4 factores por cuadrante (4 columnas estándar)."""
        sample_md = """
# Matriz FODA del Proceso

## 4.1 Fortalezas (F)
| Código | Factor | Descripción | Evidencia | Gobernanza |
| :---: | :--- | :--- | :--- | :---: |
| **F1** | Flota propia moderna | Camiones equipados | Registro de flota | 100% Interno |
| **F2** | Personal especializado | Operarios certificados | Registros RRHH | 100% Interno |
| **F3** | Protocolo ISO 9001 | Manual operativo | Certificación IRAM | 100% Interno |
| **F4** | Software ERP centralizado | Base de datos unificada | Licencias activas | 100% Interno |

## 4.2 Debilidades (D)
| Código | Brecha | Descripción | Hallazgo de Auditoría | Eje |
| :---: | :--- | :--- | :--- | :---: |
| **D1** | Incompatibilidad SoD | Mismo operador recepciona y ajusta stock | SRC-AUD-01: RCM-01 | Control Interno |
| **D2** | Triplicado en papel | Retraso de 48h en facturación | SRC-DOC-02: Formulario R-04 | Ruta Documental |
| **D3** | Recaptura manual | Doble carga en Excel y ERP | SRC-IT-03: Silo informático | Soporte TI |
| **D4** | Cuello de botella en muelle | 2 horas de cola promedio | SRC-ENT-04: Minuta entrevista | Operativo |

## 4.3 Oportunidades (O)
| Código | Oportunidad | Descripción | Fuente del Entorno | Impacto |
| :---: | :--- | :--- | :--- | :---: |
| **O1** | Maduración de SaaS logístico | Plataformas cloud a bajo costo | Tendencia tech | Alto |
| **O2** | Demanda de tracking digital | Clientes B2B valoran visibilidad | Mercado | Alto |
| **O3** | Estándares abiertos de remito | Ley de remito electrónico | Regulatorio | Medio |
| **O4** | Sensores IoT accesibles | Telemetría económica en ruta | Tecnología | Medio |

## 4.4 Amenazas (A)
| Código | Amenaza | Descripción | Fuente del Riesgo | Severidad |
| :---: | :--- | :--- | :--- | :---: |
| **A1** | Competidores nativos digitales | Plataformas ágiles de última milla | Mercado | Alta |
| **A2** | Endurecimiento normativo | Sanciones por cadena de frío | Regulatorio | Alta |
| **A3** | Volatilidad de combustibles | Suba de precios de nafta y gasoil | Económico | Alta |
| **A4** | Escasez de repuestos importados | Demoras en proveedores de piezas | Proveedores | Media |
"""
        res = parse_foda_markdown(sample_md)
        res = validate_foda_structure(res)
        self.assertTrue(res.is_valid, f"Errores inesperados: {res.errors}")
        self.assertEqual(len(res.errors), 0)

    def test_valid_catedra_3_ejes_matrix(self):
        """Verifica la estructura oficial de 3 Ejes de cátedra (PlanillaMATRICES-TPI 2026 Matriz 3)."""
        catedra_md = """
# Matriz FODA del Proceso Universitario

### 4.1 Fortalezas (F)
| Código | Factor | Eje 1: Propósito y Visión | Eje 2: Grupos de Interés | Eje 3: Resultados Actuales | Gobernanza |
|:---:|:---|:---|:---|:---|:---:|
| F1 | Experiencia docente calificada | Solidez pedagógica con visión de calidad | Docentes con alto sentido de pertenencia | 80% de resolución en primer contacto | Interno |
| F2 | Infraestructura moderna | Capacidad instalada funcional | Estudiantes disponen de aulas híbridas | Auditoría de infraestructura conforme | Interno |
| F3 | Programas de estudio actualizados | Pertinencia laboral y académica | Egresados altamente valorados | Alta tasa de inserción laboral en 6 meses | Interno |
| F4 | Convenios de pasantías consolidados | Articulación con sector productivo | Empresas con vínculos de largo plazo | 45 convenios corporativos vigentes | Interno |

### 4.2 Debilidades (D)
| Código | Brecha | Eje 1: Propósito y Visión | Eje 2: Grupos de Interés | Eje 3: Evidencia de Auditoría | Eje Temático |
|:---:|:---|:---|:---|:---|:---:|
| D1 | Oferta curricular rígida | Desalineado de nuevas demandas ágiles | Aspirantes optan por diplomaturas cortas | SRC-AUD-01: Caída de 12% en matrícula tradicional | Estratégico |
| D2 | Tiempos de respuesta lentos | Afecta promesa de acompañamiento | Alumnos reclaman demoras de más de 48h | SRC-DOC-02: Reclamo expediente físico R-12 | Administrativo |
| D3 | Sistemas TI fragmentados | Frena objetivo de transformación digital | Personal administrativo sobrecargado | SRC-IT-03: Doble carga manual en SIU y Excel | Soporte TI |
| D4 | Falta de indicadores automáticos | Dificulta la gestión basada en evidencia | Directores operan a ciegas sin alertas | RCM-04: Carencia de métricas de proceso | Control Interno |

### 4.3 Oportunidades (O)
| Código | Oportunidad | Eje 1: Propósito y Visión | Eje 2: Grupos de Interés | Eje 3: Resultados / Evidencia | Impacto |
|:---:|:---|:---|:---|:---|:---:|
| O1 | Ecosistema EdTech maduro | Habilita campus virtual innovador | Docentes y alumnos integrados | Madurez de plataformas LMS cloud | Alto |
| O2 | Redes universitarias internacionales | Facilita convenios de doble titulación | Estudiantes acceden a intercambios | Convocatorias abiertas del MERCOSUR | Alto |
| O3 | Demanda de trayectos cortos | Abre nueva fuente de ingresos | Profesionales buscan recertificación | Aumento del 40% en consultas corporativas | Medio-Alto |
| O4 | Subsidios para transformación digital | Financia equipamiento sin CAPEX | Universidad moderniza laboratorios | Programa ministerial de créditos fiscales | Medio-Alto |

### 4.4 Amenazas (A)
| Código | Amenaza | Eje 1: Propósito y Visión | Eje 2: Grupos de Interés | Eje 3: Impacto Observable | Severidad |
|:---:|:---|:---|:---|:---|:---:|
| A1 | Nuevos estándares de CONEAU | Exige acreditaciones complejas en plazos cortos | Cuerpo académico bajo presión | Nuevas resoluciones regulatorias estrictas | Alta |
| A2 | Proliferación de academias online | Presión a la baja en aranceles | Mercado atraído por cursos ultrarrápidos | Pérdida de cuota de mercado en segmento joven | Alta |
| A3 | Inflación y pérdida de poder adquisitivo | Tensión financiera en la cobranza | Familias con dificultades de pago | Tasa de morosidad sube al 18% interanual | Media-Alta |
| A4 | Cortes de conectividad troncal | Riesgo para clases híbridas | Alumnos remotos incomunicados | Registros de fallas en proveedor de fibra | Media |
"""
        res = parse_foda_markdown(catedra_md)
        res = validate_foda_structure(res)
        self.assertTrue(res.is_valid, f"Errores en formato cátedra 3 ejes: {res.errors}")
        self.assertEqual(len(res.errors), 0)
        self.assertEqual(len(res.factors["fortalezas"]), 4)
        self.assertEqual(len(res.factors["debilidades"]), 4)
        self.assertEqual(len(res.factors["oportunidades"]), 4)
        self.assertEqual(len(res.factors["amenazas"]), 4)

    def test_valid_2_column_matrix(self):
        """Verifica que una tabla de sólo 2 columnas (Código y Factor) sea parseada correctamente."""
        minimal_2col = """
## Fortalezas (F)
| Código | Factor |
|---|---|
| F1 | Flota propia mantenida |
| F2 | Personal altamente competente |
| F3 | Protocolo ISO estandarizado |
| F4 | Sistemas de monitoreo GPS |

## Debilidades (D)
| Código | Factor con Evidencia |
|---|---|
| D1 | Conflicto SoD en despacho [SRC-AUD-01] |
| D2 | Planilla manual con demora de 48h [SRC-DOC-02] |
| D3 | Silo informático sin integración ERP [SRC-IT-03] |
| D4 | Cuello de botella en muelle [SRC-ENT-04] |

## Oportunidades (O)
| Código | Factor |
|---|---|
| O1 | Oferta de plataformas SaaS logísticas |
| O2 | Tendencia de consumo con demanda de tracking |
| O3 | Normativa de remito digital vigente |
| O4 | Sensores IoT a precios accesibles |

## Amenazas (A)
| Código | Factor |
|---|---|
| A1 | Nuevos competidores con entrega en 2 horas |
| A2 | Nuevas exigencias de entes reguladores |
| A3 | Volatilidad de precios de combustibles |
| A4 | Quiebre de stocks en proveedores clave |
"""
        res = parse_foda_markdown(minimal_2col)
        res = validate_foda_structure(res)
        self.assertTrue(res.is_valid, f"Fallo al parsear tablas de 2 columnas: {res.errors}")
        self.assertEqual(len(res.factors["fortalezas"]), 4)
        self.assertEqual(len(res.factors["debilidades"]), 4)
        self.assertEqual(len(res.factors["oportunidades"]), 4)
        self.assertEqual(len(res.factors["amenazas"]), 4)

    def test_valid_numbered_lists(self):
        """Verifica que listas numeradas con formato 1. F1: Enunciado sean procesadas correctamente."""
        numbered_md = """
# Matriz FODA en Listas

## Fortalezas (F)
1. F1: Capacidad instalada propia
2. F2: Certificaciones de calidad IRAM
3. F3: Equipo técnico capacitado
4. F4: Cobertura geográfica amplia

## Debilidades (D)
1. D1: Doble carga manual de datos [Evidencia: SRC-IT-01]
2. D2: Circuito de firmas en papel [Evidencia: SRC-DOC-02]
3. D3: Incompatibilidad de funciones SoD [Evidencia: RCM-03]
4. D4: Demoras por cuellos de botella [Evidencia: SRC-ENT-04]

## Oportunidades (O)
1. O1: Crecimiento de demanda en canal digital
2. O2: Disponibilidad de microservicios en la nube
3. O3: Créditos estatales para PyMEs
4. O4: Ecosistema logístico colaborativo

## Amenazas (A)
1. A1: Plataformas extranjeras con precios subsidiados
2. A2: Regulaciones laborales restrictivas
3. A3: Escasez de microchips para vehículos
4. A4: Fluctuaciones cambiarias abruptas
"""
        res = parse_foda_markdown(numbered_md)
        res = validate_foda_structure(res)
        self.assertTrue(res.is_valid, f"Fallo al parsear listas numeradas: {res.errors}")
        self.assertEqual(len(res.factors["fortalezas"]), 4)
        self.assertEqual(len(res.factors["debilidades"]), 4)
        self.assertEqual(len(res.factors["oportunidades"]), 4)
        self.assertEqual(len(res.factors["amenazas"]), 4)

    def test_missing_quadrant_fails(self):
        """Verifica que falle si falta un cuadrante (ej. sin Amenazas)."""
        incomplete_md = """
## Fortalezas (F)
- `F1:` Factor 1
- `F2:` Factor 2
- `F3:` Factor 3
- `F4:` Factor 4

## Debilidades (D)
- `D1:` Brecha 1 [SRC-01]
- `D2:` Brecha 2 [SRC-02]
- `D3:` Brecha 3 [SRC-03]
- `D4:` Brecha 4 [SRC-04]

## Oportunidades (O)
- `O1:` Op 1
- `O2:` Op 2
- `O3:` Op 3
- `O4:` Op 4
"""
        res = parse_foda_markdown(incomplete_md)
        res = validate_foda_structure(res)
        self.assertFalse(res.is_valid)
        self.assertTrue(any("Amenazas" in e for e in res.errors))

    def test_under_cardinality_fails(self):
        """Verifica que falle si un cuadrante tiene menos de 4 factores."""
        md_text = """
## Fortalezas (F)
- `F1:` Factor 1
- `F2:` Factor 2
- `F3:` Factor 3

## Debilidades (D)
- `D1:` Brecha 1 [SRC-01]
- `D2:` Brecha 2 [SRC-02]
- `D3:` Brecha 3 [SRC-03]
- `D4:` Brecha 4 [SRC-04]

## Oportunidades (O)
- `O1:` Op 1
- `O2:` Op 2
- `O3:` Op 3
- `O4:` Op 4

## Amenazas (A)
- `A1:` Am 1
- `A2:` Am 2
- `A3:` Am 3
- `A4:` Am 4
"""
        res = parse_foda_markdown(md_text)
        res = validate_foda_structure(res)
        self.assertFalse(res.is_valid)
        self.assertTrue(any("sólo 3 factores" in e for e in res.errors))

    def test_over_cardinality_fails(self):
        """Verifica que falle si un cuadrante tiene más de 6 factores (ej. 7)."""
        md_text = """
## Fortalezas (F)
- `F1:` Factor 1
- `F2:` Factor 2
- `F3:` Factor 3
- `F4:` Factor 4
- `F5:` Factor 5
- `F6:` Factor 6
- `F7:` Factor 7

## Debilidades (D)
- `D1:` Brecha 1 [SRC-01]
- `D2:` Brecha 2 [SRC-02]
- `D3:` Brecha 3 [SRC-03]
- `D4:` Brecha 4 [SRC-04]

## Oportunidades (O)
- `O1:` Op 1
- `O2:` Op 2
- `O3:` Op 3
- `O4:` Op 4

## Amenazas (A)
- `A1:` Am 1
- `A2:` Am 2
- `A3:` Am 3
- `A4:` Am 4
"""
        res = parse_foda_markdown(md_text)
        res = validate_foda_structure(res)
        self.assertFalse(res.is_valid)
        self.assertTrue(any("excede el límite con 7 factores" in e for e in res.errors))

    def test_debilidad_missing_evidence_fails(self):
        """Verifica que falle si una debilidad no tiene evidencia o cita documental probatoria."""
        md_text = """
## Fortalezas (F)
- `F1:` Factor 1
- `F2:` Factor 2
- `F3:` Factor 3
- `F4:` Factor 4

## Debilidades (D)
| Código | Brecha | Descripción | Evidencia |
|---|---|---|---|
| D1 | Brecha 1 | Desc | SRC-01 |
| D2 | Brecha sin sustento | Afirmación abstracta sin auditoría | |
| D3 | Brecha 3 | Desc | SRC-03 |
| D4 | Brecha 4 | Desc | SRC-04 |

## Oportunidades (O)
- `O1:` Op 1
- `O2:` Op 2
- `O3:` Op 3
- `O4:` Op 4

## Amenazas (A)
- `A1:` Am 1
- `A2:` Am 2
- `A3:` Am 3
- `A4:` Am 4
"""
        res = parse_foda_markdown(md_text)
        res = validate_foda_structure(res)
        self.assertFalse(res.is_valid)
        self.assertTrue(any("D2" in e and "evidencia primaria" in e for e in res.errors))

    def test_debilidad_evidence_in_details_passes(self):
        """Verifica que la evidencia sea detectada si está en la columna de detalles o descripción."""
        md_text = """
## Fortalezas (F)
- `F1:` Factor 1
- `F2:` Factor 2
- `F3:` Factor 3
- `F4:` Factor 4

## Debilidades (D)
| Código | Brecha | Detalle con Evidencia |
|---|---|---|
| D1 | Conflicto de funciones | Detectado en auditoría interna RCM-01 |
| D2 | Retraso en remito papel | Verificado en relevamiento de ruta documental SRC-DOC-02 |
| D3 | Silo informático | Hallazgo de auditoría en área de soporte TI |
| D4 | Esperas prolongadas | Constatado en minuta de entrevista SRC-ENT-04 |

## Oportunidades (O)
- `O1:` Op 1
- `O2:` Op 2
- `O3:` Op 3
- `O4:` Op 4

## Amenazas (A)
- `A1:` Am 1
- `A2:` Am 2
- `A3:` Am 3
- `A4:` Am 4
"""
        res = parse_foda_markdown(md_text)
        res = validate_foda_structure(res)
        self.assertTrue(res.is_valid, f"Errores inesperados cuando la evidencia está en detalles: {res.errors}")

    def test_boundary_warning_on_internal_action_in_opportunity(self):
        """Verifica que advierta si una oportunidad se redacta como acción interna ('comprar software')."""
        md_text = """
## Fortalezas (F)
- `F1:` Factor 1
- `F2:` Factor 2
- `F3:` Factor 3
- `F4:` Factor 4

## Debilidades (D)
- `D1:` Brecha 1 [SRC-01]
- `D2:` Brecha 2 [SRC-02]
- `D3:` Brecha 3 [SRC-03]
- `D4:` Brecha 4 [SRC-04]

## Oportunidades (O)
- `O1:` Comprar una plataforma de logística para la empresa
- `O2:` Op 2
- `O3:` Op 3
- `O4:` Op 4

## Amenazas (A)
- `A1:` Am 1
- `A2:` Am 2
- `A3:` Am 3
- `A4:` Am 4
"""
        res = parse_foda_markdown(md_text)
        res = validate_foda_structure(res)
        self.assertTrue(any("violación de frontera en Oportunidad 'O1'" in w for w in res.warnings))

    def test_boundary_warning_on_internal_staff_in_threat(self):
        """Verifica que advierta si una amenaza se redacta culpando al personal propio."""
        md_text = """
## Fortalezas (F)
- `F1:` Factor 1
- `F2:` Factor 2
- `F3:` Factor 3
- `F4:` Factor 4

## Debilidades (D)
- `D1:` Brecha 1 [SRC-01]
- `D2:` Brecha 2 [SRC-02]
- `D3:` Brecha 3 [SRC-03]
- `D4:` Brecha 4 [SRC-04]

## Oportunidades (O)
- `O1:` Op 1
- `O2:` Op 2
- `O3:` Op 3
- `O4:` Op 4

## Amenazas (A)
- `A1:` Nuestros empleados cargan tarde las planillas de recepción
- `A2:` Am 2
- `A3:` Am 3
- `A4:` Am 4
"""
        res = parse_foda_markdown(md_text)
        res = validate_foda_structure(res)
        self.assertTrue(any("violación de frontera en Amenaza 'A1'" in w for w in res.warnings))

    def test_panoramic_2x2_fallback_parsing(self):
        """Verifica que si sólo existe la matriz sintética 2x2, los factores se recuperen vía fallback."""
        matrix_only_md = """
# Matriz FODA Sintética

| Ámbito | Factores Favorables | Factores Desfavorables |
|---|---|---|
| Interno | **FORTALEZAS**<br>• F1: Flota propia<br>• F2: Personal calificado<br>• F3: ISO 9001<br>• F4: ERP integrado | **DEBILIDADES**<br>• D1: SoD roto [SRC-01]<br>• D2: Papel físico [SRC-02]<br>• D3: Silo TI [SRC-03]<br>• D4: Espera en muelle [SRC-04] |
| Externo | **OPORTUNIDADES**<br>• O1: SaaS logístico<br>• O2: Tracking digital<br>• O3: Remito electrónico<br>• O4: Sensores IoT | **AMENAZAS**<br>• A1: Competidores ágiles<br>• A2: Nuevas normas<br>• A3: Suba de nafta<br>• A4: Escasez de piezas |
"""
        res = parse_foda_markdown(matrix_only_md)
        res = validate_foda_structure(res)
        self.assertTrue(res.is_valid, f"Fallo al parsear matriz 2x2 sintética: {res.errors}")
        self.assertEqual(len(res.factors["fortalezas"]), 4)
        self.assertEqual(len(res.factors["debilidades"]), 4)
        self.assertEqual(len(res.factors["oportunidades"]), 4)
        self.assertEqual(len(res.factors["amenazas"]), 4)


if __name__ == "__main__":
    unittest.main()
