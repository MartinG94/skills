---
name: domain-design
description: >-
  Transforma modelos de análisis y realizaciones de casos de uso en un Diagrama de
  Clases de Diseño trazable. Úsala para decidir clases, responsabilidades, interfaces
  y relaciones de diseño; no para descubrir el dominio conceptual ni mapear tablas.
---

# Diseño de dominio y DCD

Produce un modelo de solución implementable sin confundirlo con el modelo conceptual
de análisis. Conserva la terminología y las reglas del problema, pero incorpora sólo
los elementos técnicos que estén justificados por los requisitos y restricciones.

## Elegir el modo

- `course-dcd` — modo predeterminado para DSI, PPAI, RCU o consignas académicas.
  Lee [references/dcd-method.md](references/dcd-method.md).
- `rich-domain` — úsalo sólo si el usuario pide DDD táctico, agregados, objetos de
  valor o un modelo de dominio rico, o si las invariantes y límites transaccionales
  aportados lo justifican. Lee [references/rich-domain.md](references/rich-domain.md).
- `implementation` — añade código únicamente cuando el usuario lo pida. Primero
  completa uno de los modos anteriores y respeta el lenguaje y framework del proyecto.

Si el pedido no permite distinguir el modo, usa `course-dcd` y declara la decisión.

## Entradas mínimas

Busca, en este orden:

1. alcance o casos de uso y escenario concreto;
2. modelo de dominio/análisis y realizaciones disponibles;
3. reglas e invariantes explícitas;
4. restricciones no funcionales y tecnológicas;
5. convenciones de notación y formato de entrega.

No conviertas conjeturas en requisitos. Si falta un dato que cambia identidad,
cardinalidad, responsabilidad o arquitectura, déjalo como pregunta o supuesto visible.

## Flujo de trabajo

1. Delimita escenario, modo y fuentes realmente disponibles.
2. Separa elementos de análisis de decisiones de solución.
3. Traza cada participante relevante del análisis a una clase, interfaz o servicio de
   diseño, o explica por qué no aparece.
4. Asigna responsabilidades por información, cohesión, acoplamiento y navegabilidad.
5. Especifica clases con atributos, operaciones, tipos, visibilidad y relaciones sólo
   con el detalle requerido para implementar el escenario.
6. Comprueba el DCD contra las secuencias y restricciones suministradas.
7. Propone patrones o arquitectura adicional sólo cuando exista una fuerza concreta;
   `ningún patrón adicional` es una conclusión válida.

## Reglas de decisión

- Un DCD no implica automáticamente DDD, Clean Architecture ni arquitectura hexagonal.
- Un concepto sin identidad no debe convertirse automáticamente en objeto de valor:
  considera semántica de igualdad, invariantes y utilidad del tipo.
- Un agregado DDD es un límite de consistencia; no equivale a agregación UML.
- Una composición UML expresa vida compartida/propiedad fuerte, no una regla automática
  de persistencia o borrado en cascada.
- No añadas repositorios, DTO, puertos, eventos, fábricas o servicios por plantilla.
- Evita clases anémicas cuando las reglas conocidas pertenecen al objeto, pero no
  inventes reglas ni fuerces toda validación al constructor.
- No fijes lenguaje, framework, ORM, base de datos o protocolo sin evidencia.

## Producto predeterminado

Entrega de forma compacta:

1. `Alcance y modo` — escenario, fuentes y exclusiones.
2. `Hechos, supuestos y preguntas` — separados explícitamente.
3. `Trazabilidad análisis → diseño` — tabla breve por participante/responsabilidad.
4. `DCD` — un diagrama y, cuando haga falta, fichas de clases.
5. `Decisiones` — alternativas y consecuencias relevantes.
6. `Comprobaciones` — cobertura del escenario, firmas, multiplicidades y navegación.

Usa Mermaid como renderer predeterminado. Emite PlantUML u otro formato sólo si el
usuario o el repositorio lo exige; no dupliques el mismo diagrama en dos sintaxis.
Si Mermaid no representa un detalle UML exigido, declara la pérdida o usa una
herramienta UML disponible; no presentes la vista como modelo interoperable.
El código, los diagramas de arquitectura y el mapeo de persistencia son anexos optativos.

## Criterios de cierre

- Cada clase y operación tiene evidencia o está marcada como propuesta.
- El diagrama distingue análisis heredado de decisiones nuevas de diseño.
- Las relaciones muestran multiplicidades y dirección sólo cuando son conocidas.
- Las firmas son coherentes con las interacciones cubiertas, sin exigir que una
  secuencia abreviada contenga todos los tipos o retornos.
- No se introdujo un patrón, capa o tecnología sin problema demostrable.
