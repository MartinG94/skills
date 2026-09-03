# Guía de Extracción e Ingeniería Inversa de Sistemas de Diseño

Esta guía describe el protocolo sistemático para escanear un repositorio de código fuente existente (React, Vue, Svelte, Tailwind, CSS) y sintetizar su arquitectura visual en un archivo `DESIGN.md` fiel y canónico.

---

## 1. Detección de Stack y Fuentes de Verdad

Revisa en este orden de autoridad decreciente:

| Prioridad | Archivo / Fuente | Qué Extraer |
| :--- | :--- | :--- |
| **1. Máxima** | `tailwind.config.{js,ts,mjs}` | Paleta (`theme.extend.colors`), tipografías (`fontFamily`), radios (`borderRadius`), breakpoints. |
| **2. Alta** | `globals.css`, `index.css`, `theme.css` | Variables CSS en `:root` y `.dark` (`--primary`, `--background`, etc.). |
| **3. Media** | Bibliotecas de tokens (`tokens.json`, `theme.ts`, ThemeProvider) | Constantes estructuradas de colores y tamaños. |
| **4. Componentes** | `src/components/ui/` (Button, Card, Input) | Clases Tailwind recurrentes, radios y paddings de interacción. |

---

## 2. Clasificación Funcional de Colores

Al extraer colores del código, no los agrupes por tono (azul, gris); agrúpalos por rol funcional:

1. **Superficie y Base:**
   - Background principal del layout (ej. `bg-slate-50` o `#F8FAFC`).
   - Superficie de contenedores y tarjetas (ej. `bg-white` o `#FFFFFF`).
2. **Acento e Interacción:**
   - Color del botón principal, estados activos de navegación y foco.
3. **Jerarquía Tipográfica:**
   - Texto de alto contraste (títulos y texto primario).
   - Texto secundario (metadatos, placeholders, labels atenuadas).
4. **Bordes y Divisores:**
   - Líneas de contorno de 1px en tarjetas y separadores.

### Desduplicación Inteligente
Es muy habitual encontrar pequeñas variantes en proyectos reales:
- `#1E293B`, `#1E293C` y `#1F2A3D`.
**Acción:** Consolida estas variaciones en un único token normativo (ej. `{colors.primary}: "#1E293B"`) para limpiar la deuda técnica visual del repositorio.

---

## 3. Extracción de Tipografía y Escalas

1. **Familias tipográficas:**
   - Revisa fuentes locales en `@font-face` o imports de Google Fonts / Next Font (`@next/font/google`).
2. **Escala de encabezados:**
   - Mapea los estilos aplicados a `h1`, `h2`, `h3` y `p`.
   - Registra `fontSize`, `fontWeight` y `lineHeight`.
3. **Radios de curvatura:**
   - Verifica el redondeo dominante: botones rectangulares (`rounded-md`, ~6px) vs. píldoras (`rounded-full`).

---

## 4. Generación del Archivo `DESIGN.md`

El resultado debe consolidarse en `.stitch/DESIGN.md` o `./DESIGN.md`, estructurado con:
- Front-matter YAML normativo con tokens exactos.
- Prosa explicativa reflejando el propósito original del código.
- Validación final ejecutando `validate_design.ps1` para asegurar 0 errores de contraste WCAG AA.
