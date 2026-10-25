# Skill: `pair` (XP AI Pair Programming & Strict Micro-Step TDD)

Implementa una historia de usuario o archivo `plan.md` mediante **Pair Programming estilo Extreme Programming (XP)** y **TDD en micro-pasos (~50 líneas)**, donde la IA actúa como *Driver* y el desarrollador humano mantiene el volante como *Navigator*.

---

## 🎯 Propósito

Erradicar la fatiga de revisión (PRs autogenerados de 3.000 líneas) y la pérdida del modelo mental del software. En lugar de que el agente corra solo durante 15 minutos tomando decisiones arquitectónicas arbitrarias, `pair` impone paradas obligatorias en cada transición del ciclo **Rojo ➔ Verde ➔ Refactor**, permitiendo al desarrollador auditar cada cambio en 15 segundos y hacer commit del test antes de implementar el código de producción.

---

## ⚙️ Cuándo Usarla y Nivel de Modelo Recomendado

- **Cuándo:** Al momento de programar una historia refinada en `plan.md` (generado con [`story`](../story/SKILL.md)) o cualquier funcionalidad que requiera control total de diseño y TDD estricto.
- **Modelo recomendado en Antigravity:**
  - Abrir una **conversación nueva (contexto limpio)** leyendo únicamente `plan.md` y seleccionar **Nivel 1A (`Gemini 3.8 Flash Medium`)**.
  - Como cada intervención está acotada a ~50 líneas y las decisiones de arquitectura las toma el Navigator, `Flash Medium` responde en pocos segundos y protege al 100% la cuota semanal de `Gemini 4 Argon` y la ventana de 5 horas de `Claude`.

---

## 🚦 El Ciclo Semáforo con Frenos Obligatorios

1. **Fase 0 — Lista de Tests:** Lee `plan.md`, propone la lista numerada de tests concretos y **frena**.
2. **Turno A — ROJO:** Escribe **1 solo test**, ejecuta el runner (`rtk test`) comprobando que falla por la razón correcta y **frena inmediatamente** (momento ideal para que el Navigator verifique el test y haga `git commit`).
3. **Turno B — VERDE:** Escribe el **código mínimo directo** (sin crear carpetas, interfaces ni repositorios prematuros), comprueba que los tests pasen en verde y **frena inmediatamente**.
4. **Turno C — REFACTOR:** Solo cuando el Navigator lo solicita explícitamente, extrae funciones/archivos manteniendo los tests en verde y vuelve a **frenar**.
5. **Fase 2 — Cierre del Slice Vertical:** Conecta el cambio mínimo de UI/cliente para dejar la funcionalidad operativa de punta a punta.

---

## 📥 Entradas y 📤 Salidas

| Tipo | Descripción |
| :--- | :--- |
| **Entrada** | Archivo `plan.md` aprobado (o historia con criterios de aceptación) y el código fuente del proyecto. |
| **Salida** | Rebanada vertical (*Vertical Slice*) implementada paso a paso con cobertura de tests TDD verificada y arquitectura gobernada por el desarrollador. |
