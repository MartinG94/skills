# Protocolo de Orquestación Híbrida y Estrategia de Cuotas

## 1. Escalamiento Progresivo de Modelos (Plan Pro - 4 Niveles)

- **Nivel 1A (Diario y Ágil - 75%):** `Gemini 3.8 Flash (Medium)` como caballo de batalla predeterminado para navegación, chat, generación y subagente `code-executor`.
- **Nivel 1B (Planificación y Arquitectura Estándar - 10%):** `Gemini 3.8 Flash (High)` (tope de ~10K tokens de pensamiento) para formular planes interactivos (`/plan`) o abordar diseño moderado dentro del pool estándar de Gemini, **sin gastar el cupo semanal de Argon ni el de Claude**. Luego se desciende a `Medium` para ejecutar.
- **Nivel 2 (Frontera y Consola - 10%):** `Gemini 4 Argon (Medium)` para refactorizaciones en múltiples archivos, trazas extensas, depuración pesada y comandos de terminal (57.4% en Terminal-Bench). Utiliza su propio pool semanal (`Gemini 4 Argon Weekly Limit`) sin gastar la cuota de Claude ni saturar Flash. Aplica el patrón "Plan en Archivo".
- **Nivel 3 (Francotirador Crítico - 5%):** `Claude Opus 5.5 (Medium)` reservado para análisis de causa raíz y arquitectura extrema donde se requiera máxima comprensión semántica (51 pts), con salida directa a archivo de plan (`PLAN_FIX.md`).

## 2. Estrategia Operativa con Modelos de Frontera (Gemini 4 Argon y Claude Opus/Sonnet 5.5)

- **Patrón "Plan en Archivo para Implementación con Flash":**
  Cuando se utilice **Gemini 4 Argon** o **Claude** para arquitectura, resolución de bugs profundos, diseño complejo o diagnósticos críticos, la directiva principal es redactar la solución, causas raíz y especificación detallada en un archivo de plan (ej. `PLAN_FIX.md` o plan de implementación) sin implementar código masivo directamente en esa sesión.
  Posteriormente, la implementación concreta, pruebas y tareas mecánicas se delegan a Gemini Flash (o al subagente `code-executor`), protegiendo el límite semanal de Argon (`Gemini 4 Argon Weekly Limit`) y la ventana de cuota de 5 horas de Claude.

- **Blindaje Obligatorio de Subagentes:**
  Cuando el agente principal opere con Gemini 4 Argon o Claude, nunca delegar en subagentes con `model: inherit`. Se debe especificar explícitamente `model: flash` o `model: flash_lite` para evitar que la exploración o ejecución multiplique el consumo del pool de frontera de Argon o de terceros.

## 3. Delegación por Especialidad

- **Exploración y Diagnóstico Rápido:** Delegar en `explorer-low` (`model: flash_lite`) para grep, búsqueda masiva de archivos o filtrado de logs sin gastar tokens de pensamiento.
- **Implementación de Código:** Delegar en `code-executor` (`model: flash`) para aplicar cambios quirúrgicos siguiendo el plan aprobado.

## 4. Orquestación en Equipos de Trabajo Multiagente (/teamwork-preview y Cascada Jerárquica)

- **Nivel del Orquestador:** Al estructurar o invocar equipos de trabajo (`Coordinator`, `Project Orchestrator`, `Auditor`), el orquestador debe ser un modelo inteligente (`pro` o de frontera).
- **Gestión de Contexto del Orquestador:** Los orquestadores deben mantener su contexto liviano y estructurado (requisitos, criterios de aceptación, contratos de interfaces y reportes de estado); nunca deben saturarse leyendo código completo ni volcados masivos de terminal.
- **Decisión Dinámica de Inteligencia Operativa:** El orquestador es la autoridad facultada para evaluar la dificultad técnica de cada subtarea y decidir el nivel de inteligencia asignado al trabajador:
  * **Gemini 3.8 Flash Medium (`flash`):** Para lógica de negocio, edición de código acoplado, resolución de tipos y desarrollo de pruebas unitarias.
  * **Gemini 3.8 Flash Low (`flash_lite`):** Para búsquedas sintácticas, grep, inspección de rutas, generación de boilerplate repetitivo y ejecución básica de scripts.
