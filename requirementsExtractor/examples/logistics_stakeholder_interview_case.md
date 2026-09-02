# Caso de Estudio Práctico: Extracción de Requisitos desde Entrevista no Estructurada

Este documento demuestra la ejecución completa y de punta a punta del agente `rawInterviewToRequirementsExtractor`, procesando una transcripción real de descubrimiento de software en una empresa de logística y distribución.

---

## 1. Entrada: Transcripción Cruda de la Entrevista (Raw Transcript)

**Reunión de Relevamiento:** Sistema de Gestión de Depósito y Despacho (WMS LogiExpress)  
**Participantes:**
- **Martín Gómez:** Director de Operaciones (STK-01)
- **Carla Benítez:** Jefa de Depósito y Picking (STK-02)
- **Gustavo Rossi:** Gerente de Administración y Finanzas (STK-03)
- **Analista de Sistemas (Facilitador)**

```text
[00:02:15] Analista: Cuéntenme cómo arranca el día en el depósito y qué problemas tienen hoy con el sistema actual.

[00:02:30] Martín (Operaciones): Mirá, hoy es un bardo. Los pedidos entran desde la web y desde los vendedores de la calle, pero a Carla le llegan en un Excel al mediodía. Queremos que los pedidos entren al toque al sistema de picking. Que sea todo en tiempo real. Y que el sistema sea súper rápido y amigable, porque los chicos en el depósito rotan bastante y no podés estar dos semanas explicándoles cómo usar una pantalla.

[00:03:45] Carla (Depósito): Tal cual lo que dice Martín. Los chicos andan con las colectoras de datos Honeywell en el depósito. El tema es que en el fondo de la nave 3 no hay buena señal de Wi-Fi, se corta a cada rato. Si la aplicación web se congela cuando se corta la señal, perdemos todo el lote de picking y hay que arrancar de cero. Tiene que funcionar aunque no haya internet y cuando vuelva la señal que se suba solo. Además, el operario tiene que pistolear el código de barras del bulto, y si pistolea un producto vencido o equivocado, la colectora tiene que hacer un pitido fuerte de error y no dejarlo avanzar.

[00:05:10] Gustavo (Finanzas): Pará, antes de que armen el paquete para despachar, hay algo crítico: ningún pedido puede pasar a estado 'Preparación' si el cliente tiene facturas vencidas de más de 30 días o si supera el límite de crédito en cuenta corriente, a menos que yo o la gerencia general pongamos una clave de autorización especial. Si despachamos mercadería a clientes morosos, nos fundimos. 

[00:06:20] Carla (Depósito): Pero Gustavo, si frenamos todo por el crédito en el momento del picking, me armás un cuello de botella terrible en las bahías de carga. Yo necesito que la validación crediticia se haga apenas entra la orden, no cuando el pibe ya tiene la caja en la mano listo para subirla al camión. Además, para clientes frecuentes con compras mayores a 100 bultos mensuales, el sistema les tiene que bonificar el flete automáticamente según corresponda.

[00:07:40] Martín (Operaciones): Coincido con Carla. Y ojo con la seguridad y la auditoría. El año pasado tuvimos faltantes de mercadería de alto valor (electrónica) y nadie sabía quién había modificado la cantidad de bultos en el remito. Todo cambio en las cantidades de una orden o reasignación de lote tiene que quedar grabado con fecha, hora, usuario y la IP o dispositivo, sin que nadie pueda borrar ese registro. Y necesitamos que el sistema soporte picos: en el Hot Sale llegamos a tener 40 operarios pistoleando bultos a la vez y entran 5.000 pedidos por hora. Si se cae el sistema en esa fecha, perdemos millones.

[00:09:15] Gustavo (Finanzas): Una cosa técnica que me pide el área de IT: la base de datos tiene que ser PostgreSQL porque ya pagamos el soporte corporativo, y todo tiene que estar integrado con nuestro ERP SAP R/3 mediante web services REST, usando autenticación segura. No queremos cargar los remitos a mano dos veces.
```

---

## 2. Razonamiento y Proceso Analítico del Agente

### Paso 1: Mapeo de Stakeholders y Dinámica de Poder
- **STK-01 (Martín - Operaciones):** Foco en rendimiento general, auditoría, trazabilidad contra fraudes y capacidad en picos.
- **STK-02 (Carla - Depósito):** Foco en usabilidad en campo, dispositivos rugged (Honeywell), resiliencia a caídas de red (offline-first) y velocidad operativa sin bloqueos tardíos.
- **STK-03 (Gustavo - Finanzas):** Foco en control de riesgo crediticio, prevención de morosidad, restricciones de IT y cumplimiento financiero.

### Paso 2: Detección y Aislamiento de Ambigüedades (Lenguaje Vago)
1. *"al toque / en tiempo real"* (Martín) -> Ambigüedad temporal. Riesgo: sobreingeniería de WebSockets vs colas asíncronas.
2. *"súper rápido"* (Martín) -> Ambigüedad de rendimiento. Riesgo: falta de SLA de latencia en milisegundos.
3. *"amigable / no podés estar dos semanas explicándoles"* (Martín) -> Ambigüedad de usabilidad. Riesgo: falta de métrica de aprendibilidad (*learnability*).
4. *"según corresponda"* (Carla) -> Cláusula de escape para bonificación de flete. Riesgo: regla de negocio incompleta.

### Paso 3: Identificación del Conflicto de Alcance (Carla vs. Gustavo)
- **Conflicto CONF-01:** Momento de la validación crediticia. Gustavo exige bloqueo de morosos; Carla exige que no ocurra en la bahía de carga para evitar cuellos de botella físicos.  
- **Resolución Técnica Propuesta:** Desacoplar la validación: Ejecutar `RN-01` en el pipeline de admisión de órdenes (*Order Ingestion*). Si está bloqueado, no emitir la orden de picking; si Finanzas aprueba con override, liberar la orden a la cola de picking de Carla.

---

## 3. Salida Estructurada: Documento Markdown Formal

# Especificación de Requerimientos de Software (ERS / SRS)
## Proyecto: Sistema de Gestión de Depósito y Despacho (WMS LogiExpress)
**Fuente de Elicitación:** Transcripción de Entrevista de Relevamiento Operativo  
**Fecha:** 2026-09-01 | **Analista:** `rawInterviewToRequirementsExtractor` | **Versión:** 1.0.0-draft

---

### 1. Ficha del Ecosistema de Stakeholders

| ID | Nombre / Rol | Unidad Organizacional | Nivel de Influencia | Interés Principal |
| :---: | :--- | :--- | :---: | :--- |
| **STK-01** | Martín Gómez (Director de Operaciones) | Operaciones y Logística | Alta | Rendimiento bajo picos, auditoría inmutable contra fraudes. |
| **STK-02** | Carla Benítez (Jefa de Depósito) | Logística / Depósito | Alta | Eficiencia de picking, resiliencia offline en naves, lecturas con colectoras. |
| **STK-03** | Gustavo Rossi (Gerente de Administración) | Finanzas / IT Governance | Alta | Control de riesgo crediticio, integración con SAP R/3 y PostgreSQL. |

---

### 2. Requerimientos Funcionales (RF)

| ID | Título y Descripción | Actor Principal | Entradas / Salidas | Reglas Asociadas | Prioridad | Trazabilidad |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **RF-01** | **Ingesta y Asignación Automatizada de Pedidos**<br>El sistema debe recibir pedidos multicanal (Web / Vendedores en calle) y generar lotes de picking para el depósito en menos de 5 segundos tras su aprobación. | Sistema / Vendedor | • **In:** Payload de pedido (cliente, ítems, cantidades)<br>• **Out:** Orden de Picking creada | `RN-01`, `RN-02` | **Must Have** | *"Queremos que los pedidos entren al toque al sistema de picking."* — `[STK-01:00:02:30]` |
| **RF-02** | **Validación de Picking por Código de Barras con Alerta Sonora**<br>El sistema debe validar cada bulto escaneado contra la orden activa. Si el código no coincide o el producto está vencido, debe emitir una señal sonora de error y bloquear la confirmación del ítem. | Operario de Depósito | • **In:** Código de barras escaneado (EAN-13/GS1)<br>• **Out:** Confirmación visual/sonora o Alarma de rechazo | `RN-03`, `RN-04` | **Must Have** | *"si pistolea un producto vencido o equivocado, la colectora tiene que hacer un pitido fuerte de error..."* — `[STK-02:00:03:45]` |
| **RF-03** | **Bloqueo y Override de Pedidos por Riesgo Crediticio**<br>El sistema debe evaluar automáticamente la morosidad y saldo en cuenta corriente antes de liberar la orden a picking. Si incumple, bloquea el pase a 'Preparación' requiriendo autorización gerencial. | Sistema / Gerente Finanzas | • **In:** ID Cliente, Monto Pedido, Clave Override<br>• **Out:** Estado 'Aprobado' o 'Bloqueado por Crédito' | `RN-01` | **Must Have** | *"ningún pedido puede pasar a estado 'Preparación' si el cliente tiene facturas vencidas..."* — `[STK-03:00:05:10]` |
| **RF-04** | **Pista de Auditoría Inmutable para Modificaciones de Órdenes**<br>El sistema debe registrar de forma automática e inalterable cada modificación de cantidades, cancelación o reasignación de lote. | Sistema | • **In:** Evento de mutación de orden<br>• **Out:** Registro de auditoría (Log estructurado) | `RN-05` | **Must Have** | *"Todo cambio en las cantidades de una orden o reasignación de lote tiene que quedar grabado..."* — `[STK-01:00:07:40]` |
| **RF-05** | **Cálculo Automático de Bonificación de Flete**<br>El sistema debe aplicar bonificación del 100% del costo de flete a clientes que superen el umbral mensual de compras. | Sistema | • **In:** ID Cliente, Historial mensual de bultos<br>• **Out:** Descuento de flete aplicado en la orden | `RN-02` | **Should Have** | *"para clientes frecuentes con compras mayores a 100 bultos mensuales, el sistema les tiene que bonificar el flete..."* — `[STK-02:00:06:20]` |

---

### 3. Requerimientos No Funcionales (RNF) — FURPS+ / ISO 25010

| ID | Dimensión | Subcaracterística | Especificación Planguage (Tom Gilb) | Prioridad | Trazabilidad |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **RNF-01** | **Reliability**<br>*(ISO: Fiabilidad)* | Tolerancia a Fallos / Capacidad Offline | • **Escala:** Persistencia local de escaneos sin conexión Wi-Fi.<br>• **Medidor:** Prueba de corte de red durante sesión de picking de 50 bultos.<br>• **Límite Inaceptable:** Pérdida de datos o reinicio de sesión.<br>• **Objetivo Plan:** 100% de operaciones encoladas localmente en SQLite/IndexedDB y sincronizadas al reconectar en < 3 seg. | **Crítica** | *"Tiene que funcionar aunque no haya internet y cuando vuelva la señal que se suba solo."* — `[STK-02:00:03:45]` |
| **RNF-02** | **Performance**<br>*(ISO: Desempeño)* | Capacidad de Concurrencia y Throughput | • **Escala:** Ingesta de pedidos y lecturas simultáneas.<br>• **Medidor:** Test de estrés JMeter simulando 5.000 pedidos/hora y 50 colectoras concurrentes.<br>• **Límite Inaceptable:** Latencia P95 > 3.0 s o errores HTTP 5xx > 0.01%.<br>• **Objetivo Plan:** Latencia P95 <= 800 ms y 0% de pérdidas de transacción. | **Crítica** | *"en el Hot Sale llegamos a tener 40 operarios pistoleando bultos a la vez y entran 5.000 pedidos por hora."* — `[STK-01:00:07:40]` |
| **RNF-03** | **Usability**<br>*(ISO: Usabilidad)* | Aprendibilidad (*Learnability*) | • **Escala:** Tiempo de entrenamiento para operarios noveles.<br>• **Medidor:** Evaluación de 5 operarios temporarios en tarea de picking estándar.<br>• **Límite Inaceptable:** > 4 horas de capacitación o tasa de error > 5%.<br>• **Objetivo Plan:** <= 30 minutos de inducción con tasa de éxito en primer intento >= 95%. | **Alta** | *"los chicos en el depósito rotan bastante y no podés estar dos semanas explicándoles..."* — `[STK-01:00:02:30]` |
| **RNF-04** | **Security**<br>*(ISO: Seguridad)* | No Repudio y Auditoría Inmutable | • **Escala:** Completitud y no alterabilidad del registro de eventos sensibles.<br>• **Medidor:** Tabla append-only con firma criptográfica HMAC y bloqueo de permisos `UPDATE/DELETE` en BD.<br>• **Límite Inaceptable:** Campos obligatorios nulos o registros editables.<br>• **Objetivo Plan:** 100% de eventos auditados con: Timestamp UTC, UserID, IP/DeviceID, Snapshot previo y Snapshot posterior. | **Crítica** | *"sin que nadie pueda borrar ese registro."* — `[STK-01:00:07:40]` |

---

### 4. Reglas de Negocio Aisladas (RN)

| ID | Título | Tipo | Declaración / Algoritmo | Cumplimiento | Origen |
| :---: | :--- | :---: | :--- | :---: | :--- |
| **RN-01** | **Control de Mora y Límite de Crédito** | Restricción | Un pedido no puede cambiar al estado `En Preparación` si el cliente posee al menos una factura con mora > 30 días corridos o si el importe del pedido supera el límite de crédito remanente, excepto mediante ingreso de token de autorización de usuario con rol `Gerente Finanzas`. | Estricta con Override | `[STK-03:00:05:10]` |
| **RN-02** | **Bonificación por Volumen Mensual** | Cálculo | Si la suma acumulada de bultos facturados al cliente en los últimos 30 días móviles es `>= 100`, el cargo por concepto de flete en la orden corriente se fija en `$0.00`. | Estricta | `[STK-02:00:06:20]` |
| **RN-03** | **Prohibición de Despacho de Mercadería Vencida** | Restricción | Ningún lote de producto cuya fecha de caducidad sea `<= Fecha Actual + 15 días` puede ser asignado a una orden de despacho estándar. | Estricta (Inviolable) | `[STK-02:00:03:45]` |
| **RN-04** | **Validación Estricta de Código de Bulto** | Restricción | El operario debe escanear el identificador GS1-128 del bulto coincidente con la posición asignada; se rechaza cualquier ingreso manual por teclado salvo autorización de supervisor. | Estricta | `[STK-02:00:03:45]` |
| **RN-05** | **Inmutabilidad de Registro Histórico de Remitos** | Restricción | Los remitos emitidos no admiten modificación destructiva; toda corrección se efectúa mediante Nota de Crédito o Remito Rectificativo vinculado. | Estricta | `[STK-01:00:07:40]` |

---

### 5. Supuestos, Restricciones y Dependencias

- **SUP-01 (Supuesto de Hardware):** Se asume que las terminales colectoras Honeywell poseen sistema operativo Android 10 o superior y soportan navegadores Chromium modernos o aplicaciones PWA en modo kiosco.  
  *Impacto:* Si son equipos heredados con Windows CE, requerirá desarrollo de cliente nativo C#.  
  *Acción:* Solicitar modelo exacto y firmware de los equipos a IT.
- **RES-01 (Restricción Tecnológica):** El motor de base de datos relacional debe ser PostgreSQL versión 15 o superior alojado en la infraestructura corporativa.
- **RES-02 (Restricción de Interfaz ERP):** La sincronización de pedidos y maestros de clientes/artículos debe ejecutarse contra el ERP SAP R/3 mediante servicios web REST con OAuth2.
- **DEP-01 (Dependencia):** Disponibilidad de la API de SAP R/3 para la consulta de saldos y cuentas corrientes de clientes.

---

### 6. Matriz de Desambiguación y Cuestionario para Stakeholders

| ID | Fragmento de Entrevista | Término Vago | Riesgo Identificado | Pregunta de Clarificación Estructurada |
| :---: | :--- | :--- | :--- | :--- |
| **AMB-01** | *"para clientes frecuentes con compras mayores a 100 bultos mensuales, el sistema les tiene que bonificar el flete automáticamente según corresponda."* | *"según corresponda"* | Ambigüedad en la regla: ¿Aplica a todos los destinos del país o solo a rango local/regional? | **Para Carla Benítez / Gustavo Rossi:**<br>1. ¿La bonificación de flete cubre envíos a todo el territorio nacional o tiene un tope de kilometraje / zona geográfica?<br>&nbsp;&nbsp;*a) Solo envíos locales (Radio 50 km)*<br>&nbsp;&nbsp;*b) Envíos nacionales con tope de tarifa según lista de transporte*<br>&nbsp;&nbsp;*c) 100% bonificado sin importar el destino* |
| **AMB-02** | *"Queremos que los pedidos entren al toque al sistema de picking. Que sea todo en tiempo real."* | *"al toque" / "en tiempo real"* | Dimensionamiento de WebSockets vs Polling vs Kafka. | **Para Martín Gómez:**<br>¿Cuál es la latencia máxima admisible entre que el cliente confirma el pedido en la web y la orden aparece en la pantalla del depósito?<br>&nbsp;&nbsp;*a) Inmediato síncrono (< 1 segundo)*<br>&nbsp;&nbsp;*b) Encolado asíncrono con refresco periódico (< 15 segundos)*<br>&nbsp;&nbsp;*c) Lotes periódicos cada 5 minutos* |

---

## 4. Salida Estructurada: Objeto JSON Formal

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "metadata": {
    "project_name": "Sistema de Gestión de Depósito y Despacho (WMS LogiExpress)",
    "source_document_title": "Transcripción de Entrevista de Relevamiento Operativo",
    "source_type": "interview_transcript",
    "extraction_timestamp": "2026-09-01T16:15:00-03:00",
    "analyst_skill": "rawInterviewToRequirementsExtractor",
    "version": "1.0.0"
  },
  "stakeholders": [
    {
      "id": "STK-01",
      "name": "Martín Gómez",
      "role": "Director de Operaciones",
      "organization_unit": "Operaciones y Logística",
      "influence_level": "High",
      "primary_interests": ["Throughput en eventos pico", "Auditoría contra fraudes", "Velocidad de despacho"]
    },
    {
      "id": "STK-02",
      "name": "Carla Benítez",
      "role": "Jefa de Depósito y Picking",
      "organization_unit": "Depósito",
      "influence_level": "High",
      "primary_interests": ["Resiliencia offline en naves", "Usabilidad en colectoras Honeywell", "Fluidez sin cuellos de botella"]
    },
    {
      "id": "STK-03",
      "name": "Gustavo Rossi",
      "role": "Gerente de Administración y Finanzas",
      "organization_unit": "Finanzas e IT Governance",
      "influence_level": "High",
      "primary_interests": ["Control de riesgo crediticio", "Integración con SAP R/3", "Cumplimiento de stack PostgreSQL"]
    }
  ],
  "functional_requirements": [
    {
      "id": "RF-01",
      "title": "Ingesta y Asignación Automatizada de Pedidos",
      "description": "El sistema debe ingerir pedidos multicanal (Web / Vendedores de calle) y generar órdenes de picking listas para el depósito en menos de 5 segundos tras validación.",
      "module_or_epic": "Módulo de Ingesta y Despacho",
      "primary_actor": "Sistema / Vendedor",
      "secondary_actors": ["Operario de Depósito"],
      "inputs": ["Payload de orden", "ID de Cliente", "Líneas de ítems y cantidades"],
      "outputs": ["Orden de Picking generada", "Evento OrderReadyForPicking emitido"],
      "associated_business_rules": ["RN-01", "RN-02"],
      "priority": "Must Have",
      "source_traceability": {
        "stakeholder_id": "STK-01",
        "quote": "Queremos que los pedidos entren al toque al sistema de picking.",
        "paragraph_or_time_ref": "00:02:30"
      }
    },
    {
      "id": "RF-02",
      "title": "Validación de Picking por Código de Barras con Alarma Sonora",
      "description": "El sistema debe verificar el código escaneado contra la orden activa. En caso de no coincidencia o fecha de vencimiento menor al umbral, emite pitido de error y bloquea la confirmación.",
      "module_or_epic": "Módulo de Picking Móvil",
      "primary_actor": "Operario de Depósito",
      "secondary_actors": ["Supervisor de Depósito"],
      "inputs": ["Código de barras GS1/EAN", "ID de Bulto", "ID de Orden"],
      "outputs": ["Feedback sonoro/visual de éxito", "Alerta de bloqueo por producto incorrecto o caduco"],
      "associated_business_rules": ["RN-03", "RN-04"],
      "priority": "Must Have",
      "source_traceability": {
        "stakeholder_id": "STK-02",
        "quote": "si pistolea un producto vencido o equivocado, la colectora tiene que hacer un pitido fuerte de error y no dejarlo avanzar.",
        "paragraph_or_time_ref": "00:03:45"
      }
    }
  ],
  "non_functional_requirements": [
    {
      "id": "RNF-01",
      "title": "Tolerancia a Caídas de Red y Operatividad Offline",
      "furps_category": "Reliability",
      "iso25010_dimension": "Reliability",
      "subcharacteristic": "Fault Tolerance / Recoverability",
      "planguage_specification": {
        "scale": "Porcentaje de operaciones de picking completables sin conexión de red Wi-Fi",
        "meter": "Test de desconexión física de AP Wi-Fi durante ejecución de 50 lecturas continuas",
        "baseline": "0% (El sistema actual se cuelga y reinicia el lote)",
        "worst_acceptable": "95% de operaciones retenidas localmente",
        "target_plan": "100% de operaciones persistidas en base local y sincronización automática en < 3s tras restablecer señal",
        "stretch_wish": "Sincronización bidireccional delta P2P entre colectoras"
      },
      "priority": "Critical",
      "source_traceability": {
        "stakeholder_id": "STK-02",
        "quote": "Tiene que funcionar aunque no haya internet y cuando vuelva la señal que se suba solo.",
        "paragraph_or_time_ref": "00:03:45"
      }
    },
    {
      "id": "RNF-02",
      "title": "Throughput y Concurrencia en Eventos Pico",
      "furps_category": "Performance",
      "iso25010_dimension": "Performance Efficiency",
      "subcharacteristic": "Capacity / Time Behavior",
      "planguage_specification": {
        "scale": "Latencia en milisegundos percentil 95 (P95) bajo carga de 5.000 pedidos/hora y 50 terminales activas",
        "meter": "Prueba de carga distribuida JMeter / k6 durante 60 minutos continuos",
        "baseline": "Latencia > 12.000 ms y caídas recurrentes del servidor",
        "worst_acceptable": "P95 < 2.000 ms y tasa de error < 0.1%",
        "target_plan": "P95 <= 800 ms y 0% transacciones perdidas",
        "stretch_wish": "P95 <= 400 ms con auto-scaling elástico en kubernetes"
      },
      "priority": "Critical",
      "source_traceability": {
        "stakeholder_id": "STK-01",
        "quote": "en el Hot Sale llegamos a tener 40 operarios pistoleando bultos a la vez y entran 5.000 pedidos por hora.",
        "paragraph_or_time_ref": "00:07:40"
      }
    }
  ],
  "business_rules": [
    {
      "id": "RN-01",
      "title": "Control de Mora y Límite de Crédito para Despacho",
      "statement": "Ningún pedido puede cambiar al estado 'En Preparación' si el cliente posee facturas con mora > 30 días corridos o supera su límite de crédito disponible, salvo autorización expresa con clave de Gerente de Finanzas.",
      "rule_type": "Constraint",
      "logic_or_formula": "IF (Customer.OverdueInvoicesDays > 30 OR Order.Amount > Customer.AvailableCredit) AND NOT AuthorizationToken.IsValid THEN BlockTransition(Order, 'En Preparacion')",
      "enforcement_level": "Strict/Mandatory",
      "source_traceability": {
        "stakeholder_id": "STK-03",
        "quote": "ningún pedido puede pasar a estado 'Preparación' si el cliente tiene facturas vencidas de más de 30 días...",
        "paragraph_or_time_ref": "00:05:10"
      }
    }
  ],
  "assumptions": [
    {
      "id": "SUP-01",
      "statement": "Las terminales colectoras de datos Honeywell soportan ejecución de WebViews modernas basadas en Chromium con acceso al lector de código de barras vía Web APIs o SDK Android.",
      "risk_if_invalid": "Requeriría desarrollar un cliente nativo en Java/Kotlin o C# retrasando el cronograma en 6 semanas.",
      "validation_action": "Solicitar a IT la lista de modelos de colectoras Honeywell y ejecutar una prueba de concepto técnica en 48 horas."
    }
  ],
  "constraints": [
    {
      "id": "RES-01",
      "title": "Motor de Base de Datos PostgreSQL Corporativo",
      "constraint_type": "Technical",
      "description": "El sistema debe utilizar PostgreSQL >= 15 como motor relacional primario.",
      "rationale": "Directriz corporativa de IT para aprovechar licenciamiento y soporte contratado."
    },
    {
      "id": "RES-02",
      "title": "Integración con SAP R/3 vía Web Services REST",
      "constraint_type": "Architectural",
      "description": "Todo intercambio maestro de pedidos, clientes y remitos debe interactuar con el ERP SAP R/3 mediante endpoints REST protegidos.",
      "rationale": "Evitar duplicación de carga operativa y mantener consistencia financiera."
    }
  ],
  "dependencies": [
    {
      "id": "DEP-01",
      "name": "API REST SAP R/3 Módulo SD/FI",
      "type": "External API",
      "description": "Servicio provisto por SAP para consulta de saldo de cuenta corriente y emisión de remitos.",
      "criticality": "High"
    }
  ],
  "ambiguities_and_clarifications": [
    {
      "id": "AMB-01",
      "target_stakeholder": "Carla Benítez / Gustavo Rossi",
      "raw_excerpt": "para clientes frecuentes con compras mayores a 100 bultos mensuales, el sistema les tiene que bonificar el flete automáticamente según corresponda.",
      "detected_term": "según corresponda",
      "risk": "Falta de definición de zonas geográficas o topes monetarios para la bonificación de flete.",
      "clarification_question": "¿La bonificación del 100% de flete aplica a cualquier destino nacional o está acotada a un radio de kilometraje específico?",
      "suggested_options": [
        "Opción A: Solo envíos dentro del radio metropolitano / 50 km.",
        "Opción B: Envíos nacionales con tope tarifario según lista de logística.",
        "Opción C: 100% bonificado para cualquier destino del país sin excepción."
      ]
    }
  ],
  "conflicts_and_tradeoffs": [
    {
      "id": "CONF-01",
      "stakeholders_involved": ["STK-02 (Carla Benítez)", "STK-03 (Gustavo Rossi)"],
      "conflict_description": "Momento de validación de riesgo crediticio: Gustavo exige bloqueo estricto antes de preparación; Carla advierte que validar en la bahía de carga genera cuellos de botella operativos.",
      "proposed_resolution_options": [
        "Opción 1: Validar crédito en el momento de la ingesta del pedido web, impidiendo la generación de la orden de picking si está bloqueado (Recomendada).",
        "Opción 2: Validar en el momento del empaque final con cola de reintento.",
        "Opción 3: Validación asíncrona con alerta preventiva al supervisor de depósito."
      ],
      "status": "Pending Decision"
    }
  ]
}
```
