# relationalObjectMap

Herramienta de diseño y traducción de modelos orientados a objetos a esquemas de bases de datos relacionales normalizados (3FN).

---

## 1. Propósito General

`relationalObjectMap` herramienta de diseño y traducción de modelos orientados a objetos a esquemas de bases de datos relacionales normalizados (3fn).

### Capacidades Principales:
- **Mapeo de Clases a Tablas Relacionales:** Traduce atributos de diseño a columnas con tipos de datos agnósticos y restricciones de nulidad.
- **Estrategias de Herencia:** Evalúa y aplica Tabla por Jerarquía (TPH), Tabla por Clase Concreta (TPC) o Tabla por Subclase (TPT / Joined).
- **Mapeo de Asociaciones y Colecciones:** Resuelve relaciones 1:1, 1:N mediante claves foráneas y relaciones N:M mediante tablas asociativas con claves compuestas.
- **Validación de Formas Normales:** Audita que el esquema resultante cumpla estrictamente con Tercera Forma Normal (3FN).

---

## 2. Arquitectura Interna

```
relationalObjectMap/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de mapeo relacional
│   └── relational-mapping-spec.md          # Plantilla formal de especificación relacional y diccionario
└── references/                             # Directivas y reglas de mapeo
    ├── ddl-and-implementation.md           # Pautas de generación DDL y particularidades de motores
    └── mapping-decisions.md                # Diccionario de tipos lógicos y checklist de integridad 3FN
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Especificación de Mapeo Relacional
Entradas: Diagrama de Clases de Diseño de Facturación con herencia entre ClienteIndividual y ClienteEmpresa.
Salida: Especificación de tablas con estrategia TPT, claves primarias, claves foráneas e índices propuestos.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Diagrama de Clases de Diseño (DCD) o Modelo de Dominio de Objetos.
- Reglas de negocio de persistencia, unicidad e integridad referencial.

### Salidas (Outputs)
- Documento de Especificación de Mapeo Relacional con definición de tablas y campos.
- Diccionario de tipos de datos lógicos y restricciones de claves (PK/FK/UK).
- Checklist de integridad referencial y normalización 3FN.
