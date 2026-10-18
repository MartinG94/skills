---
name: addyOsmaniSkills
description: >-
  Estándares de ingeniería de producción y rendimiento web de Addy Osmani:
  entrevista técnica interactiva (modo interview-me) para destrabar requerimientos
  y casos borde, desarrollo guiado por especificación viva (modo spec-driven con SPEC.md),
  entrega por tajadas verticales atómicas (modo incremental) e ingeniería rigurosa de
  Core Web Vitals (modo web-performance con LCP < 2.5s, INP < 200ms, CLS < 0.1).
---

# Estándares de Ingeniería de Producción y Rendimiento Web

## Responsabilidad y Modos de Trabajo

La skill `addyOsmaniSkills` condensa la disciplina y mejores prácticas de ingeniería de software para sistemas de producción a escala. Establece compuertas de rigor técnico que aseguran que el código no solo funcione en condiciones ideales, sino que sea resiliente, performante en redes lentas y mantenible a largo plazo.

Opera en **cuatro modos de trabajo principales**:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Modo            │     │ Modo            │     │ Modo            │     │ Modo            │
│ interview-me    │ ──> │ spec-driven     │ ──> │ incremental     │ ──> │ web-performance │
│ (Aclaración)    │     │ (Diseño SPEC)   │     │ (Entrega Slice) │     │ (Optimización)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## 1. Modo `interview-me` (Entrevista Técnica Interactiva)

Se activa ante requerimientos complejos, ambiguos o de alto impacto arquitectónico antes de comenzar a escribir código:

1. **Objetivo:** Descubrir suposiciones no declaradas, límites operativos, requisitos no funcionales (NFRs) y condiciones de error.
2. **Dinámica:**
   - El agente asume el rol de Ingeniero Principal / Tech Lead y formula una batería concisa de 4 a 6 preguntas estructuradas al desarrollador o usuario.
   - Indaga en: volumetría de datos, concurrencia esperada, comportamiento ante fallos de servicios de terceros, políticas de reintentos, idempotencia y SLA de latencia.
3. **Compuerta:** No iniciar la codificación hasta que las respuestas críticas hayan definido el perímetro de la solución.

---

## 2. Modo `spec-driven` (Desarrollo Guiado por Especificación)

Se activa cuando se requiere diseñar una nueva arquitectura, módulo o funcionalidad crítica:

1. **Elaboración de `SPEC.md`:**
   - Documentar la solución en un archivo formal de especificación viva previo a la implementación.
   - Definir:
     - Modelos de datos estáticos y esquemas de validación (Zod, Pydantic, JSON Schema).
     - Contratos de integración de API (REST RFC 9457, gRPC, WebSocket).
     - Máquina de Estados Finita (FSM) con todos los estados posibles (`idle`, `loading`, `success`, `error`) y transiciones válidas.
     - Matriz de casos borde, concurrencia y tolerancia a fallos.
     - Plan de pruebas unitarias y de integración cuantificable.
2. **Aprobación de la Especificación:** La especificación aprobada sirve como la única fuente de verdad (*single source of truth*) durante toda la fase de desarrollo.

---

## 3. Modo `incremental` (Entrega por Tajadas Verticales)

Se activa durante la ejecución y codificación de la solución:

1. **Principio de Tajada Vertical (*Vertical Slice*):**
   - Implementar un recorrido extremo a extremo completo y funcional para un caso de uso puntual (desde la base de datos hasta la interfaz) antes de construir horizontalmente capas abstractas.
2. **Diffs Atómicos y Compactos:**
   - Generar cambios de código pequeños, legibles y verificables de manera independiente.
   - Cada commit o tarea debe dejar el repositorio en estado verde con todos sus tests pasando (`rtk test`).
3. **Prohibición de "Big Bang Merges":** Prohibir cambios masivos de cientos de líneas que modifiquen múltiples subsistemas a la vez sin comprobación intermedia.

---

## 4. Modo `web-performance` (Ingeniería de Core Web Vitals)

Se activa al auditar, construir o refactorizar interfaces y aplicaciones web:

1. **Cumplimiento de Umbrales de Core Web Vitals:**
   - **LCP (Largest Contentful Paint) $< 2.5\text{s}$:** Priorizar recursos visuales principales con `fetchpriority="high"`, pre-cargar activos críticos (`<link rel="preload">`), optimizar imágenes a AVIF/WebP y eliminar bloqueos síncronos en el renderizado inicial.
   - **INP (Interaction to Next Paint) $< 200\text{ms}$:** Descomponer tareas largas de JavaScript ($> 50\text{ms}$) cediendo el control al hilo principal (`scheduler.yield()` o `setTimeout(0)`), optimizar listeners con debounce/throttle y prevenir el *Layout Thrashing*.
   - **CLS (Cumulative Layout Shift) $< 0.1$:** Reservar dimensiones fijas (`width`/`height` o `aspect-ratio`) para imágenes, videos, iframes y banners dinámicos; mitigar saltos de fuentes con `font-display: optional` o métricas de fuentes de respaldo.
2. **Presupuesto de Bundles:**
   - Limitar el bundle inicial de JavaScript a $< 100\text{KB}$ comprimido.
   - Implementar división de código (*code-splitting*) a nivel de ruta y componentes diferidos (`React.lazy()`, dynamic imports).

---

## Guía de Referencia Avanzada

Para consultar los manuales exhaustivos de especificación técnica, optimización avanzada de Core Web Vitals, técnicas de hidratación selectiva y baterías de preguntas para entrevistas técnicas, consultar:
- [Playbooks de Ingeniería de Producción y Rendimiento Web](file:///c:/git/skills/addyOsmaniSkills/references/engineering-playbooks.md)
