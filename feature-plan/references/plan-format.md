# Formato adaptable para un plan de feature

Usar la estructura existente si sirve al encargo. Combinar u omitir apartados que no agreguen decisiones. Los ejemplos son ficticios y no aportan reglas al proyecto real.

## Información que debe poder recuperarse

| Tema | Contenido útil |
|---|---|
| Resultado y límites | Problema, escenario, resultado observable, incluido y excluido; hito/incremento de origen cuando exista. |
| Base comprobada | Fuentes relevantes y alcance de la inspección; revisión si existe; comportamiento actual, brechas y trabajo previo que preservar. |
| Decisiones | Reglas aprobadas y procedencia; elecciones técnicas; propuestas o preguntas pendientes y tareas afectadas. |
| Diseño integrado | Responsabilidades y fuente de cada contrato; interacción, datos e integraciones que cambian. |
| Secuencia | Tareas con dependencia, resultado esperado y comprobación de salida; punto de integración. |
| Validación | Aceptación, regresiones y fallos relevantes; diferenciar planificación de resultados ejecutados. |
| Transición | Sólo si aplica: compatibilidad, cambios de datos, entrega y recuperación. |
| Continuidad | Qué está listo, qué falta decidir/inspeccionar y próxima acción dentro del alcance autorizado. |

Una tabla de tareas puede usar:

| Tarea | Necesidad o decisión | Dependencia | Cambio esperado | Comprobación de salida |
|---|---|---|---|---|
| Identificador descriptivo | Fuente o referencia breve | Tarea previa o decisión pendiente | Artefacto o comportamiento concreto | Evidencia observable |

No completar columnas con supuestos para evitar huecos. Si una elección técnica puede resolverse ahora, decidirla; si falta evidencia de negocio, identificar su impacto. No agregar esfuerzo, fecha, propietario nominal o estado de aprobación sin fundamento.

## Ejemplo breve sin cambio de contrato

**Encargo ficticio:** planificar que el botón Cancelar de un editor de escritorio descarte los cambios locales y vuelva a la lista. El usuario confirma que Cancelar debe descartar sin guardar ni pedir confirmación.

**Base observada:** el editor mantiene un borrador local; el botón hoy guarda y navega. Existe un flujo de descarte reutilizable. No se solicitó alterar la API.

**Plan breve:**

- Reutilizar el descarte local en la acción Cancelar y conservar el comportamiento de Guardar.
- Comprobar que, al editar y cancelar, se vuelve a la lista sin escritura y el valor persistido permanece igual; reabrir muestra ese valor.
- Cubrir la regresión de Guardar y verificar teclado/foco según el patrón de la aplicación.

**Salida:** listo para implementar con la decisión recibida. Los nombres exactos de funciones y los comandos se obtienen del proyecto inspeccionado. No hacen falta un roadmap, un diseño de DB ni una aprobación nueva.

## Ejemplo con integración y decisiones pendientes

**Encargo ficticio:** planificar el reintento manual de una ejecución fallida en una herramienta de procesamiento. Están aprobados el permiso de operador y la prohibición de reintentar ejecuciones activas. Existen API, worker y pantalla de detalle.

**Base observada:** el worker distingue éxito y fallo; el borrador de UI propone enviar `status=queued`, pero la API existente expone un comando de reintento. Hay que preservar esa frontera o justificar su cambio.

**Decisión abierta:** al reintentar, ¿se usan los parámetros originales o los actuales? La elección afecta el contenido enviado al worker y la explicación de UI. No elegir una variante por comodidad técnica.

**Diseño a conciliar:** comando y respuesta únicos entre API y UI; validación del estado/permiso en servidor; mecanismo para impedir duplicados ante dos solicitudes simultáneas, compatible con las capacidades reales del worker.

| Trabajo | Dependencia | Evidencia para considerarlo terminado |
|---|---|---|
| Inspeccionar el comando, persistencia y garantías actuales del worker | Acceso a las fuentes | Brecha documentada y contrato de referencia identificado. |
| Resolver origen de parámetros y completar contrato de reintento | Decisión funcional | Un mismo significado en comando, ejecución y UI. |
| Implementar comportamiento de servidor y controles de concurrencia | Contrato acordado | Reintento válido; rechazo de ejecución activa y usuario sin permiso; concurrencia sin duplicar efectos. |
| Adaptar la acción en el detalle | Contrato acordado; puede avanzar con fixtures pactados | Estados pendiente, éxito y error coherentes con la respuesta; recuperación tras fallo. |
| Verificar API, worker y UI juntos | Comportamiento integrado | El operador reintenta una ejecución fallida y observa el resultado correcto; regresión del flujo original. |

**Salida:** preparación parcial. La inspección puede comenzar; el contenido del reintento depende de una decisión. No afirmar que falta una tabla o que el worker garantiza exactamente una ejecución sin comprobarlo. Las pruebas son propuestas hasta que se ejecuten.

## Al revisar un plan existente

No reescribir todo por preferencia de formato. Relacionar cada hallazgo con su evidencia, impacto y corrección necesaria. Priorizar reglas inventadas, contratos incompatibles, dependencias imposibles, pérdida de datos y ausencia de una prueba de integración.

Distinguir:

- cambio necesario para volver implementable el plan;
- mejora opcional de claridad;
- duda que requiere inspección o decisión.

Cuando se solicite actualizarlo, corregir también las referencias y tareas dependientes. Un antecedente que explica una decisión puede conservarse; una instrucción obsoleta que todavía parece vigente debe sustituirse.
