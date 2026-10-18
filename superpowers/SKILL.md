---
name: superpowers
description: >-
  Metodología integral de ingeniería de software agéntica y SDLC disciplinado:
  brainstorming interactivo con compuertas de diseño (Design Gate), planificación
  en tareas atómicas (2-5 min), ciclo TDD estricto (Red-Green-Refactor), debugging
  sistemático de 4 pasos (reproducir, aislar, corregir causa raíz, prueba de regresión)
  y compuertas de revisión de código previa al merge.
---

# Metodología y Prácticas de Ingeniería de Software Agéntica

## Responsabilidad y Filosofía Operativa

La skill `superpowers` transforma la interacción con el código en un proceso de ingeniería riguroso, predecible y altamente disciplinado. Prohíbe explícitamente saltar a ciegas a modificar código frente a requerimientos ambiguos o bugs complejos.

Su ejecución se articula en **cinco fases secuenciales obligatorias**:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Fase 1:         │     │ Fase 2:         │     │ Fase 3:         │     │ Fase 4:         │     │ Fase 5:         │
│ Brainstorming & │ ──> │ Bite-sized Plan │ ──> │ Strict TDD      │ ──> │ 4-Step Debugging│ ──> │ Pre-merge Code  │
│ Design Gate     │     │ (Tareas 2-5 min)│     │ (Red-Green-Ref) │     │ (Si hay fallos) │     │ Review          │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## Fase 1: Brainstorming & Design Gate (Compuerta de Diseño)

Ante cualquier requerimiento nuevo, refactorización o cambio arquitectónico no trivial:

1. **Comprensión y Desambiguación:**
   - Analizar los requerimientos, restricciones de contexto, supuestos ocultos y casos borde.
   - Si existen ambigüedades críticas que alteren la arquitectura o contratos públicos, detenerse y formular preguntas concretas antes de escribir una sola línea de código.
2. **Exploración de Alternativas:**
   - Proponer 2 o 3 enfoques técnicos viables comparando sus ventajas, desventajas, complejidad y compatibilidad con el stack existente.
3. **Design Gate (Compuerta de Aprobación):**
   - No avanzar a la fase de implementación hasta que el diseño conceptual, las interfaces y la estrategia técnica hayan sido presentados y validados.

---

## Fase 2: Bite-sized Implementation Plan (Plan en Tareas Atómicas)

Una vez aprobado el diseño, descomponer el trabajo en un plan ejecutable en tareas ultra-acotadas (de 2 a 5 minutos por paso):

1. **Estructura Determinista de Cada Tarea:**
   - **Ruta de Archivo Exacta:** Especificar archivos a crear, modificar o eliminar.
   - **Alcance Quirúrgico:** Funciones, clases o métodos puntuales a tocar.
   - **Comando de Verificación:** Comando de test o linter determinista (`rtk test <cmd>`, `rtk pytest`, `rtk cargo test`, etc.).
   - **Criterio de Aceptación:** Resultado observable esperado (código de salida 0, aserción específica).
2. **Gestión de Dependencias:** Ordenar los pasos de manera que cada tarea mantenga la suite de tests en estado coherente y verde.

---

## Fase 3: Strict TDD Cycle (Ciclo TDD Riguroso)

Para toda lógica nueva o modificación de comportamiento:

1. **Red (Rojo Observable):**
   - Escribir primero el test unitario o de integración más simple que exprese el comportamiento esperado.
   - Ejecutar el test con `rtk` y confirmar que **falla** por la razón esperada.
   - *Regla de Oro:* Si el test pasa sin cambios de código, el test es inválido o no está probando el comportamiento real.
2. **Green (Verde Mínimo):**
   - Implementar estrictamente el código mínimo indispensable para que el test pase.
   - Prohibido agregar abstracciones prematuras, parámetros no utilizados o lógica especulativa.
   - Ejecutar la prueba y verificar el paso en verde.
3. **Refactor (Refactorización Continua):**
   - Limpiar el código: eliminar duplicación, mejorar nombres, extraer funciones cohesionadas.
   - Verificar con `rtk test <cmd>` que todos los tests continúen en verde tras la refactorización.

---

## Fase 4: Systematic 4-Step Debugging (Depuración Sistemática de 4 Pasos)

Cuando una prueba falla o se reporta un defecto, queda prohibido aplicar "parches de síntoma" o adivinar causas. Se aplica estrictamente:

1. **Paso 1: Reproducción Determinista:**
   - Reproducir el error de forma consistente mediante un test automatizado o script mínimo de reproducción.
   - Leer exhaustivamente el mensaje de error y el stack trace completo.
2. **Paso 2: Aislamiento de Causa Raíz:**
   - Formular hipótesis científicas y trazabilidad de datos.
   - Identificar la línea exacta, condición de carrera o mutación de estado que genera la falla.
3. **Paso 3: Corrección Quirúrgica:**
   - Solucionar la causa raíz en su origen.
   - Prohibido silenciar excepciones con `try/catch` vacíos, mutar tipos a ciegas o forzar conversiones artificiales.
4. **Paso 4: Test de Regresión:**
   - Asegurar que el test de reproducción quede integrado permanentemente en la suite de pruebas como salvaguarda contra futuras regresiones.

---

## Fase 5: Subagent & Pre-merge Code Review (Revisión Previa al Merge)

Antes de dar por concluida la implementación o solicitar aprobación de cambios:

1. **Auditoría de Conformidad:**
   - Verificar cada tarea del plan contra el diff real generado (`rtk git diff`).
   - Confirmar que no se hayan modificado archivos fuera del alcance planificado.
2. **Compuerta de Calidad y Seguridad:**
   - Ejecutar la suite completa de tests y linters (`rtk test`, `rtk ruff check`, `rtk npm test`).
   - Evaluar seguridad: validación de entradas, sanitización, manejo seguro de credenciales y ausencia de fugas de memoria.
3. **Patrón de Delegación de Subagentes:**
   - Para tareas mecánicas o de implementación aislada, delegar en subagentes especializados (`code-executor`) bajo modelos ágiles (`flash`), blindando la cuota de modelos de razonamiento y aislando el contexto.

---

## Guía de Referencia Avanzada

Para consultar la especificación detallada de patrones TDD, directivas de dobles de prueba, plantillas completas de planes de tareas y listas de chequeo de depuración, consultar:
- [Guía de Flujos de Trabajo y TDD](file:///c:/git/skills/superpowers/references/workflows-and-tdd.md)
