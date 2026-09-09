# designUxUi

Herramienta integral de diseño, auditoría y prototipado de interfaces de usuario web, sistemas de diseño (DESIGN.md) y widgets interactivos embebidos.

---

## 1. Propósito General

`designUxUi` herramienta integral de diseño, auditoría y prototipado de interfaces de usuario web, sistemas de diseño (design.md) y widgets interactivos embebidos.

### Capacidades Principales:
- **Sistemas de Diseño y Tokens (`DESIGN.md`):** Genera y audita especificaciones tipográficas, paletas de color semánticas, espaciados y jerarquías visuales.
- **Matrices de Diálogo Pantalla-Gestor (DSI):** Mapea la interacción entre pantallas de usuario y controladores/gestores del sistema.
- **Auditoría Heurística de Usabilidad:** Evalúa interfaces según las 10 heurísticas de Nielsen, accesibilidad WCAG 2.1 y directivas de usabilidad.
- **Widgets Interactivos Embebidos:** Genera componentes web interactivos (`<agent-embed>`) con soporte para temas, variables CSS de host y Tailwind CSS.

---

## 2. Arquitectura Interna

```
designUxUi/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── agents/                                 # Definición de agentes especializados
│   └── openai.yaml
├── references/                             # Manuales y normativas de experiencia de usuario
│   ├── course-source-map.md                # Trazabilidad académica DSI
│   ├── design-tokens-spec.md               # Especificación técnica de tokens de diseño
│   ├── designmd-cli.md                     # Directivas de integración CLI
│   ├── dsi-dialog-matrix.md                # Matriz de diálogo Pantalla-Gestor
│   ├── extract-code-guide.md               # Guía de extracción de código frontend
│   ├── interface-craft.md                  # Pautas de diseño y microinteracciones
│   ├── preview-and-runtime.md              # Entorno de previsualización y widgets
│   ├── quality-gates.md                    # Criterios de aceptación y accesibilidad
│   ├── taste-design-guide.md               # Pautas estilísticas y de refinamiento visual
│   └── ux-method.md                        # Metodología de investigación y diseño UX
├── resources/templates/                    # Plantillas de artefactos visuales
│   ├── DESIGN-minimal.template.md          # Plantilla básica de diseño
│   ├── DESIGN-taste.template.md            # Plantilla con foco en identidad estética
│   ├── DESIGN-theme.template.md            # Plantilla con tokens de color y tema
│   ├── DESIGN.template.md                  # Plantilla maestra de especificación de diseño
│   ├── UX-AUDIT.template.md                # Plantilla de informe de auditoría heurística
│   └── widget-embed.template.html          # Esqueleto HTML de widget interactivo reactivo
└── scripts/                                # Herramientas de extracción y previsualización
    ├── export_tokens.ps1                   # Exportación de tokens a formatos consumibles
    ├── extract_tokens.py                   # Extractor de tokens desde CSS/diseños
    ├── serve_preview.py                    # Servidor local de previsualización web
    └── validate_design.ps1                 # Validador de conformidad de tokens y diseño
```

---

## 3. Prerequisitos de Entorno

- Python 3.8+ (para `serve_preview.py` y `extract_tokens.py`).\n- PowerShell 5.1+ (para scripts `.ps1`).

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Auditoría Heurística y Matriz de Diálogo
Entradas: Vistas de la aplicación de Gestión de Pacientes y flujos de navegación.
Salida: Informe UX-AUDIT con hallazgos clasificados por severidad y matriz de diálogo Pantalla-Gestor.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Requisitos de interfaz de usuario, wireframes o capturas de pantalla.
- Especificaciones de casos de uso y eventos de interfaz.
- Archivos `DESIGN.md` o estilos CSS preexistentes.

### Salidas (Outputs)
- Archivo `DESIGN.md` con tokens de diseño estandarizados.
- Matriz de Diálogo Pantalla-Gestor (DSI).
- Informe formal de auditoría de usabilidad `UX-AUDIT.md`.
- Prototipos HTML autónomos interactivos (`widget-embed.html`).
