# Contrato OpenAPI mínimo y verificable

Lee esta referencia al crear o completar una especificación OpenAPI. Conserva la
versión adoptada por el proyecto: OpenAPI 3.0 y 3.1 no comparten exactamente la misma
semántica de JSON Schema, por lo que no conviertas `nullable`, tipos o dialectos sin
una decisión explícita.

## Estructura mínima

```yaml
openapi: <versión soportada>
info:
  title: <título confirmado>
  version: <versión del contrato>
paths:
  /<recurso>:
    <método>:
      operationId: <identificador estable>
      summary: <propósito observable>
      parameters: []       # sólo parámetros reales de path/query/header/cookie
      requestBody: {}      # sólo cuando la operación recibe cuerpo
      responses:
        '<código>':
          description: <resultado observable>
components:
  schemas: {}              # sólo si existen componentes reutilizables
```

El bloque es una forma, no un ejemplo de negocio. Omite las claves opcionales vacías
en el contrato final y no copies placeholders como datos reales.

## Comprobaciones por operación

- `operationId` es único y estable si los consumidores o generadores lo usan.
- Cada parámetro declara `name`, `in`, obligatoriedad y schema; un parámetro de path
  siempre es requerido y coincide con el placeholder de la ruta.
- `requestBody` declara obligatoriedad y media type cuando existe.
- Cada respuesta relevante tiene descripción y, si lleva cuerpo, media type y schema.
- Los códigos reflejan el comportamiento real; no agregues todos los `4xx/5xx` por
  plantilla.
- La seguridad se declara sólo cuando el mecanismo y el alcance están aprobados. Una
  definición en `securitySchemes` no protege por sí sola una operación.
- Los schemas expresan required, nulabilidad, formatos, enums y límites únicamente con
  evidencia. Los ejemplos no deben crear reglas nuevas.
- Toda referencia `$ref` resuelve y no forma ciclos que la herramienta objetivo no
  soporte.

## Reutilización y compatibilidad

Usa `components` para schemas, parámetros, respuestas o esquemas de seguridad que se
reutilizan y tienen una identidad estable. No extraigas un componente sólo para
reducir líneas.

Antes de publicar un cambio, compara operaciones, parámetros, request/response y
schemas con la versión vigente. Marca como potencialmente incompatible toda
eliminación, renombre, restricción más fuerte o cambio de significado/tipo; la política
de versionado del proyecto decide el tratamiento.

## Validación

1. Detecta la versión OpenAPI y el linter/validador ya usado por el proyecto.
2. Ejecuta esa herramienta sobre el archivo exacto que se entregará.
3. Corrige primero errores de parseo y `$ref`; luego revisa semántica y compatibilidad.
4. Si no existe herramienta disponible, realiza el preflight anterior y reporta
   `validación automática no ejecutada`, sin afirmar que el contrato es válido.

No instales ni cambies un linter por defecto. Si hace falta una dependencia nueva,
explica su propósito y solicita la autorización que corresponda antes de modificar el
proyecto.
