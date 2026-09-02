# Guía de Calidad y Linteo de Requerimientos (ISO/IEC/IEEE 29148:2018 / IEEE 830 / INCOSE)

Este documento detalla las métricas, patrones sintácticos, heurísticas de detección y reglas de corrección aplicadas por el motor de linteo de requerimientos.

---

## 1. Catálogo Exhaustivo de Reglas del Linter

### LINT-01: Atomicidad y Responsabilidad Única (Atomicity)
- **Definición:** Todo enunciado de requerimiento debe expresar una y solo una meta, capacidad o función del sistema.
- **Patrones de Detección:**
  - Presencia de conjunciones copulativas o adversativas coordinando cláusulas verbales principales: ` y `, ` además `, ` así como también `, ` junto con `, ` por otra parte `, ` no obstante `, ` pero `.
  - Presencia de listas enumeradas dentro del mismo párrafo de requerimiento.
- **Riesgo:** Imposibilidad de estimar, priorizar y testear independientemente las capacidades.
- **Heurística de Remediación:**
  - Dividir la declaración en sub-requerimientos con sufijos decimales (`RF-01.1`, `RF-01.2`, `RF-01.3`).
  - Asignar a cada uno un único verbo transitivo principal en infinitivo.

---

### LINT-02: Verificabilidad y Objetividad (Testability / Verifiability)
- **Definición:** Un requerimiento es verificable si y solo si existe un proceso finito, cuantitativo y costo-efectivo mediante el cual una persona o máquina puede demostrar que el software satisface la condición.
- **Lista Negra de Términos Ambiguos / Vagos (Forbidden Weak Words):**
  - *Adjetivos de rendimiento subjetivos:* `rápido`, `inmediato`, `en tiempo real`, `instantáneo`, `ultrarrápido`.
  - *Adjetivos de usabilidad no medibles:* `fácil`, `intuitivo`, `amigable`, `sencillo`, `autoexplicativo`, `cómodo`, `moderno`.
  - *Adjetivos de calidad abstractos:* `eficiente`, `óptimo`, `robusto`, `adecuado`, `apropiado`, `flexible`, `escalable`, `seguro`.
  - *Locuciones elípticas de escape:* `etc.`, `y/o`, `entre otros`, `incluyendo pero no limitado a`, `según corresponda`, `a criterio del usuario`.
- **Heurística de Remediación:**
  - Para Usabilidad: Especificar tiempo máximo de tarea (Time-on-Task), tasa máxima de errores (% error rate) o escala SUS (System Usability Scale).
  - Para Rendimiento: Especificar percentil de latencia (ej. $P_{95} \le 800	ext{ ms}$) bajo carga concurrente nominal ($N$ peticiones/seg).

---

### LINT-03: Voz Pasiva y Agencia del Sujeto (Passive Voice & Responsible Actor)
- **Definición:** El sujeto gramatical de la oración debe ser explícitamente el sistema, un subsistema nombrado o un actor humano específico con rol reconocido.
- **Patrones de Detección:**
  - Estructuras pasivas con "ser" + participio: `serán procesados`, `será enviado`, `es calculado`.
  - Construcciones de pasiva refleja: `se registrará`, `se emitirán`, `se validará`, `se autoriza`.
- **Riesgo:** Ambigüedad en la asignación de responsabilidades arquitectónicas (¿lo valida el frontend, la API gateway, el microservicio de negocio o un batch?).
- **Heurística de Remediación:**
  - Transformar a la estructura: `[Sujeto / Actor / Subsistema] + debe + [Verbo Transitivo] + [Objeto Directo] + [Condición/Parámetro]`.

---

### LINT-04: Rigor Modal Normativo (Modal Precision - RFC 2119 / ISO 29148)
- **Definición:** Se debe utilizar exclusivamente la taxonomía modal estandarizada:
  - **DEBE (`SHALL` / `MUST`):** Obligación estricta ineludible.
  - **DEBERÍA (`SHOULD`):** Recomendación deseable sujeta a análisis de factibilidad.
  - **PUEDE (`MAY`):** Permisión u opción opcional.
- **Patrones Prohibidos:** `debería`, `podría`, `sería bueno que`, `se recomienda que`, `está previsto que`.
- **Heurística de Remediación:**
  - Sustituir por *"El sistema debe..."* o *"El [Actor] debe poder..."*.

---

### LINT-05: Coherencia y Ausencia de Contradicciones (Consistency)
- **Definición:** Ningún requerimiento o regla de negocio debe entrar en conflicto lógico o temporal con otro requerimiento del catálogo.
- **Patrones de Detección:**
  - Solapamientos en rangos numéricos o de fechas.
  - Reglas de descuento o penalización con condiciones disyuntivas no jerarquizadas.
  - Precondiciones en Casos de Uso que exigen estados inalcanzables.
- **Heurística de Remediación:**
  - Crear matriz de decisión booleana y declarar reglas de precedencia explícitas.
