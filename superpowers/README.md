# superpowers

Metodología y motor operativo de ingeniería de software agéntica disciplinada basada en `obra/superpowers`. Aplica un ciclo de vida de desarrollo de software (SDLC) estricto y predecible para agentes y desarrolladores, combinando compuertas de diseño, planificación atómica, TDD riguroso, depuración sistemática de 4 pasos y revisión de código pre-merge.

---

## 1. Propósito General

La skill `superpowers` erradica el comportamiento impulsivo de codificación a ciegas. Proporciona un marco de trabajo gobernado en 5 fases secuenciales que garantiza calidad técnica, verificabilidad continua, aislamiento de causas raíz y protección del contexto del agente.

### Capacidades Principales:
- **Brainstorming & Design Gate:** Clarificación de requerimientos, evaluación de alternativas técnicas y validación obligatoria antes de iniciar cambios.
- **Bite-sized Implementation Planning:** Descomposición algorítmica del trabajo en tareas atómicas de 2 a 5 minutos con comandos de verificación deterministas.
- **Strict TDD (Red-Green-Refactor):** Ciclo guiado por pruebas que exige un test fallido observable previo a cualquier línea de código de producción.
- **Systematic 4-Step Debugging:** Protocolo científico de resolución de incidencias (Reproducir determinísticamente ➔ Aislar causa raíz ➔ Corregir quirúrgicamente ➔ Agregar test de regresión).
- **Subagent Dispatch & Pre-merge Review:** Verificación exhaustiva de código, linters, seguridad y suite de tests antes de fusionar o cerrar tareas.

---

## 2. Arquitectura Interna

```
superpowers/
├── SKILL.md                                # Contrato operacional del agente y protocolo de las 5 fases
├── README.md                               # Documentación técnica orientada al desarrollador
└── references/                             # Guías de referencia metodológicas profundas
    └── workflows-and-tdd.md                # Reglas de TDD, checklist de 4 pasos de debugging y despacho de subagentes
```

---

## 3. Prerequisitos de Entorno

- **Runner de pruebas local:** Dependiente del stack del proyecto objetivo (`pytest`, `vitest`, `cargo test`, `jest`, `go test`, `dotnet test`, etc.).
- **Herramienta RTK:** Se recomienda la disponibilidad de `rtk` en el PATH para la optimización de tokens en la ejecución de comandos (`rtk test <cmd>`, `rtk git status`).
- **Control de versiones Git:** Repositorio Git limpio para inspección de diffs y revisiones pre-merge.

---

## 4. Ejemplos de Invocación y Uso

### Caso 1: Nueva Funcionalidad con TDD
```markdown
Modo: Fase 1 (Brainstorming) y Fase 2 (Plan Atómico)
Solicitud: Implementar política de reintentos exponenciales con jitter en el cliente HTTP.
Salida esperada:
1. Alternativas de diseño analizadas (decorador vs middleware).
2. Plan atómico de 4 pasos de 3 min cada uno.
3. Test inicial en rojo (Fase 3: RED) listo para ejecución con rtk test.
```

### Caso 2: Incidencia Crítica en Producción
```markdown
Modo: Fase 4 (Debugging Sistemático)
Solicitud: Excepción intermitente 'ConcurrentModificationException' en el procesador de colas.
Salida esperada:
1. Script mínimo de reproducción determinista bajo concurrencia.
2. Identificación del recurso compartido sin bloqueo.
3. Corrección quirúrgica del lock.
4. Test de regresión automatizado integrado en la suite.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Requisitos funcionales, historias de usuario o reportes de bugs.
- Código fuente existente, suite de pruebas automatizadas y contratos de interfaces.
- Comandos de ejecución de pruebas y linters del repositorio.

### Salidas (Outputs)
- Plan de implementación atómico con rutas exactas y comandos de verificación.
- Suites de pruebas automatizadas y tests de regresión unitarios/integración.
- Código de producción quirúrgico que cumple estrictamente con el principio Red-Green-Refactor.
- Reporte sintético de revisión de código pre-merge y cobertura de pruebas.
