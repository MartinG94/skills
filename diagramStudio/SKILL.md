---
name: diagramStudio
description: >-
  Diseña, genera, repara, sincroniza y valida diagramas visuales y estructurales tanto en sintaxis Mermaid in-line como en archivos editables .drawio (diagrams.net). Se activa automáticamente siempre que el usuario pida textualmente un diagrama (flujo/flowchart, secuencia/sequence, clases/class, entidad-relación/ERD, estados/state, arquitectura C4, mapa de procesos institucional de 3 niveles, SIPOC visual, cronograma/gantt, gitgraph, mindmap, timeline, etc.) o cuando el agente infiera que una representación gráfica o estructural es necesaria para responder a la solicitud. Soporta mode: "mermaid", mode: "drawio" y mode: "dual".
license: MIT
allowed-tools: [Bash, Read, Write, WebFetch]
metadata: {"author":"Agents365-ai / Antigravity","version":"4.0.0","category":"design","platforms":["windows","macos","linux"]}
---

# Diagram Studio (Mermaid & Draw.io Unified)

Motor unificado de diseño, generación, validación y sincronización de diagramas técnicos, organizacionales y de arquitectura. Produce tanto representaciones textuales in-line (`Mermaid`) para previsualización inmediata en Markdown/chat como archivos nativos editables (`.drawio` / diagrams.net) para entregas formales y publicación.

## Activación Automática

Esta skill se ejecuta de manera **automática e implícita** sin requerir que el usuario la invoque por su nombre cuando:
1. El usuario solicita textualmente un diagrama de cualquier tipo (flujo, secuencia, clases, ERD, estados, componentes, arquitectura, mapa de procesos, SIPOC, gantt, etc.).
2. El agente infiere que una representación visual o estructural facilitará la comprensión de una solución, diseño, modelo o proceso.

---

## Modos de Operación

Seleccioná el modo adecuado según el contexto o la solicitud:

1. **`mode: "mermaid"` (Predeterminado para chat y Markdown):**
   - Emite un bloque ```mermaid in-line directamente en la respuesta.
   - Ideal para documentación ágil, PRs, issues y visualización instantánea.
2. **`mode: "drawio"` (Para entregas ejecutivas y diseño formal):**
   - Genera o sincroniza un archivo `.drawio` XML nativo y editable.
   - Ideal para arquitecturas cloud multicapa, BPMN formal con swimlanes, esquemas de base de datos grandes y diagramas de publicación.
3. **`mode: "dual"` (Recomendado cuando se requiere entrega completa):**
   - Genera simultáneamente el bloque Mermaid in-line para visualización inmediata y compila el archivo `.drawio` editable guardado en el directorio de trabajo.

---

## Presets Especializados de Procesos

Para modelos de procesos organizacionales, utilizá los presets estandarizados:

| Preset | Cuándo usar | Referencia de diseño |
|---|---|---|
| **Mapa de Procesos Institucional** | Representar la arquitectura de procesos en sus 3 niveles canónicos (Estratégicos, Clave/Operativos, Soporte) con clientes de entrada y satisfacción de salida. | [references/presets/process-map.md](references/presets/process-map.md) |
| **SIPOC Visual** | Delimitar fronteras de un proceso en 5 columnas (Proveedores, Entradas, Proceso macro de 5 a 7 pasos, Salidas, Clientes). | [references/presets/sipoc.md](references/presets/sipoc.md) |

---

## Flujo de Trabajo: Generación Mermaid (`mode: "mermaid"`)

1. **Fijar el tipo de diagrama:** Flowchart, Sequence, Class, State, ERD, C4, Gantt, Mindmap, Timeline, etc.
2. **Cargar la referencia bajo demanda:**
   Leé el archivo correspondiente en `references/mermaid/`:
   - Flujo / Proceso: [references/mermaid/flowchart.md](references/mermaid/flowchart.md)
   - Secuencia: [references/mermaid/sequenceDiagram.md](references/mermaid/sequenceDiagram.md)
   - Estados / Ciclo de vida: [references/mermaid/stateDiagram.md](references/mermaid/stateDiagram.md)
   - Clases: [references/mermaid/classDiagram.md](references/mermaid/classDiagram.md)
   - Entidad-Relación: [references/mermaid/entityRelationshipDiagram.md](references/mermaid/entityRelationshipDiagram.md)
   - Arquitectura / C4: [references/mermaid/c4.md](references/mermaid/c4.md) o [references/mermaid/architecture.md](references/mermaid/architecture.md)
   - Cronograma: [references/mermaid/gantt.md](references/mermaid/gantt.md)
   - Mapa mental / Ideas: [references/mermaid/mindmap.md](references/mermaid/mindmap.md)
   - Índice completo de sintaxis: [references/mermaid/index.md](references/mermaid/index.md)
3. **Generar la vista mínima y robusta:**
   - IDs alfanuméricos estables y limpios; etiquetas humanas separadas entre corchetes o comillas.
   - Escapar comillas y caracteres reservados según el tipo de diagrama.
   - Balancear subgraphs y bloques.
4. **Validar:** Preflight textual estricto (IDs únicos, sintaxis compatible).

---

## Flujo de Trabajo: Generación Draw.io (`mode: "drawio"`)

1. **Rutas de autoría:**
   - **Desde Diagram IR o modelos de código/infraestructura:** Utilizá la CLI unificada `scripts/diagramctl.py`.
   - **Desde especificación XML nativa:** Consultá [references/drawio/xml-authoring.md](references/drawio/xml-authoring.md) y [references/drawio/diagram-types.md](references/drawio/diagram-types.md).
   - **Conversión de Mermaid a Draw.io:** Si el usuario tiene un Mermaid previo o se genera en modo dual, utilizá [references/drawio/mermaid-authoring.md](references/drawio/mermaid-authoring.md) o `scripts/drawio2mermaid.py`.
2. **CLI Unificada (`diagramctl.py`):**
   ```bash
   python3 scripts/diagramctl.py build model.json --from ir -o architecture.drawio
   python3 scripts/diagramctl.py sync architecture.drawio ./infra --from terraform -o architecture.next.drawio
   python3 scripts/diagramctl.py views architecture.ir.json --views executive,system,deployment,dataflow,security -o views.drawio
   python3 scripts/diagramctl.py test architecture.drawio --rules policy.yml
   python3 scripts/diagramctl.py review architecture.drawio -o review.md
   ```
3. **Invariantes de Formato y Estructura en Draw.io:**
   - IDs semánticos únicos (nunca reusar `0` o `1`).
   - Cada arista exige `<mxGeometry relative="1" as="geometry"/>`.
   - Formas y estilos verificados en [references/drawio/shapes.md](references/drawio/shapes.md) y [references/drawio/style-presets.md](references/drawio/style-presets.md).
   - Validación estructural con `scripts/validate.py <archivo.drawio> --score`.

---

## Contrato de Salida

1. **En `mode: "mermaid"`:**
   - Bloque Markdown ```mermaid con el diagrama.
   - Breve acápite de validación: tipo de diagrama, fuentes y preflight textual.
2. **En `mode: "drawio"`:**
   - Archivo `.drawio` creado o modificado con ruta absoluta.
   - Resumen estructural de capas, componentes y conexiones.
3. **En `mode: "dual"`:**
   - Bloque Markdown ```mermaid para previsualización inmediata en la respuesta.
   - Archivo `.drawio` generado en disco con enlace accesible para su edición en diagrams.net.
