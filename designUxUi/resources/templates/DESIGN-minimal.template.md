---
name: MinimalDesignSystem
colors:
  primary: "#18181B"
  accent: "#047857"
  background: "#FFFFFF"
  surface: "#F4F4F5"
  white: "#FFFFFF"
typography:
  h1:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "1.875rem"
    fontWeight: "700"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: "400"
rounded:
  md: "6px"
spacing:
  md: "12px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: "10px"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "16px"
  layout:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
---

## Overview
Líneas minimalistas y limpias inspiradas en herramientas SaaS modernas.

## Colors
- **Primary (#18181B):** Zinc oscuro para encabezados y acentos estructurales.
- **Accent (#047857):** Verde esmeralda profundo con alto contraste para acciones principales.
- **Surface (#F4F4F5):** Fondos de tarjeta y paneles de baja saturación.

## Typography
Inter en todos los elementos para consistencia universal.

## Components
Botones rectangulares con bordes ligeramente suavizados y tarjetas planas.
