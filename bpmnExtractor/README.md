# bpmnExtractor

Herramienta de extracción, modelado, auditoría y análisis comparativo de procesos de negocio bajo el perfil BPMN 2.0 y estándares de Análisis y Diseño de Sistemas.

---

## 1. Propósito General

`bpmnExtractor` transforma narrativas operativas, entrevistas y relevamientos de campo en especificaciones de procesos formalmente trazables. Abarca tanto el modelado descriptivo e institucional como la validación formal de modelos y la evaluación cuantitativa de impacto en proyectos de reingeniería y mejora de procesos.

Principales capacidades:
- **Modelado Institucional (`course-process`):** Genera la ficha institucional de proceso y la especificación detallada de pools, lanes, actividades, compuertas y eventos.
- **Previsualización BPMN-IR (`ir-preview`):** Genera representaciones en JSON BPMN-IR y compila previsualizaciones limpias en Mermaid o esquemas XML BPMN 2.0 estándar.
- **Auditoría de Modelos (`audit`):** Detecta inconsistencias sintácticas y semánticas en diagramas preexistentes (splits/joins desbalanceados, tareas sin responsable, excepciones huérfanas).
- **Sincronización SIPOC ↔ BPD (`sipoc-sync`):** Verifica matemáticamente que cada proveedor, insumo, macroetapa, salida y cliente declarado en la matriz SIPOC tenga correspondencia exacta en el diagrama de procesos.
- **Análisis Diferencial AS-IS vs. TO-BE (`diff-as-is-to-be`):** Cuantifica la reducción de desperdicios, tareas manuales automatizadas, disminución de traspasos entre áreas (*handoffs*) y optimización de controles.

---

## 2. Arquitectura Interna

```
bpmnExtractor/
├── SKILL.md                          # Contrato operacional consumido por el LLM
├── README.md                         # Documentación técnica para el desarrollador
├── scripts/                          # Herramientas de transformación y validación
│   └── bpmn_ir_transformer.py        # Compilador de BPMN-IR a Mermaid y XML BPMN 2.0
├── templates/                        # Plantillas estructuradas de artefactos
│   ├── bpmn_json_schema.json         # Esquema de validación JSON Schema para BPMN-IR
│   ├── bpmn_process_ir_example.json  # Ejemplo canónico de proceso en formato IR
│   ├── bpmn_xml_skeleton.xml         # Estructura XML de referencia
│   ├── ficha_proceso_template.md     # Plantilla institucional de caracterización
│   ├── sipoc_sync_template.md        # Matriz de consistencia SIPOC ↔ BPD
│   └── diff_as_is_to_be_template.md  # Reporte comparativo diferencial AS-IS vs TO-BE
└── references/                       # Manuales metodológicos y reglas de notación
    └── bpmn_taxonomy_and_editing.md  # Taxonomía BPMN, buenas prácticas y anti-patrones
```

---

## 3. Prerequisitos de Entorno

- **Python:** Python 3.8 o superior (para ejecutar el validador y compilador `bpmn_ir_transformer.py`). Utiliza únicamente librerías estándar (`json`, `sys`, `xml.etree.ElementTree`).
- No requiere dependencias externas (`pip`).

---

## 4. Ejemplos de Invocación y Uso

### 4.1 Compilación de BPMN-IR a Mermaid / XML
```bash
# Validar y generar vista previa Mermaid
python3 bpmnExtractor/scripts/bpmn_ir_transformer.py bpmnExtractor/templates/bpmn_process_ir_example.json --format mermaid

# Validar y exportar a XML BPMN 2.0
python3 bpmnExtractor/scripts/bpmn_ir_transformer.py bpmnExtractor/templates/bpmn_process_ir_example.json --format xml
```

### 4.2 Sincronización SIPOC ↔ BPD (`sipoc-sync`)
Permite auditar la coherencia entre una tabla de delimitación inicial y el flujo operacional detallado:
```markdown
Modo: sipoc-sync
Entradas: Matriz SIPOC de Etapa 2 y especificación BPD AS-IS.
Salida: Tabla de trazabilidad y reporte de insumos huérfanos o salidas no registradas.
```

### 4.3 Diferencial de Mejora (`diff-as-is-to-be`)
Calcula el balance cuantitativo de rediseño de procesos en Etapa 4:
```markdown
Modo: diff-as-is-to-be
Entradas: Diagrama AS-IS vs Diagrama TO-BE propuesto.
Salida: Métricas de reducción de tareas manuales (-83%), handoffs (-66%) y justificación de actividades eliminadas.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Narrativas de procesos de negocio, entrevistas o transcripciones de relevamiento.
- Matrices SIPOC de delimitación.
- Modelos de procesos actuales (AS-IS) o diagramas existentes para auditar.
- Archivos JSON de proceso conforme al esquema `bpmn_json_schema.json`.

### Salidas (Outputs)
- Ficha institucional de proceso normalizada en Markdown.
- Especificación estructurada del BPD con pools, lanes, tareas, compuertas y eventos.
- Matriz de sincronización SIPOC ↔ BPD.
- Reporte comparativo de métricas de rediseño AS-IS vs TO-BE.
- Código Mermaid o XML de intercambio.
