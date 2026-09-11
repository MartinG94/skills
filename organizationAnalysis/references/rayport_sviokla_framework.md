# Marco Teórico: Cadena de Valor Virtual (Rayport & Sviokla) y Lógica Dominante del Servicio (SDL)

Este documento compendia los fundamentos conceptuales de la **Cadena de Valor Virtual** para su aplicación en la Etapa 1 de **Gestión y Mejora de Procesos (GMP)**, integrando la teoría seminal de **Jeffrey F. Rayport y John J. Sviokla** (Harvard Business Review, 1995), el apunte de cátedra oficial **APU_U1_Cadena_de_Valor_Virtual.pdf** (UTN-FRC, Ing. Gabriela Bratti) y los aportes de **Stephen L. Vargo y Robert F. Lusch** (2004, 2008) sobre la **Lógica Dominante del Servicio (SDL)**.

---

## 1. Del Marketplace al Marketspace

En la economía contemporánea las organizaciones operan simultáneamente en dos mundos económicos paralelos:

1. **Marketplace (Espacio Físico):** El ámbito tangible donde actúan los recursos materiales, vehículos, plantas industriales, depósitos e infraestructura física. En este espacio rige la **Cadena de Valor Tradicional** (Michael Porter, 1985), compuesta por una secuencia lineal de actividades primarias (logística interna, operaciones, logística externa, marketing/ventas y servicios posventa) que transforman insumos físicos en productos manufacturados.
2. **Marketspace (Espacio Virtual):** El ámbito digital de la información, el software y las redes de telecomunicaciones. Aquí las transacciones, la coordinación y la creación de valor se desarrollan a través de flujos electrónicos y datos estructurados.

### El Doble Rol de la Información
- **Rol de Soporte en la Cadena Real:** Tradicionalmente, la información era considerada un costo administrativo o un insumo accesorio de apoyo (remitos en papel, fichas de inventario, llamadas de coordinación) subordinado a la circulación de bienes físicos.
- **Rol de Activo Estratégico en la Cadena Virtual:** En el *marketspace*, la información se emancipa del bien tangible. El flujo de datos que refleja el proceso físico es capturado y procesado sistemáticamente para generar una **propuesta de valor informacional independiente** que los clientes reconocen, valoran y demandan.

---

## 2. Los 5 Procesos Canónicos de Transformación de Información

A diferencia de la cadena física que procesa materia prima, la **Cadena de Valor Virtual** ejecuta una secuencia estricta de cinco operaciones sobre los datos:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 1.Recopilar │ ──> │ 2.Organizar │ ──> │ 3.Seleccionar│ ──> │ 4.Sintetizar│ ──> │ 5.Distribuir│
│  (Gather)   │     │  (Organize) │     │   (Select)  │     │ (Synthesize)│     │ (Distribute)│
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### 1. Recopilar / Recogida (Gather)
- **Definición de Cátedra:** Captura inicial de datos brutos directamente en el punto físico donde se originan las operaciones de negocio.
- **Objetivo:** Digitalizar los eventos del mundo real con la mayor inmediatez, fidelidad y menor intervención manual posible.
- **Tecnologías:** Dataloggers IoT, telemetría vehicular, lectores RFID, escaneo de códigos de barra o QR, formularios móviles y webhooks.

### 2. Organizar / Organización (Organize)
- **Definición de Cátedra:** Almacenamiento estructurado, limpieza, validación, tipificación y normalización de los datos capturados.
- **Objetivo:** Convertir datos heterogéneos y dispersos en repositorios consistentes, catalogados y auditables.
- **Tecnologías:** Bases de datos relacionales (PostgreSQL), Data Lakes unificados, pipelines ETL/ELT y modelos de Master Data Management (MDM).

### 3. Seleccionar / Selección (Select)
- **Definición de Cátedra:** Extracción, filtrado y segmentación de datos específicos en función del contexto operativo o decisorio.
- **Objetivo:** Aislar la información crítica o las excepciones operativas del "ruido" de datos masivos.
- **Tecnologías:** Vistas materializadas indexadas, consultas SQL optimizadas, motores de Complex Event Processing (CEP) y suscripciones a tópicos de eventos.

### 4. Sintetizar / Síntesis / Integración (Synthesize)
- **Definición de Cátedra:** Agregación, combinación multivariable, correlación matemática y modelado analítico de los datos seleccionados.
- **Objetivo:** Transformar datos aislados en **conocimiento accionable**, predicciones e indicadores de desempeño (KPIs).
- **Tecnologías:** Tableros de Business Intelligence (BI) en tiempo real, algoritmos de predicción (ETA), scoring de riesgo y cálculo dinámico de OTIF y OEE.

### 5. Distribuir / Distribución (Distribute)
- **Definición de Cátedra:** Entrega contextualizada de la información procesada al destinatario adecuado (cliente, supervisor, sistema externo) en el formato y momento oportunos.
- **Objetivo:** Cerrar el ciclo de valor habilitando la toma de decisiones informada, la mitigación de fallas o la satisfacción del cliente final.
- **Tecnologías:** Portales de autoservicio B2B/B2C, notificaciones push móviles, webhooks a ERPs y APIs REST públicas o privadas.

---

## 3. Las 3 Fases de Madurez de la Cadena de Valor Virtual

Las organizaciones adoptan los procesos de valor agregado de la información en tres etapas evolutivas:

```
┌─────────────────────────────────────────────────────────────────┐
│ Fase 3: La Matriz del Valor / Nuevas Relaciones con Clientes    │
│ (Co-creación de valor, servitización, nuevos modelos digitales) │
├─────────────────────────────────────────────────────────────────┤
│ Fase 2: Proyección de la Capacidad / Capacidad de Reflejo       │
│ (Reemplazo de tareas físicas por flujos virtuales paralelos)    │
├─────────────────────────────────────────────────────────────────┤
│ Fase 1: Visibilidad (Visibility)                                │
│ (Monitoreo y transparencia de operaciones físicas mediante TI)  │
└─────────────────────────────────────────────────────────────────┘
```

### Primera Etapa: Visibilidad (Visibility)
- **Concepto:** Las empresas utilizan sistemas tecnológicos de información para adquirir la habilidad de "ver" y coordinar sus operaciones físicas de manera más eficiente.
- **Mecanismo:** La cadena física sigue funcionando de forma tradicional, pero se torna transparente y medible en tiempo real a través de telemetría y registros sistemáticos.
- **Diagnóstico:** Si la iniciativa únicamente supervisa el estado actual de un recurso u operación física (ej. "el lote está en la cámara frigorífica"), se sitúa en Fase 1.

### Segunda Etapa: Proyección de la Capacidad (Capacidad de Reflejo / Mirroring Capability)
- **Concepto:** Las organizaciones sustituyen actividades físicas o manuales por actividades virtuales equivalentes, construyendo una cadena de valor paralela en el mercado.
- **Mecanismo:** Procesos que exigían presencia física, planillas de papel, controles visuales humanos o traslados se resuelven íntegramente en el *marketspace* mediante simulaciones, reglas de negocio automáticas o autoservicio digital.
- **Diagnóstico:** Si la iniciativa reemplaza un formulario en papel, una llamada telefónica o una revisión manual por un flujo digital automatizado, pertenece a Fase 2.

### Tercera Etapa: La Matriz del Valor (Nuevas Relaciones con Clientes / New Customer Relationships)
- **Concepto:** Los administradores diseñan flujos de información continuos aplicando los 5 procesos de valor agregado para entregar valor en formas inéditas, transformando la relación comercial en una alianza colaborativa.
- **Mecanismo:** La información sintetizada permite la personalización masiva, la co-creación de valor en tiempo real y la servitización de los productos físicos.
- **Diagnóstico:** Si la iniciativa ofrece al cliente predicciones proactivas, certificaciones digitales compartidas o plataformas de autogestión que redefinen el modelo de negocio, se ubica en Fase 3.

---

## 4. La Matriz del Valor: Cruce de la Cadena Real con la Cadena Virtual

Según expone el apunte de cátedra oficial (**APU_U1 Secciones 10.c y 18**), las cadenas real y virtual deben articularse como un método de análisis matricial:

> *"Sitúe su cadena de valor física, fase por fase, en un eje, y las cinco etapas de la cadena de valor virtual en el otro, y trate de identificar, repasando fase a fase en la cadena física, qué actividades le permiten recoger información, organizarla, seleccionarla y sintetizarla de manera que le reporte algo cognoscible, y distribuirla si procede."*

Esta perspectiva matricial permite:
1. **Identificar oportunidades desaprovechadas:** Detectar qué fases físicas generan datos valiosos que hoy se pierden o se archivan en papel sin ser explotados.
2. **Eliminar puntos ciegos:** Asegurar que cada eslabón crítico de la operación física cuente con captura fidedigna y mecanismos de alerta temprana.
3. **Potenciar la servitización:** Convertir actividades internas de control en servicios de valor agregado de cara al cliente final.

---

## 5. Desintermediación y Canales en la Era Post-Internet

El apunte **APU_U1 (Secciones 12 y 13)** analiza las consecuencias estructurales de la cadena de valor virtual sobre la circulación de bienes y la comercialización de servicios:

- **Desintermediación en Bienes:** Internet permite a los productores relacionarse directamente con el consumidor final o con las instituciones destinatarias, prescindiendo de intermediarios tradicionales que no aporten valor informacional diferenciado.
- **Comercialización de Servicios:** En el sector terciario y de servicios especializados, la cadena virtual permite crear vínculos de confianza basados en datos inmutables y trazabilidad en vivo, transformando a los operadores logísticos o asistenciales en socios indispensables del ecosistema.
- **Intranets y Valor Interno vs. Externo (Secciones 14 y 15):** La cadena virtual opera en dos dimensiones complementarias:
  - *Dimensión Interna (Intranets / ERP):* Eficiencia operativa, coordinación interdisciplinaria, reducción de tiempos muertos y automatización de flujos de trabajo.
  - *Dimensión Externa (Internet / Portales / APIs):* Satisfacción del cliente, transparencia, valor de marca y retención basada en la experiencia digital (*Value-in-Use*).

---

## 6. Articulación con la Lógica Dominante del Servicio (SDL)

La **Lógica Dominante del Servicio** (Service-Dominant Logic - SDL), formulada por **Stephen L. Vargo y Robert F. Lusch** (2004, 2008), provee la fundamentación epistemológica para la Cadena de Valor Virtual en GMP:

| Dimensión Analítica | Lógica Tradicional de Bienes (GDL) | Lógica Dominante del Servicio (SDL) |
|---|---|---|
| **Tipo de Recurso Primario** | **Operand Resources (Recursos Operandos):** Bienes tangibles estáticos (vehículos, depósitos, máquinas) que requieren de una acción externa para producir valor. | **Operant Resources (Recursos Operantes):** Conocimiento, habilidades, información dinámica y algoritmos capaces de actuar sobre otros recursos para crear valor continuo. |
| **Rol de la Cadena Virtual** | Costo administrativo secundario o gasto operativo de supervisión física. | Infraestructura estratégica fundamental que procesa recursos operantes para generar ventaja competitiva. |
| **Generación de Valor** | Producido unilateralmente en la fábrica e incrustado en el producto antes de la transacción (*Value-in-Exchange*). | Co-creado continuamente entre la organización y el beneficiario en el momento de la utilización (*Value-in-Use*). |
| **Rol del Cliente** | Destinatario pasivo y terminal de la entrega física. | Co-creador activo de valor que interactúa con la plataforma de información para optimizar sus propias decisiones. |

### Implicancia Metodológica para GMP Etapa 1
Al estructurar la Matriz de la Cadena de Valor Virtual, el ingeniero de procesos debe guiar a la organización para que transite de vender meros *recursos operandos* (ej. "mover cajas frías") a prestar un **servicio integral basado en recursos operantes** (ej. "garantizar la viabilidad terapéutica de los fármacos en quirófano con certificación digital en tiempo real"), asegurando la relevancia estratégica de la posterior selección del proceso crítico.
