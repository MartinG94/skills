# Estudio de Arquitectura y Diagramación draw.io (`drawioStudio`)

Esta skill capacita a los agentes de inteligencia artificial para diseñar, estructurar, sincronizar incrementalmente, auditar y publicar diagramas y modelos de arquitectura en formato editable `.drawio` (diagrams.net). Integra el concepto de **Diagram IR** (Representación Intermedia de Diagramas), garantizando que las modificaciones automáticas preserven las coordenadas manuales y los ajustes visuales introducidos por los ingenieros.

---

## Estructura de la Skill

```text
drawioStudio/
├── SKILL.md            # Reglas operativas del agente, catálogo de flujos y comandos CLI
├── README.md           # Este manual técnico de referencia
├── agents/             # Prompts y especificaciones para subagentes especializados
├── data/               # Índices de formas oficiales (shape-index), schemas JSON y catálogos
├── references/         # Guías de autoría XML, Diagram IR, reglas de test y estilos
│   ├── ci-gate.md              # Integración de compuertas en GitHub Actions
│   ├── cookbook.md             # Recetario de prompts para tipos de diagrama
│   ├── databricks.md           # Iconografía y patrones de Lakehouse / Databricks
│   ├── derasterize.md          # Conversión de capturas/imágenes a diagramas editables
│   ├── diagram-ir.md           # Especificación canónica del Diagram IR
│   ├── diagram-types.md        # Catálogo de familias (C4, UML, ERD, Redes, BPMN, SysML)
│   ├── mcp.md                  # Especificación del servidor MCP diagramctl
│   ├── mermaid-authoring.md    # Conversión Mermaid a .drawio nativo (draw.io >= 30)
│   ├── security.md             # Guía de data residency y aislamiento offline
│   ├── semantic-workflows.md   # Políticas de arquitectura, What-If y Story Mode
│   ├── shapes.md               # Catálogo de +10.000 formas oficiales (AWS, Azure, GCP, K8s)
│   ├── style-presets.md        # Gestión de paletas visuales (corporate, dark, handdrawn)
│   ├── toolbox.md              # Catálogo completo de scripts de transformación
│   ├── troubleshooting.md      # Diagnóstico y resolución de incidencias de exportación
│   └── xml-authoring.md        # Estándar de sintaxis XML mxGraph / draw.io
├── scripts/            # Motor determinista en Python 3 (stdlib / offline)
│   ├── diagramctl.py           # CLI unificada (doctor, build, sync, views, test, query, story)
│   ├── diagramctl_mcp.py       # Servidor MCP stdio embebido con 9 herramientas agénticas
│   ├── autolayout.py           # Motor de posicionamiento y distribución de nodos
│   ├── shapesearch.py          # Búsqueda local de estilos en el índice oficial de draw.io
│   ├── aiicons.py              # Catálogo de 321 logos de IA/LLM y almacenes de datos RAG
│   ├── diagram_ir.py           # Core del motor Diagram IR
│   ├── seqlayout.py            # Generación determinista de diagramas de secuencia
│   ├── c4.py                   # Generación de modelos C4 con drill-down entre páginas
│   ├── sqlerd.py               # Extracción de esquemas SQL DDL a ERD con patas de gallo
│   ├── tfimports.py / tfstate.py   # Extracción de infraestructura Terraform (código y estado)
│   ├── k8simports.py           # Extracción de manifiestos y clústeres Kubernetes
│   ├── pyimports.py / jsimports.py # Extracción de grafos de dependencias e importaciones
│   ├── openapiimports.py       # Extracción de especificaciones OpenAPI/Swagger
│   ├── validate.py             # Linter estructural de geometrías y conectores
│   └── drawiohtml.py           # Exportador a visores HTML interactivos independientes
└── styles/             # Presets visuales listos para aplicar (dark, corporate, etc.)
```

---

## Capacidades Principales

### 1. Sincronización Incremental sin Pérdida de Diagramación (`diagramctl sync`)
A diferencia de los generadores básicos que reescriben el archivo XML completo destruyendo el trabajo manual, `drawioStudio` utiliza **Diagram IR** para comparar la nueva especificación con el archivo `.drawio` existente:
- Preserva coordenadas `(x, y)`, anchos, alturas y dobleces de conectores ajustados manualmente.
- Actualiza únicamente nodos y relaciones modificados.
- Marca elementos eliminados en modo atenuado (*faded*) para revisión antes de podar.

### 2. Extracción Automatizada desde Fuentes Reales
Convierte artefactos de software en diagramas de arquitectura sin requerir coordenadas manuales:
- **Código y AST**: Grafos de importación en Python, TypeScript, Go y Rust; jerarquía de herencia de clases Python.
- **Infraestructura como Código (IaC)**: Terraform (asigna automáticamente iconos oficiales de AWS, Azure y GCP), Kubernetes (manifiestos YAML y clúster en vivo vía `kubectl`), Docker Compose.
- **Bases de Datos y APIs**: Scripts SQL `CREATE TABLE` a Diagramas Entidad-Relación (ERD); contratos OpenAPI a diagramas de servicios y endpoints.

### 3. Architecture-as-Test & CI Gates
Permite auditar diagramas arquitectónicos contra políticas institucionales en formato YAML/JSON:
- **Reglas de seguridad**: Prohibición de accesos directos desde el perímetro de Internet a bases de datos sin mediación de API Gateway o backend.
- **Higiene arquitectónica**: Detección de ciclos de dependencia, componentes huérfanos o falta de instrumentación de observabilidad en entornos productivos.
- **Accesibilidad**: Verificación de contrastes de color WCAG AA en los estilos utilizados.

### 4. Vistas Proyectadas y Story Mode
- **Multi-vistas**: A partir de un único modelo IR, proyecta automáticamente vistas especializadas (vista ejecutiva, vista de sistema, vista de despliegue, flujo de datos y modelo de seguridad C4).
- **Story Mode**: Genera un visor HTML autónomo, accesible por teclado y con alternativa de texto, que permite realizar recorridos guiados paso a paso de la arquitectura sin dependencias externas.

---

## Comandos Esenciales de la CLI

Todos los comandos pueden ejecutarse desde la raíz de la skill mediante Python 3:

```bash
# Diagnóstico de capacidades y dependencias locales
python scripts/diagramctl.py doctor --probe

# Construir diagrama a partir de código o infraestructura
python scripts/diagramctl.py build ./infra --from terraform --group -o arquitectura.drawio

# Sincronizar cambios preservando el layout manual existente
python scripts/diagramctl.py sync arquitectura.drawio ./infra --from terraform -o arquitectura.drawio

# Búsqueda de formas e iconos oficiales (AWS, Azure, GCP, K8s, UML, BPMN)
python scripts/shapesearch.py "aws lambda" --limit 3

# Buscar logos de marcas de IA / LLMs para arquitecturas RAG
python scripts/aiicons.py "claude" --json

# Validar calidad y reglas del diagrama
python scripts/diagramctl.py test arquitectura.drawio --rules politicas.yml
python scripts/validate.py arquitectura.drawio --score

# Exportación headless nativa (vía draw.io Desktop 31.4.2)
drawio -x -f png -e -s 2 -o arquitectura.drawio.png arquitectura.drawio
drawio -x -f pdf -e -o arquitectura.pdf arquitectura.drawio
```

---

## Integración MCP

La skill cuenta con un servidor MCP nativo expuesto a través de `scripts/diagramctl_mcp.py` que provee 9 herramientas semánticas (`build`, `sync`, `views`, `architecture_test`, `review`, `query`, `whatif`, `story`, `doctor`) configuradas en el entorno global del agente.