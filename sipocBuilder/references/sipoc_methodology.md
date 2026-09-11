# Fundamentos Metodológicos de la Matriz SIPOC (GMP Cátedra TPI)

La matriz **SIPOC** (*Suppliers, Inputs, Process, Outputs, Customers* / Proveedores, Entradas, Proceso, Salidas, Clientes) es la herramienta nuclear de delimitación, encuadre y alcance de procesos en la fase de Diagnóstico y Definición (Etapas 1 y 2 de Gestión y Mejora de Procesos - GMP, y fase *Define* de Six Sigma DMAIC), conforme a la especificación de cátedra en `PlanillaMATRICES-TPI 2026 con ejemplo.xlsx` (Etapa 2 Matriz 1) y `SLI_U1_C03` (Mapa de Procesos).

---

## 1. Propósito y Valor Metodológico

El objetivo primordial de SIPOC no es documentar tareas microscópicas ni describir procedimientos paso a paso, sino **fijar con precisión quirúrgica las fronteras del sistema intervenido**:
1. **Evitar la dispersión de alcance (*scope creep*):** Define inequívocamente qué está dentro del proceso (*in-scope*) y qué pertenece a su entorno proveedor o cliente (*out-of-scope*).
2. **Alinear la Voz del Cliente (VoC) con la Voz del Negocio (VoB):** Conecta directamente las necesidades de los clientes con las especificaciones técnicas requeridas a los proveedores.
3. **Servir de bisagra entre el nivel estratégico y el operacional:** Proporciona la estructura macro requerida antes de emprender el modelado formal BPMN 2.0 (`bpmnExtractor`) o la auditoría de control interno (`processAuditor`).

---

## 2. Los 6 Campos Canónicos de Encuadre de Cátedra (Etapa 2 Matriz 1)

En la guía y matriz oficial del TPI 2026, la matriz SIPOC no existe en el vacío; está precedida y articulada por 6 campos deterministas de definición del proceso elegido para la mejora:

1. **Nombre del Proceso:** Enunciado en infinitivo con foco en la transformación integral (`[Verbo] + [Objeto Sustantivo]`, ej. *Gestión de la Trayectoria, Formación Integral y Graduación del Estudiante* o *Despacho y Distribución Farmacéutica con Cadena de Frío*).
2. **Cliente Principal:** Identificación del beneficiario primario (interno o externo) que recibe el valor diferencial del proceso.
3. **Objetivo del Proceso:** Qué asegura el proceso a lo largo de todo su ciclo formativo u operativo.
4. **Alcance y Límites del Proceso:**
   - *Alcance:* Descripción concisa de las situaciones, sedes o áreas cubiertas.
   - *Hito de Inicio (Desde / Disparador):* Evento o solicitud objetiva que activa la primera macroetapa (P1).
   - *Hito de Fin (Hasta / Evento Terminal):* Evento fáctico que marca la conclusión y entrega del resultado/salida final.
5. **Marco Regulatorio:**
   - *Normativa Externa:* Leyes nacionales, resoluciones ministeriales, normas de acreditación o marcos regulatorios que imponen restricciones.
   - *Reglas de Negocio Internas:* Estatuto de la organización, reglamentos de personal/alumnos, ordenanzas y manuales operativos.
6. **Valor Creado por el Proceso:** El "corazón" del proceso: ¿Por qué existe y qué valor diferencial entrega al cliente?

---

## 3. Taxonomía de Proveedores y Clientes (Alineación con `SLI_U1_C03`)

Según los lineamientos de la clase `SLI_U1_C03_Mapa_de_Procesos`, las organizaciones gestionan procesos organizados en tres familias:
- **Procesos Estratégicos:** Definen dirección, lineamientos y objetivos de largo plazo.
- **Procesos Operativos (Misionales / Clave):** Crean valor directo para el cliente y constituyen el núcleo del negocio.
- **Procesos de Soporte:** Apoyan el funcionamiento de los procesos operativos (TI, Finanzas, RRHH).

En la matriz SIPOC:
- **Proveedores (S):**
  - *Proveedores Externos:* Agentes que operan fuera de la frontera organizacional (clientes solicitantes, fabricantes, proveedores de materias primas).
  - *Procesos del Mapa de Procesos:* Procesos internos identificados en el Mapa de Procesos que transfieren información, autorizaciones o recursos al proceso en análisis (ej. *Proceso de Gestión de TI*, *Proceso de Facturación*).
- **Clientes (C):**
  - *Cliente Principal:* Beneficiario directo del producto o servicio.
  - *Clientes Internos:* Otros procesos del mapa que consumen salidas intermedias (ej. procesos downstream).
  - *Cliente Externo Final / Sociedad y Mercado:* El mercado laboral, entes reguladores y la comunidad.

---

## 4. La Regla Canónica de 4 a 7 Macroetapas

En la columna **Proceso (P)**, toda matriz SIPOC metodológicamente conforme debe declarar entre **4 y 7 macroetapas**:

$$\text{Cantidad de Macroetapas } (P) \in [4, 7]$$

### Rationale Cognitivo y Estructural:
- **Límite Inferior ($P < 4$): Sub-delimitación.** Menos de 4 pasos suele indicar que se está modelando una tarea elemental o una actividad aislada en lugar de un proceso de negocio de punta a punta.
- **Límite Superior ($P > 7$): Sobre-especificación y degeneración operativa.** Superar las 7 etapas viola el principio de *chunking* de la memoria de trabajo (Ley de Miller, $7 \pm 2$) y arrastra el análisis a un nivel procedimental/operativo (tareas de lane o micro-pasos de software), desvirtuando el propósito de delimitación de alto nivel de SIPOC.
- **Regla Sintáctica de Redacción:** Cada macroetapa debe redactarse obligatoriamente con la estructura:
  $$[\text{Verbo en Infinitivo de Acción}] + [\text{Objeto Sustantivo}]$$

---

## 5. Especificaciones Técnicas y Requisitos de Calidad de Insumos y Salidas

En `sipocBuilder`, cada entrada y cada salida debe incorporar obligatoriamente **requisitos técnicos y criterios de calidad verificables**:

### 5.1 Requisitos Técnicos en Entradas (Insumos)
Definen las condiciones que el insumo debe satisfacer antes de ser admitido por la primera macroetapa del proceso (Criterio de Aceptación):
- **Formato y Medio:** ¿Es papel físico, payload JSON vía REST API, archivo EDIFACT, formulario firmado?
- **Completitud y Validación:** ¿Qué campos o datos son obligatorios? (ej. CUIT verificado, pago aprobado).
- **Frescura y Tolerancia Temporal:** ¿Cuál es la antigüedad máxima aceptable del dato o lote?
- **Tolerancia Física/Química:** Temperatura, humedad, embalaje intacto.

### 5.2 Especificaciones de Calidad en Salidas (Entregables)
Definen los estándares de calidad con los cuales el cliente evalúa y acepta el resultado del proceso (Criterio de Calidad Crítico / CTQ):
- **Acuerdo de Nivel de Servicio (SLA):** Tiempo máximo de entrega (*Lead Time* comprometido).
- **Exactitud y Confiabilidad:** Tasa de error admisible (ej. Scrap < 0.1%, exactitud de inventario 99.8%).
- **Criterio de Conformidad:** Cómo valida el cliente la recepción (firma de remito digital, checksum criptográfico, acuse de recibo legal).

---

## 6. Trazabilidad y Sincronización con el Ecosistema GMP

| Artefacto / Skill Downstream | Mapeo SIPOC | Validación Automatizada |
|---|---|---|
| **bpmnExtractor (`sipoc-sync`)** | $S \rightarrow$ Pools/Lanes externos e internos<br>$I \rightarrow$ Data Objects / Message Events<br>$P \rightarrow$ Subprocesos o grupos de tareas<br>$O \rightarrow$ Data Objects generados<br>$C \rightarrow$ Pools/Lanes receptores | Detección matemática de insumos huérfanos, salidas no producidas y desajustes de fronteras. |
| **processWorkbench (E2)** | $S$ y $C \rightarrow$ Matriz de Stakeholders (Expectativas y Obstáculos)<br>$I$ y $O \rightarrow$ Insumos para Matriz FODA (fallas de control interno y ruta documental). | Coherencia entre actores clave identificados y proveedores/clientes de SIPOC. |
| **diagramStudio** | Mapeo directo a bloque visual Mermaid `flowchart LR` con subgraphs temáticos coloreados y preset Draw.io editable. | Generación automática mediante `validate_sipoc.py --export-mermaid`. |
