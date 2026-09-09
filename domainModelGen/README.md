# domainModelGen

Herramienta de extracción y generación de modelos conceptuales del dominio en UML a partir de requisitos del negocio y narrativas operativas.

---

## 1. Propósito General

`domainModelGen` herramienta de extracción y generación de modelos conceptuales del dominio en uml a partir de requisitos del negocio y narrativas operativas.

### Capacidades Principales:
- **Modelado Conceptual del Dominio:** Extrae clases conceptuales sustantivas, atributos del problema y asociaciones semánticas sin sesgo tecnológico ni de base de datos.
- **Catálogo de Patrones Coad / ASI:** Aplica patrones canónicos como *Transacción - Detalle de Transacción*, *Lugar*, *Catálogo - Ítem*, *Rol de Participante* y *Regla de Negocio*.
- **Multiplicidades Rigurosas:** Define multiplicidades exactas (1, 0..1, *, 1..*) en ambos extremos de cada asociación justificadas por el dominio.
- **Prevención de Antipatrones:** Evita la inclusión de claves foráneas relacionales, botones de interfaz, métodos de software o clases no sustantivadas.

---

## 2. Arquitectura Interna

```
domainModelGen/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas del modelo de dominio
│   └── domain-model-template.md            # Plantilla formal de diccionario y diagrama conceptual
└── references/                             # Patrones conceptuales de cátedra
    └── asi_domain_patterns.md              # Catálogo de patrones de Peter Coad con diagramas y multiplicidades
```

---

## 3. Prerequisitos de Entorno

- No requiere dependencias externas.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Generación de Modelo Conceptual de Dominio
Entradas: Relevamiento del circuito de Logística de Distribución y Reglas de Negocio.
Salida: Diccionario de clases conceptuales, tabla de relaciones con multiplicidades y diagrama Mermaid.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Especificaciones de Requisitos Funcionales y Reglas de Negocio.
- Transcripciones de entrevistas de relevamiento con usuarios.
- Fichas o narrativas de procesos de negocio.

### Salidas (Outputs)
- Diccionario formal de Clases Conceptuales y Atributos.
- Tabla de Asociaciones semánticas con multiplicidades justificadas.
- Diagrama conceptual del dominio en sintaxis Mermaid o draw.io.
