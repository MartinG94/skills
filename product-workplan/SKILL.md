---
name: product-workplan
description: Crea, revisa o reprioriza el plan de evolución de un producto de software desde necesidades, dominio y estado real. Define hitos, alcance inicial, incrementos, dependencias y aceptación con evidencia, tanto para ideas como para sistemas existentes. Úsala para el roadmap o workplan global; el diseño detallado de una feature corresponde a su plan específico.
---

# Product Workplan

Construir un plan de evolución que explique qué resultado entregar primero, qué se reutiliza, qué depende de qué y cómo se sabrá que cada entrega sirve. Combinar comprensión del negocio con diagnóstico del producto existente, cuando lo haya.

## Encuadrar el encargo

Identificar si se pide crear el plan, revisar su viabilidad o actualizar prioridades. Conservar objetivo, audiencia, formato, destino y restricciones aprobadas. Un roadmap puede cubrir todo el producto o un horizonte acotado; no ampliarlo por defecto.

- Si se pide revisión, entregar hallazgos y alternativas; modificar el plan cuando esté solicitado o autorizado.
- Planificar no autoriza implementar todas las entregas. Si el encargo incluye ejecución, continuar con la parte autorizada sin introducir aprobaciones internas redundantes.
- No exigir un repositorio, un modelo de dominio completo ni documentos con nombres determinados. Usar las fuentes disponibles y señalar el alcance de la evidencia.
- Ajustar profundidad al producto: un plan breve puede ser suficiente. No imponer stack, arquitectura, etapas A/B/C, metodología, equipo, duración o cantidad de hitos.

## Relacionar necesidad y estado real

Recuperar instrucciones del proyecto, decisiones vigentes, fuentes del negocio y estado reciente pertinentes. Identificar usuarios/actores, problemas, flujos de trabajo, resultados buscados y restricciones. Reutilizar requisitos y dominio aprobados; sintetizar lo necesario para planificar sin reconstruir todos los modelos. Dejar recuperables el vocabulario, las capacidades y las reglas relevantes, con sus fuentes y pendientes, en el plan o mediante enlaces; no exigir un documento de dominio separado.

Si faltan reglas, distinguir información inspeccionable, decisiones funcionales y elecciones técnicas. Investigar lo accesible antes de preguntar. Plantear sólo preguntas que cambien el alcance, orden, viabilidad o aceptación; una duda localizada no bloquea el resto del plan. Usar hipótesis explícitas para explorar alternativas, sin convertirlas en requisitos aprobados.

En un sistema existente, contrastar documentación con código, contratos, pruebas e historial pertinentes mediante las herramientas disponibles y las preferencias del repositorio. Comprobar revisión y cambios locales antes de proponer trabajo sobre ellos. Una tabla o pantalla no prueba una capacidad completa. Separar capacidades verificadas, parciales, simuladas, faltantes y no verificadas, con evidencia y fecha cuando importe.

Para un producto nuevo, partir del proceso actual y sus herramientas si existen; si es una idea sin operación previa, usar el problema, los usuarios y las hipótesis disponibles, sin inventar un proceso actual. Si no hay acceso al software, registrar las verificaciones necesarias y mantener el plan condicionado sólo donde afecten decisiones.

La regla aprobada define el comportamiento requerido; el código muestra el comportamiento observado. Una divergencia es una brecha que resolver. No presentar pruebas históricas como ejecutadas ahora, ni inferir uso productivo por un commit o una demo.

## Definir hitos de valor y recortar alcance

Conectar cada capacidad con un flujo o resultado. Separar el alcance global de lo que debe incluir la próxima versión; una lista amplia de deseos no define por sí sola el MVP.

Cuando aporte, distinguir un piloto para aprender con usuarios de una primera versión que pueda sostener el trabajo acordado. Explicar qué operación permite cada uno, con qué límites y qué evidencia habilita ampliarlo. No imponer ambos hitos si el producto o encargo no los necesita.

Recortar por escenarios completos y útiles: usuario, acción, información necesaria y resultado. Evitar un roadmap compuesto sólo por capas como «toda la DB → todo el backend → toda la UI». Las tareas preparatorias pueden ser necesarias, pero deben habilitar una entrega identificada y tener un criterio de salida.

Someter el corte inicial a revisión crítica:

- ¿Permite completar un recorrido real y comprobar valor temprano?
- ¿Depende innecesariamente de una integración, automatización o enriquecimiento posterior?
- ¿Qué trabajo manual o convivencia con el sistema actual es aceptable, y quién lo confirmó?
- ¿Faltan condiciones necesarias para usarlo: datos iniciales, acceso, recuperación, formación o soporte, según el contexto?
- ¿Qué podría diferirse sin incumplir el resultado o una restricción aprobada?

No recortar silenciosamente funciones comprometidas. Proponer alternativas con sus consecuencias. La revisión del agente es una recomendación; la aceptación corresponde al usuario o a una persona con autoridad explícitamente delegada.

## Ordenar por dependencias, valor y aprendizaje

Para cada incremento, definir resultado observable, alcance, exclusiones relevantes, dependencia y criterio de aceptación. Detallar el horizonte próximo y mantener las entregas lejanas como opciones condicionadas al aprendizaje, sin congelar prematuramente su diseño. Conservar identificadores existentes cuando faciliten trazabilidad; no renumerar todo al cambiar una prioridad.

Distinguir dependencias técnicas o de datos, decisiones funcionales pendientes, condiciones externas y preferencias de orden. Explicar qué impide comenzar y qué puede avanzar en paralelo. Detectar ciclos y dependencias demasiado amplias: precisar la parte requerida o proponer un corte distinto, sin fingir que la dependencia desaparece.

Justificar prioridades por valor, obligación aprobada, riesgo, incertidumbre y esfuerzo conocido. No fabricar puntuaciones, porcentajes de avance, capacidad de equipo, fechas o presupuestos. Si se solicita calendario o estimación, usar datos disponibles y explicitar supuestos y confianza; distinguir objetivo temporal de compromiso.

Introducir investigación o prototipos sólo para una incertidumbre concreta, con una pregunta y evidencia de salida. Su resultado debe poder cambiar el plan. No ordenar una reescritura o una fase extensa de saneamiento sin demostrar cómo bloquea las entregas.

Distribuir calidad, seguridad, integridad, accesibilidad y operabilidad donde sean necesarias para cada uso; no dejarlas todas para una etapa final. Tampoco ejecutar auditorías o suites completas por defecto al planificar: aplicar las reglas locales y comprobaciones que resuelvan incertidumbres reales.

## Conservar coherencia arquitectónica sin sobrediseñar

Describir arquitectura actual y dirección propuesta al nivel que afecta el orden de entrega: módulos/capacidades, responsabilidades, fuentes de datos, integraciones y restricciones compartidas. Distinguir lo observado de alternativas técnicas todavía abiertas.

Comprobar que los incrementos no dupliquen propietarios de datos o cierres de un mismo proceso. Evaluar compatibilidad, transición de información, convivencia y retirada del sistema previo cuando corresponda. No convertir el modelo conceptual directamente en tablas ni cerrar todos los DTOs, endpoints o migrations desde el roadmap.

Consultar perspectivas o skills especializadas disponibles cuando cambien una decisión; no exigir un equipo fijo. Consolidar contradicciones entre sus aportes y las fuentes aprobadas. El workplan identifica las decisiones compartidas y sus consecuencias; el detalle de implementación pertenece al plan de la entrega.

## Validar, entregar y mantener el plan

Usar [Formato adaptable y ejemplos](references/workplan-format.md) al crear un plan nuevo o mejorar uno insuficiente. Reutilizar estructura y destino del proyecto. Si no se acordó persistencia ni existe una convención aplicable, entregar en la conversación. Actualizar también la memoria que exija el proyecto, distinguiendo estado vigente e historial, sin duplicar el plan.

Antes de cerrar, comprobar que:

1. Cada hito se vincula a un resultado del producto y declara sus límites.
2. La primera entrega es utilizable o aprende algo concreto, con condiciones de entrada identificadas.
3. Los incrementos tienen aceptación observable y se verifica también el flujo acumulado, no sólo piezas aisladas.
4. El orden tiene dependencias justificadas; lo diferido no impide sin advertencia el resultado prometido.
5. Las dudas, restricciones, riesgos y medidas propuestas tienen impacto localizado.
6. Se distinguen estado comprobado, propuestas y decisiones pendientes; otra persona puede continuar.

Informar el alcance listo para detallar o ejecutar, los bloqueos y el siguiente paso. La preparación del plan no acredita implementación, UAT, migrations o deploy.

Al actualizar prioridades o recibir aprendizaje del piloto, propagar el cambio a hitos, dependencias, aceptación y alcance diferido. Incorporar también la evidencia devuelta desde diseño o entrega: actualizar los hechos acreditados y propagar las decisiones aprobadas; los cambios de alcance o prioridad todavía no decididos quedan como propuestas o pendientes localizados. Conservar historia según las convenciones locales; retirar instrucciones vigentes incompatibles y no presentar un hito ya aceptado como pendiente sin evidencia nueva que lo justifique. Mantener una fuente del plan y enlazar el estado operacional, evitando duplicarlo en cada documento.

Para detallar un incremento elegido, entregar a `feature-plan` si está disponible: objetivo, límites, fuentes, dependencias, decisiones, riesgos y aceptación. No es una dependencia obligatoria para producir este workplan. Tampoco generar automáticamente un plan detallado para cada incremento ni iniciar el siguiente por el solo hecho de aparecer en el roadmap.
