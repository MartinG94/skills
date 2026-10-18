# addyOsmaniSkills

Conjunto de estándares y flujos de trabajo de ingeniería de software de grado de producción inspirados en `addyosmani/agent-skills`. Integra entrevistas técnicas para clarificación de requisitos (`interview-me`), desarrollo guiado por especificaciones vivas (`spec-driven`), entrega continua por tajadas verticales (`incremental`) e ingeniería de alto rendimiento web enfocada en Core Web Vitals (`web-performance`).

---

## 1. Propósito General

`addyOsmaniSkills` asegura que el software desarrollado no se quede en un mero prototipo frágil, sino que cumpla con los estándares de robustez, escalabilidad, resiliencia y velocidad de los sistemas de producción modernos. Combina el rigor de diseño previo mediante especificaciones formales con la optimización milimétrica de la experiencia de usuario y el rendimiento del navegador.

### Capacidades Principales:
- **Entrevista Técnica (`interview-me`):** Desbloqueo sistemático de ambigüedades, requerimientos no funcionales (NFRs), casos de error y supuestos ocultos.
- **Desarrollo Guiado por Especificación (`spec-driven`):** Redacción y mantenimiento de archivos `SPEC.md` con modelos de datos, contratos de API, máquinas de estados finitas y planes de prueba.
- **Entrega Incremental (`incremental`):** Implementación de tajadas verticales (*vertical slices*) funcionales con diffs compactos y verificación continua.
- **Ingeniería de Core Web Vitals (`web-performance`):** Optimización matemática y arquitectónica de LCP ($< 2.5\text{s}$), INP ($< 200\text{ms}$) y CLS ($< 0.1$), presupuesto de bundles y estrategias de hidratación/renderizado.

---

## 2. Arquitectura Interna

```
addyOsmaniSkills/
├── SKILL.md                                # Contrato operacional del agente y los 4 modos de trabajo
├── README.md                               # Documentación técnica de la skill
└── references/                             # Playbooks y manuales de ingeniería
    └── engineering-playbooks.md            # Guías de SPEC.md, optimización de CWV y baterías de entrevista
```

---

## 3. Prerequisitos de Entorno

- Compatible con proyectos web frontend (Next.js, React, Astro, Vue, Svelte, Angular, vanilla JS/TS) y arquitecturas backend (Node.js, Python, Go).
- Para auditoría de rendimiento en desarrollo, se recomienda la integración con Chrome DevTools MCP o Lighthouse CLI.

---

## 4. Ejemplos de Invocación y Uso

### Caso 1: Clarificación Previa de Funcionalidad Crítica
```markdown
Modo: interview-me
Solicitud: El usuario pide "Implementar un sistema de checkout de suscripciones recurrentes con Stripe".
Comportamiento:
- El agente detiene la codificación inmediata.
- Pregunta sobre manejo de pagos fallidos (dunning), sincronización por webhooks, estados de gracia y políticas de reembolso antes de redactar el SPEC.md.
```

### Caso 2: Auditoría y Optimización de Core Web Vitals
```markdown
Modo: web-performance
Solicitud: Optimizar la landing page principal porque el LCP está en 4.2s y el INP en 350ms.
Diagnóstico y Solución:
- Aplica fetchpriority="high" y preload a la imagen hero en formato AVIF.
- Divide tareas largas de JavaScript en el hilo principal usando scheduler.yield().
- Declara aspect-ratio en componentes dinámicos para reducir CLS a 0.02.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Requisitos de producto, historias de usuario o incidencias de rendimiento.
- Código fuente existente, perfiles de performance y métricas de Core Web Vitals (Lighthouse / DevTools).
- Esquemas de bases de datos o contratos de APIs de servicios externos.

### Salidas (Outputs)
- Documento formal de especificación viva `SPEC.md`.
- Implementaciones de código por tajadas verticales con pruebas automatizadas en verde.
- Optimizaciones de rendimiento con mediciones verificadas de LCP, INP y CLS.
- Reporte técnico de compuertas de calidad senior y resiliencia en producción.
