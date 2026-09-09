# ormMaster

Herramienta de auditoría, diagnóstico de rendimiento y optimización de capas de acceso a datos y mapeo objeto-relacional (ORM).

---

## 1. Propósito General

`ormMaster` herramienta de auditoría, diagnóstico de rendimiento y optimización de capas de acceso a datos y mapeo objeto-relacional (orm).

### Capacidades Principales:
- **Detección de Problemas N+1:** Identifica consultas repetitivas provocadas por carga diferida (*lazy loading*) y relaciones no pre-cargadas.
- **Optimización de Consultas SQL:** Diagnostica productos cartesianos en consultas con múltiples colecciones y recomienda estrategias de Fetch Joins o Entity Graphs.
- **Gestión de Transaccionalidad:** Evalúa el alcance de transacciones, límites de demarcación (`@Transactional`), niveles de aislamiento y bloqueos optimistas/pesimistas.
- **Checklist de Auditoría para PRs:** Provee criterios estandarizados para revisiones de código de capas de persistencia.

---

## 2. Arquitectura Interna

```
ormMaster/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de auditoría de persistencia
│   └── orm-audit-report.md                 # Plantilla de reporte de auditoría con comparativa antes/después
└── references/                             # Catálogo de antipatrones y listas de verificación
    └── anti-patterns-and-checklist.md      # Catálogo de 6 antipatrones ORM críticos y checklist de PR
```

---

## 3. Prerequisitos de Entorno

- No requiere dependencias externas.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Auditoría de Acceso a Datos ORM
Entradas: Código de repositorio de Órdenes y logs SQL mostrando 101 consultas para listar 100 pedidos.
Salida: Informe de diagnóstico con causa raíz (N+1 en Items), solución con Join Fetch y comparativa de métricas.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Entidades de persistencia y archivos de configuración ORM (JPA, EF Core, SQLAlchemy, etc.).
- Trazas de ejecución o logs de consultas SQL generadas.
- Esquema de base de datos relacional y restricciones existentes.

### Salidas (Outputs)
- Informe formal de Auditoría ORM con métricas antes/después.
- Diagnóstico de consultas problemáticas y planes de ejecución.
- Recomendaciones concretas de refactorización de código y mapeo.
