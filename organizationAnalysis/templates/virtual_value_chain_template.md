# Matriz de Cadena de Valor Virtual (Rayport & Sviokla) — GMP Etapa 1

## 1. Encuadre Organizacional y Espejo Físico-Virtual (Matriz 1 de Cátedra)

### 1.1 Definición de la Organización bajo Estudio
- **Nombre de la Organización:** `[Ej. BioTrace Logística Farmacéutica S.A.]`
- **Rubro y Actividad Organizacional:** `[Definición de la actividad desarrollada por la organización, ej. Logística y distribución de productos farmacéuticos y biológicos con cadena de frío]`
- **Ámbito o Alcance de Negocio:** `[Local, regional, nacional o internacional, ej. Regional (Provincia de Córdoba y zona centro de Argentina)]`
- **Tipo de Organización / Modelo de Negocio / Estructura Interna:** `[Descripción de estructura interna, sedes, canales de venta, gobernanza y modelo de ingresos, ej. Empresa privada con centro de distribución centralizado y flota propia/tercerizada, gobernanza centralizada en Gerencia de Operaciones]`
- **Misión:** `[Finalidad para la cual fue creada la organización, qué hace HOY, frase concisa con foco interno, ej. Proveer soluciones de distribución logística farmacéutica segura y trazable, garantizando la integridad de los medicamentos para preservar la salud de los pacientes]`
- **Visión:** `[Qué queremos ser A FUTURO, mediano/largo plazo, cómo aspiramos a ser percibidos, ej. Ser la plataforma líder en logística de salud inteligente y sustentable del Cono Sur, reconocida por su excelencia operativa y tecnología de trazabilidad en tiempo real]`
- **Objetivos Estratégicos:** `[Metas estratégicas de la organización, preferentemente con criterios SMART]`
  - `[• Objetivo 1: Disminuir el índice de mermas por quiebre de cadena de frío en un 50% al cierre del ejercicio 2026]`
  - `[• Objetivo 2: Alcanzar un nivel de servicio OTIF (On-Time In-Full) superior al 98% en entregas hospitalarias críticas]`
  - `[• Objetivo 3: Implementar una plataforma de trazabilidad digital integral en el 100% de la flota en un plazo de 18 meses]`
- **Cliente de la Organización:** `[Identificación y caracterización del cliente o beneficiario principal, ej. Hospitales de alta complejidad, clínicas privadas, sanatorios y laboratorios productores de fármacos]`
- **Producto / Servicio:** `[Descripción detallada del servicio principal, características, garantías, soporte y producto de salida / entregable final]`
  - **Servicio:** `[Ej. Servicio de custodia, almacenamiento y transporte capilar de productos termosensibles entre +2°C y +8°C]`
  - **Producto de Salida (Entregable Final):** `[Ej. Medicamento o reactivo entregado en destino bajo estricto cumplimiento térmico con remito conformado y acta de conformidad regulatoria]`

### 1.2 Proceso Seleccionado y Cadena de Valor Física Subyacente
- **Proceso Crítico Seleccionado:** `[Nombre del proceso sobre el cual se aplicará la mejora, acordado para la intervención GMP]`
- **Cadena de Valor Física Subyacente (Porter):** `[Mapeo de las actividades primarias físicas donde se originan los datos brutos]`
  - **Logística Interna:** `[Recepción de lotes del laboratorio, verificación física y almacenamiento en cámaras frigoríficas]`
  - **Operaciones:** `[Acondicionamiento térmico de conservadoras, embalaje con refrigerantes y preparación de pedidos]`
  - **Logística Externa:** `[Carga de utilitarios térmicos, ruteo de distribución y transporte capilar hacia centros de salud]`
  - **Marketing y Ventas:** `[Comercialización de contratos de distribución y fijación de acuerdos de nivel de servicio (SLA)]`
  - **Servicio Posventa:** `[Gestión de reclamos de temperatura, emisión de certificados de calidad y archivo de remitos]`
- **Objetivo del Análisis Virtual:** Identificar cómo el flujo de información que acompaña a las actividades físicas se captura, procesa y distribuye para crear una cadena de valor paralela en el *marketspace*, transitando de recursos operandos a operantes bajo la Lógica Dominante del Servicio (SDL).

---

## 2. Matriz Bidimensional de la Cadena de Valor Virtual (Rayport & Sviokla)

### 2.1 Matriz Cruzada Físico-Virtual ("La Matriz del Valor" — APU_U1 Sección 10.c y 18)
*Cruce sistemático entre las actividades primarias de la cadena de valor física y los 5 procesos genéricos de transformación de información:*

| Etapa de la Cadena Física (Porter) | 1. Recopilar (Gather) | 2. Organizar (Organize) | 3. Seleccionar (Select) | 4. Sintetizar (Synthesize) | 5. Distribuir (Distribute) |
|---|---|---|---|---|---|
| **Logística Interna (Recepción e Ingreso)** | `[Captura de datos de ingreso, lote, temp]` | `[Registro en catálogo de ingresos y stock]` | `[Filtrado de lotes con desvío en recepción]` | `[Índice de calidad de proveedores en ingreso]` | `[Aviso de ingreso conforme a compras/calidad]` |
| **Operaciones (Acondicionamiento y Packing)** | `[Lectura de códigos de bulto y temp de armado]` | `[Asignación en base de datos al pedido]` | `[Identificación de bultos con riesgo de demora]` | `[Tiempo estándar de armado vs real]` | `[Instrucción de carga prioritaria al chofer]` |
| **Logística Externa (Transporte y Entrega)** | `[Telemetría IoT de viaje, GPS y firma]` | `[Ingesta continua en repositorio de viajes]` | `[Motor de alertas ante desvío térmico/ruta]` | `[Estimación predictiva de ETA y score de ruta]` | `[Notificación en vivo a la farmacia receptora]` |
| **Marketing y Ventas (Contratos y SLA)** | `[Registro de requerimientos térmicos de cliente]` | `[Estructuración de SLAs en perfiles de cliente]` | `[Segmentación de cuentas por nivel de criticidad]` | `[Análisis de rentabilidad por ruta y servicio]` | `[Propuesta de servicios diferenciados por app]` |
| **Servicios Posventa (Garantía y Conformidad)** | `[Captura de reclamos y actas de recepción]` | `[Normalización en gestor de no conformidades]` | `[Detección de patrones reiterados de queja]` | `[Tasa OTIF consolidada y cálculo de merma]` | `[Certificado digital de trazabilidad al cliente]` |

### 2.2 Matriz Canónica de las 5 Etapas de Información (AS-IS vs TO-BE y Fases de Madurez)

| Etapa Virtual | Definición Metodológica de Cátedra | Práctica Operativa Actual (AS-IS) | Oportunidad de Valor Digital (TO-BE) | Datos Clave Involucrados | Fase de Madurez Digital (1: Visibilidad / 2: Proyección de Capacidad / 3: Matriz del Valor) |
|---|---|---|---|---|---|
| **1. Recopilar (Gather)** | Captura inicial de datos brutos generados en las actividades físicas u operativas en el punto de origen. | `[Descripción AS-IS: planillas en papel, registros manuales, llamadas]` | `[Propuesta TO-BE: sensores IoT, apps móviles, escaneo QR/código de barras]` | `[Atributos técnicos: id_lote, temp_celsius, timestamp_utc, gps_lat_long]` | `Fase 1: Visibilidad` |
| **2. Organizar (Organize)** | Almacenamiento estructurado, limpieza, normalización y catalogación en repositorios consistentes. | `[Descripción AS-IS: archivos Excel locales dispersos, biblioratos físicos]` | `[Propuesta TO-BE: Data Lake unificado, base de datos relacional Postgres, MDM]` | `[Atributos técnicos: id_guia, estado_viaje, id_cliente, rango_min_max]` | `Fase 1: Visibilidad` |
| **3. Seleccionar (Select)** | Extracción, filtrado, segmentación y aplicación de reglas de negocio para aislar excepciones o datos críticos. | `[Descripción AS-IS: revisión visual humana caso a caso, consultas ad-hoc]` | `[Propuesta TO-BE: motor de reglas de eventos (CEP), vistas indexadas, filtros automáticos]` | `[Atributos técnicos: flag_alerta_frio, delta_temperatura, minutos_desvio]` | `Fase 2: Proyección de la Capacidad` |
| **4. Sintetizar (Synthesize)** | Agregación, combinación multivariable, correlación analítica y modelado predictivo para generar conocimiento. | `[Descripción AS-IS: reportes mensuales estáticos desfasados en tiempo]` | `[Propuesta TO-BE: tablero de control BI interactivo, predicción de ETA, scoring de riesgo]` | `[Atributos técnicos: kpi_otif_pct, score_confiabilidad, prob_incumplimiento]` | `Fase 2: Proyección de la Capacidad` |
| **5. Distribuir (Distribute)** | Entrega oportuna de información contextualizada a destinatarios finales, clientes o sistemas en formato omnicanal. | `[Descripción AS-IS: llamadas reactivas ante reclamo, remitos físicos a la semana]` | `[Propuesta TO-BE: portal de autogestión B2B, webhooks a ERP, alertas push automáticas]` | `[Atributos técnicos: url_certificado_digital, token_tracking, eta_mins]` | `Fase 3: La Matriz del Valor (Nuevas Relaciones con Clientes)` |

---

## 3. Diagnóstico de Madurez y Evolución Digital

- **Fase de Madurez Global del Proceso Actual:** `[Fase 1: Visibilidad (Incompleta/Parcial) / Fase 2: Proyección de la Capacidad / Fase 3: La Matriz del Valor]`
- **Cuello de Botella en el Flujo de Información:** `[Identificación exacta de la transición donde se estanca o pierde el dato, ej. Transición de Recopilar a Organizar por recaptura manual demorada]`
- **Evaluación bajo Lógica Dominante del Servicio (SDL — Vargo & Lusch):**
  - **Recursos Operandos (Bienes Tangibles):** `[Ej. Camiones refrigerados, conservadoras isotérmicas y combustible (recursos estáticos que requieren acción)]`
  - **Recursos Operantes (Conocimiento e Información Dinámica):** `[Ej. Algoritmos de predicción térmica, flujos de telemetría en tiempo real y protocolos automatizados de respuesta]`
  - **Transición de Valor:** `[Explicar el paso de Value-in-Exchange (cobro por transportar bultos fríos) a Value-in-Use (co-creación de seguridad clínica y garantía de disponibilidad terapéutica)]`
- **Desintermediación y Redefinición de Canales (APU_U1 Secciones 12 y 13):**
  - `[Analizar el impacto de la era post-Internet en el vínculo directo con los clientes y la eliminación de intermediarios innecesarios en la circulación de información y servicios]`

---

## 4. Acciones Prioritarias de Intervención Digital (Insumo para Etapa 3 GMP)

1. **Acción de Entrada / Captura y Organización (Recopilar / Organizar):**
   - `[Iniciativa concreta de digitalización en origen, ej. Implementación de sensores IoT Bluetooth en conservadoras con sincronización móvil automática]`
2. **Acción de Procesamiento y Filtrado (Seleccionar):**
   - `[Iniciativa concreta de automatización de reglas, ej. Despliegue de un motor de reglas CEP que emita alertas inmediatas ante desvíos térmicos >+7.5°C]`
3. **Acción de Analítica y Modelado Situacional (Sintetizar):**
   - `[Iniciativa concreta de analítica, ej. Tablero interactivo de control de viajes con cálculo dinámico de OTIF y alertas de mantenimiento preventivo]`
4. **Acción de Salida y Co-creación de Valor (Distribuir):**
   - `[Iniciativa concreta de servicio omnicanal, ej. Portal B2B de autoservicio para directores técnicos hospitalarios con descarga de certificados inviolables en línea]`
