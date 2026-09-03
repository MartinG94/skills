---
name: StandardDesignSystem
colors:
  primary: "#0F172A"
  secondary: "#475569"
  accent: "#1D4ED8"
  neutral-light: "#F8FAFC"
  neutral-white: "#FFFFFF"
typography:
  h1:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "2.25rem"
    fontWeight: "700"
  h2:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "1.5rem"
    fontWeight: "600"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: "400"
  caption:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: "400"
rounded:
  sm: "4px"
  md: "8px"
  lg: "12px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "24px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.neutral-white}"
    rounded: "{rounded.md}"
    padding: "12px"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.neutral-white}"
    rounded: "{rounded.md}"
    padding: "12px"
  card:
    backgroundColor: "{colors.neutral-white}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "24px"
  page-container:
    backgroundColor: "{colors.neutral-light}"
    textColor: "{colors.primary}"
---

## Overview
Identidad visual técnica y moderna. Equilibra legibilidad con contraste accesible para aplicaciones analíticas y SaaS.

## Colors
- **Primary (#0F172A):** Azul pizarra profundo para encabezados, texto principal y bordes estructurales.
- **Secondary (#475569):** Neutro intermedio para texto secundario, iconos y botones de apoyo.
- **Accent (#1D4ED8):** Azul cobalto de alta visibilidad para acciones principales e interacciones clave.
- **Neutral Light (#F8FAFC):** Superficie de fondo general suave para descanso visual.
- **Neutral White (#FFFFFF):** Fondo de tarjetas modulares, diálogos y paneles.

## Typography
Inter provee excelente legibilidad en pantalla para interfaces densas de datos.

## Layout
Grilla con espaciados múltiplos de 8px (8px, 16px, 24px) para mantener un ritmo vertical armónico.

## Elevation & Depth
Superficies nítidas con bordes de 1px en color secundario tenue y sombras sutiles.

## Shapes
Radios de curvatura de 8px en componentes de acción y 12px en paneles contenedores.

## Components
Botones con padding proporcional y contraste verificado WCAG AA. Tarjetas estructuradas con padding de 24px.

## Do's and Don'ts
- **HACER:** Utilizar el color de acento `#1D4ED8` con texto blanco para garantizar ratio > 4.5:1.
- **NO HACER:** Emplear colores de acento en texto pequeño sobre fondos de color saturado.
