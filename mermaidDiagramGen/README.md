# Generador de Diagramas Mermaid y Síntesis de Estados (`mermaidDiagramGen`)

Esta skill permite a los agentes de inteligencia artificial diseñar, estructurar, validar y generar diagramas formales en **Mermaid.js** con máxima precisión visual y sintáctica, basándose estrictamente en las especificaciones oficiales y evitando errores comunes de compilación. Además, incorpora capacidades avanzadas de **Síntesis Formal de Máquinas de Estados UML 2.5** y generación de **Matrices de Transición de Estados (MTE)**.

---

## Estructura de la Skill

```text
mermaidDiagramGen/
├── SKILL.md            # Instrucciones del agente, reglas sintácticas, linter pre-vuelo y catálogo
├── README.md           # Este manual de referencia y documentación de la skill
└── references/         # Catálogo local de 30 especificaciones oficiales de sintaxis de Mermaid
    ├── architecture.md             # Arquitectura cloud e infraestructura (layout fcose)
    ├── block.md                    # Diagramas de bloques posicionales y compuestos
    ├── c4.md                       # Modelo C4 (Context, Container, Component, Deployment)
    ├── classDiagram.md             # Diagramas de clases UML y relaciones de dominio
    ├── cynefin.md                  # Matriz de toma de decisiones Cynefin
    ├── entityRelationshipDiagram.md# Diagramas Entidad-Relación (ERD) con PK/FK
    ├── eventmodeling.md            # Modelado de eventos en arquitecturas distribuidas
    ├── examples.md                 # Galería y ejemplos transversales de diagramas
    ├── flowchart.md                # Flujogramas, subgrafos y formas v11.3+ (@{ shape: ... })
    ├── gantt.md                    # Cronogramas y dependencias de proyecto Gantt
    ├── gitgraph.md                 # Flujos de ramificación y releases Git
    ├── ishikawa.md                 # Diagramas de causa-efecto (espina de pescado)
    ├── kanban.md                   # Tableros Kanban de gestión de tareas
    ├── mindmap.md                  # Mapas mentales conceptuales y jerárquicos
    ├── packet.md                   # Protocolos de red y maquetación de paquetes de bits
    ├── pie.md                      # Gráficos circulares de porcentajes
    ├── quadrantChart.md            # Matrices 2x2 (priorización, DAFO/SWOT)
    ├── radar.md                    # Gráficos multivariables de radar/araña
    ├── requirementDiagram.md       # Diagramas de requerimientos y trazabilidad SysML
    ├── sankey.md                   # Diagramas de flujo y balance de recursos/costos
    ├── sequenceDiagram.md          # Diagramas de secuencia UML con activaciones y loops
    ├── stateDiagram.md             # Diagramas de máquina de estados UML 2.5
    ├── timeline.md                 # Líneas temporales e hitos cronológicos
    ├── treeView.md                 # Vistas de árbol jerárquicas
    ├── treemap.md                  # Mapas de árbol rectangulares proporcionales
    ├── userJourney.md              # Flujos de experiencia de usuario y satisfacción
    ├── venn.md                     # Diagramas de conjuntos e intersecciones de Venn
    ├── wardley.md                  # Mapas estratégicos de Wardley (valor vs evolución)
    ├── xyChart.md                  # Gráficos cartesianos de barras y líneas
    └── zenuml.md                   # Diagramas de secuencia con sintaxis lógica ZenUML
```

---

## Capacidades Principales

### 1. Catálogo Completo de 30 Familias de Diagramas
Cubre la totalidad del ecosistema Mermaid.js bajo el principio de *Progressive Disclosure*: el agente consulta la especificación exacta en `references/` únicamente cuando la tarea lo requiere, economizando la ventana de contexto.

### 2. Síntesis Formal de Máquinas de Estados (UML 2.5)
- **Principio de Identidad de Ciclo de Vida**: Modela el ciclo de vida estricto de entidades transaccionales del dominio (`Pedido`, `Factura`, `Turno`, `Contrato`, etc.).
- **Matriz de Transición de Estados (MTE)**: Produce tablas formales con Estado Actual, Evento Disparador, Condición de Guarda `[Guarda]`, Acción Transaccional y Estado Siguiente.
- **Auditoría de Defectos**: Detecta y elimina estados inalcanzables (orphan states), deadlocks involuntarios y transiciones no deterministas.

### 3. Linter Pre-Vuelo y Prevención de Errores Sintácticos
Previene los errores de renderizado más frecuentes en Mermaid:
1. **La trampa de `end`**: Evita la palabra reservada `end` en minúscula dentro de diagramas de flujo.
2. **Ambigüedad con prefijos `o` y `x`**: Previene colisiones con puntas especiales en aristas (`---o`, `---x`).
3. **Caracteres especiales en etiquetas**: Fuerza el entrecomillado doble `["..."]` para textos con corchetes, llaves, paréntesis o barras.
4. **Markdown Strings (v11+)**: Aplica la sintaxis moderna `["`texto **negrita**`"]` para títulos complejos y saltos de línea limpios.
5. **Dos puntos en mensajes de secuencia**: Resuelve colisiones sintácticas al comunicar respuestas HTTP o códigos de error.
6. **Subgrafos legibles**: Define la orientación explícita (`direction LR/TB`) en subgrafos para prevenir diagramas espagueti.

---

## Cómo Solicitar Diagramas al Agente

Con la skill activa, puedes solicitar diagramas complejos con instrucciones naturales como:
- *"Genera un diagrama C4 Container de nuestra arquitectura de microservicios con API Gateway, Auth Service y PostgreSQL."*
- *"Diseña la máquina de estados formal y la Matriz de Transición (MTE) para el ciclo de vida de un Contrato de Alquiler."*
- *"Crea un diagrama de secuencia de autenticación OAuth2 con manejo de refresh token y bloques alt para errores."*
- *"Modela un diagrama Entidad-Relación para un sistema de historias clínicas con cardinalidades y claves foráneas."*
- *"Construye un gráfico de cuadrantes 2x2 para priorizar deuda técnica según impacto y esfuerzo."*
