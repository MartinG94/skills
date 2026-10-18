# Catálogo Maestro de Estilos UI, Paletas Semánticas, Tipografía y Ergonomía

Este documento es la referencia enciclopédica de la skill `uiUxProMax`, inspirada en la arquitectura de diseño de `nextlevelbuilder/ui-ux-pro-max-skill`. Proporciona matrices de decisión y especificaciones directas para interfaces web, móviles y de escritorio.

---

## 1. Matriz de Selección de Estilos Visuales

| Estilo Visual | Atmósfera y Lenguaje | Casos de Uso Ideales | Propiedades Clave de CSS / Tokens |
|---|---|---|---|
| **Editorial Minimalism** | Espacio negativo generoso, titulares con serifa de alto contraste, tipografía como protagonista, lujo silencioso. | Marcas premium, plataformas de lectura, moda, arquitectura, publicaciones de alta gama. | Fondos marfil/blanco puro, titulares `serif` (`Playfair`, `Newsreader`), `letter-spacing: -0.02em`, líneas de separación ultra-delgadas `0.5px`. |
| **Technical Dark UI** | Estética técnica de alta precisión, negro profundo con bordes sutiles de luminancia, detalles en monospace. | Herramientas para desarrolladores (DevTools), consolas cloud, terminales de datos, plataformas cripto. | Fondo `oklch(0.14 0.01 260)` / `#09090b`, bordes `1px solid oklch(0.24 0.02 260)`, acentos cian/violeta eléctrico, `tabular-nums`. |
| **Bento Grid** | Distribución modular asimétrica de tarjetas (`col-span-1/2/3`), alta densidad visual organizada, ritmo dinámico. | Páginas de producto, dashboards ejecutivos, resúmenes de características tipo Apple/Linear. | CSS Grid interactivo, bordes redondeados consistentes (`rounded-2xl` o `16px`), fondos de tarjeta `rgba(255,255,255,0.03)` o gris suave. |
| **Swiss International** | Grilla matemática rigurosa, legibilidad absoluta, tipografía grotesca limpia, funcionalidad sin artificios. | Software empresarial, sistemas de gestión pública, paneles de control corporativos, ERPs. | `Inter` / `Neue Haas Grotesk`, alineación estricta a grilla de 8 columnas, jerarquía por peso tipográfico, paleta acromática con acento único. |
| **Controlled Neo-Brutalism** | Bordes negros gruesos, sombras proyectadas sin desenfoque (*hard shadows*), colores saturados con energía cruda. | Herramientas creativas, apps para comunidades jóvenes, fintechs disruptivas, startups Web3. | Bordes `2px solid #000`, sombras `box-shadow: 4px 4px 0px #000`, micro-rotaciones `transform: rotate(-1deg)` en hover, botones táctiles. |
| **High-Craft Glassmorphism** | Capas translúcidas con desenfoque de fondo profundo, bordes reflectivos y orbes de luz ambiental. | Sistemas operativos modernos, interfaces espaciales (Spatial UI), modales flotantes, reproductores de audio. | `backdrop-filter: blur(20px)`, fondo `rgba(255, 255, 255, 0.05)`, borde `1px solid rgba(255, 255, 255, 0.12)`, gradientes radiales difusos. |
| **Spatial UI** | Profundidad óptica multicapa, elevación física, sombras de ambiente direccionales, interfaces en lienzo infinito. | Editores de nodos, canvas colaborativos, aplicaciones de realidad extendida o escritorio profesional. | Sombras dobles compuestas (sombra difusa amplia + sombra de contacto compacta), z-index jerarquizado, escalas en interacción. |

---

## 2. Paletas de Color Semánticas por Industria (Hex & OKLCH)

### 2.1. SaaS B2B y Software Empresarial
*Enfoque:* Fiabilidad, estabilidad, contraste nítido y reducción de fatiga visual.
- **Background Principal:** `#f8fafc` / `oklch(0.98 0.005 240)` (Dark: `#0f172a` / `oklch(0.18 0.03 260)`)
- **Superficie de Tarjeta:** `#ffffff` / `oklch(1.0 0 0)` (Dark: `#1e293b` / `oklch(0.24 0.03 260)`)
- **Texto Principal:** `#0f172a` / `oklch(0.18 0.03 260)` (Dark: `#f8fafc` / `oklch(0.98 0.005 240)`)
- **Color Primario (Brand):** `#2563eb` / `oklch(0.54 0.22 260)` (Azul royal corporativo)
- **Acento Semántico (Success):** `#10b981` / `oklch(0.70 0.17 155)` (Esmeralda)
- **Borde / Separador:** `#e2e8f0` / `oklch(0.92 0.01 240)` (Dark: `oklch(0.28 0.03 260)`)

### 2.2. Fintech y Gestión Patrimonial
*Enfoque:* Prestigio, precisión numérica, claridad entre activos, rendimientos y alertas.
- **Background Principal:** `#ffffff` (Dark: `#080c14` / `oklch(0.12 0.02 250)`)
- **Superficie Elevada:** `#f1f5f9` (Dark: `#111827` / `oklch(0.19 0.02 255)`)
- **Color Primario:** `#0f766e` / `oklch(0.51 0.10 195)` (Verde azulado profundo / Teal patrimonial)
- **Acento Rendimiento Positivo (Profit):** `#16a34a` / `oklch(0.65 0.20 145)`
- **Acento Rendimiento Negativo (Drawdown):** `#dc2626` / `oklch(0.58 0.22 25)`
- **Acento Metales / Oro:** `#d97706` / `oklch(0.68 0.16 65)`

### 2.3. AI Platforms & Developer Tools
*Enfoque:* Inmersión técnica, contraste de código, tokens visuales eléctricos.
- **Background Principal (Canvas):** `#09090b` / `oklch(0.14 0.01 260)` (Zinc puro)
- **Superficie de Trabajo:** `#18181b` / `oklch(0.20 0.01 260)`
- **Bordes y Guías:** `oklch(0.28 0.02 260)` (`1px solid`)
- **Acento Primario (AI / Prompt):** `#8b5cf6` / `oklch(0.62 0.24 290)` (Violeta eléctrico) o `#06b6d4` (Cian)
- **Sintaxis de Código:** Monospace con tokens diferenciados (Strings en ámbar `#f59e0b`, Funciones en zafiro `#3b82f6`).

### 2.4. E-Commerce & Retail de Consumo
*Enfoque:* Impulso visual de producto, llamadas a la acción irresistibles, calidez.
- **Background:** `#fafaf9` / `oklch(0.98 0.003 80)` (Tono piedra cálido)
- **Superficies:** `#ffffff`
- **Texto Principal:** `#1c1917` / `oklch(0.18 0.01 50)`
- **Botón Primario (CTA):** `#18181b` (Negro táctil absoluto) o `#ea580c` / `oklch(0.62 0.21 40)` (Naranja terracota)
- **Badges de Descuento / Stock:** `#e11d48` / `oklch(0.58 0.24 15)`

---

## 3. Motor de Emparejamiento Tipográfico

| Nombre del Paquete | Display / Titulares | Cuerpo de Texto (UI Sans) | Código / Métricas (Mono) | Personalidad Visual |
|---|---|---|---|---|
| **Tech Performance** | `Geist Sans` / `Inter Display` | `Inter` / `Geist Sans` | `Geist Mono` / `JetBrains Mono` | Rápido, nítido, moderno, densidad óptima. |
| **Editorial Heritage** | `Fraunces` / `Newsreader` | `Plus Jakarta Sans` | `IBM Plex Mono` | Distinguido, narrativo, elegante, cálido. |
| **Swiss System** | `Neue Haas Grotesk` / `Archivo` | `SF Pro` / `Inter` | `Space Mono` | Objetivo, analítico, neutral, corporativo. |
| **Neo-Brutalist Bold** | `Space Grotesk` | `Satoshi` / `General Sans` | `Fira Code` | Enérgico, experimental, con presencia gráfica. |

### Regla de Oro Tipográfica
- Aplicar siempre `font-variant-numeric: tabular-nums` a columnas de datos numéricos, precios, timestamps y tablas financieras.
- Utilizar `text-wrap: balance` para encabezados (evita viudas) y `text-wrap: pretty` para bloques de texto editorial.

---

## 4. Matriz de Selección de Visualizaciones y Gráficos (Data Viz)

| Objetivo Analítico | Tipo de Gráfico Recomendado | Evitar Rigurosamente |
|---|---|---|
| **Tendencia temporal continua** | Gráfico de Líneas con spline suave o Área degradada. | Gráfico de barras con más de 25 categorías temporales. |
| **Comparación entre categorías discretas** | Gráfico de Barras Horizontales (permite etiquetas largas sin rotar). | Gráfico de pastel (pie chart) con etiquetas en diagonal. |
| **Composición de parte a todo** | Donut Chart con $\le 4$ rebanadas y leyenda central o barras apiladas normalizadas. | Gráfico de pastel 3D con múltiples categorías diminutas. |
| **Distribución y densidad** | Histograma, Box Plot o Diagrama de Violín. | Gráfico de dispersión sin transparencia (overplotting). |
| **Métrica ejecutiva única** | Card KPI con valor destacado, delta porcentual con badge de color y mini sparkline de 7 días. | Gráfico de tacómetro o velocímetro skeuomórfico recargado. |

---

## 5. Ergonomía Cross-Platform y Presets de Movimiento

### 5.1. Reglas por Plataforma
- **Web Responsive:** Áreas táctiles mínimas de $44 \times 44\text{px}$ en móvil; navegación inferior anclada (*bottom navigation*) para pantallas táctiles y teclado rápido (*shortcuts*) en desktop.
- **iOS HIG (Human Interface Guidelines):** Respetar Safe Area insets (`env(safe-area-inset-top/bottom)`), transiciones nativas tipo UINavigation y retroalimentación háptica en acciones críticas.
- **Android Material 3:** Enfoque en esquinas orgánicas (`shape: rounded`), colores dinámicos derivados de la paleta del sistema y comportamiento predictivo de retroceso.
- **Desktop Pro:** Densidad compacta de información, soporte exhaustivo de teclado (`Tab`, `Esc`, `Cmd+K` / `Ctrl+K`), menús contextuales al clic derecho y tooltips instantáneos.

### 5.2. Presets de Física y Movimiento
- **Micro-interacción táctil (Botón/Switch):** `150ms cubic-bezier(0.16, 1, 0.3, 1)` (respuesta de resorte instantánea).
- **Aparición de Modal / Popover:** `250ms cubic-bezier(0.25, 0.9, 0.3, 1)` con escala de `0.96` a `1.0` y opacidad progresiva.
- **Expansión de Tarjeta / Layout Morphing:** `400ms cubic-bezier(0.32, 0.72, 0, 1)` (física suave sin rebote excesivo).
