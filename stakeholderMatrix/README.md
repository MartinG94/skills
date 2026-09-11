# stakeholderMatrix

Estudio metodológico y herramienta atómica para el relevamiento, clasificación, ponderación y diagnóstico estructural de **Partes Interesadas (Stakeholders)** en la Etapa 2 de Gestión y Mejora de Procesos (GMP / Ciclo PDCA).

---

## 1. Propósito General y Enfoque de Cátedra GMP

`stakeholderMatrix` formaliza el análisis del ecosistema humano y organizacional vinculado a un proceso crítico de negocio, incorporando de manera rigurosa las directivas metodológicas de la cátedra de GMP (PlanillaMATRICES 2026):

1. **Principio Rector de Bidireccionalidad:**
   > *"En lugar de analizar únicamente cómo el stakeholder afecta al proceso en análisis, deben preguntarse: ¿Cómo nos afecta este stakeholder en la ejecución de este proceso en particular, y cómo afecta este proceso al stakeholder?"*
2. **La Triple Columna Canónica:**
   - **Resultados (¿Qué reciben? - Lo Tangible):** Outputs contractuales, objetivos y medibles entregados formalmente por el servicio del proceso (bienes, pagos, reportes, diplomas, contratos).
   - **Expectativas (¿Qué esperan? - Lo Intangible):** Atributos de calidad percibida, agilidad, soporte, trato, ergonomía y libertad de innovación que determinan la satisfacción del actor.
   - **Obstáculos y Riesgos (¿Qué podría fallar?):**
     - **Obstáculos (Falla actual AS-IS):** Fricciones, trabas burocráticas, sobrecargas o cuellos de botella reales ya constatados en la auditoría del proceso actual.
     - **Riesgos (Potencial si no se gestiona):** Contingencias futuras, pérdida de clientes, multas regulatorias o resistencia al cambio si el proceso no se rediseña debidamente.

El entregable de esta skill provee los insumos primarios para:
- **Matriz FODA del Proceso (`fodaProcess`):** Conversión de los *Obstáculos actuales* en **Debilidades (D)** y los *Riesgos potenciales* en **Amenazas (A)**.
- **Matriz CAME y Acciones de Valor EERR (`cameStrategizer` / `valueActionsBuilder`):** Transformación de los dolores relevados en iniciativas bajo las palancas *Eliminar*, *Reducir*, *Incrementar* y *Crear*.
- **Gestión del Cambio Organizacional:** Diagnóstico de resistencias y diseño de estrategias según los 4 cuadrantes de la matriz de Poder vs. Interés de Mendelow.

---

## 2. Arquitectura Interna del Módulo

```
stakeholderMatrix/
├── SKILL.md                                  # Contrato operativo del agente (progressive disclosure)
├── README.md                                 # Documentación técnica orientada a desarrolladores/usuarios
├── templates/                                # Plantillas formales de artefactos
│   └── stakeholder_matrix_template.md        # Plantilla oficial canónica para 'stakeholders.md'
├── scripts/                                  # Herramientas de automatización y validación
│   └── validate_stakeholders.py              # Validador CLI de sintaxis, triple columna, bidireccionalidad y taxonomía
├── references/                               # Fundamentos metodológicos y guías conceptuales
│   └── stakeholder_classification_guide.md   # Guía de análisis, caso Universidad Privada (cátedra) y trade-offs
└── tests/                                    # Pruebas automatizadas del validador
    └── test_validate_stakeholders.py         # Suite unittest para casos borde, tablas auxiliares y regresión
```

---

## 3. Prerequisitos de Entorno

- **Python:** Python 3.8 o superior (para ejecutar el validador CLI `scripts/validate_stakeholders.py`). Utiliza exclusivamente módulos de la biblioteca estándar de Python (`argparse`, `os`, `re`, `sys`, `pathlib`), sin dependencias de terceros.
- **Entorno del Agente:** Herramientas de lectura/escritura de archivos locales (`view_file`, `write_to_file`, `run_command`).

---

## 4. Ejemplos de Invocación y Casos de Uso

### 4.1 Invocación Directa desde el Agente (CLI / Chat)
Cuando el usuario o un orquestador solicite relevar partes interesadas de un proceso:
```markdown
"Analiza los stakeholders del proceso de despacho de farmacia utilizando la skill stakeholderMatrix y genera el archivo stakeholders.md"
```
El agente identificará los actores clave, aplicará el análisis de bidireccionalidad, clasificará los 6 grupos de interés (operativos, supervisores, gerencia/dueños, clientes, proveedores/socios, reguladores), estructurará la triple columna (Resultados, Expectativas, Obstáculos/Riesgos) y guardará `stakeholders.md`.

### 4.2 Validación Automatizada del Artefacto desde Terminal
```bash
# Validar un archivo generado 'stakeholders.md' en el directorio actual
python "skills/stakeholderMatrix/scripts/validate_stakeholders.py" stakeholders.md

# Validar en modo verboso con detalle de cuadrantes, columnas y categorías identificadas
python "skills/stakeholderMatrix/scripts/validate_stakeholders.py" -v stakeholders.md

# Validar la plantilla canónica de la skill
python "skills/stakeholderMatrix/scripts/validate_stakeholders.py" --check-template
```

**Ejemplo de salida exitosa:**
```text
[*] Validando archivo de matriz de stakeholders: templates/stakeholder_matrix_template.md
  [OK] Sección encontrada: '1. Encuadre y Alcance del Proceso'
  [OK] Sección encontrada: '2. Matriz Principal de Partes Interesadas'
  [OK] Sección encontrada: '3. Matriz de Prominencia / Mendelow'
  [OK] Sección encontrada: '4. Análisis de Tensiones y Conflictos Inter-Actor'
  [OK] Sección encontrada: '5. Conclusiones e Insumos Críticos para el Rediseño TO-BE'
  [OK] Columna identificada (Columna Stakeholder/Actor) en índice 1
  [OK] Columna identificada (Columna 1: Resultados) en índice 4
  [OK] Columna identificada (Columna 2: Expectativas) en índice 5
  [OK] Columna identificada (Columna 3: Obstáculos y Riesgos) en índice 6
  [OK] Categoría cubierta en matriz: 'Interno - Nivel Operativo'
  [OK] Categoría cubierta en matriz: 'Interno - Supervisión / Mandos Medios'
  [OK] Categoría cubierta en matriz: 'Interno - Gerencia / Dirección'
  [OK] Categoría cubierta en matriz: 'Externo - Cliente / Destinatario'
  [OK] Categoría cubierta en matriz: 'Externo - Proveedor / Socio'
  [OK] Categoría cubierta en matriz: 'Externo - Regulador / Control'

[ÉXITO] El archivo cumple al 100% con la estructura canónica de cátedra, triple columna y taxonomía de stakeholderMatrix.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- **Relevamiento Cualitativo:** Entrevistas a usuarios, minutas de relevamiento, observaciones de campo y audios transcriptos.
- **Ficha y Alcance del Proceso:** Nombre del proceso, límites inicio/fin, productos entregados.
- **Reporte de Auditoría Forense (`processAuditor`):** Evidencia documental de fallas de control interno, duplicaciones de formularios y sobrecargas operativas (`EV-xx`).
- **Diagrama de Proceso / SIPOC (`sipocBuilder` / `bpmnExtractor`):** Proveedores, entradas, salidas y clientes directos.

### Salidas (Outputs)
- **Archivo persistido:** `stakeholders.md` (guardado deterministamente en la raíz de trabajo).
- **Contenido estructurado:**
  1. **Encuadre y Alcance:** Metadatos del proceso, sponsor y alcance operativo.
  2. **Matriz Canónica de Triple Columna:** Tabla formal con ID, actor, categoría, rol, resultados tangibles, expectativas intangibles, obstáculos actuales vs riesgos potenciales y anclaje fáctico (`EV-xx`).
  3. **Matriz de Mendelow (Poder vs. Interés):** Cuadrantes estratégicos para la gobernanza del cambio (*Gestionar de Cerca*, *Mantener Satisfecho*, *Mantener Informado*, *Monitorear*).
  4. **Mapa de Tensiones Inter-Actor:** Identificación de trade-offs críticos (ej. velocidad vs control, carga de datos vs ergonomía).
  5. **Insumos para FODA y CAME:** Derivación directa hacia debilidades/amenazas y requerimientos de cambio EERR.

---

## 6. Componibilidad en el Ecosistema de Skills GMP

```
[processWorkbench] (Orquestador E1-E3) / [processImprovementPlanner] (Orquestador E1-E4)
       │
       ├──► Etapa 1: [organizationAnalysis] ──► cadena_valor_virtual.md
       │
       ├──► Etapa 2: [processAuditor] ──► Evidencia fáctica (EV-xx)
       │           ▼
       │     [stakeholderMatrix] ──► stakeholders.md (Resultados / Expectativas / Obstáculos y Riesgos)
       │           ▼
       │     [fodaProcess] ──► foda.md (Fortalezas, Oportunidades, Debilidades, Amenazas)
       │
       └──► Etapa 3: [cameStrategizer] ──► came.md
                   ▼
             [valueActionsBuilder] ──► acciones_valor.md (EERR)
```
