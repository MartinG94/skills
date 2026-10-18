# uiUxProMax

Motor de inteligencia de diseño y dirección de arte UI/UX basado en `nextlevelbuilder/ui-ux-pro-max-skill`. Proporciona catálogos estructurados de estilos visuales, paletas cromáticas semánticas por vertical de negocio en OKLCH/Hex, emparejamientos tipográficos calibrados, heurísticas de visualización de datos y directrices ergonómicas para aplicaciones Web, iOS, Android y Desktop.

---

## 1. Propósito General

`uiUxProMax` eleva el estándar visual y funcional de los productos digitales. Su objetivo es erradicar el diseño plano o estereotipado generado por modelos de lenguaje, sustituyéndolo por decisiones de diseño fundamentadas en la semántica de la industria, la jerarquía óptica y la ergonomía del usuario.

### Capacidades Principales:
- **Matriz de Estilos Visuales:** Criterios formales para Editorial Minimalism, Technical Dark UI, Bento Grid, Swiss International, Neo-Brutalism, High-Craft Glassmorphism y Spatial UI.
- **Paletas Semánticas en OKLCH y Hex:** Paletas calibradas para SaaS B2B, Fintech, AI & DevTools, Healthcare y E-commerce, con contraste garantizado WCAG AAA.
- **Sistema de Tipografía y Escalas:** Emparejamientos calibrados (Display + UI Sans + Monospace), espaciado óptico y tratamiento numérico (`tabular-nums`).
- **Data Visualization Intelligence:** Selección matemáticamente adecuada de gráficos estadísticos según el tipo de variable y audiencia.
- **Ergonomía Multiplataforma:** Adaptación a las guías de diseño de Apple (iOS HIG), Google (Material 3) y aplicaciones de escritorio complejas.

---

## 2. Arquitectura Interna

```
uiUxProMax/
├── SKILL.md                                # Contrato operacional del agente y las 4 compuertas de diseño
├── README.md                               # Documentación técnica de la skill
└── references/                             # Catálogos y matrices de diseño
    └── styles-palettes-typography.md       # Tablas de estilos, paletas por industria, fuentes y física de animación
```

---

## 3. Prerequisitos de Entorno

- No requiere dependencias de software complejas.
- Compatible con frameworks de estilos modernos: Tailwind CSS v3/v4, CSS Modules, Styled Components, vanilla CSS con variables nativas o tokens de Figma/Tokens Studio.

---

## 4. Ejemplos de Invocación y Uso

### Caso 1: Dirección de Arte para Plataforma AI DevTools
```markdown
Solicitud: Diseñar la interfaz de un playground de prompts y consola de logs.
Decisión uiUxProMax:
- Estilo: Technical Dark UI con acentos cian/violeta.
- Paleta: Fondo #09090b, bordes oklch(0.24 0.02 260) de 1px.
- Tipografía: Geist Sans para interfaz y JetBrains Mono para código y números tabulares.
- Ergonomía: Barra de comandos flotante (Cmd+K) y atajos de teclado para ejecución rápida.
```

### Caso 2: Dashboard Financiero de Inversiones
```markdown
Solicitud: Proponer visualizaciones y paleta para panel de gestión de carteras patrimoniales.
Decisión uiUxProMax:
- Estilo: Swiss International con Bento Grid asimétrico.
- Paleta: Teal patrimonial (#0f766e), verde esmeralda para ganancias y carmesí para pérdidas.
- Visualización: Gráfico de área suavizada para evolución del portfolio y donut chart (máx. 3 clases de activos) para asset allocation.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Descripción del producto, público objetivo e industria.
- Requisitos funcionales de pantallas, vistas o componentes.
- Restricciones de marca existentes (logotipos, fuentes corporativas o colores primarios).

### Salidas (Outputs)
- Especificación de tokens de diseño (CSS variables, configuración Tailwind o tema de componentes).
- Código de componentes HTML/CSS/React/Vue estructurados con accesibilidad nativa y física de interacción fluida.
- Justificación técnica de la selección de estilos, tipografías y visualizaciones analíticas.
