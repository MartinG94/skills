---
name: sipocBuilder
description: >-
  Construye, normaliza y valida la matriz SIPOC (Suppliers, Inputs, Process, Outputs, Customers)
  para delimitación y alcance de procesos de negocio en GMP y Análisis de Sistemas. Especifica requisitos
  técnicos y de calidad para cada entrada y salida, asegura de 4 a 7 macroetapas en el proceso, define
  fronteras de inicio/fin y habilita la exportación directa a diagramStudio (Mermaid y Draw.io). Genera y
  guarda deterministamente el entregable en 'sipoc.md'.
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.0.0","category":"process-atomic","platforms":["windows","macos","linux"]}
---

# SIPOC Matrix Builder (GMP Etapa 2 Matriz 1 - Delimitación y Alcance)

Skill atómica especialista para la construcción, normalización y validación formal de la matriz **SIPOC** (*Suppliers, Inputs, Process, Outputs, Customers* / Proveedores, Entradas, Proceso, Salidas, Clientes), modelada según los estándares de **Gestión y Mejora de Procesos (GMP / Ciclo PDCA)** y el Trabajo Práctico Integrador (TPI - Etapa 2 Matriz 1).

Delimita quirúrgicamente el alcance y las fronteras de los procesos de negocio, articulando la taxonomía de procesos del mapa institucional (Estratégicos, Operativos y de Soporte según `SLI_U1_C03`) con el modelado formal BPMN 2.0 (`bpmnExtractor`) y la diagramación ejecutiva (`diagramStudio`).

---

## 1. Límites de Autoridad y Reglas Invariables

1. **Persistencia Determinista Obligatoria:**
   - El resultado debe persistirse obligatoriamente en el archivo Markdown `sipoc.md` en el directorio de trabajo actual. Queda prohibido usar nombres alternativos (`matriz_sipoc.md`, `tabla_sipoc.md`, etc.).
2. **Estructura Canónica de Cátedra (Etapa 2 Matriz 1):**
   Toda matriz debe contener obligatoriamente los 6 campos de encuadre institucional definidos en la guía oficial de GMP:
   - **Nombre del Proceso:** Redactado en infinitivo (`[Verbo] + [Objeto Sustantivo]`).
   - **Cliente Principal:** Beneficiario principal directo (interno o externo) a quien se le entrega la propuesta de valor.
   - **Objetivo del Proceso:** Qué asegura el proceso para la organización y el cliente.
   - **Alcance Operativo y Límites del Proceso (Fronteras):**
     - *Alcance:* Descripción concisa de áreas, sedes y situaciones cubiertas.
     - *Hito de Inicio (Desde / Disparador):* Evento o solicitud objetiva que activa la primera macroetapa (P1).
     - *Hito de Fin (Hasta / Evento Terminal):* Evento que marca la conclusión y entrega del resultado/salida final.
   - **Marco Regulatorio:**
     - *Normativa Externa:* Leyes, decretos, resoluciones ministeriales, normas de acreditación o entes de control.
     - *Reglas de Negocio Internas:* Estatutos, políticas institucionales, reglamentos y manuales de calidad.
   - **Valor Creado por el Proceso:** El "corazón" del proceso: por qué existe y qué valor diferencial entrega al cliente.
3. **Regla Canónica de 4 a 7 Macroetapas en Proceso ($4 \le P \le 7$):**
   - La dimensión **Proceso (P)** debe contener estrictamente entre 4 y 7 macroetapas.
   - Menos de 4 macroetapas indica sub-delimitación o modelado de una tarea aislada.
   - Más de 7 macroetapas viola la abstracción macro (Ley de Miller) y degenera en nivel de tarea operativa de lane.
   - Toda macroetapa debe formularse como: `[Verbo en Infinitivo de Acción] + [Objeto Sustantivo]`.
4. **Requisitos Técnicos Obligatorios en Entradas y Salidas:**
   - Queda estrictamente prohibido listar entradas o salidas como simples sustantivos abstractos sin especificación.
   - **Toda Entrada (I):** Debe detallar criterios técnicos de recepción y aceptación (formato de datos, medio físico/digital, completitud, tolerancia o frescura).
   - **Toda Salida (O):** Debe detallar especificaciones de calidad y acuerdos de servicio (SLAs de entrega, umbral de tolerancia, tasa de defectos admisible, medio de entrega).
5. **Taxonomía de Proveedores y Clientes (Alineación con Mapa de Procesos):**
   - **Proveedores (S):** Deben categorizarse en *Proveedores Externos* (clientes, fabricantes, terceros) y *Procesos del Mapa de Procesos* (Estratégicos, Clave/Operativos o de Soporte, según `SLI_U1_C03`).
   - **Clientes (C):** Deben diferenciarse en *Cliente Principal* (beneficiario directo), *Clientes Internos / Procesos* (procesos downstream del mapa) y *Cliente Externo / Sociedad y Mercado* (mercado laboral, entes reguladores).
6. **Trazabilidad y Ausencia de Orfandad:**
   - Cada entrada debe provenir de al menos un proveedor identificado.
   - Cada salida debe tener al menos un cliente o destinatario formal.
7. **Principio de Evidencia Fáctica (No Alucinación):**
   - Los insumos, participantes y sistemas deben sustentarse en la evidencia provista en el caso o relevamiento. Si faltan datos técnicos específicos, marcar explícitamente como `[TBD]`.

---

## 2. Modos de Operación

- **`build` (Predeterminado):** Construcción integral de la matriz SIPOC desde una narrativa, minuta de relevamiento o especificación de proceso.
- **`normalize`:** Refactorización y estandarización de una matriz SIPOC preexistente que carece de requisitos técnicos de calidad, omite los campos de cátedra o viola la regla de 4-7 pasos.
- **`validate`:** Auditoría metodológica determinista mediante el script `scripts/validate_sipoc.py` con verificación de estructura, conteo de etapas y especificaciones.

---

## 3. Flujo de Trabajo Paso a Paso

### Paso 1: Encuadre Institucional y Fijación de Fronteras
1. Documentar los campos de cabecera de la cátedra:
   - Proceso, Dueño, Cliente Principal y Objetivo.
   - Alcance operativo y las dos fronteras limítrofes: *Inicio (Desde)* y *Fin (Hasta)*.
   - Marco regulatorio (externo e interno) y el *Valor Creado* ("corazón del proceso").

### Paso 2: Enfoque Outside-In (Salidas y Clientes)
1. Identificar a los destinatarios: Cliente Principal, Clientes Internos (procesos del mapa) y Clientes Externos (mercado/sociedad).
2. Especificar qué entregables (**Salidas / O**) recibe cada grupo.
3. Redactar las **Especificaciones de Calidad** de cada salida: SLAs de entrega, tolerancias técnicas y criterios de conformidad.

### Paso 3: Determinación de las 4 a 7 Macroetapas del Proceso (P)
1. Descomponer la transformación en una secuencia macro de 4 a 7 pasos: $P_1 \rightarrow P_2 \rightarrow \dots \rightarrow P_n$ ($4 \le n \le 7$).
2. Comprobar que no se incluyan tareas de micro-software ni pasos microscópicos.

### Paso 4: Enfoque Inside-Out (Insumos y Proveedores)
1. Identificar los insumos (**Entradas / I**) requeridos para operar cada macroetapa.
2. Identificar el origen de cada entrada (**Proveedores / S**), mapeándolos a proveedores externos o procesos del mapa institucional (`SLI_U1_C03`).
3. Formular los **Requisitos Técnicos** de cada insumo: formatos admitidos, completitud y criterios de aceptación.

### Paso 5: Validación Metodológica Determinista
Ejecutar el script de validación determinista para certificar el cumplimiento de todas las reglas:
```bash
python sipocBuilder/scripts/validate_sipoc.py sipoc.md
```
O probar directamente el conteo de macroetapas:
```bash
python sipocBuilder/scripts/validate_sipoc.py --test-steps 5
```

### Paso 6: Integración Visual con diagramStudio
Incrustar la representación visual en Mermaid conforme al preset oficial de `diagramStudio` (`references/presets/sipoc.md`):
- Flujo `flowchart LR` con subgraphs temáticos coloreados: S, I, P, O, C.
- Conexiones dirigidas de bloque: $S \implies I \implies P \implies O \implies C$.
- Secuencia interna numerada entre macroetapas: $P_1 \rightarrow P_2 \rightarrow \dots \rightarrow P_n$.
- Clases de estilo canónicas (`sStyle`, `iStyle`, `pStyle`, `oStyle`, `cStyle`).

### Paso 7: Persistencia y Generación del Entregable
Instanciar la plantilla [templates/sipoc_template.md](templates/sipoc_template.md) y guardar obligatoriamente en `sipoc.md`.

---

## 4. Contrato de Salida

La skill genera y persiste deterministamente:
- **Archivo:** `sipoc.md`
- **Estructura Requerida:**
  1. `1. Definición y Delimitación del Proceso (Encuadre de Cátedra)`: Proceso, Cliente Principal, Dueño, Objetivo, Alcance, Límites (Inicio/Fin), Marco Regulatorio (Externo/Interno) y Valor Creado.
  2. `2. Matriz SIPOC Principal`: Tabla de 5 columnas con categorización formal de Proveedores (externos vs procesos del mapa) y Clientes (principal, internos, sociedad).
  3. `3. Especificaciones Técnicas y Requisitos de Calidad de Entradas`: Tabla con ID, Insumo, Proveedor, Requisito Técnico / Criterio de Aceptación y Medio/Formato.
  4. `4. Especificaciones Técnicas y Requisitos de Calidad de Salidas`: Tabla con ID, Salida, Cliente Destinatario, Especificación de Calidad / SLA y Criterio de Conformidad.
  5. `5. Representación Visual SIPOC`: Bloque Mermaid ejecutable según el preset de `diagramStudio`.
  6. `6. Matriz de Trazabilidad y Validación de Fronteras`: Conteo de pasos, consistencia de mapa de procesos y preparación para sincronización con `bpmnExtractor` (`sipoc-sync`).
