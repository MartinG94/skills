---
name: uiUxProMax
description: >-
  Motor de inteligencia de diseño UI/UX para Web, Mobile y Desktop: selección
  determinista de estilos visuales (Editorial Minimalism, Technical Dark UI,
  Bento Grid, Swiss International, Neo-Brutalism, Glassmorphism, Spatial UI),
  paletas semánticas por vertical de industria en OKLCH/Hex, emparejamientos
  tipográficos calibrados, matriz de gráficos y ergonomía multiplataforma.
---

# Motor de Inteligencia de Diseño UI/UX y Dirección de Arte

## Responsabilidad y Enfoque

La skill `uiUxProMax` dota al agente de criterios avanzados de dirección de arte, diseño de sistemas de interfaz y ergonomía visual para aplicaciones Web, Móviles (iOS/Android) y de Escritorio. Impide la generación de interfaces genéricas o "clichés de IA" (gradientes púrpuras indiscriminados, sombras sucias, tipografía plana sin contraste de escala o grillas monótonas de 3 tarjetas).

Su flujo de trabajo opera a través de **cuatro compuertas de diseño integradas**:

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Compuerta 1:     │     │ Compuerta 2:     │     │ Compuerta 3:     │     │ Compuerta 4:     │
│ Matriz de Estilo │ ──> │ Paleta Semántica │ ──> │ Tipografía y     │ ──> │ Ergonomía y      │
│ & Dirección Visual│     │ por Industria    │     │ Visualización    │     │ Plataforma       │
└──────────────────┘     └──────────────────┘     └──────────────────┘     └──────────────────┘
```

---

## Compuerta 1: Matriz de Estilo y Dirección Visual

Antes de proponer componentes, hojas de estilo o maquetas, seleccionar el lenguaje visual adecuado según el contexto y la audiencia:

1. **Editorial Minimalism:** Espacios en blanco amplios, serifa refinada, contrastes tipográficos limpios para productos de contenido, lujo, arquitectura y cultura.
2. **Technical Dark UI:** Fondos zinc/carbón ultra-oscuros (`#09090b`), bordes milimétricos (`1px solid oklch(...)`), acentos técnicos y datos tabulares para DevTools, terminales y consolas cloud.
3. **Bento Grid:** Distribución modular asimétrica de tarjetas con pesos visuales variados (`col-span-1/2/3`) para escaparates de producto y paneles ejecutivos.
4. **Swiss International:** Grillas matemáticas puras de 8 a 12 columnas, sans-serif grotesca (`Inter`, `Neue Haas`), máxima legibilidad y sobriedad para software corporativo y ERPs.
5. **Controlled Neo-Brutalism:** Bordes oscuros gruesos (`2-3px solid`), sombras planas proyectadas sin desenfoque (`box-shadow: 4px 4px 0px`), micro-rotaciones y colores vivos para apps de creadores o comunidades.
6. **High-Craft Glassmorphism:** Difuminado de fondo multicapa (`backdrop-filter: blur(20px)`), bordes reflectivos y orbes ambientales para reproductores, modales e interfaces modernas.
7. **Spatial UI:** Jerarquía tridimensional, elevaciones compuestas y navegación en lienzo infinito para editores gráficos o suites de productividad.

---

## Compuerta 2: Paletas Semánticas y Contraste por Industria

Definir los tokens de color primarios, de superficie y de estado garantizando accesibilidad WCAG AAA en texto y AA en controles:

- **SaaS B2B & Enterprise:** Azules royal corporativos (`oklch(0.54 0.22 260)`), fondos neutros pizarra (`#f8fafc` / `#0f172a`), esmeralda para éxitos y bordes delgados de bajo contraste.
- **Fintech & Wealth:** Verdes azulados patrimoniales (`#0f766e`), fondos inmaculados, distinción rigurosa entre rendimientos positivos (verde bosque) y pérdidas (carmesí), con acentos ámbar/dorado para metales.
- **AI & Developer Platforms:** Lienzo carbón zinc (`#09090b`), acentos en violeta eléctrico (`#8b5cf6`) o cian (`#06b6d4`), sintaxis diferenciada con tokens legibles en monospace.
- **E-Commerce & Retail:** Fondos cálidos en piedra/marfil (`#fafaf9`), botones de acción directa en negro profundo o naranja terracota (`#ea580c`), y badges de stock en rubí vibrante.

---

## Compuerta 3: Emparejamiento Tipográfico y Visualización de Datos

1. **Escala y Emparejamiento Tipográfico:**
   - Asignar una combinación intencional de 3 familias: **Display** (titulares de impacto), **UI Sans** (cuerpo legible y optimizado para pantallas) y **Monospace** (métricas y código).
   - Aplicar `tabular-nums` a todo dato cuantitativo, hora o moneda.
   - Usar `text-wrap: balance` en encabezados y `text-wrap: pretty` en párrafos.
2. **Matriz de Gráficos (Data Viz):**
   - **Series temporales continuas:** Gráficos de línea o área suave.
   - **Comparación entre categorías:** Gráficos de barras horizontales (evitan rotación de etiquetas).
   - **Parte a todo:** Donut chart con leyenda central (máximo 4 categorías) o barra apilada normalizada; nunca gráficos de tarta en 3D ni con más de 5 divisiones.
   - **KPIs ejecutivos:** Cards de métrica con número principal, badge de tendencia porcentual y mini sparkline contextual.

---

## Compuerta 4: Ergonomía Multiplataforma

Asegurar que la experiencia respete las directrices nativas de cada sistema operativo:

- **Web Moderna:** Áreas interactivas mínimas de $44 \times 44\text{px}$, soporte de navegación por teclado (`Tab`, `Esc`, focus rings visibles con offset) y modo oscuro automático mediante `prefers-color-scheme`.
- **Móvil iOS (Apple HIG):** Respeto estricto a las áreas seguras (`env(safe-area-inset-*)`), navegación fluida con gestos de deslizamiento (*swipe to go back*) y micro-vibraciones hápticas en acciones destructivas.
- **Móvil Android (Material 3):** Esquinas suaves con radios orgánicos, soporte de color dinámico y animación de retroceso predictivo.
- **Desktop Profesional:** Alta densidad de información, atajos de teclado globales (`Cmd/Ctrl + K`), barras de comandos flotantes y persistencia de estado de paneles colapsables.

---

## Guía de Referencia Avanzada

Para consultar las tablas exhaustivas de estilos, valores exactos en Hex/OKLCH, combinaciones tipográficas de Google Fonts / Web fonts y especificaciones de curvas de movimiento, consultar:
- [Catálogo Maestro de Estilos UI, Paletas y Tipografía](file:///c:/git/skills/uiUxProMax/references/styles-palettes-typography.md)
