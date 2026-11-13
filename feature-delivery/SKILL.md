---
name: feature-delivery
description: Implementa, continúa, revisa o cierra un incremento de software autorizado desde un plan o criterios suficientes. Contrasta trabajo heredado, integra cambios, valida el comportamiento y deja evidencia y handoff. Úsala para ejecutar o comprobar una entrega concreta; no para redefinir el roadmap ni para convertir una revisión sola en permiso de modificar código.
---

# Feature Delivery

Llevar el incremento encargado hasta su resultado comprobable, preservando decisiones, trabajo previo y límites de autorización. La salida depende del pedido: implementación validada, revisión con hallazgos o cierre con evidencia; no una promesa de hacerlo después.

## Precisar el trabajo autorizado

Identificar si se pide implementar/continuar, revisar, corregir o cerrar una entrega. Conservar instrucciones y autorizaciones ya recibidas en la conversación.

- Un pedido de implementación autoriza los cambios y comprobaciones necesarios dentro de su alcance; no detenerse en el plan ni pedir aprobación entre tareas internas ya cubiertas.
- Una revisión sola produce hallazgos y evidencia. Corregir código cuando el encargo también lo autorice; no convertir la revisión en una reescritura.
- Un cierre puede requerir únicamente comprobar estado y documentarlo. No reconstruir una feature ya entregada.
- Commit, PR, merge, cambios remotos y deploy dependen del alcance autorizado. No deducir ese permiso de un documento histórico, un checklist verde o un dictamen de otro agente; tampoco pedirlo de nuevo si sigue vigente.

Usar el plan existente o los criterios de aceptación suficientes. No exigir un archivo de plan para un cambio pequeño. Si falta diseño relevante, resolver lo necesario dentro del encargo; `feature-plan` puede ayudar si está disponible, sin ser una dependencia obligatoria.

## Reconstruir la base y preservar trabajo

Leer instrucciones locales, decisiones funcionales y estado reciente pertinentes. Identificar código, contratos, pruebas y procedimientos existentes con las herramientas disponibles y las preferencias del proyecto. No exigir carpetas, stack, sistema de memoria ni comandos predeterminados.

Cuando exista Git, comprobar revisión/branch, historial relevante, status y diff antes de editar. Distinguir cambios heredados de los propios y preservar su contenido. Reutilizar el checkout adecuado; crear branch o worktree sólo cuando el encargo, las reglas locales o el aislamiento necesario lo justifiquen.

Conservar del plan recibido su alcance, decisiones, contratos, tareas listas/bloqueadas y aceptación; comprobar su vigencia sin reiniciar toda la planificación. Contrastar el plan y los reportes con la implementación real. El código demuestra lo existente, no sustituye una regla aprobada. Una afirmación histórica de tests, UAT o deploy conserva su fecha, entorno y procedencia; no cuenta como comprobación de esta intervención.

Antes de integrar trabajo ajeno, revisar sus contratos y comportamiento con el mismo criterio que el propio. Si hay ediciones concurrentes, coordinar la frontera de archivos o integrar sobre el estado vigente; no restaurar versiones anteriores para borrar un diff que no se reconoce.

## Ejecutar e integrar el incremento

Relacionar cada cambio con un requisito, decisión o fallo del alcance. Ordenar por dependencias y comprobar resultados intermedios relevantes. Los cambios pueden organizarse por capas, pero debe verificarse el recorrido integrado que el usuario pidió.

Reutilizar patrones y componentes del proyecto. Mantener compatibles los contratos compartidos o ejecutar la transición aprobada. Revisar que productores, consumidores y persistencia coincidan en nombres, tipos, estados, errores y responsabilidades relevantes.

Cubrir, según el caso, autorización, aislamiento, integridad, concurrencia, errores recuperables, accesibilidad y continuidad del flujo. Elegir los controles que requieren el comportamiento y los riesgos; no imponer un catálogo completo a una tarea pequeña.

Si se usan subagentes, asignar alcance, fuentes, límites de edición y resultado comprobable. Paralelizar trabajo independiente; acordar contratos antes de integrar. Inspeccionar el resultado y resolver contradicciones: una declaración de «terminado» no reemplaza la evidencia.

Separar impedimentos:

| Situación | Acción |
|---|---|
| Dato disponible pero no inspeccionado | Investigar antes de preguntar. |
| Elección técnica interna | Resolverla respetando arquitectura y compatibilidad. |
| Decisión funcional nueva | Localizar impacto, preguntar lo necesario y continuar trabajo independiente autorizado. |
| Problema ajeno al incremento | Registrar evidencia e impacto; corregir sólo si está autorizado o es indispensable para completar el alcance de forma compatible. |
| Falta de acceso o herramienta | Completar lo posible y dejar la comprobación pendiente con su causa y forma de retomarla. |

No introducir reglas para hacer pasar un caso, ni extenderse al próximo incremento. Si el diseño aprobado no puede implementarse como estaba previsto, explicar la divergencia y ajustar lo técnicamente resoluble; pedir decisión sólo sobre el cambio funcional o de alcance que realmente la requiera.

## Validar el resultado real

Obtener los comandos y gates del proyecto. Ejecutar los obligatorios y las comprobaciones pertinentes al cambio: pruebas de comportamiento, contratos, regresiones, integración, UI o datos según corresponda. Si una acción de validación modifica un entorno, comprobar que ese entorno y efecto estén dentro del alcance autorizado.

Preferir pruebas que detecten fallos de comportamiento. Agregar o modificar tests cuando aporten cobertura del riesgo; no imponer TDD, framework, porcentaje ni tests que sólo reflejen la implementación. Un ajuste reversible de bajo impacto puede verificarse sin tests nuevos, respetando los gates locales.

Si algo falla, investigar antes de atribuirlo. Distinguir defecto introducido, fallo heredado comprobado e impedimento ambiental; sin evidencia suficiente, mantener la causa abierta. Corregir lo propio y repetir la comprobación afectada. Un fallo previo puede limitar el cierre aunque no haya sido causado por esta entrega.

No borrar tests, debilitar expectativas correctas ni ocultar advertencias para obtener verde. Tampoco ejecutar reintentos idénticos indefinidamente: antes de repetir, formular una causa, cambiar una condición pertinente o buscar evidencia adicional. Registrar límites cuando el fallo no pueda resolverse en el alcance.

Tras el último cambio, asegurar que la evidencia cubra el estado entregado y las dependencias afectadas. Conservar resultados anteriores sólo donde los cambios posteriores no los invaliden. No repetir suites ya satisfactorias sin un cambio, fallo o incertidumbre que lo justifique.

Revisar el diff final y el status: cambios ajenos preservados, compatibilidad, archivos generados, secretos y ampliaciones accidentales de alcance. La inspección estática, una prueba focal y una suite completa acreditan cosas distintas.

## UAT y operación cuando correspondan

La validación técnica no constituye aceptación humana. Si el producto requiere UAT, preparar el recorrido y un entorno adecuado con datos sintéticos o anonimizados. Registrar aceptación sólo cuando provenga del usuario o de una persona con autoridad explícitamente delegada. No hacer depender una tarea pequeña de UAT si el encargo y el proyecto no la requieren.

Ante feedback, distinguir defecto y cambio de decisión. Corregir lo autorizado y revalidar su impacto. Durante el diseño, la implementación o la UAT, propagar decisiones aprobadas a la fuente funcional, el plan de feature y los contratos afectados; reflejar también su efecto en hitos, dependencias o aceptación del workplan cuando corresponda. Actualizar sólo lo autorizado y enlazar las fuentes, sin copiar el estado operacional en cada plan. Si un hallazgo requiere nuevas prioridades o alcance, devolver evidencia y alternativas como propuesta para `product-workplan` o `feature-plan`, si están disponibles, sin iniciar otro incremento. Una aceptación global no demuestra que alguien ejecutó cada caso individual.

Para cambios de datos o liberación, seguir los procedimientos reales del proyecto y la autorización vigente. Comprobar destino y revisión, precondiciones, compatibilidad y mecanismo de recuperación adecuados antes de mutar. Una migration creada no está aplicada; un merge no es un deploy. Si la operación está autorizada, ejecutarla y verificar su resultado sin dejarla en propuesta. Si el estado de una mutación es incierto, inspeccionarlo antes de reintentar para evitar duplicarla.

Si la operación requiere autorización aún ausente, terminar primero la preparación verificable y presentar la acción concreta pendiente. No abrir un flujo de permisos para acciones ya cubiertas ni usar el cierre técnico como autorización implícita.

## Cerrar con evidencia y continuidad

Al revisar trabajo heredado o preparar el cierre, usar [Revisión y handoff](references/review-and-handoff.md) si hace falta estructurar hallazgos o separar estados operacionales.

Actualizar la memoria según las reglas del proyecto; si tiene estado consolidado e historial, reconciliar ambos cuando cambie el estado y preservar las sesiones previas. No crear por defecto un archivo de progreso ni duplicar la misma información en varios documentos. Sin convención de persistencia, dejar el handoff en la respuesta.

Informar resultado, qué cambió, cómo se comprobó, qué permanece pendiente y la siguiente acción. En una revisión, priorizar hallazgos accionables con ubicación e impacto; si no se encontraron, declarar los límites de lo revisado.

Considerar completa la entrega sólo cuando se completó el alcance autorizado y su validación requerida. Si queda trabajo solicitado sin resolver, informar estado parcial o bloqueado con su causa y el trabajo restante; documentar un pendiente no lo convierte en resuelto. Un cierre local puede estar completo aunque producción quede fuera del encargo; si el pedido incluía liberación, no darlo por completo sin comprobarla. Detenerse al completar la entrega solicitada.
