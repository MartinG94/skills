---
name: stakeholderMatrix
description: >-
  Releva, clasifica y analiza formalmente las partes interesadas (stakeholders) internas y externas
  de un proceso en la Etapa 2 de Gestión y Mejora de Procesos (GMP). Aplica el principio de bidireccionalidad
  de cátedra y construye la matriz obligatoria de triple columna: Resultados (lo tangible), Expectativas
  (lo intangible) y Obstáculos/Riesgos (problemas actuales AS-IS y contingencias potenciales). Cubre roles internos
  (operativos, supervisores, gerencia/dueños) y externos (clientes, proveedores/socios, entes reguladores),
  mapea tensiones inter-actor y genera deterministamente el entregable en 'stakeholders.md'.
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.1.0","category":"process-atomic","platforms":["windows","macos","linux"]}
---

# Matriz de Partes Interesadas (Stakeholder Matrix - GMP Etapa 2)

Skill atómica especialista para el relevamiento, categorización y análisis de **Partes Interesadas (Stakeholders)** en la Etapa 2 de Gestión y Mejora de Procesos (GMP). Transforma testimonios, narrativas operativas y evidencias de campo en una matriz formal de triple columna basada en los lineamientos metodológicos de cátedra (PlanillaMATRICES 2026), diagnosticando tensiones organizacionales y fundamentando el rediseño del proceso.

---

## Límites de Autoridad y Reglas Invariables

1. **Persistencia Determinista Obligatoria:**  
   El resultado final del análisis debe guardarse obligatoriamente en el archivo Markdown `stakeholders.md` en el directorio de trabajo del caso o proyecto actual. No usar nombres alternativos.

2. **Principio Rector de Bidireccionalidad (Cátedra GMP):**  
   El relevamiento nunca debe limitarse a cómo el actor impacta pasivamente al proceso. Debe formularse de manera bidireccional:
   - *¿Cómo nos afecta este stakeholder en la ejecución de este proceso en particular?* (Insumos, tiempos, autorizaciones, restricciones, comportamientos).
   - *¿Cómo afecta este proceso al stakeholder?* (Entregables recibidos, satisfacción, carga operativa, predictibilidad, ergonomía).

3. **Estructura Mandatoria de Triple Columna:**  
   Cada parte interesada debe evaluarse bajo tres dimensiones conceptualmente distintas:
   - **1. Resultados (¿Qué reciben? - Lo Tangible):** Qué resultados o qué requiere formalmente el actor de la salida o servicio del proceso (productos, pagos, títulos, contratos, comprobantes).
   - **2. Expectativas (¿Qué esperan? - Lo Intangible):** Atributos de calidad percibida, agilidad, ergonomía laboral, transparencia, libertad de innovación o soporte que condicionan su satisfacción.
   - **3. Obstáculos y Riesgos (¿Qué podría fallar?):**
     - **Obstáculo:** Problema real y activo en el proceso AS-IS que ya impide o dificulta alcanzar los intereses del interesado (trámites burocráticos lentos, transcripción manual en papel, silos TI).
     - **Riesgo:** Problema potencial o contingencia futura si la situación no se gestiona adecuadamente (deserción, pérdida de clientes, sanciones regulatorias, rechazo gremial).

4. **Taxonomía Exhaustiva de Actores (Cobertura de 6 Grupos):**  
   Toda matriz de stakeholders debe relevar y segmentar ambas dimensiones:
   - **Actores Internos:**
     - *Nivel Operativo:* Ejecutores directos de tareas, personal de planta, operarios, docentes, choferes o cajeros.
     - *Nivel de Supervisión / Mandos Medios:* Coordinadores, líderes de turno o jefes de área responsables del balanceo diario y asignación de recursos.
     - *Nivel Gerencial / Dirección / Dueños:* Responsables estratégicos del proceso, socios propietarios, directores y sponsors enfocados en rentabilidad, metas y SLAs.
   - **Actores Externos:**
     - *Clientes / Destinatarios:* Receptores primarios o finales del bien o servicio prestado.
     - *Proveedores / Socios Comerciales:* Abastecedores de insumos, servicios tercerizados o socios de integración.
     - *Organismos Reguladores / Fiscales:* Entes públicos o auditores externos que imponen normativas, regulaciones técnicas, sanitarias o tributarias.

5. **Trazabilidad Fáctica Estricta (No-Invención):**  
   Cada afirmación, expectativa o dolor registrado debe estar respaldado por la evidencia documental o testimonial del caso (`EV-xx`, cita de entrevista, minuta o diagrama AS-IS). Si un actor clave no cuenta con información suficiente en el expediente, debe incluirse en la matriz marcando los campos faltantes como `TBD` junto a la pregunta de clarificación específica a formular.

6. **Mapeo de Conflictos y Tensiones Inter-Actor:**  
   La skill debe explicitar las colisiones entre las expectativas de diferentes actores (ej. velocidad de despacho solicitada por clientes frente al control documental estricto exigido por el organismo fiscalizador).

---

## Flujo de Trabajo Paso a Paso

### Paso 1: Relevamiento y Mapeo del Ecosistema de Actores
- Identificar a todos los involucrados directos e indirectos a partir de entrevistas, minutas de relevamiento, matriz SIPOC o fichas de proceso.
- Asegurar la representatividad de los 6 grupos de interés (operativos, supervisores, gerencia/dueños, clientes, proveedores/socios, reguladores).

### Paso 2: Análisis de Bidireccionalidad y Caracterización
- Aplicar la pregunta doble de cátedra a cada rol identificado.
- Definir el rol concreto en el flujo: ejecutor, aprobador, consultado, informado, receptor o fiscalizador.
- Determinar el nivel de poder e influencia sobre el rediseño y su nivel de interés en el resultado (Matriz de Mendelow: *Gestionar de cerca*, *Mantener satisfecho*, *Mantener informado*, *Monitorear*).

### Paso 3: Construcción de la Triple Columna Canónica
- Formular con precisión analítica:
  1. *Resultados (Lo Tangible):* Bienes físicos, transacciones, certificados, reportes objetivos.
  2. *Expectativas (Lo Intangible):* Nivel de servicio deseado, experiencia, agilidad, transparencia.
  3. *Obstáculos y Riesgos:* Desglosando con viñetas explícitas:
     - `• Obstáculos (Falla actual AS-IS): [Descripción del problema existente]`
     - `• Riesgos (Potencial futuro): [Descripción del impacto potencial si no se gestiona]`

### Paso 4: Análisis Cruzado de Tensiones y Fricciones Inter-Actor
- Detectar divergencias de objetivos:
  - Presupuesto vs Nivel de Servicio.
  - Rapidez operativa vs Segregación de Funciones (SoD) y Control Interno.
  - Autonomía operativa vs Rigidez de registro documental.

### Paso 5: Derivación de Insumos para FODA y CAME
- **Conexión con FODA (`fodaProcess`):**  
  - Los **Obstáculos internos actuales** alimentan directamente las *Debilidades (D)* del proceso.
  - Los **Riesgos potenciales externos** y exigencias no controlables alimentan las *Amenazas (A)*.
  - Las **Expectativas de mercado y tecnología** alimentan las *Oportunidades (O)*.
- **Conexión con CAME y Acciones de Valor (`cameStrategizer` / `valueActionsBuilder`):**  
  - Cada fricción crítica demanda una acción de valor bajo el esquema EERR (Eliminar, Reducir, Incrementar, Crear).
- **Gestión del Cambio Organizacional:**  
  - Identificar actores con riesgo de resistencia al cambio para prever estrategias de co-diseño y capacitación temprana.

### Paso 6: Persistencia Determinista y Validación
- Instanciar la plantilla canónica [templates/stakeholder_matrix_template.md](templates/stakeholder_matrix_template.md).
- Guardar el resultado en `stakeholders.md`.
- Validar la integridad del entregable ejecutando el script:
  `python "skills/stakeholderMatrix/scripts/validate_stakeholders.py" stakeholders.md`

---

## Contrato de Salida

La skill produce y guarda deterministamente:
- **Archivo:** `stakeholders.md`
- **Estructura Mandatoria:**
  1. `Encuadre y Alcance del Proceso`: Datos del proceso, dueño, objetivo y alcance operativo.
  2. `Matriz Principal de Partes Interesadas`: Tabla Markdown con principio de bidireccionalidad, triple columna (Resultados, Expectativas, Obstáculos/Riesgos) y trazabilidad fáctica.
  3. `Matriz de Poder vs Interés (Mendelow)`: Clasificación en los 4 cuadrantes de gestión estratégica.
  4. `Análisis de Tensiones y Conflictos Inter-Actor`: Trade-offs y desalineaciones identificadas con propuestas de resolución TO-BE.
  5. `Conclusiones e Insumos Críticos para el Rediseño TO-BE`: Vínculo explícito con FODA, CAME y Gestión del Cambio.
