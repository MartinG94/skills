# apiDesign

Herramienta de diseño y auditoría de contratos HTTP/REST y especificaciones OpenAPI 3.0.3 / 3.1 trazables a casos de uso y requisitos funcionales.

---

## 1. Propósito General

`apiDesign` herramienta de diseño y auditoría de contratos http/rest y especificaciones openapi 3.0.3 / 3.1 trazables a casos de uso y requisitos funcionales.

### Capacidades Principales:
- **Diseño de Contratos RESTful:** Modela endpoints, métodos HTTP semánticos (RFC 9110), códigos de estado y esquemas de datos JSON.
- **Especificación OpenAPI 3.0.3 / 3.1:** Genera contratos OpenAPI estructurados con componentes reutilizables, parámetros tipados y ejemplos representativos.
- **Estandarización de Errores (RFC 9457):** Modela objetos de error uniformes mediante *Problem Details for HTTP APIs*.
- **Idempotencia y Concurrencia:** Diseña mecanismos de control de concurrencia optimista (`ETag`, `If-Match`) y garantías de idempotencia (`Idempotency-Key`).
- **Auditoría de APIs:** Evalúa contratos existentes contra el modelo de madurez de Richardson (RMM Nivel 2+) y previene malas prácticas de diseño.

---

## 2. Arquitectura Interna

```
apiDesign/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas y esqueletos de contratos
│   └── openapi-rest-template.yaml          # Plantilla OpenAPI 3.0.3 canónica con CRUD y RFC 9457
└── references/                             # Guías de referencia y normativas
    ├── openapi-contract-checklist.md       # Criterios de diseño REST y niveles de madurez
    └── problem-details-rfc9457.md          # Especificación canónica de errores HTTP (RFC 9457)
```

---

## 3. Prerequisitos de Entorno

- No requiere dependencias de ejecución externas para el diseño de contratos.\n- Se recomienda visor/linter de OpenAPI (Swagger Editor, Redocly CLI o Spectral) para validación sintáctica.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Contrato OpenAPI REST
Entradas: Requisitos de CU-01 Registrar Pedido y CU-02 Consultar Estado de Pedido.
Salida: Archivo OpenAPI 3.0.3 YAML con esquemas de entidades, códigos 201/400/404/409/422 y Problem Details.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Especificaciones de Casos de Uso y Requisitos Funcionales aprobados.
- Modelos de dominio conceptuales o diagramas de clases de diseño.
- Contratos preexistentes OpenAPI (YAML o JSON) para tareas de auditoría.

### Salidas (Outputs)
- Especificación formal OpenAPI 3.0.3 / 3.1 en formato YAML o JSON.
- Checklist de conformidad RESTful y buenas prácticas de idempotencia/seguridad.
- Esquemas de errores estandarizados según RFC 9457.
