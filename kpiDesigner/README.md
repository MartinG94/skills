# kpiDesigner

Estudio universal para el diseño, formulación, gobernanza y validación algorítmica de Indicadores Clave de Desempeño (KPIs) y métricas cuantitativas.

---

## 1. Propósito General

`kpiDesigner` estandariza la definición de sistemas de medición en múltiples dominios técnicos y organizacionales. Garantiza que toda métrica esté vinculada a objetivos SMART sintácticamente conformes, cuente con una fórmula matemática dimensionalmente balanceada y posea una fuente de datos primaria verificable.

Abarca 4 dominios principales:
1. **Operaciones y Procesos (GMP / Lean / Six Sigma):** Distinción formal entre Indicadores de Resultado (O1 - Eficacia/Impacto) e Indicadores de Proceso (O2 - Eficiencia/Tiempos), Lead Time, Cycle Time, Scrap, First Pass Yield y OEE.
2. **Negocio y Estrategia:** Cuadro de Mando Integral (Balanced Scorecard de Kaplan & Norton: Finanzas, Clientes, Procesos, Aprendizaje), OKRs, ROI y EBITDA.
3. **Ingeniería de Software & DevOps:** Las 4 métricas DORA (Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR) y marco SRE de Google (SLIs, SLOs, SLAs y presupuestos de error / Error Budgets).
4. **Producto y Experiencia de Usuario:** HEART Framework de Google (Happiness, Engagement, Adoption, Retention, Task Success), North Star Metric y modelos de cohortes/churn.

---

## 2. Arquitectura Interna

```
kpiDesigner/
├── SKILL.md                          # Contrato operacional consumido por el LLM
├── README.md                         # Documentación técnica y estándares de gobernanza
├── scripts/                          # Herramientas CLI de validación
│   └── validate_kpi.py               # Validador regex SMART y de campos obligatorios
├── templates/                        # Plantillas de diccionario y especificación
│   ├── kpi_dictionary_template.md    # Plantilla completa de diccionario de KPI
│   ├── smart_objective_template.md   # Guía y patrones de formulación SMART
│   └── kpi_catalog_example.json      # Catálogo de ejemplo ejecutable en JSON
└── references/                       # Referencias metodológicas y bibliografía
```

---

## 3. Prerequisitos de Entorno

- **Python:** Python 3.8 o superior (para ejecutar el validador `scripts/validate_kpi.py`). Utiliza únicamente la librería estándar (`argparse`, `json`, `re`, `sys`, `pathlib`).
- Sin dependencias de terceros.

---

## 4. Ejemplos de Invocación y Uso

### 4.1 Validación de sintaxis SMART desde terminal
```bash
# Probar un objetivo SMART interactivo
python3 kpiDesigner/scripts/validate_kpi.py --test-smart "Reducir el tiempo promedio de despacho de pedidos de 48 horas a 4 horas para el 31 de diciembre de 2026"
# Salida: OK: Objetivo SMART sintácticamente conforme.
```

### 4.2 Validación de un catálogo formal de indicadores en JSON
```bash
python3 kpiDesigner/scripts/validate_kpi.py kpiDesigner/templates/kpi_catalog_example.json
# Salida: EXITO: 3 KPI(s) validados con éxito. Todos cumplen gobernanza, SMART y dimensionalidad.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Objetivos estratégicos o Acciones de Valor de procesos (`processWorkbench`).
- Acuerdos de nivel de servicio o requisitos no funcionales (`qualityScenarioSpecifier`).
- Esquemas de bases de datos o fuentes de logs para identificar la procedencia del dato.

### Salidas (Outputs)
- Fichas de diccionario de KPIs en formato tabular Markdown.
- Catálogo de métricas con metas cuantitativas, línea base y umbrales semafóricos.
- Archivo JSON estructurado validado algorítmicamente mediante `validate_kpi.py`.
