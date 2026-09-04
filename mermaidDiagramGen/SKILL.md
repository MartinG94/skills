---
name: mermaid-diagram-gen
description: >-
  Genera, corrige y valida diagramas Mermaid a partir de contenido ya definido: flujos, secuencias,
  clases, ERD, estados, arquitectura, cronogramas y otras familias soportadas. También puede expresar
  una máquina de estados y una MTE cuando el ciclo de vida está documentado. Usar para elegir sintaxis,
  renderizar o depurar Mermaid; no usar como autoridad para inventar dominio, arquitectura o requisitos.
---

# Generación y validación Mermaid

Transformá semántica provista por el usuario o por una skill especialista en un único diagrama legible. Separá siempre tres afirmaciones distintas: sintaxis Mermaid válida, semántica consistente con la fuente y fidelidad a UML u otra notación.

## Límites

- Esta skill es autoridad de **representación**, no del contenido. Casos de uso, dominio, arquitectura, procesos o responsabilidades se deciden en sus skills respectivas.
- No completes nodos, relaciones, cardinalidades, transiciones, métricas ni tecnologías por simetría visual.
- No llames “UML formal” a una representación Mermaid si la sintaxis no cubre toda la semántica usada.
- No garantices compilación solo por inspección. Decí `render validado` únicamente si ejecutaste un renderer e informá su versión/entorno; de otro modo, `preflight textual aprobado, render no ejecutado`.
- Generá un formato y una vista por defecto. Variantes o el código fuente más una imagen se entregan solo si se piden o facilitan una decisión real.

## Seleccionar modo

1. `generate` — crear Mermaid desde una especificación o inventario de elementos.
2. `repair` — corregir un bloque que no renderiza, preservando su significado.
3. `review` — evaluar legibilidad, sintaxis y fidelidad sin editar.
4. `state-model` — derivar DTE/MTE desde eventos y estados documentados; no se activa por el solo hecho de que una entidad sea persistente.

## Flujo de trabajo

### 1. Fijar el contrato

Determiná propósito, audiencia, tipo de diagrama, dirección preferida, renderer/versión si se conoce y nivel de detalle. Si falta la versión, evitá sintaxis experimental salvo que el usuario la pida.

### 2. Construir un inventario semántico

Antes del código, enumerá internamente los elementos y relaciones con su fuente. Marcá `TBD` donde una decisión afecte el diagrama. En modo `repair`, conservá un mapa `original → corrección` y no cambies nombres o relaciones para hacer más cómodo el layout.

### 3. Cargar una referencia bajo demanda

Leé solo el documento correspondiente de `references/`:

| Necesidad | Referencia |
|---|---|
| flujo/BPMN preview | [flowchart.md](references/flowchart.md) |
| secuencia | [sequenceDiagram.md](references/sequenceDiagram.md) |
| estados | [stateDiagram.md](references/stateDiagram.md) |
| clases | [classDiagram.md](references/classDiagram.md) |
| ERD | [entityRelationshipDiagram.md](references/entityRelationshipDiagram.md) |
| C4 | [c4.md](references/c4.md) |
| requisitos | [requirementDiagram.md](references/requirementDiagram.md) |

Para otra familia, elegí por nombre en `references/`. Los documentos son un snapshot local y pueden contener enlaces upstream no incluidos; no sigas esos enlaces como si fueran recursos instalados.

### 4. Generar la vista mínima

- IDs estables, únicos y simples; etiquetas humanas separadas de los IDs.
- Agrupación solo cuando expresa un límite real.
- Etiquetas y aristas breves; notas para detalle excepcional.
- Estilos mínimos y con contraste; no ocultes significado solo en color.
- Escapá comillas y caracteres que el tipo de diagrama trate como sintaxis.
- No uses `autonumber`, visibilidad de clases, PK/FK, cardinalidades o estados finales si la fuente no los necesita o no los define.

### 5. Validar

Ejecutá tres capas:

1. **Preflight textual:** fence correcto, encabezado válido, IDs únicos, referencias existentes, bloques balanceados y palabras reservadas según la familia.
2. **Render:** si hay renderer disponible, compilá exactamente el bloque entregado. No corrijas el contenido semántico para silenciar el parser.
3. **Fidelidad:** compará cada nodo y relación con el inventario; explicá pérdidas de semántica debidas a Mermaid.

Si el render falla, informá el error exacto, aplicá la corrección mínima y volvé a ejecutar. Si no hay renderer, no simules el resultado.

## Modo máquina de estados

Usalo solo para un objeto con estados observables y comportamiento dependiente del estado, o cuando la consigna exige DTE/MTE.

1. Extraé estado inicial si está definido, estados, eventos, guardas, efectos y destinos.
2. Cada fila de la MTE conserva un localizador de evidencia o `TBD`.
3. Detectá estados inalcanzables, eventos duplicados con guardas solapadas y estados sin salida **solo dentro de la cobertura provista**.
4. Un estado sin salida puede ser terminal aunque no se dibuje `[*]`; confirmá la intención antes de marcar deadlock.
5. No fuerces una máquina por entidad, historial temporal, patrón State ni una transición final universal.

Formato MTE opcional:

| Estado origen | Evento | Guarda | Efecto | Estado destino | Evidencia |
|---|---|---|---|---|---|

Usá la forma `evento [guarda] / efecto` únicamente para las partes conocidas. Omitir una parte desconocida es preferible a inventarla.

## Reparaciones frecuentes

- `end` como ID o token ambiguo en flowcharts: cambiá el ID, no la etiqueta de negocio.
- caracteres especiales en una etiqueta: citá/escapá según la referencia de esa familia.
- prefijos `o`/`x` pegados a conectores: agregá separación o un ID explícito.
- dos puntos o saltos en mensajes de secuencia: aplicá la sintaxis documentada sin alterar el mensaje.
- subgraph/bloque sin cierre: balanceá la estructura.

No apliques todas estas reglas preventivamente: verificá que el parser y la versión realmente las requieran.

## Contrato de salida

- En `generate`, `repair` y `state-model`, entregá `### Diagrama` con un único bloque `mermaid` y luego `### Validación`: tipo y propósito; fuente semántica/cobertura; renderer y versión o `no disponible`; resultado (`render validado`, `preflight textual` o error pendiente); y supuestos o pérdidas de fidelidad.
- En `repair`, agregá una lista corta de correcciones.
- En `review`, entregá hallazgos con localizadores y cambios propuestos. Incluí un bloque corregido solo si el usuario lo pide o si es necesario para demostrar una reparación; no reimprimas el diagrama sin necesidad.

## Control final

- ¿El tipo elegido responde a la pregunta del usuario?
- ¿Cada elemento proviene de la fuente y no del gusto del generador?
- ¿Se cargó solo la referencia necesaria?
- ¿El bloque entregado es el mismo que se validó?
- ¿Se distingue sintaxis, semántica y fidelidad notacional?
- ¿La salida evita vistas y tablas redundantes?
