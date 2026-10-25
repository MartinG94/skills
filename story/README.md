# Skill: `story` (XP Single-Story Refinement & Acceptance Criteria)

Toma **una única historia de usuario vertical** (desde `backlog.md` o indicada por el usuario) y la refina justo a tiempo (*Just-in-Time*) mediante preguntas de desambiguación, de 2 a 3 criterios de aceptación en formato *Dado/Cuando/Entonces*, un mini-plan funcional de máximo 5 puntos y una sección explícita de *Out of Scope*.

---

## 🎯 Propósito

Sustituir los documentos de especificación monolíticos del SDD tradicional por un acuerdo de alcance quirúrgico (`plan.md`) para **una sola rebanada vertical a la vez**, blindando la futura sesión de codificación contra la invención de requerimientos y las abstracciones prematuras.

---

## ⚙️ Cuándo Usarla y Nivel de Modelo Recomendado

- **Cuándo:** Antes de programar una historia de usuario seleccionada de `backlog.md` o una feature mediana/compleja.
- **Modelo recomendado en Antigravity:**
  - **Nivel 1B (`Gemini 3.8 Flash High`)** o **Nivel 2 (`Gemini 4 Argon Medium`)** para destrabar casos borde y formular los criterios de aceptación.
  - Una vez generado `plan.md`, se recomienda abrir una **conversación nueva limpia** con **Nivel 1A (`Gemini 3.8 Flash Medium`)** e invocar la skill [`pair`](../pair/SKILL.md).

---

## 📏 Reglas de Oro de `story`

1. **Una historia a la vez:** Prohibido refinar múltiples historias en simultáneo.
2. **Regla de los 3 Criterios:** Entre 2 y 3 criterios de aceptación (*Given/When/Then*). Si requiere 4 o más, la historia es demasiado grande y debe partirse en dos.
3. **Cero Diseño Especulativo:** El Mini-Plan (máx. 5 bullets) describe pasos funcionales observables, sin recetar *Repositories*, *Factories*, *Interfaces* ni árboles de directorios.
4. **Out of Scope Obligatorio:** Documenta explícitamente qué queda excluido en esta iteración.

---

## 📥 Entradas y 📤 Salidas

| Tipo | Descripción |
| :--- | :--- |
| **Entrada** | Una historia de usuario individual (leída de `backlog.md` o provista en el prompt). |
| **Salida** | Archivo `plan.md` aprobado con Criterios de Aceptación, Mini-Plan de máximo 5 puntos y Out of Scope, listo para ejecutar en [`pair`](../pair/SKILL.md). |
