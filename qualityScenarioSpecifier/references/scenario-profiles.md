# Perfiles de escenarios de calidad

## Perfil de cátedra: tres campos

Usa por defecto:

| Atributo | Estímulo | Respuesta |
|---|---|---|
| característica/subcaracterística del perfil declarado | condición o evento relevante | comportamiento observable esperado |

Ejemplo de forma, sin valores inventados:

| Atributo | Estímulo | Respuesta |
|---|---|---|
| Eficiencia de desempeño / comportamiento temporal | Durante `[operación y carga TBD]`, un usuario solicita `[acción]` | El sistema completa la operación dentro del umbral `[TBD: acordar con stakeholder]` y registra la medición definida. |

El ejemplo enseña estructura, no ofrece un umbral reutilizable.

Cuando la entrega académica también pide caracterizar RNF, puede añadirse:

| ID | Descripción | Atributo | SPA | Prioridad | Justificación | Fuente |
|---|---|---|---|---|---|---|

`SPA` indica si el requisito es arquitectónicamente significativo según su impacto en
decisiones estructurales y trade-offs. Usa `TBD` si no hay suficiente contexto.

## Perfil de seis partes

Úsalo sólo cuando se pida o aporte precisión necesaria:

| Parte | Pregunta |
|---|---|
| Fuente | ¿Quién o qué origina el estímulo? |
| Estímulo | ¿Qué evento/condición ocurre? |
| Entorno | ¿En qué estado o condición opera el sistema? |
| Artefacto | ¿Qué parte del sistema recibe el impacto? |
| Respuesta | ¿Qué comportamiento observable realiza? |
| Medida | ¿Cómo se decide si la respuesta cumple? |

No rellenes campos por plausibilidad. Una versión parcial con `TBD` es más fiel que un
escenario cuantificado sin fuente.

## Cómo convertir lenguaje vago

| Expresión | Pregunta útil |
|---|---|
| rápido | ¿Qué operación, percentil, carga, ventana y umbral? |
| disponible | ¿Qué funciones, horario, dependencias, SLO y exclusiones? |
| seguro | ¿Qué activo, amenaza, actor, control y resultado verificable? |
| fácil de modificar | ¿Qué cambio representativo, alcance y esfuerzo máximo? |
| usable | ¿Qué usuario, tarea, contexto y criterio de eficacia/eficiencia? |

No conviertas automáticamente estas preguntas en una lista que bloquee el trabajo.
Pregunta sólo lo que cambie materialmente el escenario; lo demás puede quedar `TBD`.

## Conflictos

Registra tensiones como seguridad–usabilidad, consistencia–disponibilidad,
rendimiento–coste o modificabilidad–complejidad. No resuelvas el conflicto dentro de la
especificación; eleva la decisión al diseño con prioridades y evidencia.
