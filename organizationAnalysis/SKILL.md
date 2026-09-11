---
name: organizationAnalysis
description: >-
  Define institucionalmente a la organización bajo estudio (misión actual, visión futura,
  objetivos estratégicos SMART, cliente, producto/servicio) y modela la Cadena de Valor Virtual
  (Rayport & Sviokla) en la Etapa 1 de Gestión y Mejora de Procesos (GMP). Mapea los 5 procesos
  de información (Recopilar, Organizar, Seleccionar, Sintetizar, Distribuir), el cruce físico-virtual
  de Porter (La Matriz del Valor) y las 3 fases de madurez digital bajo SDL. Genera deterministamente
  el entregable en 'cadena_valor_virtual.md'.
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.2.0","category":"process-atomic","platforms":["windows","macos","linux"]}
---

# organizationAnalysis: Definición Institucional y Cadena de Valor Virtual (GMP Etapa 1)

Skill atómica especialista para el encuadre institucional y el modelado, auditoría y diseño de la **Cadena de Valor Virtual** (Rayport & Sviokla, 1995; apunte de cátedra oficial `APU_U1_Cadena_de_Valor_Virtual.pdf` e Ing. Gabriela Bratti). Define la circunstancia de la organización en el mercado (Matriz 1 de `PlanillaMATRICES-TPI 2026`) y analiza cómo la información generada en las operaciones físicas se captura, procesa y distribuye en el *marketspace* para crear nuevas fuentes de valor digital, desmaterializar actividades burocráticas y habilitar la **Lógica Dominante del Servicio (SDL)**.

---

## Límites de Autoridad y Reglas Invariables

1. **Persistencia Determinista Obligatoria:** El entregable final debe persistirse obligatoriamente en el archivo Markdown `cadena_valor_virtual.md` en el directorio de trabajo del usuario o proyecto.
2. **Encuadre Organizacional de Cátedra (Matriz 1):** Todo entregable debe comenzar con el encuadre formal extraído de la pestaña *'Etapa 1 Situación actual'* Matriz 1 de `PlanillaMATRICES-TPI 2026 con ejemplo.xlsx`:
   - Nombre de la organización, rubro/actividad, ámbito o alcance de negocio, tipo/modelo de negocio.
   - Misión (qué hace HOY, foco interno), Visión (aspiración a futuro de mediano/largo plazo) y Objetivos Estratégicos (SMART).
   - Cliente de la organización, Producto / Servicio (y producto de salida / entregable final).
   - Proceso Seleccionado y Cadena de Valor Física Subyacente (mapeo de las 5 actividades primarias de Michael Porter: Logística Interna, Operaciones, Logística Externa, Marketing/Ventas, Servicios Posventa).
3. **Los 5 Procesos Canónicos de la Información:** Toda matriz debe cubrir rigurosamente las 5 actividades secuenciales sin omitir, fusionar ni alterar el orden:
   - `1. Recopilar / Recogida (Gather)`: Captura de datos brutos en el punto físico donde ocurren los hechos.
   - `2. Organizar / Organización (Organize)`: Almacenamiento estructurado, limpieza, validación y normalización.
   - `3. Seleccionar / Selección (Select)`: Filtrado, segmentación y aplicación de reglas de negocio o detección de excepciones.
   - `4. Sintetizar / Síntesis (Synthesize)`: Agregación multivariable, modelado analítico, predicción y cálculo de KPIs.
   - `5. Distribuir / Distribución (Distribute)`: Entrega omnicanal de la información contextualizada al destinatario adecuado.
4. **Mapeo de las 3 Fases de Madurez de Cátedra (APU_U1 Secc. 10):** Cada etapa debe clasificarse de forma justificada en:
   - **Fase 1: Visibilidad (Visibility):** Uso de tecnologías de información para "ver" y coordinar operaciones físicas con mayor eficiencia, sin sustituir la ejecución material.
   - **Fase 2: Proyección de la Capacidad (Capacidad de Reflejo / Mirroring):** Sustitución de actividades físicas, papeles o presencialidad por flujos virtuales paralelos en el *marketspace*.
   - **Fase 3: La Matriz del Valor (Nuevas Relaciones con Clientes):** Flujos continuos de información para entregar valor de formas inéditas, personalización y co-creación colaborativa.
5. **Cruce Matricial Físico-Virtual ("La Matriz del Valor" — APU_U1 Secc. 10.c y 18):** Se debe representar el cruce matricial entre las 5 etapas físicas de Porter (en un eje) y los 5 procesos de información (en el otro eje), mostrando cómo cada actividad material nutre el flujo digital.
6. **No invención de infraestructura ni datos:** Los sistemas, formatos de datos y problemas actuales (AS-IS) deben basarse estrictamente en la evidencia provista en el caso o relevamiento. Si faltan datos técnicos, indicar explícitamente `TBD`.
7. **Articulación Obligatoria con SDL (Vargo & Lusch):** Evaluar explícitamente el paso de *recursos operandos* (bienes físicos) a *recursos operantes* (información y conocimiento dinámicos) y la transición de *Value-in-Exchange* a *Value-in-Use* (co-creación).
8. **Validación Automática de Gobernanza:** Antes de dar por concluida la tarea, debe ejecutarse el validador oficial `python scripts/validate_virtual_value_chain.py cadena_valor_virtual.md` confirmando 0 errores críticos.

---

## Flujo de Trabajo Paso a Paso (Progressive Disclosure)

### Paso 1: Relevamiento y Encuadre Organizacional (Matriz 1 Cátedra)
- Extraer de la narrativa de negocio o minuta los 9 campos institucionales de Matriz 1 de `PlanillaMATRICES-TPI 2026`.
- Mapear las 5 actividades de la cadena de valor física de Michael Porter asociadas al proceso crítico bajo estudio.
- Definir el objetivo estratégico de la digitalización e ingreso al *marketspace*.

### Paso 2: Análisis Cruzado Físico-Virtual (La Matriz del Valor)
- Cruzar cada fase física (Logística Interna, Operaciones, Logística Externa, Ventas, Posventa) con los 5 procesos de información (Recopilar, Organizar, Seleccionar, Sintetizar, Distribuir).
- Identificar qué datos brutos se generan en cada eslabón físico y cómo alimentan la cadena paralela.

### Paso 3: Relevamiento AS-IS y Diseño TO-BE de la Cadena Virtual
- Para cada uno de los 5 procesos de información:
  - **AS-IS:** Relevar la práctica operativa actual (ej. formularios de papel, planillas Excel aisladas, llamadas telefónicas reactivas).
  - **TO-BE:** Proponer soluciones de valor digital viables (IoT, base Postgres/Data Lake, reglas CEP, tableros BI en tiempo real, webhooks y portales B2B).
  - **Datos Clave Involucrados:** Detallar atributos técnicos y campos de datos exactos (ej. `id_lote`, `temp_celsius`, `timestamp_utc`, `gps_lat_long`).
  - **Fase de Madurez:** Asignar y justificar Fase 1, Fase 2 o Fase 3 según el alcance del cambio TO-BE.

### Paso 4: Diagnóstico de Madurez, Cuello de Botella y SDL
- Evaluar la madurez global del proceso actual (Fase 1 incompleta, Fase 2 incipiente, etc.).
- Identificar el **cuello de botella informacional** crítico donde se produce la mayor pérdida, desfasaje temporal o recaptura manual.
- Formular el impacto cualitativo en la **Lógica Dominante del Servicio (SDL)**, diferenciando recursos operandos de operantes y documentando la co-creación de valor (*Value-in-Use*).
- Analizar el potencial de **desintermediación** en la circulación de bienes y servicios (APU_U1 Secc. 12 y 13).

### Paso 5: Formulación de Acciones Prioritarias de Intervención Digital
- Delinear las iniciativas clave que alimentarán la Etapa 3 de GMP (Matriz CAME y Acciones de Valor EERR de `valueActionsBuilder`):
  1. Acción de Captura y Organización en Origen (Recopilar/Organizar).
  2. Acción de Filtrado y Reglas de Negocio (Seleccionar).
  3. Acción de Analítica y Modelado Situacional (Sintetizar).
  4. Acción de Salida y Co-creación de Servicio (Distribuir).

### Paso 6: Generación, Persistencia y Validación Determinista
- Utilizar la plantilla oficial [templates/virtual_value_chain_template.md](templates/virtual_value_chain_template.md).
- Guardar el documento final exactamente como `cadena_valor_virtual.md`.
- Ejecutar el script validador:
  ```bash
  python scripts/validate_virtual_value_chain.py cadena_valor_virtual.md
  ```

---

## Contrato de Salida

La skill genera y persiste exactamente un artefacto:
- **Ruta de archivo:** `cadena_valor_virtual.md`
- **Estructura requerida:**
  1. `## 1. Encuadre Organizacional y Espejo Físico-Virtual (Matriz 1 de Cátedra)` (Campos organizacionales 1.1 y mapeo de cadena física Porter 1.2).
  2. `## 2. Matriz Bidimensional de la Cadena de Valor Virtual (Rayport & Sviokla)` (2.1 Matriz Cruzada Físico-Virtual + 2.2 Matriz Canónica de las 5 Etapas con 6 columnas).
  3. `## 3. Diagnóstico de Madurez y Evolución Digital` (Fase global, cuello de botella, recursos operandos/operantes, co-creación SDL y desintermediación).
  4. `## 4. Acciones Prioritarias de Intervención Digital (Insumo para Etapa 3 GMP)` (4 iniciativas de intervención digital estructuradas).

---

## Recursos, Referencias y Herramientas

- **Plantilla Oficial:** [templates/virtual_value_chain_template.md](templates/virtual_value_chain_template.md).
- **Fundamentos Teóricos y Cátedra:** [references/rayport_sviokla_framework.md](references/rayport_sviokla_framework.md) (referencia exhaustiva a Rayport & Sviokla, apunte de cátedra `APU_U1_Cadena_de_Valor_Virtual.pdf` e Ing. Gabriela Bratti, y SDL Vargo & Lusch).
- **Ejemplo Completo Resuelto:** [examples/bio_trace_cadena_virtual.md](examples/bio_trace_cadena_virtual.md) (Caso BioTrace Logística Farmacéutica con cadena de frío).
- **Script Validador CLI:** [scripts/validate_virtual_value_chain.py](scripts/validate_virtual_value_chain.py).
- **Pruebas Automatizadas:** [tests/test_validate_virtual_value_chain.py](tests/test_validate_virtual_value_chain.py).
