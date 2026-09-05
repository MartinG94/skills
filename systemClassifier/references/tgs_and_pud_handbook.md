# Criterios de clasificación, prefactibilidad y PUD

Consulta solo la sección correspondiente al modo activo.

## 1. Diagnóstico de SI

Modelo operativo mínimo:

```text
entradas -> transformación/proceso -> salidas
                         ^             |
                         +-- retroalimentación/control
```

Registra objetivo y límite antes de clasificar componentes. Personas, procedimientos, datos, hardware y software pueden formar parte del SI; la presencia de software no convierte al SI completo en una aplicación.

Preguntas discriminantes:

- ¿Qué información o recursos ingresan y de dónde?
- ¿Qué transformación relevante ocurre?
- ¿Qué resultado útil recibe quién?
- ¿Qué información permite corregir o controlar el proceso?
- ¿Qué parte es manual y cuál computarizada?

## 2. Tipos de SI

| Tipo | Evidencia fuerte | No basta por sí solo |
| --- | --- | --- |
| TPS | registro rutinario de operaciones, alto volumen, reglas estructuradas | que exista una base de datos |
| MIS | reportes regulares, resumen y control de gestión | cualquier listado operativo |
| DSS | análisis ad hoc, alternativas o modelos para decidir | un dashboard estático |
| ESS | información agregada y estratégica para dirección | que el usuario sea gerente |
| KMS | capturar, organizar, compartir o reutilizar conocimiento | repositorio documental sin uso descrito |
| AI/experto | inferencia, recomendación o explicación basada en conocimiento/modelo | automatización convencional |

Clasifica por capacidad. Explica qué evidencia satisface el criterio y qué falta.

## 3. Prefactibilidad

La evaluación inicial responde si vale la pena continuar estudiando o desarrollar el proyecto con los recursos y contexto conocidos.

- **Técnica:** disponibilidad/capacidad de equipamiento, tecnología base, integración y competencias.
- **Económica:** costos y beneficios, capacidad/disposición de inversión; separar datos de estimaciones.
- **Operativa:** aceptación, uso real, cambios de procedimiento, capacitación y resistencia.

Un riesgo no equivale a inviabilidad. Para `CONDICIONADA`, expresa condición, responsable de resolverla si consta y evidencia necesaria. Para `NO DETERMINADO`, indica el dato faltante sin estimarlo.

## 4. PUD

Conceptos:

- fase: tramo del ciclo con objetivos;
- iteración: recorrido acotado por los flujos de trabajo;
- flujo: actividades, roles y artefactos de un aspecto como requisitos, análisis o diseño;
- artefacto: resultado producido por un flujo.

Las fases se solapan con los flujos: requisitos, análisis, diseño, implementación y prueba pueden aparecer en cada iteración con distinta intensidad. No deduzcas porcentajes universales.

Antes de ubicar un elemento, pregunta si se está describiendo trabajo previsto, artefacto existente o criterio de decisión. La prefactibilidad puede aportar a Inicio, pero por sí sola no prueba que Inicio haya terminado.
