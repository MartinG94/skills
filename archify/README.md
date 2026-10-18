# archify

Herramienta para generar documentos de arquitectura interactivos y autónomos en HTML sin dependencias externas (zero-dependency standalone HTML) y mapas visuales del sistema a partir de código o especificaciones técnicas.

Inspirada en `tt-a1i/archify`, permite a equipos de ingeniería explorar, presentar y auditar la arquitectura de software de forma interactiva y visual en cualquier navegador web.

---

## 1. Propósito General

`archify` automatiza la creación de visualizaciones arquitectónicas de nivel profesional sin obligar al usuario a instalar servidores pesados o configurar herramientas complejas:
- **Autonomía:** Produce un único archivo `.html` autocontenido que se abre directamente con doble clic (`file:///`).
- **Exploración Interactiva:** Incluye filtrado por capas, buscador en tiempo real, cambio de tema claro/oscuro y panel de inspección de componentes.
- **Múltiples Perspectivas:** Proporciona vistas estructurales C4, flujos de datos, matrices de dependencias y secuencias en orientación horizontal (`LR`).

---

## 2. Arquitectura Interna

```
archify/
├── SKILL.md                                # Contrato operacional del agente (YAML frontmatter + directivas)
├── README.md                               # Documentación técnica para desarrolladores
└── references/                             # Especificaciones y plantillas de diseño
    └── html-architecture-spec.md          # Especificación del documento HTML autónomo y esquema JSON
```

---

## 3. Prerequisitos de Entorno

- **Para generar el documento:** Ninguno obligatorio; el agente genera el archivo HTML autónomo directamente.
- **Para visualizar el resultado:** Cualquier navegador moderno (Chrome, Firefox, Safari, Edge) capaz de abrir archivos locales (`file://`).

---

## 4. Ejemplos de Invocación y Uso

### Generar Documento Completo de Arquitectura
```markdown
/archify
```
*Equivalente en lenguaje natural:* "Analiza el repositorio actual y genera un documento interactivo architecture.html con la estructura de capas, componentes y dependencias."

### Generar Mapa Visual para una Especificación Concreta
```markdown
/archify --spec docs/SPEC.md
```
*Equivalente en lenguaje natural:* "Toma la especificación técnica en docs/SPEC.md y crea un mapa visual de arquitectura interactivo con sus flujos de datos."

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Código fuente del proyecto o repositorio (`C:\git\<repo>`).
- Especificación técnica, archivo de diseño o plan de arquitectura (`SPEC.md`, `PLAN.md`).
- Grafos o modelos preexistentes (`graphify-out/graph.json` o índices de `codebase-memory`).

### Salidas (Outputs)
- `architecture.html`: Documento interactivo autónomo con estilos CSS, scripts de interacción, datos JSON embebidos y diagramas.
- Resumen ejecutivo en Markdown (`ARCHITECTURE_SUMMARY.md`) con diagramas Mermaid `flowchart LR` para lectura rápida en pull requests o terminal.
