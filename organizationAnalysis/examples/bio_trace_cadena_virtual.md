# Matriz de Cadena de Valor Virtual (Rayport & Sviokla) — Caso BioTrace Logística Farmacéutica

## 1. Encuadre Organizacional y Espejo Físico-Virtual (Matriz 1 de Cátedra)

### 1.1 Definición de la Organización bajo Estudio
- **Nombre de la Organización:** BioTrace Logística Farmacéutica S.A.
- **Rubro y Actividad Organizacional:** Logística integral, almacenamiento especializado y distribución capilar de productos biológicos, oncológicos, vacunas y reactivos termolábiles bajo estricta cadena de frío (+2°C a +8°C).
- **Ámbito o Alcance de Negocio:** Regional (Provincia de Córdoba, Santa Fe y San Luis, con centro de distribución principal en la ciudad de Córdoba, Argentina).
- **Tipo de Organización / Modelo de Negocio / Estructura Interna:** Sociedad Anónima privada de mediana envergadura. Cuenta con un Centro de Distribución Automatizado (CDA) en Córdoba y 3 bases logísticas regionales secundarias. Opera con una flota propia de 28 camionetas térmicas equipadas y personal especializado de choferes y técnicos en refrigeración. La toma de decisiones operativas está centralizada en la Gerencia de Operaciones y Logística, reportando al Directorio General.
- **Misión:** Garantizar la disponibilidad, eficacia y seguridad terapéutica de medicamentos y reactivos biológicos críticos mediante una cadena logística de frío de excelencia operativa, preservando la salud de los pacientes y la confianza de las instituciones sanitarias.
- **Visión:** Ser el operador logístico farmacéutico de cadena de frío referente del interior del país, reconocido por su vanguardia tecnológica, trazabilidad termométrica en tiempo real e interoperabilidad con los sistemas de salud públicos y privados.
- **Objetivos Estratégicos:**
  - Reducir el índice de merma y descarte de productos biológicos por fluctuación térmica por debajo del 0.05% anual al cierre del ejercicio 2026.
  - Aumentar el indicador de entrega perfecta en tiempo y forma (OTIF térmico) del 86% actual al 98.5% en un horizonte de 12 meses.
  - Implementar una plataforma de trazabilidad digital integral basada en IoT y analítica en tiempo real para el 100% de los envíos hospitalarios en los próximos 18 meses.
  - Desmaterializar el 100% de la documentación de remitos físicos y registros térmicos manuales hacia certificaciones digitales inviolables en un plazo de 2 años.
- **Cliente de la Organización:** Directores de farmacia de hospitales públicos y privados, jefes de compras de clínicas de alta complejidad, laboratorios farmacéuticos multinacionales proveedores y droguerías de distribución secundaria.
- **Producto / Servicio:**
  - **Servicio:** Custodia, acondicionamiento térmico y transporte seguro de productos farmacológicos biológicos con tolerancia estricta de temperatura (+2°C a +8°C) y monitoreo de humedad/vibración.
  - **Producto de Salida (Entregable Final):** Lote de medicamentos entregado en la farmacia hospitalaria destino con certificado digital de cumplimiento térmico continuo, acta de conformidad legalizada y remito electrónico conformado.

### 1.2 Proceso Seleccionado y Cadena de Valor Física Subyacente
- **Proceso Crítico Seleccionado:** Proceso de Gestión de Transporte y Distribución con Cadena de Frío a Clientes Hospitalarios.
- **Cadena de Valor Física Subyacente (Porter):**
  - **Logística Interna:** Recepción de lotes de laboratorios en muelles refrigerados (+5°C), verificación física de precintos y almacenamiento en cámara frigorífica central de 1200 m³.
  - **Operaciones:** Fraccionamiento de pedidos hospitalarios, colocación de refrigerantes eutécticos calificados en conservadoras térmicas de poliuretano y sellado de seguridad de bultos.
  - **Logística Externa:** Asignación y carga de bultos en camionetas térmicas con equipos de frío autónomos, diseño manual de hojas de ruta y despacho físico hacia las instituciones médicas.
  - **Marketing y Ventas:** Comercialización de contratos de distribución para laboratorios, fijación de tarifas por volumen/distancia y definición de acuerdos de nivel de servicio (SLA) de entrega.
  - **Servicio Posventa:** Gestión de rechazos de mercadería por sospecha térmica, recepción telefónica de no conformidades y entrega diferida de remitos conformados.
- **Objetivo del Análisis Virtual:** Modelar la transformación de los datos operacionales generados a lo largo de la cadena logística física en un flujo continuo de información en el *marketspace*, identificando la transición de recursos operandos a recursos operantes para habilitar la co-creación de valor asistencial (Lógica Dominante del Servicio).

---

## 2. Matriz Bidimensional de la Cadena de Valor Virtual (Rayport & Sviokla)

### 2.1 Matriz Cruzada Físico-Virtual ("La Matriz del Valor" — APU_U1 Sección 10.c y 18)
*Cruce sistemático entre las 5 actividades de valor primarias físicas de Porter y los 5 procesos genéricos de transformación de información:*

| Etapa de la Cadena Física (Porter) | 1. Recopilar (Gather) | 2. Organizar (Organize) | 3. Seleccionar (Select) | 4. Sintetizar (Synthesize) | 5. Distribuir (Distribute) |
|---|---|---|---|---|---|
| **Logística Interna (Recepción e Ingreso)** | Captura de ID de lote, laboratorio origen, termómetro testigo del fabricante y fecha de caducidad. | Ingesta de datos del remito en la base relacional de stock; vinculación con la orden de compra en el ERP. | Filtrado automático de lotes recibidos con temperatura superior a +6°C para cuarentena inmediata. | Cálculo del índice de cumplimiento térmico por laboratorio proveedor al momento de la descarga. | Emisión automática de comprobante electrónico de recepción conforme al área de abastecimiento y calidad. |
| **Operaciones (Acondicionamiento y Packing)** | Lectura de código QR de bulto, registro de temperatura de conservadora y tipo de refrigerante colocado. | Vinculación del bulto físico con la orden hospitalaria y el protocolo de embalaje validado. | Identificación de bultos armados que superen los 20 minutos de espera en muelle sin refrigeración activa. | Medición del tiempo promedio de armado vs. curva teórica de degradación del hielo refrigerante. | Instrucción digital en terminal móvil del operario indicando prioridad de estiba hacia el vehículo. |
| **Logística Externa (Transporte Capilar)** | Telemetría IoT en ruta (lectura cada 60 seg de temperatura, GPS latitud/longitud, velocidad, apertura de puertas). | Streaming continuo hacia base de datos PostgreSQL unificada y Data Lake de eventos en tiempo real. | Motor CEP de reglas para aislar eventos de desvío térmico (>+8°C por >10 min) o paradas no autorizadas. | Correlación multivariable: cálculo de probabilidad de quiebre térmico, score de riesgo de ruta y predicción de ETA. | Alerta inmediata por mensajería al chofer y notificación push con tracking en vivo a la farmacia receptora. |
| **Marketing y Ventas (Contratos y SLAs)** | Captura de requerimientos térmicos especiales por tipo de medicamento y horarios de recepción de farmacias. | Catalogación de perfiles de clientes y matrices de tolerancia térmica por contrato en el CRM. | Segmentación de clientes hospitalarios de alta criticidad (oncológicos / neonatología) frente a pedidos estándar. | Matriz de rentabilidad por cliente contrastada con el costo de mantenimiento de cadena de frío y mermas. | Publicación de cotizaciones dinámicas y SLAs garantizados en el portal comercial institucional. |
| **Servicios Posventa (Garantía y Conformidad)** | Captura de firma digital del farmacéutico receptor, hora exacta de entrega y lectura final de temperatura en mano. | Normalización del remito electrónico conformado y almacenamiento inmutable en repositorio documental. | Detección automática de discrepancias entre la cantidad declarada y la recibida por la farmacia. | Consolidación del índice OTIF térmico mensual y cálculo de costos por pérdidas evitadas frente al histórico. | Envío inmediato de certificado digital inviolable (PDF firmado con hash criptográfico) al ERP del hospital. |

### 2.2 Matriz Canónica de las 5 Etapas de Información (AS-IS vs TO-BE y Fases de Madurez)

| Etapa Virtual | Definición Metodológica de Cátedra | Práctica Operativa Actual (AS-IS) | Oportunidad de Valor Digital (TO-BE) | Datos Clave Involucrados | Fase de Madurez Digital (1: Visibilidad / 2: Proyección de Capacidad / 3: Matriz del Valor) |
|---|---|---|---|---|---|
| **1. Recopilar (Gather)** | Captura inicial de datos brutos directamente en el punto físico donde ocurren los hechos, con inmediatez y fidelidad. | Choferes completan planillas térmicas manuales en papel cada 4 horas con termómetros analógicos de aguja y firman remitos en papel triplicado en cada entrega. | Dataloggers IoT (Bluetooth Low Energy + 4G) instalados dentro de cada conservadora con lectura por minuto, complementados con app móvil del chofer para escaneo de QR y captura de firma táctil digital. | `id_lote`, `temp_celsius`, `timestamp_utc`, `gps_lat_long`, `id_vehiculo`, `id_chofer`, `firma_digital_base64` | `Fase 1: Visibilidad` |
| **2. Organizar (Organize)** | Almacenamiento estructurado, limpieza, validación, normalización y catalogación en repositorios centralizados y confiables. | Las planillas en papel se archivan en biblioratos semanales; los datos de las rutas se transcriben manualmente en hojas de cálculo Excel locales dispersas por chofer y sucursal. | Ingesta continua en base de datos PostgreSQL unificada y Data Lake de eventos normalizados bajo el estándar internacional GS1-128 con validación de esquemas y tipos de datos. | `id_guia_envio`, `estado_viaje`, `id_cliente_destinatario`, `rango_termico_min_max`, `tiempo_carga_utc`, `checksum_trazabilidad` | `Fase 1: Visibilidad` |
| **3. Seleccionar (Select)** | Extracción, filtrado, segmentación y reglas de negocio para aislar información crítica o excepciones del volumen masivo de datos. | Supervisores de calidad realizan revisiones visuales selectivas de planillas de papel entre 48 y 72 horas posteriores a la finalización de los viajes o cuando surge un reclamo formal. | Motor de procesamiento de eventos complejos (Complex Event Processing - CEP) que evalúa flujos en memoria y dispara alertas inmediatas ante desvíos (>+8°C por >10 min) o retrasos de ruta (>25 min). | `flag_alerta_frio`, `delta_temperatura_celsius`, `minutos_desvio_acumulado`, `desvio_geo_km`, `nivel_criticidad_medicamento` | `Fase 2: Proyección de la Capacidad` |
| **4. Sintetizar (Synthesize)** | Agregación multivariable, combinación de métricas y modelado analítico para transformar datos aislados en conocimiento predictivo y accionable. | Elaboración artesanal de reportes mensuales estáticos en Excel con estadísticas tardías de reclamos, mermas de stock y descartes de medicamentos por pérdida de frío. | Tablero de Business Intelligence interactivo en tiempo real con monitoreo global de flota, scoring de confiabilidad térmica por ruta/chofer y modelo analítico predictivo de tiempo de arribo (ETA). | `kpi_otif_termico_pct`, `score_confiabilidad_ruta`, `probabilidad_quiebre_pct`, `costo_merma_evitada_usd`, `tiempo_medio_viaje_mins` | `Fase 2: Proyección de la Capacidad` |
| **5. Distribuir (Distribute)** | Entrega omnicanal de la información contextualizada y oportuna al destinatario adecuado para cerrar el ciclo de servicio y decisión. | Los clientes hospitalarios llaman reactivamente por teléfono para averiguar el paradero de sus pedidos; los remitos conformados en papel tardan entre 7 y 10 días hábiles en entregarse. | Portal de autogestión B2B para directores técnicos hospitalarios, webhooks automáticos hacia el sistema de gestión del cliente y notificaciones push/SMS de aproximación con enlace a certificado inviolable. | `url_certificado_digital_pdf`, `push_notif_token`, `eta_estimado_mins`, `link_tracking_en_vivo`, `webhook_payload_entrega` | `Fase 3: La Matriz del Valor (Nuevas Relaciones con Clientes)` |

---

## 3. Diagnóstico de Madurez y Evolución Digital

- **Fase de Madurez Global del Proceso Actual:** **Fase 1 Incompleta (Baja Visibilidad Reactiva).**
  - La organización cuenta con mecanismos de recolección de datos pero estos residen en soportes físicos (papel, planillas locales). No existe visibilidad integral en tiempo real ni interoperabilidad sistémica. Los administradores conocen las anomalías térmicas cuando el producto ya ha sufrido daño biológico irreversible y es rechazado en destino.
- **Cuello de Botella en el Flujo de Información:**
  - El quiebre crítico se localiza en la transición entre **Recopilar y Organizar**. La demora de 48 a 72 horas en transcribir planillas analógicas a formatos estructurados esteriliza el valor de la información para la toma de decisiones operativas. El dato no viaja a la velocidad del evento físico.
- **Evaluación bajo Lógica Dominante del Servicio (SDL — Vargo & Lusch):**
  - **Recursos Operandos (Bienes Físicos Estáticos):** Camionetas térmicas, motores de frío, conservadoras de telgopor/poliuretano y refrigerantes. En la lógica de bienes tradicional (*Goods-Dominant Logic*), BioTrace solo vende el transporte pasivo de paquetes de un punto A a un punto B (*Value-in-Exchange*).
  - **Recursos Operantes (Información Dinámica y Conocimiento):** Algoritmos de predicción térmica, flujos telemétricos en tiempo real, certificación criptográfica inmutable y analítica de ruta.
  - **Co-creación de Valor (*Value-in-Use*):** Al migrar a Fase 3, el servicio se transforma en **"Garantía de Continuidad Terapéutica y Certeza Hospitalaria"**. El hospital co-crea valor con BioTrace: programa el quirófano y asigna a su equipo médico conociendo con 15 minutos de precisión la llegada del lote biológico y validando en pantalla que la cadena de frío nunca superó los +7°C, evitando la suspensión de cirugías y eliminando el sobrestock de seguridad.
- **Desintermediación y Redefinición de Canales (APU_U1 Secciones 12 y 13):**
  - En la era pre-Internet, la comunicación entre laboratorios, operadores logísticos y hospitales exigía múltiples intermediarios administrativos y cadenas telefónicas burocráticas.
  - La plataforma virtual permite la **desintermediación informacional**: el laboratorio productor puede auditar en línea la curva térmica de sus lotes mientras el hospital recibe directamente la custodia del producto sin depender de gestores ni verificadores intermedios, consolidando a BioTrace como un socio estratégico indispensable.

---

## 4. Acciones Prioritarias de Intervención Digital (Insumo para Etapa 3 GMP)

1. **Acción de Entrada / Captura y Organización (Recopilar / Organizar):**
   - *Iniciativa:* Despliegue de sensores registradores IoT con conexión Bluetooth Low Energy en todas las conservadoras y provisión de smartphones corporativos a los choferes con app de captura en origen, sincronizada automáticamente vía 4G contra la base PostgreSQL central (Fase 1 consolidada).
2. **Acción de Procesamiento y Filtrado de Excepciones (Seleccionar):**
   - *Iniciativa:* Implementación de un motor de reglas CEP que filtre en tiempo real los paquetes telemétricos y active alertas prioritarias cuando la temperatura de un bulto supere los +7.2°C durante más de 5 minutos, notificando al chofer para ajustar el termostato antes de que el biológico se comprometa (Fase 2).
3. **Acción de Analítica Situacional y Modelado Predictivo (Sintetizar):**
   - *Iniciativa:* Construcción del Tablero de Control de Gestión Logística en Grafana/Metabase con cálculo dinámico del KPI OTIF térmico, índice de confiabilidad por chofer y estimación predictiva de tiempo de arribo (ETA) en función de congestión de tránsito (Fase 2).
4. **Acción de Salida y Co-creación de Servicio (Distribuir):**
   - *Iniciativa:* Puesta en marcha del Portal B2B de Autogestión Hospitalaria y API de interoperabilidad HL7/REST para que las farmacias de los sanatorios reciban la curva térmica del lote en formato PDF firmado digitalmente en el mismo momento del desembarque físico (Fase 3).
