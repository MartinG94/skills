# qualityScenarioSpecifier

Herramienta de elicitación y formalización de requisitos no funcionales mediante escenarios de calidad verificables bajo ISO 25010 y SEI.

---

## 1. Propósito General

`qualityScenarioSpecifier` herramienta de elicitación y formalización de requisitos no funcionales mediante escenarios de calidad verificables bajo iso 25010 y sei.

### Capacidades Principales:
- **Escenarios de Calidad de 6 Partes (SEI):** Especifica Fuente, Estímulo, Artefacto, Entorno, Respuesta y Medida de Respuesta mensurable.
- **Taxonomía ISO/IEC 25010:2011:** Clasifica requisitos en las 8 características de calidad de software y sus 31 subcaracterísticas asociadas.
- **Tácticas Arquitectónicas de Soporte:** Asocia tácticas de ingeniería (redundancia, balanceo, caché, autenticación, circuit breaker) para satisfacer cada escenario.
- **Matriz de Trazabilidad RNF:** Documenta matrices concisas de atributos-estímulo-respuesta para análisis ágil o especificaciones de cátedra.

---

## 2. Arquitectura Interna

```
qualityScenarioSpecifier/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de escenarios de calidad
│   ├── quality-scenario-6-part-template.md # Plantilla canónica SEI de 6 partes
│   └── rnf-scenario-matrix-dsi.md          # Matriz simplificada de escenarios de calidad DSI
└── references/                             # Taxonomías y catálogos de tácticas
    ├── iso25010-2011-taxonomy.md           # Taxonomía completa ISO/IEC 25010 con definiciones
    ├── scenario-profiles.md                # Perfiles típicos de escenarios por dominio
    └── tactics-and-validation.md           # Catálogo de tácticas arquitectónicas SEI y validación
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Escenario de Calidad de 6 Partes
Entradas: Requisito no funcional 'El sistema de pagos debe ser rápido y no caerse ante picos'.
Salida: Escenario formal SEI con estímulo de 10.000 req/s, tiempo de respuesta < 200ms en p99 y tácticas asociadas.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Requisitos no funcionales o expectativas de calidad de stakeholders.
- Acuerdos de Nivel de Servicio (SLA) o métricas de negocio.
- Restricciones de infraestructura y arquitectura tecnológica.

### Salidas (Outputs)
- Especificaciones formales de Escenarios de Calidad de 6 Partes.
- Matriz de trazabilidad de RNF clasificados bajo ISO 25010.
- Catálogo de tácticas arquitectónicas recomendadas para la implementación.
