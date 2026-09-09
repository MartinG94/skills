# umlConsistency

Herramienta de auditoría de consistencia horizontal y vertical entre modelos y diagramas UML (Secuencia, Clases, Máquinas de Estado y Código).

---

## 1. Propósito General

`umlConsistency` herramienta de auditoría de consistencia horizontal y vertical entre modelos y diagramas uml (secuencia, clases, máquinas de estado y código).

### Capacidades Principales:
- **Auditoría Secuencia ↔ Clases (RCU vs DCD):** Verifica que cada mensaje en el diagrama de secuencia corresponda a un método visible en la clase receptora con tipos y parámetros compatibles.
- **Validación de Navegabilidad y Dependencias:** Comprueba que la clase emisora tenga una referencia o relación estructural válida para interactuar con la receptora.
- **Consistencia de Estados ↔ Eventos:** Valida que las transiciones de la máquina de estados coincidan con los métodos invocados en las realizaciones de casos de uso.
- **Reporte Normalizado:** Genera reportes estructurados compatibles con `audit-report.schema.json` clasificando hallazgos por severidad.

---

## 2. Arquitectura Interna

```
umlConsistency/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas y esquemas de auditoría
│   ├── audit-report.md                     # Plantilla de informe de auditoría de consistencia
│   └── audit-report.schema.json            # Esquema JSON Schema para validación de reportes de auditoría
└── references/                             # Catálogos de inconsistencias y reglas
    └── inconsistency-catalog.md            # Catálogo de tipos de inconsistencia (INC-01 a INC-06) y reglas
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.\n- Compatible con validadores JSON Schema para `audit-report.schema.json`.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Auditoría Cruzada Secuencia vs Clases
Entradas: Diagrama de Secuencia RCU-03 y Diagrama de Clases de Diseño DCD-01.
Salida: Reporte de inconsistencias señalando métodos faltantes en GestorReserva y falta de navegabilidad.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Diagramas de Secuencia (Mermaid, PlantUML o texto).
- Diagramas de Clases de Diseño o Modelo de Dominio.
- Máquinas de Estado o especificaciones de ciclo de vida de entidades.

### Salidas (Outputs)
- Informe de Auditoría de Consistencia UML (`audit-report.md`).
- Reporte estructurado JSON conforme a `audit-report.schema.json`.
- Plan de remediación priorizado con pasos concretos de alineación.
