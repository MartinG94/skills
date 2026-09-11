# Matriz CAME: Cruces Estratégicos de Intervención (Etapa 3)

**Proceso Crítico Evaluado:** Admisión, Enrolamiento y Cobro de Alumnos  
**Organización / Unidad:** Universidad Privada Siglo XXI  
**Analista / Equipo:** Equipo de Gestión y Mejora de Procesos (GMP)  
**Fecha:** 2026-09-11  
**Versión:** 1.0  
**Documento Fuente de Diagnóstico:** foda.md / Informe de Auditoría Operativa E2 / PlanillaMATRICES-TPI 2026  

---

## 1. Registro de Factores FODA de Entrada (Línea Base)

A continuación se resumen los factores identificados y catalogados en el diagnóstico previo (Etapa 2), con sus respectivos identificadores normalizados para garantizar trazabilidad estricta en los cruces.

### 1.1 Factores Internos (Controlables)

| ID Factor | Tipo | Denominación Corta | Descripción del Factor / Evidencia de Auditoría |
|---|---|---|---|
| `F1` | Fortaleza | Reputación Académica y Docente | Cuerpo docente altamente calificado con reconocimiento en el medio profesional y baja rotación |
| `F2` | Fortaleza | Infraestructura Adecuada y Moderna | Campus universitario propio con laboratorios tecnológicos y equipamiento informático de primer nivel |
| `D1` | Debilidad | Control Manual de Requisitos y Aranceles | Demoras burocráticas en admisiones por verificación manual de legajos y recibos físicos en ventanilla |
| `D2` | Debilidad | Carga de Datos Duplicada y Silos TI | El sistema de inscripción de aspirantes no se comunica con el sistema contable y académico central |

### 1.2 Factores Externos (No Controlables)

| ID Factor | Tipo | Denominación Corta | Descripción del Factor / Tendencia del Entorno |
|---|---|---|---|
| `O1` | Oportunidad | Demanda de Formación Híbrida | Preferencia creciente de estudiantes y profesionales por cursados semipresenciales y trayectos cortos |
| `O2` | Oportunidad | Fondos de Modernización y APIs Cloud | Disponibilidad de pasarelas de pago digitales (MercadoPago, Stripe) y microservicios educativos SaaS |
| `O3` | Oportunidad | Demanda Creciente de Educación Continua | Necesidad del mercado laboral de especializaciones ejecutivas y certificaciones de competencias rápidas |
| `A1` | Amenaza | Competidores 100% Digitales Low-Cost | Proliferación de academias y universidades virtuales con enrolamiento inmediato y menores aranceles |
| `A2` | Amenaza | Regulaciones de Acreditación Estrictas | Nuevos estándares de la autoridad educativa ministerial sobre trazabilidad documental y auditorías académicas |

---

## 2. Matriz Conceptual CAME (Cuadrantes de Cátedra)

De acuerdo con la guía oficial de cátedra (*SLI_U3_C04* y *PlanillaMATRICES-TPI*):

| Análisis Interno \ Análisis Externo | **OPORTUNIDADES (O)** | **AMENAZAS (A)** |
|---|---|---|
| **FORTALEZAS (F)** | **EXPLOTAR OPORTUNIDADES (E) — FO Ofensiva**<br>• Posicionamiento y desarrollo de ventajas competitivas.<br>• *Fórmula:* $F_i \times O_j$ | **MANTENER FORTALEZAS (M) — FA Defensiva**<br>• Evaluar riesgos, defender y movilizar recursos.<br>• *Fórmula:* $F_i \times A_k$ |
| **DEBILIDADES (D)** | **CORREGIR DEBILIDADES (C) — DO Reorientación**<br>• Inversión, digitalización y reingeniería de procesos.<br>• *Fórmula:* $D_m \times O_j$ | **AFRONTAR AMENAZAS (A) — DA Supervivencia**<br>• Control de daños, mitigación de riesgos y continuidad.<br>• *Fórmula:* $D_m \times A_k$ |

---

## 3. Matriz CAME de Cruces Estratégicos Formales

Los cruces estratégicos se construyen combinando los factores internos con los factores externos:

### 3.1 Tabla Consolidada de Cruces CAME

| ID Estrategia | Tipo CAME | Cruce de Factores (IDs) | Descripción de Factores | Enunciado Estratégico de Intervención | Acción de Mejora Concreta Derivada | Procesos Involucrados | Alineación Estratégica / Stakeholder |
|---|---|---|---|---|---|---|---|
| `EST-FO-01` | **FO (Ofensiva)** | `F2 x O3` | Infraestructura adecuada x Demanda educación continua | Ampliar la oferta académica desarrollando programas innovadores y atractivos adaptados a la demanda creciente | CREAR: Estructuración y despliegue de Trayectos de Especialización Cortos (Diplomaturas) con matriculación digital | Gestión Académica, Admisión y Enrolamiento | Objetivo: Crecimiento sostenible de matrícula. Stakeholder: Alumnos / Profesionales |
| `EST-FO-02` | **FO (Ofensiva)** | `F1 x O1` | Prestigio docente x Formación híbrida | Capitalizar la reputación académica para posicionar carreras ejecutivas en modalidad combinada | CREAR: Aulas virtuales híbridas sincrónicas y material multimedia interactivo | Extensión Universitaria, Soporte TI | Objetivo: Expansión geográfica de alumnos. Stakeholder: Docentes / Alumnos |
| `EST-FA-01` | **FA (Defensiva)** | `F2 x A1` | Infraestructura moderna x Competidores low-cost | Diferenciarse frente a la oferta 100% virtual destacando el acceso a infraestructura de laboratorios reales | INCREMENTAR: Talleres prácticos presenciales y clínicas profesionales en campus | Calidad Institucional, Marketing | Objetivo: Percepción de valor superior. Stakeholder: Alumnos / Empleadores |
| `EST-FA-02` | **FA (Defensiva)** | `F1 x A2` | Cuerpo docente calificado x Regulaciones de acreditación | Asegurar la acreditación ministerial apoyándose en la solvencia y antecedentes del equipo docente | MANTENER: Programa continuo de categorización y registro de publicaciones docentes | Secretaría Académica, Legales | Objetivo: Cumplimiento regulatorio 100%. Stakeholder: Autoridad Ministerial |
| `EST-DO-01` | **DO (Reorientación)** | `D1 x O2` | Control manual x Pasarelas digitales y APIs | Erradicar la verificación presencial de pagos implementando cobro electrónico con validación automática | AUTOMATIZAR: Pasarela de cobro digital (MercadoPago/Stripe) integrada al portal de aspirantes | Admisión, Tesorería, TI | Objetivo: Reducción del ciclo de inscripción de 5 días a 10 minutos. Stakeholder: Aspirantes |
| `EST-DO-02` | **DO (Reorientación)** | `D2 x O2` | Carga duplicada x APIs cloud | Superar la fragmentación entre admisiones y contabilidad mediante interfaces de sincronización en tiempo real | ELIMINAR: Doble tipeo manual mediante conector API REST entre CRM de postulantes y ERP académico | TI, Administración Contable | Objetivo: Cero discrepancias en padrón. Stakeholder: Personal Administrativo |
| `EST-DA-01` | **DA (Supervivencia)** | `D1 x A1` | Control burocrático x Competidores digitales ágiles | Agilizar drásticamente la admisión para evitar que los aspirantes deserten hacia plataformas online inmediatas | SIMPLIFICAR: Validación documental mediante carga de fotos/PDFs y aceptación condicional digital | Admisión y Matrícula | Objetivo: Tasa de abandono en inscripción < 5%. Stakeholder: Dirección Financiera |
| `EST-DA-02` | **DA (Supervivencia)** | `D2 x A2` | Silos de información x Nuevas regulaciones | Blindar los registros de admisión y legajos ante auditorías oficiales de la autoridad educativa | CREAR: Repositorio documental digital único con firma de archivo y registro de trazabilidad inalterable | Archivo Central, Asesoría Legal | Objetivo: Riesgo de sanción ministerial cero. Stakeholder: Directorio Universitario |

---

## 4. Síntesis de Cobertura y Trazabilidad a Etapa 3 (Acciones de Valor)

### 4.1 Balance de Cuadrantes CAME

- **Estrategias Ofensivas (FO):** 2 cruces formulados (`EST-FO-01`, `EST-FO-02`). Foco en nuevos trayectos cortos de posgrado y modalidad híbrida.
- **Estrategias Defensivas (FA):** 2 cruces formulados (`EST-FA-01`, `EST-FA-02`). Foco en calidad presencial ante rivales online y acreditación ministerial.
- **Estrategias de Reorientación (DO):** 2 cruces formulados (`EST-DO-01`, `EST-DO-02`). Foco en eliminación del trámite en ventanilla y sincronización API de datos.
- **Estrategias de Supervivencia (DA):** 2 cruces formulados (`EST-DA-01`, `EST-DA-02`). Foco en mitigación de fuga de aspirantes y repositorio seguro para auditorías.

### 4.2 Handoff hacia Inventario de Acciones de Valor EERR (`acciones_valor.md`)

Las acciones de mejora concretas derivadas en la columna 6 son transferidas directamente al inventario **EERR** de `valueActionsBuilder`:
1. `EST-FO-01` ➔ Palanca **Crear** (Trayectos de Especialización Cortos). Proceso primario: Académica. Afectados: Admisión, Calidad.
2. `EST-DO-01` ➔ Palanca **Eliminar** (Control manual en ventanilla) y **Crear/Automatizar** (Pasarela digital de cobro). Proceso primario: Admisión. Afectados: Tesorería, TI.
3. `EST-DO-02` ➔ Palanca **Eliminar** (Doble carga de datos) y **Reducir** (Tiempo de registración). Proceso primario: TI. Afectados: Administración.
4. `EST-DA-01` ➔ Palanca **Reducir** (Tasa de deserción de postulantes). Proceso primario: Admisión. Afectados: Comercial.
5. `EST-DA-02` ➔ Palanca **Crear** (Repositorio digital con trazabilidad inalterable). Proceso primario: Archivo. Afectados: Legal, Calidad.
