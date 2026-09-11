# Matriz de Partes Interesadas (Stakeholder Matrix)

## 1. Encuadre y Alcance del Proceso

- **Proceso Analizado:** `[Nombre del Proceso Crítico de Negocio]`
- **Dueño / Líder del Proceso:** `[Rol / Cargo del responsable]`
- **Alcance Operativo:** Desde `[Evento disparador / Solicitud inicial]` hasta `[Entregable final / Cierre de la transacción]`
- **Fecha de Relevamiento / Versión:** `[YYYY-MM-DD / v1.0]`
- **Objetivo del Análisis:** Mapear de forma bidireccional las necesidades, expectativas, obstáculos actuales y riesgos potenciales de todos los actores internos y externos para diagnosticar tensiones organizacionales y fundamentar el rediseño TO-BE.

---

## 2. Matriz Principal de Partes Interesadas (Triple Columna de Cátedra GMP)

> **Principio Metodológico de Bidireccionalidad (Cátedra GMP):**  
> En lugar de analizar únicamente cómo el stakeholder impacta al proceso, el análisis debe formularse en doble sentido:  
> *1. ¿Cómo nos afecta este stakeholder en la ejecución de este proceso en particular?*  
> *2. ¿Cómo afecta este proceso al stakeholder y a su nivel de satisfacción?*

| ID | Stakeholder / Actor | Categoría y Nivel | Rol en el Proceso | 1. Resultados (¿Qué reciben? - Lo Tangible) | 2. Expectativas (¿Qué esperan? - Lo Intangible) | 3. Obstáculos y Riesgos (¿Qué podría fallar?) | Evidencia / Localizador Fáctico |
|---|---|---|---|---|---|---|---|
| **STK-01** | **Operarios de Depósito / Almacén** | Interno - Nivel Operativo | Ejecución física de picking, embalaje y estiba | Órdenes de preparación claras, insumos disponibles y equipos de manipulación operativos | Carga de trabajo predecible, ergonomía adecuada y eliminación de transcripciones manuales redundantes | • **Obstáculos:** Doble registro en planillas de papel y transpaletas manuales desgastadas.<br>• **Riesgos:** Errores de preparación y lesiones ergonómicas por fatiga. | `[EV-01: Entrevista Operario]` |
| **STK-02** | **Supervisores de Turno / Coordinadores** | Interno - Supervisión / Mandos Medios | Planificación de turnos, control de avance y resolución de contingencias | Indicadores de cumplimiento horario, estado de pedidos en tiempo real y personal presente | Herramientas ágiles de reasignación de carga sin tener que consolidar manualmente al final del día | • **Obstáculos:** Ausencia de panel en tiempo real; necesidad de recorrer pasillos físicamente.<br>• **Riesgos:** Pérdida de control ante picos de demanda y demoras en despachos. | `[EV-02: Minuta Supervisión]` |
| **STK-03** | **Gerencia de Operaciones y Logística** | Interno - Gerencia / Dirección | Responsable de SLAs, presupuesto operativo y eficiencia global | Informes consolidados de cumplimiento OTIF, costos por bulto y ratios de incidencias | Visibilidad end-to-end con datos confiables para toma de decisiones y reportes inmediatos a Directorio | • **Obstáculos:** Desfase de información de 48h entre inventario físico y contable.<br>• **Riesgos:** Desviaciones presupuestarias no detectadas y pérdida de competitividad. | `[EV-03: Reporte Trimestral]` |
| **STK-04** | **Clientes Corporativos / Destinatarios** | Externo - Cliente / Destinatario | Receptores del pedido y pagadores del servicio | Mercadería correcta, completa y dentro de la ventana horaria pactada | Trazabilidad online proactiva del envío, remito electrónico inmediato y trato ágil ante reclamos | • **Obstáculos:** Ventanas horarias difusas y remitos ilegibles en papel.<br>• **Riesgos:** Pérdida de clientes corporativos y deterioro del NPS/CSAT. | `[EV-04: Encuesta CSAT]` |
| **STK-05** | **Proveedores de Transporte y Flota** | Externo - Proveedor / Socio | Aprovisionamiento de vehículos, choferes y flete troncal | Hojas de ruta optimizadas, tiempos de espera mínimos en muelle y liquidación de fletes puntual | Procesos de carga y descarga rápidos sin demoras en andén que afecten el tacógrafo o rentabilidad | • **Obstáculos:** Tiempos muertos de espera de más de 3 horas en muelle de carga.<br>• **Riesgos:** Rechazo de viajes por parte de transportistas y sobrecostos por estadía. | `[EV-05: Entrevista Transportista]` |
| **STK-06** | **Organismo de Control Sanitario / Fiscal** | Externo - Regulador / Control | Fiscalización del cumplimiento normativo y trazabilidad legal | Guías de tránsito fiscal conformes, registro ininterrumpido de cadena de frío y licencias vigentes | Transparencia inmediata ante inspecciones y auditorías sin demoras ni pérdida de documentación | • **Obstáculos:** Falta de registro continuo de temperatura en tramos de transbordo y archivo físico disperso.<br>• **Riesgos:** Clausuras preventivas, multas pecuniarias o pérdida de acreditación. | `[EV-06: Acta de Inspección]` |

---

## 3. Matriz de Prominencia y Gestión Estratégica (Poder vs Interés de Mendelow)

| Cuadrante Estratégico | Criterio de Priorización | Stakeholders Asignados | Estrategia de Gestión y Comunicación |
|---|---|---|---|
| **Gestionar de Cerca** *(Alto Poder / Alto Interés)* | Actores clave cuya decisión condiciona el éxito del rediseño y asignación de fondos | `STK-03 (Gerencia de Operaciones)`, `STK-04 (Clientes Clave Corporativos)` | Involucramiento continuo, validación de hitos, co-diseño de soluciones y comunicación semanal de avance. |
| **Mantener Satisfecho** *(Alto Poder / Bajo Interés)* | Actores institucionales o reguladores que no intervienen en el día a día pero poseen poder de veto o sanción | `STK-06 (Organismo de Control Fiscal/Sanitario)` | Cumplimiento normativo riguroso, entrega puntual de requerimientos formales y auditorías de conformidad preventivas. |
| **Mantener Informado** *(Bajo Poder / Alto Interés)* | Actores directamente impactados por la operatoria diaria que pueden generar fuerte resistencia u objeciones | `STK-01 (Operarios de Depósito)`, `STK-02 (Supervisores de Turno)` | Talleres de capacitación, canales abiertos de feedback ergonómico, resolución temprana de inquietudes operativas. |
| **Monitorear** *(Bajo Poder / Bajo Interés)* | Actores de soporte con bajo impacto directo en las decisiones de diseño del proceso | `STK-05 (Proveedores de Transporte Secundario)` | Canales estándar de comunicación operativa, encuestas periódicas de servicio y monitoreo de SLAs contractuales. |

---

## 4. Análisis de Tensiones y Conflictos Inter-Actor (Trade-offs Críticos)

1. **Velocidad de Despacho vs Rigor del Control Interno (Clientes / Operaciones vs Control / Calidad):**
   - *Tensión:* El Cliente (`STK-04`) y la Gerencia (`STK-03`) exigen tiempos de despacho ultra rápidos (<2h), lo cual tienta al personal operativo (`STK-01`) a obviar validaciones manuales de doble firma o chequeo térmico, colisionando con las exigencias del Regulador (`STK-06`).
   - *Solución Requerida:* Automatización de captura mediante lectura óptica/RFID y registro de temperatura por telemetría IoT, garantizando control instantáneo sin penalizar tiempo.

2. **Carga Operativa de Registro vs Información para Decisión (Operarios vs Supervisión / Gerencia):**
   - *Tensión:* Supervisión (`STK-02`) y Gerencia (`STK-03`) requieren múltiples datos granulares para sus métricas, lo que hoy satura a los operarios (`STK-01`) con formularios papel repetitivos que consumen hasta el 25% de su jornada.
   - *Solución Requerida:* Eliminar captura manual por parte del operario; recolectar datos pasivamente a partir de eventos de escaneo de código de barras / terminales móviles de mano.

3. **Eficiencia de Costos de Transporte vs Tiempo de Espera en Muelle (Gerencia vs Proveedores de Flota):**
   - *Tensión:* Gerencia busca consolidar cargas completas antes de despachar camiones, generando demoras de hasta 3 horas para el transportista (`STK-05`), encareciendo el flete por sobreestadía.
   - *Solución Requerida:* Implementación de turnero digital (Dock Scheduling) y notificación anticipada de preparación de carga.

---

## 5. Conclusiones e Insumos Críticos para el Rediseño TO-BE

### 5.1 Aportes Directos a la Matriz FODA (`fodaProcess`)
- **Debilidades Internas (originadas en Obstáculos AS-IS de STK-01, STK-02, STK-03):**
  - Transcripción manual reiterada en planillas de papel (riesgo de error y fatiga operativa).
  - Ceguera operativa durante la jornada por falta de tablero en tiempo real.
  - Desfase temporal de 48 horas en la consolidación de informes gerenciales.
- **Amenazas Externas (originadas en Riesgos potenciales de STK-04, STK-05, STK-06):**
  - Riesgo de sanciones regulatorias o clausura por falta de registro trazable continuo de temperatura.
  - Deterioro de relación con proveedores de transporte por tiempos muertos no remunerados.
  - Fuga de clientes corporativos ante competidores con plataformas de seguimiento GPS en vivo.

### 5.2 Requerimientos de Cambio para Acciones de Valor CAME (`cameStrategizer` / `valueActionsBuilder`)
- **Eliminar (E):** Formularios triplicados de despacho en papel y dobles planillas de control manual en depósito.
- **Reducir (R):** Tiempos de espera de choferes en muelle y desfase de reportes de 48h a minutos.
- **Incrementar (I):** Precisión del inventario disponible para picking y cumplimiento de ventanas horarias de entrega.
- **Crear (C):** Portal de autogestión de citas para transportistas y portal de tracking online para clientes finales con remito electrónico firmado digitalmente.

### 5.3 Plan de Mitigación de Resistencias al Cambio (Gestión del Cambio)
- **Actores Críticos con Riesgo de Fricción:** `STK-01 (Operarios)` por temor a mayor control o complejidad tecnológica.
- **Acción Preventiva:** Co-diseño de la interfaz móvil con operarios referentes, ergonomía de terminales de escaneo tipo anillo o pistola liviana, y programa de entrenamiento práctico de 2 semanas antes del despliegue productivo.
