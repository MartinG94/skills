# Especificación Técnica de Tokens DESIGN.md

La especificación `DESIGN.md` es un estándar abierto desarrollado por Google Labs para comunicar sistemas de diseño e identidades visuales a agentes de programación autónomos.

## Estructura del Archivo

El archivo reside convencionalmente en la raíz del repositorio (`./DESIGN.md`) y cuenta con dos capas:

1. **YAML Front-matter (Tokens Normativos)**:
   - Delimitado por `---` al inicio del archivo.
   - Procesa y tipa valores para colores, tipografía, radios de curvatura, espaciados y componentes.
2. **Cuerpo Markdown (Razón de Ser / Semántica)**:
   - Encabezados de segundo nivel `##`.
   - Explica el contexto de producto, la jerarquía visual y la intención de marca.

## Esquema de Tokens YAML

```yaml
version: "alpha"          # Opcional
name: "NombreDelSistema"
description: "Descripción breve"
omitted: []               # Opcional: lista de secciones a omitir intencionalmente
colors:
  <nombre-token>: <Color>
typography:
  <nombre-escala>: <TypographyObject>
rounded:
  <nivel-escala>: <Dimension>
spacing:
  <nivel-escala>: <Dimension>
components:
  <nombre-componente>:
    backgroundColor: <Color | TokenRef>
    textColor: <Color | TokenRef>
    rounded: <Dimension | TokenRef>
    padding: <Dimension | string>
```

### Tipos de Valores Admitidos

| Tipo | Formato admitido | Ejemplo |
| :--- | :--- | :--- |
| **Color** | Hexadecimal, rgb(), oklch() | `"#0F172A"`, `"#FFFFFF"` |
| **Dimension** | Número con unidad (px, rem, em) | `"4px"`, `"1rem"`, `"16px"` |
| **Token Reference** | Sintaxis `{categoria.nombre}` | `"{colors.accent}"`, `"{rounded.md}"` |
| **Typography Object**| Objeto con propiedades tipográficas | `fontFamily`, `fontSize`, `fontWeight`, `lineHeight` |

## Orden Canónico de Secciones Markdown

Para una interpretación óptima por linters y modelos de lenguaje, las secciones deben seguir este orden:
1. `## Overview` (o `## Brand & Style`)
2. `## Colors`
3. `## Typography`
4. `## Layout` (o `## Layout & Spacing`)
5. `## Elevation & Depth` (o `## Elevation`)
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`
