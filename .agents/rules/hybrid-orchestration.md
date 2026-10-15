# Protocolo de Orquestación Híbrida y Estrategia de Cuotas

## 1. Estrategia con Modelos Claude (Opus 5.5 / Sonnet 5.5)

- **Patrón "Plan en Archivo para Implementación con Flash":**
  Cuando se utilice un modelo de la familia Claude para arquitectura, diagnóstico de causas raíz complejas o diseño de soluciones críticas, la directiva principal es redactar la solución, causas raíz y especificación detallada en un archivo de plan (ej. `PLAN_FIX.md` o plan de implementación) sin implementar código masivo directamente en esa sesión de Claude.
  Posteriormente, la implementación concreta, pruebas y tareas mecánicas se delegan a Gemini Flash (o al subagente `code-executor`).

- **Blindaje de Subagentes:**
  Cuando el agente principal opere con Claude, nunca delegar en subagentes con `model: inherit`. Se debe especificar explícitamente `model: flash` o `model: flash_lite` para evitar que la exploración o ejecución multiplique el consumo del pool de terceros.

## 2. Delegación por Especialidad

- **Exploración y Diagnóstico Rápido:** Delegar en `explorer-low` (`model: flash_lite`) para grep, búsqueda masiva de archivos o filtrado de logs sin gastar tokens de pensamiento.
- **Implementación de Código:** Delegar en `code-executor` (`model: flash`) para aplicar cambios quirúrgicos siguiendo el plan aprobado.
