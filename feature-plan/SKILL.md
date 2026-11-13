---
name: feature-plan
description: Prepara, revisa o actualiza el plan implementable de una feature o incremento concreto desde requisitos y evidencia del proyecto. Integra alcance, decisiones, contratos, dependencias y aceptación. Úsala para planificar una entrega específica; no para definir por sí sola todo el roadmap ni para sustituir una implementación ya solicitada.
---

# Feature Plan

Convertir una necesidad acotada en un plan que otro agente pueda ejecutar sin inventar reglas ni redescubrir decisiones. El plan debe explicar qué cambia, por qué, qué se reutiliza, cómo se integra y qué evidencia permitirá aceptarlo.

## Encargo y tamaño

Identificar si se pide crear, revisar o actualizar un plan. Conservar el objetivo, formato, destino y autorización de la conversación.

- Si sólo se pidió planificación, entregar el plan y su estado; no implementar la feature.
- Si también se pidió implementar, usar el plan como preparación y continuar con el alcance autorizado. Esta skill no introduce una aprobación adicional entre tareas internas.
- Si se pide revisar, devolver hallazgos y correcciones propuestas; editar el plan sólo cuando esté solicitado o autorizado.
- Un ajuste pequeño puede resolverse con unos párrafos y tareas. Separar diseños sólo cuando su volumen, responsabilidades o ciclo de mantenimiento lo justifiquen.

No imponer stack, arquitectura, número de agentes, etapas numeradas, estimaciones ni artefactos. Adaptar idioma, términos y convenciones al proyecto.

## Recuperar la base pertinente

Consultar las instrucciones aplicables, el estado reciente y las fuentes funcionales del incremento. Identificar sus equivalentes disponibles: conversación, tickets, documentación, decisiones de arquitectura, contratos, código, pruebas y memoria de trabajo. No exigir archivos con nombres predeterminados ni crear un sistema documental completo para poder planificar.

Si existe repositorio, comprobar revisión/branch, cambios locales y la implementación afectada con las herramientas de descubrimiento disponibles y las preferencias del proyecto. Preservar trabajo ajeno; planificar no requiere por sí mismo cambiar de branch, crear un worktree ni modificar código.

Distinguir:

- **Necesidad y decisión aprobada:** lo que el producto debe hacer y quién lo decidió.
- **Estado observado:** lo que el código, los contratos y las pruebas existentes muestran hoy.
- **Evidencia histórica:** una comprobación anterior con fecha, entorno y alcance propios.

El código demuestra comportamiento existente; no decide por sí solo la regla de negocio correcta. Cuando diverge de una decisión vigente, explicar la brecha. Un diseño o una pantalla de demostración no acredita persistencia real; un informe anterior de tests no acredita una nueva ejecución.

Sin repositorio o con acceso parcial, planificar con las fuentes disponibles y localizar las verificaciones pendientes. No presentar módulos, rutas, comandos o estado remoto supuestos como comprobados. Leer sólo el contexto que cambia decisiones del incremento.

## Delimitar y resolver decisiones

Expresar el escenario de usuario, resultado observable, alcance incluido, exclusiones relevantes y dependencias. Si proviene de un workplan, conservar la referencia al hito/incremento y sus condiciones de entrada; no exigir ese antecedente a una tarea independiente. Verificar lo que ya existe antes de agregar tareas. No avanzar a otra feature por su posición en el roadmap.

Separar los pendientes según su naturaleza:

| Pendiente | Tratamiento |
|---|---|
| Información que puede inspeccionarse | Buscarla en las fuentes disponibles antes de preguntar. |
| Elección técnica interna | Resolverla con criterio y explicar el motivo cuando afecte el plan. |
| Decisión funcional o restricción no definida | Localizar su impacto, presentar alternativas útiles y preguntar sólo si cambia materialmente el resultado o bloquea trabajo. |

Registrar procedencia de las decisiones importantes y señalar propuestas como tales. No inventar permisos, obligatoriedad de campos, políticas de retención, límites numéricos o reglas para completar una plantilla.

Una duda bloquea las tareas que dependen de ella, no necesariamente toda la feature. Preparar y continuar trabajo independiente autorizado. No volver a pedir una decisión ya recibida; comprobar si la instrucción actual adopta propuestas del plan.

## Integrar perspectivas y contratos

Cubrir las perspectivas que cambian el resultado: producto, interacción, aplicación/integración, datos u operación según el caso. Usar skills especializadas disponibles cuando aporten y subagentes cuando sus tareas sean independientes; no requerir un equipo fijo ni paquetes concretos para funcionar.

Al delegar, dar el alcance, fuentes pertinentes y una pregunta o producto acotado. Consolidar los hallazgos: resolver diferencias, no concatenar informes.

Para cada frontera afectada, acordar lo necesario antes de paralelizar trabajo dependiente:

- propietario del dato y fuente autoritativa;
- operación, entradas/salidas, estados y errores relevantes;
- compatibilidad con consumidores y comportamiento existente;
- autorización, concurrencia, idempotencia o temporalidad cuando el caso lo requiera.

Mantener una definición de referencia por contrato compartido; enlazarla desde los demás diseños. Si se propone cambiar un contrato vigente, identificar consumidores e impacto y definir cómo convivirán las versiones cuando corresponda. Invocar una especialidad no autoriza a reemplazar convenciones del proyecto.

Resolver incompatibilidades que afecten la implementación o dejarlas como decisiones localizadas con las tareas dependientes pendientes. No crear endpoints, tablas, migrations, diagramas o documentos separados por obligación de formato.

## Convertir el diseño en trabajo comprobable

Ordenar tareas por dependencias y riesgo. Cada tarea debe conectar la decisión o necesidad que satisface con un cambio concreto y una comprobación de salida. Usar IDs y responsables sólo cuando faciliten seguimiento o colaboración.

Distinguir el incremento funcional de las tareas técnicas por capas. Una tarea de datos o UI puede ser preparatoria; indicar dónde se prueba el recorrido integrado. El paralelismo requiere contratos suficientemente acordados y límites de edición claros.

Derivar aceptación de comportamientos observables y de fallos relevantes. Incluir regresiones afectadas y datos sintéticos cuando correspondan. Obtener comandos de validación del proyecto; distinguir pruebas propuestas, código de pruebas inspeccionado y comprobaciones realmente ejecutadas. No ejecutar suites completas ni crear fixtures por defecto para redactar un plan; hacerlo cuando las instrucciones del proyecto o una incertidumbre concreta lo justifiquen.

Evaluar transición de datos, despliegue, recuperación y medición sólo si el cambio los necesita. Una migration puede ser innecesaria. No prometer SLA o rendimiento productivo a partir de una estimación o una medición local.

## Entregar o actualizar el plan

Usar [Formato adaptable y ejemplos](references/plan-format.md) al estructurar un plan nuevo o cuando el existente resulte insuficiente. Es una guía, no un conjunto obligatorio de secciones.

Reutilizar el documento y destino existentes. Si no se acordó persistencia y no hay una convención aplicable, entregar en la conversación. No duplicar el mismo plan en varias fuentes. Actualizar la memoria del proyecto conforme a sus reglas, preservando historia y separando estado vigente de antecedentes.

Ante una nueva decisión, identificar y actualizar los contratos, tareas, dependencias y criterios de aceptación afectados. Si cambia una regla o un compromiso del producto, reconciliar también la fuente funcional y el workplan afectados dentro del alcance autorizado. Si sólo se identificó una alternativa o un impacto fuera del encargo, dejarlo como propuesta o pendiente con su destino, sin repriorizar por cuenta propia. Retirar instrucciones vigentes incompatibles; conservar antecedentes sólo con contexto suficiente para no confundirlos con el plan actual.

Antes de cerrar, comprobar:

1. El alcance permite decidir qué trabajo pertenece a esta entrega.
2. Cada tarea lista puede empezar sin inventar reglas funcionales; los bloqueos están localizados.
3. Los contratos necesarios son consistentes y la secuencia permite integrar el escenario completo.
4. La aceptación comprueba resultados y riesgos pertinentes.
5. Las fuentes, decisiones, comprobaciones realizadas y siguiente acción permiten retomar el trabajo.

Informar si el plan está listo, listo parcialmente o pendiente de decisiones, indicando qué se puede iniciar y qué falta. Ese estado describe preparación técnica, no aceptación humana ni autorización operacional. Un dictamen de un agente no concede permiso de merge, migration remota o deploy. Distinguir esas dimensiones sólo en la medida en que formen parte del encargo.

Para pasar a ejecución, entregar alcance autorizado, base comprobada, decisiones y contratos de referencia, tareas listas/bloqueadas y aceptación. `feature-delivery` puede usar ese contexto si está disponible; no es una dependencia ni exige otro archivo. Si la ejecución ya está solicitada, continuar con lo autorizado conservando los pendientes; si sólo se pidió el plan, este handoff no autoriza implementarlo.
