# Catálogo de Sistemas de Diseño de Referencia y Reglas de Acabado

Este documento reúne perfiles de diseño de referencia inspirados en los estándares visuales de mayor prestigio de la industria moderna (`marvkr/better-design` y `madebymustafa/design-taste`). Proporciona tokens, superficies, bordes, tipografía y reglas de componentes para proyectos que requieran una dirección estética específica, junto con la guía de consulta del servidor MCP `better-design`.

---

## 1. Integración con el Servidor MCP `better-design`

Cuando el servidor MCP `better-design` esté configurado y disponible en el entorno, puede consultarse directamente para extraer especificaciones vivas:

### Herramientas MCP Disponibles:
1. `get-design-system`:
   - Permite consultar tokens, paletas de color, radios y jerarquía tipográfica para estilos específicos (ej. `linear`, `vercel`, `stripe`, `supabase`, `apple`, `notion`).
2. `get-review-rules`:
   - Recupera el checklist exhaustivo de reglas de revisión antes de entregar código frontend (focos accesibles, contraste, `tabular-nums`, prevención de CLS).
3. `get-component-pattern`:
   - Provee la implementación canónica y accesible de componentes interactivos (modales, dropdowns, command palettes, bento grids).

*Protocolo de Fallback:* Si el servidor MCP no está activo, utilizar directamente los 6 perfiles canónicos documentados en la siguiente sección.

---

## 2. Perfiles de Diseño de Referencia

### 2.1 Perfil "Linear" (Precision Dark UI / Developer Tool)
- **Tono y Filosofía:** Herramienta experta de alta velocidad, densidad compacta, sobria y orientada al teclado.
- **Superficies y Fondos:**
  - Base: `#08090a` o `#0f1012`
  - Superficie / Card: `#151619`
  - Hover / Elevado: `#1e2024`
- **Bordes y Sombras:**
  - Borde de luminancia: `1px solid rgba(255, 255, 255, 0.08)`
  - Sombras: Mínimas, sólo para popovers flotantes (`0 8px 24px rgba(0,0,0,0.6)`).
- **Radios:**
  - Controles y botones: `6px`
  - Tarjetas y paneles: `8px`
- **Tipografía:**
  - `Inter` con `font-feature-settings: 'cv02', 'cv03', 'cv04', 'cv11'`.
  - Jerarquía contenida: tamaños de texto entre `12px` y `14px` para la mayoría de controles, métricas en `tabular-nums`.
- **Acentos:**
  - Acento funcional: Índigo desaturado o azul eléctrico (`#5e6ad2`), utilizado exclusivamente en elementos interactivos primarios y focos.

### 2.2 Perfil "Vercel / Geist" (High-Contrast Geometric Minimalism)
- **Tono y Filosofía:** Contraste radical blanco/negro, precisión de ingeniería, ausencia de sombras difusas, aire técnico.
- **Superficies:**
  - Base: `#000000` (Dark) / `#ffffff` (Light)
  - Superficie: `#111111` (Dark) / `#fafafa` (Light)
  - Bordes: `1px solid #333333` (Dark) / `1px solid #eaeaea` (Light)
- **Radios:**
  - Botones y campos: `4px` o `6px` (ángulos geométricos limpios, sin formas de píldora salvo tags específicos).
- **Tipografía:**
  - `Geist Sans` para prosa e interfaces; `Geist Mono` para métricas, rutas, código y hashes.
- **Detalles Distintivos:**
  - Status dots de 6px (`#0070f3`, `#50e3c2`, `#ee0000`), grillas cuadriculadas tenues y divisores nítidos de 1px.

### 2.3 Perfil "Stripe" (Refined Enterprise FinTech)
- **Tono y Filosofía:** Confianza, dinamismo corporativo de alta gama, calidez y profundidad multicapa.
- **Superficies:**
  - Base: `#f6f9fc` (Light) / `#0a2540` (Dark corporativo)
  - Superficie: `#ffffff` con sombras multicapa cálidas y translúcidas:
    ```css
    box-shadow: 0 2px 4px rgba(50,50,93,0.06), 0 1px 1.5px rgba(0,0,0,0.04);
    ```
- **Radios:**
  - `8px` en inputs y botones; `12px` a `16px` en tarjetas principales.
- **Tipografía:**
  - Tipografía sans-serif editorial limpia con espaciado generoso (`line-height: 1.6`).
- **Acentos:**
  - Violeta corporativo (`#635bff`), aguamarina (`#00d4aaa`), naranja cálido y verde esmeralda para balances positivos.

### 2.4 Perfil "Supabase" (Developer Platform / Emerald Slate)
- **Tono y Filosofía:** Plataforma abierta de datos, amigable pero potente, alto contraste de legibilidad para logs y tablas.
- **Superficies:**
  - Base: `#121212` o `#171717`
  - Superficie / Sidebar: `#1c1c1c`
  - Borde: `1px solid #2e2e2e`
- **Acentos:**
  - Verde Esmeralda emblemático (`#3ecf8e` / `#24b47e`), aplicado a botones primarios, switches activos y estados de éxito.
- **Radios:**
  - `6px` uniforme en controles y tarjetas; compatibilidad estética directa con Radix UI y Tailwind CSS.

### 2.5 Perfil "Apple HIG" (Vibrancy, Blur & Human-Centered)
- **Tono y Filosofía:** Claridad, deferencia al contenido y profundidad ambiental mediante translucidez y materiales.
- **Superficies:**
  - Materiales acrílicos: `background: rgba(255, 255, 255, 0.72); backdrop-filter: blur(20px) saturate(180%);`
  - Dark Mode: `background: rgba(30, 30, 30, 0.75); backdrop-filter: blur(25px);`
- **Radios:**
  - Generosos y fluidos: `12px` en botones, `18px` a `24px` en tarjetas y hojas modales.
  - Estricto cumplimiento de radios concéntricos: $R_{outer} = R_{inner} + Padding$.
- **Tipografía:**
  - `SF Pro Display` / `SF Pro Text` con pesos contrastados y espaciado de seguimiento óptico (*optical tracking*).

### 2.6 Perfil "Notion" (Document-First / Warm Editorial Workspace)
- **Tono y Filosofía:** Espacio de trabajo sereno, mínimo ruido visual, sensación de papel mate y foco en escritura.
- **Superficies:**
  - Fondo: Blanco cálido (`#ffffff`) o modo oscuro tenue (`#191919`).
  - Divisores: Líneas ultra-delgadas (`rgba(55, 53, 47, 0.09)`).
- **Tipografía:**
  - Prosa estructurada, encabezados expresivos, etiquetas con fondos pasteles suaves desaturados (amarillo, azul, marrón suave).
- **Interacción:**
  - Controles que aparecen en hover (*progressive disclosure*) para mantener el documento despejado durante la lectura.

---

## 3. Matriz Comparativa de Tokens

| Atributo | Linear | Vercel | Stripe | Supabase | Apple | Notion |
|---|---|---|---|---|---|---|
| **Tema Primario** | Dark First | Monocromo Dark/Light | Light First | Dark Slate | Adaptable / Blur | Papel Neutro |
| **Borde Típico** | 1px Luminance (`8%`) | 1px Stark (`#333`) | Sutil / Sin borde | 1px Slate (`#2e2e`) | Translúcido | 1px tenue |
| **Radio de Card** | `8px` | `4px - 6px` | `12px - 16px` | `6px` | `18px - 24px` | `4px - 6px` |
| **Sombra** | Casi nula | Inexistente (bordes) | Cálida multicapa | Muy suave | Sombra difusa amplia | Casi nula |
| **Acento** | Índigo `#5e6ad2` | Azul `#0070f3` | Índigo `#635bff` | Verde `#3ecf8e` | Azul `#007aff` | Monocromo / Pasteles |
| **Tipografía** | Inter | Geist Sans/Mono | Modern Sans | Inter / Mono | SF Pro | Sans Editorial / Serif |
