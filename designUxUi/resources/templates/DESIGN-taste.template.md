---
version: "alpha"
name: "EditorialStudioTaste"
description: "Punto de partida editorial neutro para adaptar cuando no existe una identidad visual previa"
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
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "2.5rem"
    fontWeight: "700"
    letterSpacing: "-0.03em"
  h1:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "2rem"
    fontWeight: "600"
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Geist, system-ui, sans-serif"
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
Plantilla inicial con tono editorial sobrio. Debe adaptarse a la audiencia, el contenido y la marca del producto; no usarla si ya existe un sistema de diseño. Los valores del frontmatter son propuestas editables, no requisitos universales.

## Colors
- **Primary (#121214):** Carbón profundo para titulares y texto primario en esta propuesta.
- **Secondary (#52525B):** Neutro pizarra equilibrado para metadatos, subtítulos y elementos de apoyo.
- **Accent (#1E3A8A):** Azul marino usado como acento principal; agregar o reemplazar colores si la semántica o la marca lo requieren.
- **Background (#FAFAFA):** Lienzo neutro claro para esta dirección visual.
- **Surface (#FFFFFF):** Tarjetas nítidas delimitadas por un borde sutil de 1px.

## Typography
Geist puede usarse si está disponible y autorizada; `system-ui` es el fallback. La monospace se reserva para cifras o código cuando mejore la lectura. Sustituir estas familias por las de la marca o del proyecto existente.

## Layout
Usar composición asimétrica en secciones donde exista una prioridad editorial real. Para elementos equivalentes, una grilla regular puede comunicar mejor la comparación.

## Elevation & Depth
Superficies planas con bordes de 1px (`#E4E4E7`) como punto de partida. Ajustar sombras y profundidad a la plataforma y al sistema existente.

## Shapes
Radios de 6px a 10px en esta propuesta; reemplazarlos por los tokens del producto si existen.

## Components
- **button-primary:** Respuesta visual al presionar, expresada con el mecanismo del stack existente; un desplazamiento vertical de 1px es solo una opción.
- **card:** Tarjetas estructuradas con espaciado interno amplio (24px) y jerarquía clara.

## Do's and Don'ts
- **HACER:** Verificar los umbrales de contraste aplicables a texto, componentes y estados.
- **HACER:** Confirmar que las fuentes estén disponibles, licenciadas y tengan fallback.
- **HACER:** Adaptar tokens y composición a contenido, marca y accesibilidad.
- **NO HACER:** Reemplazar un sistema existente solo para aplicar esta estética.
- **NO HACER:** Generar métricas, testimonios o datos ficticios si no provienen de fuentes reales.
