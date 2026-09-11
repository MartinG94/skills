# valueActionsBuilder

Módulo atómico y especialista para la formulación del **Inventario de Acciones de Valor**, clasificación bajo el esquema **EERR** (Eliminar, Reducir, Incrementar, Crear / Automatizar, Simplificar, Modificar, Incorporar) y evaluación sistemática de viabilidad operativa mediante el **Filtro de Restricciones Operativas** en la Etapa 3 de Gestión y Mejora de Procesos (GMP).

---

## 1. Fundamentación Metodológica y Fuentes de Cátedra

`valueActionsBuilder` actúa como puente metodológico y operativo entre las directrices estratégicas de la Matriz CAME y el rediseño tangible de procesos (BPD TO-BE, indicadores cuantitativos y cronograma de implantación de Etapa 4).

Este componente formaliza de manera automatizada y determinista los lineamientos pedagógicos y operativos de la cátedra de **Gestión y Mejora de Procesos (GMP)** de la **Universidad Tecnológica Nacional - Facultad Regional Córdoba (UTN FRC)**, extrayendo estructura, heurísticas y campos de los siguientes materiales oficiales:

1. **`SLI_U3_C05_Acciones_de_Valor.pdf` (Clase 5: Acciones de Valor):**
   - *Concepto rector (Diapositiva 5):* "Una acción de valor no es una 'idea abstracta'. Es una intervención en el proceso actual."
   - *Decodificación del CAME y Filtro Operativo (Diapositivas 6 y 7):*
     - **Disparador:** Cruces estratégicos CAME (`FO`, `FA`, `DO`, `DA`) derivados de las expectativas de los stakeholders y causas raíz FODA.
     - **Filtro de Restricciones Operativas en 4 dimensiones:**
       1. *Plazos y tiempos:* Demoras en desarrollo o implementación.
       2. *Costos / Presupuesto:* Limitaciones financieras para la mejora.
       3. *Dependencia tecnológica:* Integraciones complejas de sistemas.
       4. *Resistencia al cambio:* Curva de aprendizaje o necesidad de capacitación.
     - **El resultado:** Descripción clara de la nueva mecánica del proceso.
     - **Los objetivos:** Beneficios para la organización y alineación con objetivos estratégicos.
   - *Casos de aplicación práctica (Diapositivas 8 a 10):* Casos ofensivo (Chatbot con IA), defensivo (programa de agentes mentores) e innovación (tracking logístico integrado).

2. **`PlanillaMATRICES-TPI 2026 con ejemplo.xlsx` (Hoja *'Etapa 3 Propuesta de mejora'*, Matriz 2):**
   - *Matriz 2:* **PROPUESTA DE MEJORA Y ALINEACIÓN ESTRATÉGICA. ¿Qué queremos hacer y a quién beneficia?**
   - *Columnas canónicas de cátedra:*
     - **Columna H - Estrategia CAME de Origen:** Referencia formal a la estrategia que dispara la iniciativa (ej. `FO (F2 x O3)`).
     - **Columna I - PROPUESTA DE VALOR (¿Qué se va a hacer?):** Nombre y descripción concreta de la iniciativa de mejora, identificando la palanca principal del cambio:
       - *Automatizar / Digitalizar:* Reemplazar ejecución manual o física por tecnología o flujos automáticos (suele derivar en la eliminación de tareas manuales).
       - *Eliminar / Simplificar:* Suprimir pasos, burocracia, duplicación de cargas o controles que no agregan valor.
       - *Modificar / Rediseñar (Cambio):* Reconfigurar el flujo existente, reglas de negocio o responsabilidades sin necesariamente cambiar de tecnología.
       - *Crear / Incorporar:* Diseñar un proceso, servicio o estándar totalmente nuevo que hoy no existe.
       - *Efecto directo en el proceso:* Explicitar taxativamente qué cambia en la rutina operativa (ej. eliminación del control manual de requisitos y carga duplicada).
     - **Columna J - PROCESOS INVOLUCRADOS (Directa o indirectamente):** Identificar qué procesos del mapa se ven afectados o cuáles deben dar soporte en su implementación (base fundamental para construir el Diagrama de Gantt y asignar responsabilidades).
     - **Columna K - ALINEACIÓN ESTRATÉGICA / EXPECTATIVA DEL STAKEHOLDER:**
       - "¿Esta mejora que estoy proponiendo en el proceso, a qué meta general de la organización le mueve la aguja?"
       - "¿A qué Stakeholders da respuesta?"

---

## 2. Correspondencia Metodológica: Palancas EERR y Cátedra

| Palanca de Cátedra (Planilla TPI) | Palanca EERR (Reingeniería) | Significado Operativo en el Proceso | Efecto Directo Típico en el Proceso |
|---|---|---|---|
| **Crear / Incorporar** | **Crear [C]** | Diseñar un servicio, canal o estándar totalmente nuevo que hoy no existe. | Apertura de nuevos canales de autoservicio, diplomaturas o servicios digitales. |
| **Automatizar / Digitalizar** | **Crear [C] / Eliminar [E]** | Sustituir tareas manuales por software, pasarelas de pago o flujos automáticos. | Eliminación de formularios impresos, colas de espera y digitación manual en ventanilla. |
| **Eliminar / Simplificar** | **Eliminar [E]** | Suprimir pasos redundantes, duplicación de cargas o visados burocráticos sin valor. | Desaparición de sellos de autorización por montos menores o archivos físicos transitorios. |
| **Modificar / Rediseñar** | **Reducir [R] / Incrementar [I]** | Reconfigurar el flujo, reglas de decisión o responsabilidades entre actores. | Reducción del TMO/lead time o incremento en la frecuencia de actualización y exactitud. |

---

## 3. Arquitectura Interna del Paquete

```
valueActionsBuilder/
├── SKILL.md                          # Contrato operacional del agente (frontmatter YAML + progressive disclosure)
├── README.md                         # Documentación técnica, guías de uso y gobernanza para desarrolladores
├── scripts/                          # Herramientas CLI de validación y control de calidad
│   └── validate_value_actions.py     # Validador sintáctico, de trazabilidad CAME y reglas del filtro
├── templates/                        # Plantillas institucionales canónicas
│   └── value_actions_template.md     # Estructura canónica del entregable 'acciones_valor.md'
├── references/                       # Marcos conceptuales y estándares de cátedra
│   └── eerr_methodology.md           # Guía completa de heurísticas, 4 dimensiones del filtro y mitigaciones
└── tests/                            # Pruebas automatizadas de unidad e integración
    └── test_validate_value_actions.py # Suite de testeo algorítmico de tablas, esquemas y gobernanza
```

---

## 4. Prerequisitos de Entorno

- **Python:** Python 3.8 o superior (para ejecutar el script validador `scripts/validate_value_actions.py` y los tests).
- **Librerías estándar:** Utiliza únicamente módulos de la librería estándar (`argparse`, `json`, `re`, `sys`, `pathlib`, `unittest`). No requiere dependencias externas (`pip install` no requerido).
- **Plataformas compatibles:** Windows, macOS, Linux.

---

## 5. Ejemplos de Invocación y Uso

### 5.1 Invocación Atómica por Agente de IA
```text
Usuario: "A partir de la matriz CAME generada para la Universidad Privada, elaborá el inventario de Acciones de Valor con palancas EERR, pasalas por el filtro de restricciones operativas en sus 4 dimensiones e identificá los procesos afectados."
Agente: Invoca 'valueActionsBuilder' -> genera y valida deterministamente 'acciones_valor.md'.
```

### 5.2 Invocación Integrada en Pipelines Orquestadores
- **`processWorkbench`:** En Etapa 3, tras formular la Matriz FODA y los cruces estratégicos CAME, delega en `valueActionsBuilder` la construcción del inventario de acciones y la evaluación del filtro.
- **`processImprovementPlanner`:** Consume `acciones_valor.md` como insumo primario para modelar el diagrama TO-BE en BPMN (`bpmnExtractor`), formalizar los indicadores de desempeño (`kpiDesigner`) y construir el cronograma de Gantt de Etapa 4.

### 5.3 Validación Algorítmica desde Línea de Comandos (CLI)
```bash
# Validación de un archivo generado en formato texto
python "skills/valueActionsBuilder/scripts/validate_value_actions.py" acciones_valor.md

# Validación en formato JSON estructurado para pipelines de integración continua
python "skills/valueActionsBuilder/scripts/validate_value_actions.py" acciones_valor.md --json
```

---

## 6. Especificación del Entregable: 'acciones_valor.md'

El archivo canónico `acciones_valor.md` contiene 5 secciones estructuradas:

1. **1. Encuadre y Trazabilidad de Cruces Estratégicos CAME:**
   - Proceso bajo estudio, organización y propósito de intervención.
   - Tabla síntesis de los cruces CAME de referencia con IDs de factores FODA (`F#`, `D#`, `O#`, `A#`).
2. **2. Matriz 2 de Cátedra: Propuesta de Mejora y Alineación Estratégica:**
   - Columnas: `ID Acción`, `Estrategia CAME de Origen`, `Propuesta de Valor (Iniciativa de Cambio)`, `Palanca EERR (Principal y Derivadas)`, `Efecto Directo en el Proceso`, `Procesos Involucrados (Directa o Indirectamente)`, `Alineación Estratégica / Expectativa del Stakeholder`.
3. **3. Matriz del Filtro de Restricciones Operativas (Las 4 Dimensiones Canónicas):**
   - Columnas: `ID Acción`, `1. Plazos y Tiempos`, `2. Costos / Presupuesto`, `3. Dependencia Tecnológica`, `4. Resistencia al Cambio`, `Dictamen de Viabilidad`, `Medida de Mitigación / Ajuste Requerido`.
4. **4. Mapeo Integral de Procesos Involucrados y Soporte (Base para Gantt):**
   - Tabla de distribución de roles (Líder, Soporte TI, Calidad, Administración) para definir la columna de Responsables del Gantt.
5. **5. Plan de Traspaso a Etapa 4 (Diseño Operativo, KPIs y Cronograma):**
   - Conexión con Matriz 1 de Etapa 4: Pasos detallados para rediseño TO-BE, recursos críticos (activos/roles), formulación de KPIs (O1 Resultado / O2 Proceso) y fuente primaria del dato.

---

## 7. Criterios de Aceptación y Reglas de Calidad

1. **Trazabilidad Inquebrantable:** Ninguna acción puede estar huérfana de cruce CAME.
2. **Efecto Directo Obligatorio:** Debe explicitarse qué tarea manual, control o demora se altera en el proceso AS-IS.
3. **Filtro Cuádruple Completo:** Las 4 dimensiones de cátedra (*Plazos*, *Costos*, *TI*, *Resistencia*) deben evaluarse individualmente para cada acción.
4. **Mitigación Mandatoria:** Si el dictamen es `APROBADA CON MITIGACIÓN`, la columna de mitigación no puede estar vacía ni indicar "N/A".
5. **Código de Salida Cero:** El entregable debe aprobar el script `validate_value_actions.py` sin errores críticos.
