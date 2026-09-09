---
name: bpmn-extractor
description: >-
  Modela procesos de negocio a partir de narrativas, entrevistas o fichas mediante el perfil BPMN
  usado en Análisis de Sistemas. Produce una ficha institucional y una especificación trazable del BPD
  descriptivo u operacional, audita un modelo existente, valida la concordancia SIPOC ↔ BPD (sipoc-sync)
  o compara cuantitativamente modelos AS-IS vs TO-BE (diff-as-is-to-be). Usa BPMN-IR solo para procesos
  simples de una pool cuando se solicita una vista Mermaid o XML de intercambio no ejecutable. No usar para
  diagramas de flujo genéricos, casos de uso ni automatización de un motor BPMN.
---

# BPMN desde evidencia de negocio

Convertí el trabajo observado en un proceso trazable sin completar con tecnología, reglas, roles o métricas que la fuente no menciona. La fuente autoritativa es la narrativa y, si existe, la ficha institucional; BPMN-IR y los renderers son representaciones derivadas.

## Elegir el producto antes de modelar

Usá un solo modo por defecto:

1. `course-process` — ficha institucional y especificación lista para modelar el BPD de una entrega de Análisis de Sistemas. Es el modo predeterminado. Entregá el BPD gráfico solo si hay una herramienta BPMN capaz de representarlo; Mermaid no lo sustituye y el XML sin BPMNDI no conserva su disposición visual.
2. `ir-preview` — JSON BPMN-IR y, a elección, Mermaid o XML de modelo. Solo para el subconjunto soportado por el script.
3. `audit` — diagnóstico de un modelo existente con evidencia, impacto y corrección propuesta. No mutar el original salvo pedido explícito.
4. `sipoc-sync` — evaluación de consistencia bidireccional entre la matriz SIPOC y el BPD (asociación unívoca de proveedores, entradas, macroactividades, salidas y clientes con pools, lanes, data objects y tareas).
5. `diff-as-is-to-be` — comparación estructural y cuantitativa entre el proceso actual (AS-IS) y el propuesto (TO-BE), computando variaciones en tareas manuales/automáticas, handoffs entre lanes y compuertas de decisión.

Preguntá por nivel descriptivo u operacional solo si cambia materialmente el resultado y no puede inferirse de la consigna. En nivel descriptivo conservá macroactividades y áreas; en operacional detallá tareas, eventos, decisiones, excepciones y responsables observables.

## Límites de autoridad

- Describí el proceso de negocio, que puede incluir trabajo manual y automatizado. No lo conviertas automáticamente en una solución de software.
- Conservá cada dato como `expreso`, `derivado` o `desconocido`. Una inferencia necesaria debe explicitar su fuente y confianza.
- No inventes sistemas, integraciones, normativa, plazos, fórmulas, KPI, tipos de tarea ni rutas de excepción.
- No transformes una ausencia documental en una regla de negocio. Registrala como pregunta abierta.
- Mermaid es una vista previa del flujo, no notación BPMN interoperable.
- El XML generado por esta skill es un modelo BPMN 2.0 **no ejecutable**, sin BPMNDI, colaboración entre pools, message flows, datos ni extensiones de motor. No prometas importación visual, ejecución o compatibilidad con Camunda/Bizagi.
- Si hacen falta varias pools, message flows, subprocesos, eventos de borde o BPMN ejecutable, modelalos en la herramienta BPMN indicada por el usuario; no los fuerces dentro de BPMN-IR.

## Flujo de trabajo

### 1. Construir un registro de evidencia

Extraé en una pasada:

| ID | Fragmento o localizador | Hecho de proceso | Estado |
|---|---|---|---|
| `EV-01` | fuente y ubicación | actor, actividad, evento, regla o excepción | expreso/derivado/desconocido |

Separá hechos actuales (`as-is`) de cambios deseados (`to-be`). Si la entrada mezcla ambos, no consolides los futuros como si ya operaran.

### 2. Delimitar el proceso

Definí, con evidencia:

- nombre en infinitivo + objeto;
- objetivo;
- cliente y producto/resultado;
- evento inicial y resultados finales;
- roles internos, participantes externos e información intercambiada;
- variantes, excepciones, reglas y restricciones.

Un participante independiente es una pool; un rol o área dentro de la organización es una lane. El flujo de secuencia no cruza pools y el flujo de mensaje no conecta elementos dentro de la misma pool.

### 3. Completar la ficha institucional

Usá [templates/ficha_proceso_template.md](templates/ficha_proceso_template.md). Sus campos base son: nombre, objetivo, cliente, productos, proveedores e insumos, recursos, formularios/registros/información, reglas, restricciones, actividades y excepciones.

- Marcá `TBD` y vinculá la pregunta cuando falte un campo.
- Dueño, clasificación estratégica, SIPOC ampliado e indicadores son extensiones opcionales: incluilos solo si la consigna o la fuente los requiere.
- No redactes ejemplos de normativa o KPI como si fueran datos del caso.

### 4. Derivar el flujo

- Actividad: `verbo en infinitivo + objeto` (`Registrar solicitud`).
- Evento: estado o hecho nominal (`Solicitud recibida`, `Solicitud rechazada`). Evitá prefijos decorativos `Inicio:` y `Fin:`.
- Ubicá la compuerta después de la actividad que obtiene o evalúa la información.
- No escribas una pregunta dentro de la compuerta. Etiquetá sus flujos salientes con condiciones claras y, para XOR, mutuamente excluyentes.
- Usá XOR para una alternativa exclusiva y AND para ramas realmente simultáneas que luego se sincronizan. Usá OR o compuertas basadas en eventos solo cuando la evidencia exija esa semántica.
- Tipá `manualTask`, `userTask`, `serviceTask`, etc. únicamente cuando el modo de ejecución esté documentado; si no, usá tarea genérica.
- Toda excepción debe finalizar, reingresar por un punto explícito o converger de modo semánticamente válido.

Consultá [references/bpmn_taxonomy_and_editing.md](references/bpmn_taxonomy_and_editing.md) solo para elegir un elemento, validar un anti-patrón o usar el subconjunto BPMN-IR.

### 5. Verificar antes de entregar

Comprobá:

- cobertura: cada actividad, decisión, rol y excepción deriva de evidencia;
- límites: inicio, finales, cliente y producto son coherentes;
- semántica: pools/lanes y sequence/message flows no se confunden;
- control: condiciones explícitas, ramas alcanzables y joins compatibles con el split;
- lenguaje: actividades con verbo + objeto y eventos nominales;
- incertidumbre: ningún `TBD` fue convertido en hecho;
- legibilidad: el diagrama responde al nivel solicitado sin detalle técnico accidental.

No declares el modelo “completo”, “certificado” o “ejecutable”. Indicá cobertura y límites concretos.

## Modo BPMN-IR

BPMN-IR representa un proceso white-box único con lanes y sequence flows. Admite tareas, eventos simples/intermedios y gateways XOR/OR/AND anidados. Requiere un único start de nivel superior y al menos un end alcanzable.

1. Partí de [templates/bpmn_process_ir_example.json](templates/bpmn_process_ir_example.json).
2. Contrastalo con [templates/bpmn_json_schema.json](templates/bpmn_json_schema.json) y validá además las restricciones documentadas en la referencia. El script es la implementación autoritativa; [templates/bpmn_xml_skeleton.xml](templates/bpmn_xml_skeleton.xml) es solo una muestra estructural, no una segunda plantilla de generación.
3. Resolvé primero un intérprete Python 3 disponible: `python3`, `python`, `py -3` o
   el runtime provisto por el host. Llamalo `<python-3>` en los comandos siguientes;
   si ninguna opción existe, reportá que la validación no pudo ejecutarse.
4. Desde la raíz de este repositorio ejecutá, con separadores de ruta aceptados por el
   host:

```text
<python-3> bpmnExtractor/scripts/bpmn_ir_transformer.py bpmnExtractor/templates/bpmn_process_ir_example.json --format mermaid
<python-3> bpmnExtractor/scripts/bpmn_ir_transformer.py bpmnExtractor/templates/bpmn_process_ir_example.json --format xml
```

Elegí un formato; `--format both` solo si el usuario pide ambos. La validación del script cubre estructura, IDs/referencias y alcanzabilidad del grafo soportado, no conformidad BPMN completa ni calidad del proceso.

## Modo SIPOC-Sync

Usalo para auditar la concordancia entre la matriz SIPOC y el BPD (asociación unívoca y detección de brechas):
1. Partí de la plantilla [templates/sipoc_sync_template.md](templates/sipoc_sync_template.md).
2. Verificá que cada **S** (Proveedor) corresponda a una Pool externa o Lane remitente.
3. Verificá que cada **I** (Insumo) ingrese como Data Object, Message Flow o evento disparador.
4. Verificá que cada **P** (Proceso macro) contenga un bloque de tareas coherente en el BPD.
5. Verificá que cada **O** (Salida) sea producida explícitamente por una actividad del BPD.
6. Verificá que cada **C** (Cliente) reciba la salida correspondiente (Lane o Pool receptora).
7. Reportá insumos huérfanos, salidas no producidas o inconsistencias de fronteras.

## Modo Diff AS-IS vs TO-BE

Usalo para evaluar cuantitativa y cualitativamente el impacto de las mejoras propuestas:
1. Partí de la plantilla [templates/diff_as_is_to_be_template.md](templates/diff_as_is_to_be_template.md).
2. Computá las métricas estructurales: total de actividades, tareas manuales (`manualTask`), tareas asistidas (`userTask`), tareas automáticas (`serviceTask`), handoffs entre lanes, y compuertas de decisión (`gateways`).
3. Enumerá el inventario de modificaciones: actividades eliminadas (desperdicio Lean), tareas automatizadas, y nuevas actividades de valor o control preventivo.
4. Identificá la reducción de fricción y tiempos de espera en los traspasos entre roles.

## Contrato de salida

Entregá, en este orden:

1. `Alcance y nivel` — modo (`course-process`, `ir-preview`, `audit`, `sipoc-sync`, `diff-as-is-to-be`), as-is/to-be, límites y fuentes.
2. `Ficha / Matriz` — en `course-process` la ficha de proceso; en `sipoc-sync` la matriz de sincronización; en `diff-as-is-to-be` la tabla comparativa cuantitativa y análisis de handoffs.
3. `Modelo` — la especificación del BPD y, si se produjo con una herramienta BPMN, el BPD gráfico; en `ir-preview`, un único formato derivado.
4. `Trazabilidad` — elementos relevantes ↔ IDs de evidencia/reglas/acciones de valor.
5. `Hallazgos` — errores confirmados, posibles problemas y aspectos no verificables.
6. `Preguntas abiertas` — solo las que cambian el proceso.

En una auditoría, cada hallazgo debe incluir localizador, regla aplicada, impacto, confianza y corrección propuesta. Aplicá cambios al modelo únicamente después de identificar qué artefacto es autoritativo.

