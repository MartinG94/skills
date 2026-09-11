# sipocBuilder

Skill atómica especialista para la construcción, normalización, aseguramiento de calidad y validación algorítmica de matrices **SIPOC** (*Suppliers, Inputs, Process, Outputs, Customers* / Proveedores, Entradas, Proceso, Salidas, Clientes), modelada según el estándar de **Gestión y Mejora de Procesos (GMP / Ciclo PDCA)** y la cátedra universitaria (`PlanillaMATRICES-TPI 2026 con ejemplo.xlsx` Etapa 2 Matriz 1).

---

## 1. Propósito General

`sipocBuilder` estandariza la delimitación, alcance y encuadre de procesos de negocio críticos. Conecta la arquitectura del negocio (taxonomía de procesos Estratégicos, Operativos y de Soporte de `SLI_U1_C03`) con el diagnóstico de control interno (`processAuditor`), el modelado procedimental BPMN 2.0 (`bpmnExtractor`) y la diagramación visual ejecutiva (`diagramStudio`).

A diferencia de aproximaciones tradicionales que listan tareas informales sin rigor técnico, `sipocBuilder` impone los estándares metodológicos de cátedra:
1. **Encuadre Canónico de Cátedra (Etapa 2 Matriz 1):** Captura explícita de los 6 campos rectores: Nombre del Proceso, Cliente Principal, Objetivo, Alcance Operativo, Límites (Hito de Inicio / Disparador "Desde" e Hito de Fin / Evento Terminal "Hasta"), Marco Regulatorio (Normas Externas y Reglas Internas) y Valor Creado ("corazón del proceso").
2. **Taxonomía de Proveedores y Clientes:** Clasifica a los proveedores en *Proveedores Externos* vs *Procesos del Mapa de Procesos*, y a los clientes en *Cliente Principal* (beneficiario directo), *Clientes Internos* (otros procesos downstream del mapa) y *Cliente Externo / Sociedad* (mercado laboral, entes reguladores).
3. **Regla Canónica de 4 a 7 Macroetapas en Proceso ($4 \le P \le 7$):** Asegura que el flujo represente un macroproceso de punta a punta sin sub-delimitación ni degeneración en micro-pasos de sistema.
4. **Especificaciones Técnicas y Criterios de Calidad en Entradas y Salidas:** Exige para cada insumo sus criterios de aceptación técnicos (formato, soporte, tolerancia, frescura) y para cada salida sus acuerdos de nivel de servicio (SLAs, umbrales de tolerancia y criterios de conformidad).

---

## 2. Arquitectura Interna

```
sipocBuilder/
├── SKILL.md                          # Contrato operacional consumido por el LLM (progressive disclosure)
├── README.md                         # Documentación técnica, metodológica y de arquitectura
├── scripts/                          # Herramientas CLI de validación y generación
│   ├── validate_sipoc.py             # Validador de reglas SIPOC y generador Mermaid
│   └── test_validate_sipoc.py        # Suite de pruebas unitarias automatizadas (13 tests)
├── templates/                        # Plantillas de artefactos y ejemplos ejecutables
│   ├── sipoc_template.md             # Plantilla canónica en Markdown para 'sipoc.md' (GMP Etapa 2 M1)
│   └── sipoc_example.json            # Modelo estructurado de referencia con campos de cátedra
└── references/                       # Fundamentos teóricos y guías metodológicas
    └── sipoc_methodology.md          # Principios de delimitación, Ley de Miller y especificaciones
```

---

## 3. Prerequisitos de Entorno

- **Python:** Python 3.8 o superior (probado en Python 3.13).
- **Dependencias:** Utiliza exclusivamente librerías estándar de Python (`argparse`, `json`, `re`, `sys`, `pathlib`, `unittest`). Cero dependencias de terceros (`pip`).

---

## 4. Ejemplos de Invocación y Uso

### 4.1 Validación de un entregable Markdown (`sipoc.md`)
```bash
python sipocBuilder/scripts/validate_sipoc.py sipoc.md
```
*Salida exitosa:*
```text
EXITO: Matriz SIPOC 'Despacho y Distribución Farmacéutica con Cadena de Frío' validada con éxito.
- Proveedores (S): 4
- Entradas (I): 4 (todas con especificaciones técnicas)
- Macroproceso (P): 5 pasos (conforme al rango 4-7)
- Salidas (O): 3 (todas con especificaciones de calidad)
- Clientes (C): 3
- Fronteras delimitadas: Inicio = 'Recepción y validación de orden...', Fin = 'Entrega de medicamentos conformes...'
```

### 4.2 Verificación rápida del conteo de macroetapas
```bash
# Probar si un número de pasos cumple con la regla canónica (4 a 7)
python sipocBuilder/scripts/validate_sipoc.py --test-steps 5
# Salida: OK: 5 macroetapas está dentro del rango canónico (4 a 7).

python sipocBuilder/scripts/validate_sipoc.py --test-steps 2
# Salida: ERROR: 2 macroetapas fuera de rango. Debe tener entre 4 y 7 (actual: 2).
```

### 4.3 Exportación automática a sintaxis visual de diagramStudio (Mermaid)
```bash
python sipocBuilder/scripts/validate_sipoc.py sipocBuilder/templates/sipoc_example.json --export-mermaid
```
Genera directamente el bloque de código Mermaid `flowchart LR` con subgraphs temáticos coloreados conforme al preset oficial `diagramStudio/references/presets/sipoc.md`.

### 4.4 Ejecución de la suite de pruebas unitarias
```bash
python -m unittest sipocBuilder/scripts/test_validate_sipoc.py
# Salida: Ran 13 tests in 0.037s - OK
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Narrativas de proceso, minutas de relevamiento o entrevistas operativas.
- Mapa de Procesos de la Organización (`SLI_U1_C03` / `diagramStudio`).
- Proceso Crítico seleccionado en Etapa 1 (`processWorkbench` / `processMap`).

### Salidas (Outputs)
- **Artefacto Canónico Primario:** `sipoc.md` (guardado obligatoriamente en el directorio de trabajo actual).
- **Estructura del Artefacto:**
  1. *Definición y Delimitación del Proceso (Encuadre de Cátedra):* Proceso, Cliente Principal, Dueño, Objetivo, Alcance Operativo, Límites (Hito de Inicio / Hito de Fin), Marco Regulatorio (Externo/Interno) y Valor Creado.
  2. *Matriz SIPOC Principal:* Tabla de 5 columnas con categorización formal de Proveedores (externos vs procesos del mapa) y Clientes (principal, internos, sociedad).
  3. *Especificaciones Técnicas de Entradas:* ID, Insumo, Proveedor, Requisito Técnico / Criterio de Aceptación y Medio/Formato.
  4. *Especificaciones Técnicas de Salidas:* ID, Salida, Cliente Destinatario, Especificación de Calidad / SLA y Criterio de Conformidad.
  5. *Diagrama Visual diagramStudio:* Bloque Mermaid `flowchart LR` oficial.
  6. *Matriz de Trazabilidad y Verificación de Fronteras:* Estado de consistencia para sincronización con `bpmnExtractor` (`sipoc-sync`).

---

## 6. Integración en el Ecosistema de Skills

| Skill | Rol de Integración con `sipocBuilder` |
|---|---|
| [**diagramStudio**](../diagramStudio/README.md) | Motor de visualización. Consume la matriz SIPOC para renderizar el diagrama de 5 columnas en modo `mermaid`, `drawio` o `dual`. |
| [**bpmnExtractor**](../bpmnExtractor/README.md) | Validación matemática bidireccional mediante `sipoc-sync`: asocia proveedores/clientes con pools/lanes, macroetapas con grupos de tareas, e insumos/salidas con data objects. |
| [**processWorkbench**](../processWorkbench/README.md) | Coordinación analítica de Etapas 1, 2 y 3. Vincula proveedores y clientes con la Matriz de Stakeholders e insumos/salidas con el FODA del proceso. |
| [**processImprovementPlanner**](../processImprovementPlanner/README.md) | Orquestación general. Integra la matriz `sipoc.md` dentro del Informe Técnico Maestro de GMP. |
