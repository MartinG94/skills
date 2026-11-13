# Formato adaptable para un workplan de producto

La estructura sirve para decidir y continuar el trabajo. Combinar u omitir apartados que no aporten; conservar el formato existente si resulta útil. Los ejemplos son ficticios y no definen reglas para otros productos.

## Contenido recuperable del plan

| Tema | Información que cambia decisiones |
|---|---|
| Encuadre | Problema, usuarios, flujo actual, resultados, restricciones y horizonte solicitado. |
| Fuentes y base | Vocabulario y reglas relevantes, decisiones aprobadas, fuentes disponibles, capacidades reales/parciales/simuladas y límites de inspección. |
| Alcance | Qué debe resolver el producto, qué se entrega primero y qué queda diferido o fuera. |
| Dirección técnica | Responsabilidades, fuentes de datos, integraciones y restricciones que condicionan entregas; propuestas diferenciadas de hechos. |
| Hitos | Resultado útil o aprendizaje esperado, condiciones de entrada, aceptación y límites de uso. |
| Incrementos | Escenarios acotados, dependencias, alcance, comprobación de salida y relación con el hito. |
| Riesgos y decisiones | Incertidumbre concreta, impacto sobre el plan, forma de resolverla y responsable sólo si está identificado. |
| Adopción y continuidad | Datos iniciales, convivencia, operación y aceptación acumulativa cuando apliquen; próxima entrega y evidencia para retomarla. |

Una fila de roadmap puede ser suficiente:

| Incremento | Resultado observable | Base que reutiliza | Dependencia y motivo | Evidencia de aceptación |
|---|---|---|---|---|
| Identificador del proyecto | Escenario que funciona al terminar | Capacidad comprobada o fuente disponible | Lo que necesita y por qué | Prueba o aceptación propuesta, sin fingir ejecución |

Si se requiere más detalle para una entrega, incluir su alcance/exclusiones, impacto técnico, decisiones abiertas y riesgos. No multiplicar documentos para completar columnas.

## Ejemplo desde una idea sin repositorio

**Encargo ficticio:** organizar el desarrollo de una herramienta para prestar instrumentos musicales en una asociación. Hoy se usan un cuaderno y una planilla. La responsable aprobó identificar instrumento y socio, registrar préstamo/devolución y consultar disponibilidad. La comunicación telefónica puede continuar durante el piloto. Multas, pagos y reservas online no están definidos.

**Corte propuesto:** probar el recorrido instrumento disponible → préstamo → devolución → disponible, con un conjunto acotado de datos representativos. El piloto permite validar el uso; no supone que pueda reemplazar todavía todos los registros.

| Entrega | Resultado | Dependencia | Aceptación propuesta |
|---|---|---|---|
| Preparación necesaria | Identificar los datos mínimos y cómo se tratarán los préstamos abiertos | Inspección de cuaderno/planilla y decisión de la responsable | Campos y casos ambiguos documentados; no convertir dudas en datos inventados. |
| Recorrido piloto | Registrar y devolver un instrumento, reflejando disponibilidad | Identidad mínima y regla de préstamo acordadas | Un caso representativo completa el recorrido y evita dos préstamos activos del mismo instrumento, si esa regla se confirma. |
| Adopción acordada | Incorporar préstamos abiertos y empezar a operar en el alcance elegido | Decisión sobre datos existentes y resultado del piloto | Conciliación con registros previos y recuperación comprobada según el riesgo del uso real. |

La restricción sobre préstamos simultáneos se consulta antes de cerrar su lógica; no impide relevar datos ni preparar el plan. Las reglas de multas no bloquean el recorrido aprobado si permanecen fuera del alcance. No se eligen framework, servidor, número de sprints o fechas por defecto.

Una primera versión operativa podría coincidir con el piloto si la responsable confirma que sus límites bastan; no hacen falta dos lanzamientos artificiales.

## Ejemplo de evolución con un prototipo

**Encargo ficticio:** priorizar un portal para solicitar mantenimiento de equipos. Ya existe identidad corporativa y un listado persistente de equipos. La pantalla de solicitudes usa datos simulados; el plan antiguo la marca como terminada. La responsable aprobó crear, asignar y cerrar solicitudes. Analítica predictiva e integración con un proveedor son deseos posteriores.

**Diagnóstico:** reutilizar identidad y equipos tras comprobar el alcance necesario. Registrar como brecha la persistencia y el ciclo real de solicitudes; la pantalla existente sirve como referencia, no como evidencia de operación completa.

**Secuencia propuesta:** un recorrido mínimo de solicitud a cierre con usuarios representativos; después, extensión de volumen/adopción y consulta del historial según necesidades confirmadas. Investigar la integración externa en paralelo sólo si una duda concreta afecta el corte futuro; no hacerla requisito del primer recorrido sin fundamento.

El workplan define quién origina, asigna y cierra y qué resultados deben conservarse. Un plan posterior concreta el contrato y tareas de esa entrega. Si aún falta la política de reasignación, localizar las operaciones afectadas y conservar el avance independiente.

**Aceptación acumulativa:** comprobar que una solicitud creada en la primera entrega conserva su identidad, estado e historial al incorporarse las siguientes capacidades. No basta con validar cada pantalla por separado.

## Revisión o cambio de prioridades

Evaluar consecuencias sobre el plan vigente, no sólo reordenar filas:

- Ante una fecha fija, separar alcance necesario, alternativas y viabilidad condicionada; no declarar una estimación sin capacidad y esfuerzo.
- Ante una dependencia externa demorada, distinguir el flujo bloqueado de los recorridos independientes y proponer una alternativa sólo si el usuario la admite.
- Ante capacidades ya aceptadas, conservarlas como base; no volver a construirlas porque aparezcan en una lista antigua.
- Ante un MVP demasiado amplio, proponer qué se difiere y qué resultado conserva cada alternativa.
- Ante un cambio de prioridad, actualizar el criterio de éxito y las dependencias afectadas; el trabajo ya hecho no justifica por sí solo mantener una prioridad obsoleta.

Una revisión puede terminar con un plan listo para detallar, un plan parcialmente listo o alternativas pendientes de una decisión concreta. Evitar un «aprobado» genérico que oculte bloqueos o se confunda con autorización de operación.
