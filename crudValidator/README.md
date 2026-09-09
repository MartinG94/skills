# crudValidator

Herramienta de auditoría de consistencia y matriz de trazabilidad CRUD entre clases del dominio conceptual y casos de uso o requisitos del sistema.

---

## 1. Propósito General

`crudValidator` herramienta de auditoría de consistencia y matriz de trazabilidad crud entre clases del dominio conceptual y casos de uso o requisitos del sistema.

### Capacidades Principales:
- **Matriz de Trazabilidad CRUD:** Cruza sistemáticamente entidades de dominio contra casos de uso documentados para mapear operaciones Create, Read, Update y Delete.
- **Diagnóstico de Cobertura Operativa:** Detecta entidades huérfanas sin creación, entidades de solo lectura no justificadas, y clases sin ciclo de vida completo.
- **Heurísticas de Inferencia Operativa:** Determina operaciones implícitas a partir del rol de la clase (Transacciones, Catálogos, Tablas de Unión) y la semántica del caso de uso.
- **Auditoría de Calidad IEEE 29148:** Identifica términos débiles, ambigüedades o asunciones infundadas en los enunciados de casos de uso analizados.

---

## 2. Arquitectura Interna

```
crudValidator/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de reporte de auditoría
│   └── crud-matrix-report-template.md      # Plantilla Markdown de matriz CRUD con diagnóstico
└── references/                             # Criterios analíticos y guías de inferencia
    ├── crud-inference-guide.md             # Heurísticas de inferencia de operaciones CRUD por rol
    └── ieee29148-quality-rules.md          # Reglas de redacción, voz activa y palabras débiles
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo. Opera como analizador metodológico textual y estructural.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Matriz CRUD de Consistencia
Entradas: Modelo de Dominio (Pedido, DetallePedido, Cliente, Producto) y Casos de Uso (CU-01 a CU-05).
Salida: Matriz de cobertura CRUD con diagnóstico de entidades huérfanas y justificación de asimetrías.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Lista de clases del Modelo de Dominio o Diagrama de Clases Conceptual.
- Catálogo o especificaciones de Casos de Uso del sistema.

### Salidas (Outputs)
- Matriz de trazabilidad cruzada [Clases × Casos de Uso] con desglose C, R, U, D.
- Reporte de vacíos (Gaps), inconsistencias y recomendaciones de completitud.
