# DDL e implementación opcionales

Lee esta referencia sólo si el usuario pide DDL, migración o handoff de implementación.

## Precondiciones de DDL

Antes de generar texto ejecutable confirma:

- motor y versión;
- esquema/naming conventions;
- estado inicial: base nueva o esquema existente;
- herramienta/formato de migraciones;
- política de compatibilidad y rollback;
- tipos, longitudes, precisión y reglas todavía `TBD`.

Si falta un dato crítico, entrega DDL parcial marcado o solicita la decisión. No elijas
un dialecto ni una configuración por ejemplos anteriores.

## Salida segura

- Para base nueva, genera sólo creación ordenada y restricciones justificadas.
- Para esquema existente, produce una migración incremental; separa operaciones que
  puedan bloquear, perder datos o requerir backfill.
- No incluyas borrado/recreación general ni datos de conexión.
- No ejecutes nada como parte de la generación.
- Acompaña la salida con supuestos, riesgos y una estrategia de verificación.

## Implementación

El modelo relacional no determina por sí solo DAO, repositorio, ORM ni unidad de trabajo.
Si el usuario pide código:

1. detecta framework y patrones existentes;
2. conserva ownership de transacción y ciclo de vida de conexiones del framework;
3. usa consultas parametrizadas y configuración externa;
4. implementa sólo el alcance solicitado;
5. verifica compilación y pruebas disponibles.

Evita helpers globales con conexión o transacción mutable compartida. No incrustes
secretos ni deshabilites validaciones de transporte. Las optimizaciones de carga,
caching y tracking requieren evidencia de consultas reales.

## Validación

Revisa sintaxis con tooling del dialecto si está disponible, pero no confundas parseo
exitoso con seguridad de migración. Para cambios de esquema, documenta precondiciones,
compatibilidad, backfill, validación de datos y recuperación antes de recomendar uso.
