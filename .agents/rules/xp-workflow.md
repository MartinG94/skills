# Regla de Flujo Híbrido Anti-SDD: Desarrollo Orgánico (ODD) y XP (`backlog` ➔ `story` ➔ `pair`)

## 1. Selección de Enfoque según Complejidad (ODD vs. XP Vertical Slices)

- **Cambios Chicos, Bugs Acotados o Retoques Directos (Enfoque ODD — *Gentleman Programming*):**
  - **Complejidad a demanda:** No forzar rituales rígidos de especificación previa ni planes pesados para cambios puntuales. Resolver directamente con `Gemini 3.8 Flash (Medium)` (**Nivel 1A**).
  - **Delegación determinista por tokens (`exploring` ➔ `implementing`):** En lugar de reglas arbitrarias por cantidad de archivos, evaluar el costo en tokens. Si se requiere explorar el repositorio, delegar la fase de exploración en el subagente `explorer-low` (`model: flash_lite`) antes de pasar a la implementación, ahorrando hasta 3x en tokens y preservando limpio el contexto principal.

- **Features Nuevas o Complejas (Enfoque XP / `hola-ai` — *Nicolás Schurmann*):**
  - Evitar el *Spec-Driven Development (SDD)* monolítico por capas horizontales (1º toda la BD, 2º toda la API, 3º toda la UI).
  - Cortar el software en **Vertical Slices** (rebanadas verticales funcionales de punta a punta) y mantener el control humano mediante la secuencia de skills: `backlog` (`backlog.md`) ➔ `story` (`plan.md`) ➔ `pair` (TDD en micro-pasos).

---

## 2. Reglas Estrictas del Flujo XP (`backlog`, `story`, `pair`)

Cuando el usuario invoque o esté trabajando dentro del flujo de las skills `backlog`, `story` o `pair`:

1. **Respetá los checkpoints obligatorios:** Nunca pases de `/backlog` a `/story`, ni de `/story` a `/pair` en el mismo turno. Esperá siempre la confirmación explícita del usuario antes de escribir `backlog.md` o `plan.md`.
2. **Prohibido el "One-Shotting" en modo `/pair`:** Cuando la skill `pair` esté activa, tenés terminantemente prohibido implementar múltiples tests seguidos o encadenar el paso Rojo y el paso Verde en el mismo turno sin confirmación del usuario entre cada paso (~50 líneas), salvo que el usuario indique explícitamente cuántas iteraciones correr.
3. **Cero abstracciones especulativas (Anti-YAGNI):** No introduzcas capas de arquitectura (servicios, repositorios, interfaces, middlewares, carpetas nuevas) por iniciativa propia. Escribí el código en el lugar más directo posible y esperá a que el *Navigator* (usuario) te pida refactorizar.
4. **Control de Git y Tests:** En modo `/pair`, jamás ejecutes `git commit` sin orden explícita del usuario ni modifiques/borres un test existente para forzar que pase.

---

## 3. Asignación Óptima de Modelos por Fase (Sinergia con Cuotas)

- **Para `backlog` y `story` (Descubrimiento y Refinamiento):**
  - Utilizar modelos de alto razonamiento para detectar agujeros lógicos y casos borde: **Nivel 1B (`Gemini 3.8 Flash High`)** dentro del pool estándar de Gemini, o escalar a **Nivel 2 (`Gemini 4 Argon Medium`)** / **Nivel 3 (`Claude Opus 5.5 Medium`)** según la criticidad del dominio, volcando el resultado en `backlog.md` y `plan.md`.
- **Para `pair` (Construcción TDD en Micro-Pasos):**
  - Abrir una **conversación nueva (contexto limpio, leyendo solo `plan.md`)** y utilizar el modelo veloz **Nivel 1A (`Gemini 3.8 Flash Medium`)**. Al dirigir la arquitectura en pasos de 20 a 50 líneas con frenos en cada semáforo (Rojo ➔ Verde ➔ Refactor), `Flash Medium` responde en pocos segundos sin consumir el pool semanal de Argon ni la ventana de 5 horas de Claude.
