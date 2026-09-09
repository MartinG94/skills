# useCaseExtractor

Herramienta para el descubrimiento, modelado, estructuración y especificación formal de Casos de Uso del Sistema (CUS) trazables a requisitos.

---

## 1. Propósito General

`useCaseExtractor` herramienta para el descubrimiento, modelado, estructuración y especificación formal de casos de uso del sistema (cus) trazables a requisitos.

### Capacidades Principales:
- **Delimitación del Sistema y Actores:** Identifica actores primarios, secundarios y de soporte, definiendo claramente la frontera del sistema.
- **Relaciones UML de Casos de Uso:** Modela formalmente relaciones de dependencia (`<<include>>` para obligatorias, `<<extend>>` con puntos de extensión para opcionales).
- **Especificaciones Institucionales Detalladas:** Genera especificaciones completas con precondiciones, postcondiciones (garantías de éxito), flujos principales, alternativos y de excepción.
- **Heurísticas de Granularidad:** Aplica la prueba del objetivo elemental del negocio (EBO) de Cockburn evitando la sobre-fragmentación o mega-casos de uso.

---

## 2. Arquitectura Interna

```
useCaseExtractor/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de especificación
│   └── use-case-specification.template.md  # Plantilla formal de especificación de Casos de Uso
└── references/                             # Heurísticas metodológicas
    └── use-case-heuristics.md              # Heurísticas de identificación, granularidad, relaciones y antipatrones
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Especificación Detallada de Caso de Uso
Entradas: Requisito Funcional RF-12 Registrar Devolución de Producto y Reglas de Negocio asociadas.
Salida: Especificación institucional completa con flujo principal, excepciones por producto dañado y postcondiciones.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Registro de Requisitos Funcionales aprobados.
- Fichas o narrativas de procesos de negocio.
- Modelos de casos de uso preexistentes para revisión o detalle.

### Salidas (Outputs)
- Diagrama del Modelo de Casos de Uso en sintaxis Mermaid o draw.io.
- Especificaciones institucionales de Casos de Uso en formato Markdown.
- Matriz de trazabilidad [Requisito Funcional × Caso de Uso].
