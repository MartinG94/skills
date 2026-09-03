---
name: DualThemeSystem
colors:
  primary: "#0F172A"
  primary-dark: "#F8FAFC"
  surface-light: "#FFFFFF"
  surface-dark: "#1E293B"
  accent: "#2563EB"
  accent-dark: "#1D4ED8"
  text-on-accent: "#FFFFFF"
typography:
  h1:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "2.5rem"
    fontWeight: "700"
  body:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: "400"
rounded:
  sm: "4px"
  md: "8px"
spacing:
  sm: "8px"
  md: "16px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text-on-accent}"
    rounded: "{rounded.md}"
    padding: "12px"
  button-primary-dark:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.text-on-accent}"
    rounded: "{rounded.md}"
    padding: "12px"
  card-light:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "16px"
  card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.primary-dark}"
    rounded: "{rounded.sm}"
    padding: "16px"
---

## Overview
Sistema de diseño con paletas coordinadas para soporte de modo claro y modo oscuro.

## Colors
Colores estructurados en pares coordinados para asegurar contraste óptimo en ambos temas.

## Typography
Public Sans proporciona neutralidad geométrica y alta legibilidad en displays digitales.

## Components
Componentes con variantes para tema claro y tema oscuro sin perder coherencia métrica.
