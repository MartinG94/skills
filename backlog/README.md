# Skill: `backlog` (XP Vertical Slices Product Backlog)

Transforma una idea general o requerimiento de negocio en un backlog ágil y minimalista de **historias de usuario verticales de una sola línea** bajo los principios de **Extreme Programming (XP)** y **Vertical Slices** (basado en `nschurmann/hola-ai`).

---

## 🎯 Propósito

Evitar el vicio del *Spec-Driven Development (SDD)* tradicional —donde el agente inventa requerimientos, diseña arquitecturas especulativas en el momento de mayor ignorancia y divide el trabajo por capas horizontales (1º Base de Datos, 2º Backend, 3º UI)— forzando una descomposición en rebanadas verticales funcionales de punta a punta verificables desde el primer día.

---

## ⚙️ Cuándo Usarla y Nivel de Modelo Recomendado

- **Cuándo:** Al iniciar un proyecto nuevo, un MVP o un módulo funcional grande donde aún no están delimitadas las historias de usuario.
- **Modelo recomendado en Antigravity:**
  - **Nivel 1B (`Gemini 3.8 Flash High`)** por defecto (alta capacidad analítica dentro del pool estándar de Gemini).
  - **Nivel 2 (`Gemini 4 Argon Medium`)** o **Nivel 3 (`Claude Opus 5.5 Medium`)** para dominios de negocio complejos con múltiples actores o restricciones regulatorias.

---

## 🔄 Flujo Operativo

1. **Paso 1 — Descubrimiento Mínimo:** Formula de 2 a 4 preguntas breves con una opción ultra-simple por defecto y **frena esperando respuesta**.
2. **Paso 2 — Propuesta de Backlog Vertical:** Presenta entre 4 y 8 historias de una sola línea (`Como [usuario], quiero [acción] para [beneficio]`), sin conjunciones `"y"` que oculten múltiples alcances y sin detalles técnicos ni estimaciones.
3. **Paso 3 — Checkpoint y Persistencia:** Tras la aprobación explícita del usuario en el chat, guarda la lista en `backlog.md`.

---

## 📥 Entradas y 📤 Salidas

| Tipo | Descripción |
| :--- | :--- |
| **Entrada** | Idea de producto, narrativa funcional o requerimiento general del usuario. |
| **Salida** | Archivo `backlog.md` con historias de usuario verticales numeradas, listo para ser consumido historia por historia mediante la skill [`story`](../story/SKILL.md). |
