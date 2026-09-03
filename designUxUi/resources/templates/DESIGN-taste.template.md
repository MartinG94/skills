---
version: "alpha"
name: "EditorialStudioTaste"
description: "Sistema de diseño premium con estética de estudio de arquitectura y altos estándares tipográficos"
colors:
  primary: "#121214"
  secondary: "#52525B"
  accent: "#1E3A8A"
  background: "#FAFAFA"
  surface: "#FFFFFF"
  border-subtle: "#E4E4E7"
  text-white: "#FFFFFF"
typography:
  display:
    fontFamily: "Geist, Cabinet Grotesk, sans-serif"
    fontSize: "2.5rem"
    fontWeight: "700"
    letterSpacing: "-0.03em"
  h1:
    fontFamily: "Geist, Cabinet Grotesk, sans-serif"
    fontSize: "2rem"
    fontWeight: "600"
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Geist, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: "400"
    lineHeight: "1.6"
  mono:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "0.8125rem"
    fontWeight: "400"
rounded:
  sm: "4px"
  md: "6px"
  lg: "10px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "40px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text-white}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "24px"
  divider:
    backgroundColor: "{colors.border-subtle}"
    height: "1px"
  layout-base:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
---

## Overview
Estética inspirada en un estudio de diseño contemporáneo y publicación editorial de alta gama. El espacio negativo es generoso y los elementos respiran sin apretujarse. Se evitan por completo los clichés de diseño de inteligencia artificial.

## Colors
- **Primary (#121214):** Carbón profundo mate (Zinc-950) para titulares y texto primario. Cero negro absoluto.
- **Secondary (#52525B):** Neutro pizarra equilibrado para metadatos, subtítulos y elementos de apoyo.
- **Accent (#1E3A8A):** Azul marino profundo de alta distinción como único color de interacción.
- **Background (#FAFAFA):** Lienzo neutro roto que elimina la fatiga del blanco puro.
- **Surface (#FFFFFF):** Tarjetas nítidas delimitadas por un borde sutil de 1px.

## Typography
Uso exclusivo de Geist y Cabinet Grotesk con espaciado entre letras track-tight en titulares para dar sensación de precisión arquitectónica. Las cifras y valores numéricos se renderizan en JetBrains Mono.

## Layout
Composición asimétrica en secciones principales (Split 60/40). Cuadrículas tipo bento-box con proporciones calibradas en lugar de filas de 3 tarjetas repetidas.

## Elevation & Depth
Superficies planas con bordes de precisión de 1px (`#E4E4E7`). Sombras hiper-difuminadas casi imperceptibles, sin resplandores de color.

## Shapes
Radios contenidos (6px a 10px) que otorgan solidez y madurez formal sin caer en redondeos excesivos.

## Components
- **button-primary:** Respuesta táctil al presionar (`active:translate-y-[1px]`), sin sombras brillantes ni efectos de rebote artificial.
- **card:** Tarjetas estructuradas con espaciado interno amplio (24px) y jerarquía clara.

## Do's and Don'ts
- **HACER:** Mantener la relación de contraste WCAG AA siempre por encima de 4.5:1.
- **HACER:** Usar tipografías con carácter (Geist / Cabinet Grotesk / Outfit).
- **NO HACER:** Agregar emojis decorativos en títulos o controles.
- **NO HACER:** Usar negro puro `#000000`, sombras de neón o gradientes violetas.
- **NO HACER:** Generar métricas o datos ficticios de rendimiento si no provienen de requerimientos reales.
