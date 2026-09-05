---
name: grasp-sequence-realizer
description: >-
  Deriva realizaciones de casos de uso y diagramas de secuencia trazables, separando
  análisis BCE/GRASP de diseño detallado. Úsala cuando se pide una RCU, una secuencia o
  asignación de responsabilidades sobre un CU descrito; no para descubrir casos de uso
  ni seleccionar patrones GoF sin una variación concreta.
---

# Realización de casos de uso

Convierte un escenario de caso de uso en una colaboración coherente. Mantén separados
el modelo lógico de análisis y el modelo físico de diseño.

Esta es la única skill del catálogo que produce realizaciones. `use-case-extractor`
descubre y describe el CU; recibe de ella el escenario y devuelve aquí cualquier vacío
de precondición, flujo o resultado, sin reescribir el CU silenciosamente.

## Seleccionar el modo

- `analysis-rcu` — predeterminado cuando se pidió una realización sin nivel, todavía no
  existe DCD o el encargo dice ASI, “realización de análisis” o clases BCE. Lee
  [references/analysis-realization.md](references/analysis-realization.md).
- `design-rcu` — úsalo cuando existe un DCD, la consigna pide realización de diseño o
  deben especificarse firmas/colaboradores de solución. Lee
  [references/design-realization.md](references/design-realization.md).

No mezcles ambos modos en un mismo diagrama. Si el material de entrada mezcla niveles,
señala la inconsistencia y elige el nivel que exige el entregable.

## Entradas

Necesitas un escenario concreto del caso de uso y, cuando existan:

- actor, precondiciones, flujo principal y alternativas;
- modelo de dominio o clases de análisis;
- reglas, estados y datos ya definidos;
- DCD/contratos para el modo de diseño;
- convención de nombres y renderer exigido.

No inventes pantallas, DAOs, eventos, estados, servicios externos o algoritmos para
llenar el diagrama. Registra una pregunta cuando su ausencia impide decidir un mensaje.

## Flujo común

1. Fija escenario, precondición, resultado y nivel de abstracción.
2. Extrae los eventos actor–sistema en el orden de la especificación.
3. Elige el controlador del caso/evento y los colaboradores que poseen la información.
4. Asigna cada mensaje al receptor responsable; evita que la interfaz contenga reglas.
5. Justifica cómo el emisor conoce al receptor: atributo, parámetro, creación o retorno.
6. Modela condiciones, ciclos y creación sólo si aparecen en el escenario.
7. Comprueba que cada mensaje conserva vocabulario, orden y resultado del caso de uso.
8. Contrasta participantes y operaciones con los artefactos estáticos disponibles.

## GRASP sin sobrediseño

En análisis usa como conjunto curricular predeterminado:

- Experto en Información;
- Creador;
- Bajo Acoplamiento;
- Alta Cohesión;
- Controlador.

`boundary`, `control` y `entity` son roles/estereotipos de análisis, no patrones GRASP.
Otros GRASP o GoF pueden considerarse en diseño, pero sólo ante una fuerza observada.
No debe aparecer un patrón en cada mensaje. `Ningún patrón adicional` es una decisión
válida y preferible a una colaboración artificial.

## Notación

Usa Mermaid `sequenceDiagram` por defecto. Si el usuario o repositorio exige PlantUML,
usa PlantUML en lugar de Mermaid; nunca emitas ambos por rutina.
Declara cualquier semántica UML que el renderer no pueda representar; no confundas
una vista legible con un modelo UML interoperable.

- Usa nombres de operación del lenguaje del caso de uso.
- Representa retornos sólo cuando aclaran una decisión o dato posterior.
- Usa `alt`, `opt` y `loop` sólo cuando el escenario los contenga.
- Muestra `create` únicamente en el punto real de creación.
- No agregues `finCU()`, `close()` ni liberación de pantalla salvo que sea un paso o
  responsabilidad observable del sistema.

## Producto predeterminado

1. `Modo y alcance` — CU, escenario y fuentes.
2. `Hechos, supuestos y preguntas`.
3. `Participantes y responsabilidades` — tabla breve.
4. `Diagrama de secuencia` — una notación.
5. `Trazabilidad` — paso del CU → mensaje/responsable → evidencia.
6. `Comprobaciones` — orden, visibilidad, estados y coherencia estática.

Incluye una tabla patrón→mensaje sólo si el usuario pide justificar patrones o si una
decisión no es obvia. No produzcas código, DCD, persistencia ni infraestructura salvo
que formen parte explícita del pedido.

## Criterios de cierre

- El diagrama cubre un escenario identificable, no una mezcla de variantes.
- Ningún participante existe sólo para demostrar un patrón.
- Cada creación y navegación es explicable con la información disponible.
- Las alternativas relevantes conservan precondiciones y resultados.
- Las discrepancias con DCD, estados o firmas se reportan; no se corrigen silenciosamente.
