# requirementsExtractor

Herramienta integral de elicitación, extracción, normalización y auditoría semántica de requisitos funcionales y no funcionales.

---

## 1. Propósito General

`requirementsExtractor` herramienta integral de elicitación, extracción, normalización y auditoría semántica de requisitos funcionales y no funcionales.

### Capacidades Principales:
- **Extracción y Clasificación:** Extrae Requisitos Funcionales (RF), Requisitos No Funcionales (RNF) y Reglas de Negocio (RN) desde entrevistas y notas.
- **Historias de Usuario y BDD:** Modela historias ágiles bajo la sintaxis canónica (Como... Quiero... Para...) con criterios de aceptación Given-When-Then.
- **Detección de Ambigüedades (IEEE 29148):** Audita el texto identificando palabras débiles, términos vagos, pasividad y declaraciones no verificables.
- **Validación Semántica Automatizada:** Incluye scripts en Python para verificar la consistencia estructural y calidad semántica del inventario de requisitos.

---

## 2. Arquitectura Interna

```
requirementsExtractor/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── examples/                               # Casos de estudio y ejemplos de referencia
│   └── logistics_stakeholder_interview_case.md # Caso completo de entrevista logística
├── templates/                              # Plantillas de especificación de requisitos
│   ├── extracted_requirements.schema.json  # Esquema JSON Schema para validación de requisitos
│   ├── requirements_specification.template.md # Plantilla formal de Especificación de Requisitos
│   └── user_stories.template.md            # Plantilla de Historias de Usuario con BDD
├── references/                             # Manuales y taxonomías de elicitación
│   ├── ambiguity_detection_lexicon.md      # Léxico de detección de ambigüedades (palabras débiles)
│   ├── elicitation_heuristics.md           # Heurísticas de extracción y preguntas orientadoras
│   └── furps_and_iso25010_taxonomy.md      # Taxonomía comparada FURPS+ e ISO 25010
└── scripts/                                # Scripts de validación automatizada
    ├── test_validate_requirements_semantics.py # Suite de pruebas unitarias de validación
    └── validate_requirements_semantics.py  # Script de auditoría y validación semántica
```

---

## 3. Prerequisitos de Entorno

- Python 3.8+ (para ejecutar `validate_requirements_semantics.py` y sus tests).

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```bash
# Ejecutar validación semántica sobre requisitos extraídos
python3 requirementsExtractor/scripts/validate_requirements_semantics.py ruta/a/requisitos.json

# Ejecutar suite de pruebas
python3 -m unittest requirementsExtractor/scripts/test_validate_requirements_semantics.py
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Transcripciones de entrevistas con usuarios o partes interesadas.
- Minutas de reuniones de relevamiento o pliegos de licitación.
- Documentación de procesos o sistemas preexistentes.

### Salidas (Outputs)
- Documento formal de Especificación de Requisitos de Software (RF / RNF / RN).
- Catálogo de Historias de Usuario con criterios de aceptación BDD (Gherkin).
- Reporte de ambigüedades detectadas y preguntas abiertas para clarificación.
