# epcFlowGen

Orquestador metodológico para el análisis y resolución integral de Ejercicios Prácticos Complementarios (EPC) y enunciados académicos de ASI y DSI.

---

## 1. Propósito General

`epcFlowGen` orquestador metodológico para el análisis y resolución integral de ejercicios prácticos complementarios (epc) y enunciados académicos de asi y dsi.

### Capacidades Principales:
- **Descomposición de Consignas:** Desglosa enunciados complejos de casos prácticos identificando restricciones explícitas, asunciones válidas y entregables requeridos.
- **Orquestación Multidisciplinar:** Coordina el flujo ordenado de resolución asignando tareas a skills especializadas (Requisitos -> Dominio -> Casos de Uso -> RCU -> DCD -> Mapeo Relacional -> Pruebas).
- **Matriz de Cobertura de Consigna:** Garantiza que cada requerimiento solicitado en el ejercicio tenga trazabilidad exacta con su artefacto de respuesta.
- **Ensamble y Consolidación:** Ensambla un documento maestro de entrega formal con coherencia transversal entre análisis y diseño.

---

## 2. Arquitectura Interna

```
epcFlowGen/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
└── templates/                              # Plantillas de resolución integral
    └── epc-resolution-template.md          # Plantilla consolidada con matriz de cobertura y secciones académicas
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Resolución Integral de EPC
Entradas: Enunciado de cátedra del sistema de Gestión de Flota de Transporte (Consignas 1 a 6).
Salida: Informe consolidado con descomposición de consigna, artefactos producidos y matriz de trazabilidad.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Enunciados de ejercicios prácticos, exámenes o casos de estudio de sistemas.
- Pautas específicas de cátedra o lineamientos institucionales.

### Salidas (Outputs)
- Informe integral de resolución de EPC normalizado en Markdown.
- Matriz de trazabilidad cruzada [Consigna del Ejercicio × Artefactos Producidos].
- Inventario de asunciones técnicas y de negocio debidamente justificadas.
