# Referencia de CLI @google/design.md

La herramienta oficial de línea de comandos de Google Labs permite validar, comparar y exportar archivos `DESIGN.md`.

## Uso en Windows y PowerShell

> [!CAUTION]
> En Windows, invocar directamente `npx @google/design.md` puede fallar o abrir el archivo en tu editor Markdown debido a que la extensión `.md` coincide con la asociación del sistema operativo para archivos Markdown.
> **Solución:** Utiliza el alias `designmd` pasando el paquete con `-p`:
> ```powershell
> npx -p @google/design.md designmd <comando> [argumentos]
> ```

## Comandos Principales

### 1. `lint` (Validar)
Audita la sintaxis YAML, comprueba que las referencias no estén rotas y verifica el contraste de colores WCAG AA (mínimo 4.5:1).

```powershell
# En consola / terminal
npx -p @google/design.md designmd lint DESIGN.md

# Formato JSON para agentes
npx -p @google/design.md designmd lint --format json DESIGN.md
```

**Reglas clave:**
- `broken-ref`: Error si una referencia `{colors.xyz}` no existe.
- `contrast-ratio`: Warning/Error si el par `backgroundColor` / `textColor` de un componente no supera 4.5:1 en texto regular.
- `missing-primary`: Alerta si no se declara un color `primary`.
- `orphaned-tokens`: Alerta sobre colores definidos que ningún componente utiliza.

### 2. `diff` (Regresiones Visuales)
Compara dos archivos `DESIGN.md` para detectar cambios en tokens y reportar si aumentaron los errores o advertencias.

```powershell
npx -p @google/design.md designmd diff DESIGN.md DESIGN-v2.md
```

### 3. `export` (Transformar a Frameworks)
Genera configuraciones directas para motores de estilos:

- **Tailwind CSS v3:**
  ```powershell
  npx -p @google/design.md designmd export --format json-tailwind DESIGN.md > tailwind.theme.json
  ```
- **Tailwind CSS v4 (CSS variables `@theme`):**
  ```powershell
  npx -p @google/design.md designmd export --format css-tailwind DESIGN.md > theme.css
  ```
- **W3C Design Tokens (DTCG):**
  ```powershell
  npx -p @google/design.md designmd export --format dtcg DESIGN.md > tokens.json
  ```
