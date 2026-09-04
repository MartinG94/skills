# Perfil BPMN y contrato BPMN-IR

Cargá esta referencia únicamente cuando debas escoger elementos BPMN, revisar un defecto semántico o ejecutar el transformador. No es una especificación completa de OMG BPMN.

## Perfil de modelado

| Elemento | Usarlo cuando | Evitar cuando |
|---|---|---|
| `task` | Se conoce la unidad de trabajo, no su mecanismo | Se está suponiendo automatización |
| `manualTask` | Una persona actúa sin una aplicación | Solo se sabe que interviene una persona |
| `userTask` | Una persona usa una aplicación | La aplicación no está documentada |
| `serviceTask` | La ejecución automática está confirmada | Solo se menciona “el sistema” |
| `sendTask` / `receiveTask` | El envío o espera es la tarea misma | Basta un evento o una tarea genérica |
| `businessRuleTask` | Está documentado un motor/servicio de reglas | Existe una regla de negocio, sin motor |
| `scriptTask` | Un motor BPMN ejecutará un script concreto | Se modela un cálculo de negocio conceptual |

Eventos admitidos por el IR: `startEvent`, `endEvent`, `intermediateCatchEvent` e `intermediateThrowEvent`. `timerEventDefinition` solo se admite en eventos de captura (`startEvent` e `intermediateCatchEvent`); `messageEventDefinition`, en los cuatro tipos. El detalle temporal o del mensaje no se vuelve ejecutable por declararlo en el IR.

Gateways:

- XOR: exactamente una condición de salida verdadera; puede tener una única ruta por defecto documentada.
- OR: una o más condiciones verdaderas; puede tener una única ruta por defecto documentada.
- AND: todas las ramas se activan y deben alcanzar el join; no encierra decisiones.

## Controles semánticos mínimos

- Una actividad usa verbo en infinitivo + objeto; un evento expresa un hecho/estado nominal.
- La compuerta no contiene la pregunta de negocio: las condiciones viven en los flujos salientes.
- Un sequence flow permanece dentro de una pool; un message flow cruza participantes.
- Una lane representa rol o área interna, no otra organización.
- No agregues un join por simetría visual: usalo si las rutas continúan en un punto común y la semántica lo requiere.
- Un end dentro de una rama paralela impediría el join en el subconjunto IR y no está permitido.

## Anti-patrones verificables

| Código | Problema | Comprobación/corrección |
|---|---|---|
| `BPMN-01` | Sequence flow entre pools | Reemplazar por message flow si existe interacción documentada |
| `BPMN-02` | Message flow dentro de una pool | Usar sequence flow |
| `BPMN-03` | Actividad o evento sin evidencia | Retirar o marcar como hipótesis |
| `BPMN-04` | Condiciones XOR solapadas o ausentes | Precisar condiciones o registrar TBD |
| `BPMN-05` | Rama sin salida | Finalizar, converger o volver explícitamente |
| `BPMN-06` | AND usado como decisión | Sustituir por el gateway correspondiente |
| `BPMN-07` | Rol modelado como pool | Convertirlo en lane |
| `BPMN-08` | Tecnología inferida | Volver a tarea genérica hasta obtener evidencia |

## Subconjunto BPMN-IR

El archivo raíz contiene `id`, `name` y `process`; `process` es una lista secuencial. Los gateways anidan `branches`:

- XOR/OR: objetos `{condition?, path, next?, is_default?}`. Una rama no predeterminada requiere `condition`; `is_default: true` identifica como máximo una rama por gateway y no se combina con `condition`.
- AND: listas `path`; el transformador crea el join.
- `next` apunta a un ID explícito del mismo modelo y permite salida o bucle; no se admite dentro de una rama AND porque podría evitar su sincronización.
- `has_join` crea `<gateway_id>_join`; ese ID queda reservado.

Restricciones comprobadas por el script:

- IDs explícitos y generados globalmente únicos y aptos para XML/Mermaid, incluidos proceso, lanes, flows, joins y definiciones de evento;
- una única entrada `startEvent` como primer elemento de nivel superior y sin flujos entrantes;
- ramas mínimas y tipos soportados;
- destinos `next` existentes;
- IDs de flujo y referencias válidos después de aplanar;
- nodos alcanzables desde el inicio y con al menos un camino a un end.

El transformador no representa múltiples pools, message flows, objetos de datos, subprocesos, boundary events, event subprocesses, BPMNDI ni expresiones ejecutables. El XML usa `isExecutable="false"`; las condiciones son nombres legibles de sequence flows. La vista Mermaid antepone `P_`, `L_` y `N_` a IDs de proceso, lanes y nodos para evitar palabras reservadas sin perder su correspondencia; rotula ramas predeterminadas y distingue eventos de temporizador/mensaje de forma textual.

## Edición de modelos existentes

No existe un “change engine” en esta skill. Para una modificación:

1. identificá el elemento por ID y la fuente del cambio;
2. proponé el diff semántico;
3. modificá el JSON solo si el usuario pidió cambiarlo;
4. reejecutá el validador y compará cobertura/trazabilidad;
5. conservá un registro de elementos agregados, modificados o retirados.
