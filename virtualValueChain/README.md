# virtualValueChain

Skill atómica especialista para el modelado, diagnóstico, diseño y validación de la **Cadena de Valor Virtual** (Rayport & Sviokla, 1995; apunte de cátedra oficial `APU_U1_Cadena_de_Valor_Virtual.pdf` e Ing. Gabriela Bratti) en la **Etapa 1 de Gestión y Mejora de Procesos (GMP)**.

---

## 1. Propósito General

`virtualValueChain` proporciona un marco operativo y analítico para diagnosticar cómo los datos operativos generados a lo largo de las actividades físicas de una organización pueden transformarse en una fuente independiente de valor digital, desmaterializando tareas burocráticas y habilitando nuevos modelos de servicio.

El modelo articula la interacción entre dos mundos económicos paralelos:
- **Marketplace (Espacio Físico):** Donde operan los activos tangibles, plantas de manufactura, vehículos, almacenes e infraestructura física bajo la Cadena de Valor Tradicional de Michael Porter (1985).
- **Marketspace (Espacio Virtual):** Donde la información deja de ser un costo administrativo secundario para convertirse en el **activo estratégico central**.

Dentro del ciclo metodológico de GMP, esta skill opera en la **Etapa 1 (Situación Actual y Encuadre)** para:
1. Extraer y formalizar el **Encuadre Organizacional de Cátedra (Matriz 1)** de la *Planilla de Matrices TPI 2026*.
2. Mapear de qué forma la cadena física se proyecta en una cadena de información paralela mediante **La Matriz del Valor** (cruce de las 5 actividades físicas de Porter con los 5 procesos de información).
3. Evaluar el nivel de madurez digital actual de los flujos de datos en las **3 fases evolutivas de Rayport & Sviokla** (Visibilidad, Proyección de la Capacidad / Capacidad de Reflejo, y La Matriz del Valor / Nuevas Relaciones con Clientes).
4. Servitizar las operaciones tradicionales bajo los principios de la **Lógica Dominante del Servicio (SDL — Vargo & Lusch)**, transitando de *recursos operandos* (bienes físicos estáticos) a *recursos operantes* (conocimiento y algoritmos que actúan dinámicamente para co-crear valor con el beneficiario).
5. Producir el insumo estratégico de iniciativas de digitalización para alimentar los cruces CAME y las Acciones de Valor EERR en la **Etapa 3 de GMP**.

### Principio de Atomicidad y Componibilidad
Como building block del catálogo de skills GMP:
- **Ejecución Autónoma:** Puede invocarse de manera aislada ante un caso de estudio, minuta de relevamiento o proceso operativo, produciendo su entregable canónico `cadena_valor_virtual.md`.
- **Ejecución Orquestada:** Se integra armónicamente en el pipeline estratégico coordinado por `processWorkbench` (mesa analítica de Etapas 1 a 3) y `processImprovementPlanner` (orquestador integral PDCA de 4 etapas).

---

## 2. Arquitectura Interna del Módulo

El módulo sigue la arquitectura estandarizada de documentación dual, progressive disclosure y validación automatizada:

```
virtualValueChain/
├── SKILL.md                               # Contrato operacional consumido por el LLM (YAML Frontmatter + Flujo)
├── README.md                              # Guía metodológica integral para el desarrollador y usuario humano
├── templates/                             # Plantillas institucionales normalizadas
│   └── virtual_value_chain_template.md    # Plantilla completa con Encuadre Matriz 1, Matriz 2D y 6 columnas
├── references/                            # Fundamentos conceptuales y marcos teóricos
│   └── rayport_sviokla_framework.md       # Marco de Rayport & Sviokla, apunte cátedra APU_U1 y Lógica Dominante del Servicio
├── examples/                              # Casos prácticos resueltos de referencia
│   └── bio_trace_cadena_virtual.md        # Caso práctico BioTrace Logística Farmacéutica con cadena de frío
├── scripts/                               # Herramientas deterministas de auditoría y validación
│   └── validate_virtual_value_chain.py    # Validador CLI determinista de estructura, 5 etapas, 3 fases y gobernanza
└── tests/                                 # Suite de pruebas automatizadas
    └── test_validate_virtual_value_chain.py # Tests unitarios de validación y CLI
```

---

## 3. Fundamentos Teóricos y Metodológicos

### 3.1 Encuadre Organizacional de Cátedra (Matriz 1 de PlanillaMATRICES)
La skill adopta los campos de la pestaña *'Etapa 1 Situación actual'* Matriz 1 de `PlanillaMATRICES-TPI 2026 con ejemplo.xlsx` (UTN-FRC):
- **Nombre de la Organización**, **Rubro / Actividad Organizacional**, **Ámbito o Alcance de Negocio**, **Tipo de Organización / Modelo de Negocio / Estructura Interna**.
- **Misión:** Finalidad para la cual fue creada, qué hace HOY, con foco interno y producto/servicio que entrega.
- **Visión:** Qué queremos ser A FUTURO, visión de mediano/largo plazo, cómo aspira a ser percibida.
- **Objetivos Estratégicos:** Metas cuantificables con criterios SMART.
- **Cliente de la Organización:** Caracterización del beneficiario principal.
- **Producto / Servicio:** Servicio prestado y Producto de Salida (entregable final).
- **Proceso Seleccionado y Cadena Física de Porter:** Mapeo de las 5 actividades primarias (Logística Interna, Operaciones, Logística Externa, Marketing/Ventas, Posventa).

### 3.2 Los 5 Procesos Canónicos de la Información (Rayport & Sviokla)
1. **Recopilar / Recogida (Gather):** Captura inicial de datos brutos en el punto de origen de la actividad física (sensores IoT, escaneo QR/código de barras, formularios móviles, telemetría).
2. **Organizar / Organización (Organize):** Almacenamiento estructurado, limpieza, validación y normalización en repositorios centrales (PostgreSQL, Data Lake, esquemas MDM).
3. **Seleccionar / Selección (Select):** Filtrado contextual, segmentación y reglas de negocio para aislar anomalías o información decisoria (vistas SQL indexadas, motores de reglas CEP).
4. **Sintetizar / Síntesis (Synthesize):** Agregación multivariable, modelado analítico y predicción para generar conocimiento accionable (tableros BI en tiempo real, scoring de riesgo, predicción de demoras ETA).
5. **Distribuir / Distribución (Distribute):** Entrega omnicanal de la información contextualizada al usuario, cliente o sistema de destino (notificaciones push, webhooks B2B, portales de autoservicio).

### 3.3 Las 3 Fases de Madurez Digital de Cátedra (APU_U1 Sección 10)
- **Fase 1: Visibilidad (Visibility):** Uso de tecnologías de información a gran escala para coordinar y supervisar actividades en la cadena de valor física. La operación física no cambia sustancialmente, pero se vuelve medible y transparente en tiempo real.
- **Fase 2: Proyección de la Capacidad (Capacidad de Reflejo / Mirroring Capability):** Sustitución de actividades físicas por virtuales; las empresas crean una cadena paralela en el marketspace donde procesos antes manuales o presenciales se ejecutan enteramente de forma digital.
- **Fase 3: La Matriz del Valor (Nuevas Relaciones con Clientes):** Los administradores diseñan flujos de información continuos para entregar valor en formas inéditas, personalización masiva y co-creación de valor asistencial o comercial.

### 3.4 La Matriz del Valor: Cruce Bidimensional Físico-Virtual (APU_U1 Sección 10.c y 18)
El apunte de cátedra establece explícitamente situar la cadena de valor física en un eje y los 5 procesos de la cadena virtual en el otro, identificando sistemáticamente qué datos brutos se recogen, organizan, seleccionan, sintetizan y distribuyen en cada eslabón material.

### 3.5 Articulación con la Lógica Dominante del Servicio (SDL)
La información deja de ser un costo para transformarse en un **recurso operante** (conocimiento y capacidad analítica activa). El valor no se transfiere como una propiedad estática incrustada en un bien físico (*Value-in-Exchange*), sino que se co-crea en la interacción continua y en el uso que hace el beneficiario (*Value-in-Use*).

---

## 4. Prerequisitos de Entorno y Ejecución

- **Entorno de Ejecución:** Python 3.10+ para el script de validación `scripts/validate_virtual_value_chain.py` y la suite de pruebas `tests/test_validate_virtual_value_chain.py`.
- **Compatibilidad de SO:** Totalmente compatible con Windows, macOS y Linux.
- **Sin Dependencias Binarias:** Utiliza exclusivamente la biblioteca estándar de Python (`argparse`, `json`, `re`, `pathlib`, `subprocess`, `unittest`).

---

## 5. Ejemplos de Invocación y Casos de Uso

### Caso 1: Invocación Autónoma ante un Relato Operativo
**Entrada (Prompt del Usuario):**
> "Somos una distribuidora de medicamentos con cadena de frío (+2°C a +8°C). Los choferes anotan las temperaturas a mano en planillas de papel cada 4 horas y las hojas se archivan en biblioratos. Cuando un hospital reclama porque un lote llegó con desvío térmico, demoramos 3 días en revisar las hojas. Queremos transformar este proceso en el marco de la Etapa 1 de GMP."

**Comportamiento de la Skill:**
1. Completa el encuadre organizacional de Matriz 1 (Misión, Visión, Objetivos SMART, Proceso, Cadena Física Porter).
2. Construye la matriz cruzada de las 5 actividades físicas contra los 5 procesos virtuales.
3. Estructura la tabla canónica de 6 columnas contrastando AS-IS vs. TO-BE, datos técnicos (`temp_celsius`, `gps_lat_long`) y fases de madurez.
4. Identifica el cuello de botella en la transición Recopilar ➔ Organizar (demora de 72 horas).
5. Documenta el impacto SDL (transición de flete de paquetes a garantía de integridad terapéutica).
6. Persiste el resultado deterministamente en `cadena_valor_virtual.md`.
7. Ejecuta la validación CLI determinista.

### Caso 2: Invocación Orquestada dentro de `processWorkbench`
En el encuadre de la Etapa 1 de GMP, `processWorkbench` delega en `virtualValueChain` para construir la Matriz de la Cadena de Valor Virtual y su diagnóstico de madurez antes de proceder a la Matriz Multicriterio de Selección Ponderada del Proceso Crítico.

---

## 6. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Narrativa de negocio, relevamiento de procesos o transcripción de entrevistas operativas.
- Misión, visión y objetivos estratégicos de la organización.
- Mapeo preliminar de las operaciones físicas primarias (Porter).
- Requisitos de servicio y puntos de dolor expresados por clientes.

### Salidas (Outputs)
- **Archivo Canónico Obligatorio:** `cadena_valor_virtual.md`
- **Secciones del Documento:**
  1. `## 1. Encuadre Organizacional y Espejo Físico-Virtual (Matriz 1 de Cátedra)`: 1.1 Definición organizacional completa (9 campos) y 1.2 Mapeo de la cadena física de Porter.
  2. `## 2. Matriz Bidimensional de la Cadena de Valor Virtual (Rayport & Sviokla)`: 2.1 Matriz Cruzada Físico-Virtual ("La Matriz del Valor") y 2.2 Tabla Canónica de las 5 Etapas (6 columnas).
  3. `## 3. Diagnóstico de Madurez y Evolución Digital`: Fase de madurez global, cuello de botella informacional, análisis de recursos operandos/operantes bajo SDL y desintermediación en canales.
  4. `## 4. Acciones Prioritarias de Intervención Digital (Insumo para Etapa 3 GMP)`: 4 acciones concretas estructuradas para nutrir los cruces CAME y el inventario EERR.

---

## 7. Integración en el Ecosistema de Skills GMP

```
┌────────────────────────────────────────────────────────────────────────────┐
│                              GMP ETAPA 1                                   │
│                                                                            │
│   ┌───────────────────────────┐         ┌──────────────────────────────┐   │
│   │    virtualValueChain      │ ──────> │       processWorkbench       │   │
│   │ (cadena_valor_virtual.md) │         │ (Encuadre & Selección 5 Cri) │   │
│   └───────────────────────────┘         └──────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                              GMP ETAPA 2                                   │
│                                                                            │
│   ┌───────────────────────────┐         ┌──────────────────────────────┐   │
│   │       sipocBuilder        │ ──────> │        processAuditor        │   │
│   │        (sipoc.md)         │         │     (4 Ejes de Auditoría)    │   │
│   └───────────────────────────┘         └──────────────────────────────┘   │
│                 │                                      │                   │
│                 ▼                                      ▼                   │
│   ┌───────────────────────────┐         ┌──────────────────────────────┐   │
│   │     stakeholderMatrix     │ ──────> │         fodaProcess          │   │
│   │     (stakeholders.md)     │         │          (foda.md)           │   │
│   └───────────────────────────┘         └──────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                              GMP ETAPA 3                                   │
│                                                                            │
│   ┌───────────────────────────┐         ┌──────────────────────────────┐   │
│   │      cameStrategizer      │ ──────> │    valueActionsBuilder       │   │
│   │        (came.md)          │         │     (acciones_valor.md)      │   │
│   └───────────────────────────┘         └──────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                              GMP ETAPA 4                                   │
│                                                                            │
│   ┌───────────────────────────┐         ┌──────────────────────────────┐   │
│   │        kpiDesigner        │ ──────> │  processImprovementPlanner   │   │
│   │    (kpi_catalog.json)     │         │   (Informe Maestro & Gantt)  │   │
│   └───────────────────────────┘         └──────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Control de Calidad y Validación Automatizada

Para validar formalmente un entregable generado por esta skill:

```bash
# Validación con salida detallada en consola:
python scripts/validate_virtual_value_chain.py cadena_valor_virtual.md

# Validación programática con formato JSON:
python scripts/validate_virtual_value_chain.py cadena_valor_virtual.md --json

# Ejecución de la suite de pruebas automatizadas:
python -m unittest discover -s tests -p "test_*.py"
```

### Criterios de Aceptación Invariables
1. **Nombre Canónico:** Debe llamarse exactamente `cadena_valor_virtual.md`.
2. **Campos de Encuadre:** Deben incluirse los campos de Matriz 1 de `PlanillaMATRICES-TPI 2026`.
3. **Las 5 Etapas en Orden:** Deben existir filas independientes y en secuencia estricta para Recopilar, Organizar, Seleccionar, Sintetizar y Distribuir.
4. **Datos Clave Técnicos:** La columna de datos debe contener nombres concretos de campos/variables (`id_lote`, `temp_celsius`, `gps_lat_long`).
5. **Fase de Madurez Asignada:** Toda etapa debe clasificarse válidamente como Fase 1 (Visibilidad), Fase 2 (Proyección de la Capacidad / Reflejo) o Fase 3 (La Matriz del Valor / Nuevas Relaciones).
6. **Alineación SDL:** Diagnóstico explícito del cambio cualitativo en recursos operandos/operantes y co-creación de valor (*Value-in-Use*).
