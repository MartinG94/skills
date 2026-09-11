---
name: process-critical-selector
description: >-
  Evalúa, prioriza y selecciona el proceso crítico de negocio a intervenir en la Etapa 1
  de Gestión y Mejora de Procesos (GMP) aplicando la matriz de decisión multicriterio
  ponderada oficial de los 5 factores de cátedra: 1) Impacto en la estrategia, 2) Tendencias
  del entorno / SDL, 3) Problemas identificados (costos, fallas, cuellos de botella), 4) Cliente,
  y 5) Producto/Servicio. Calcula puntajes ponderados matemáticos, establece rankings y genera
  la justificación formal en 'seleccion_proceso.md'.
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.0.0","category":"process-atomic","platforms":["windows","macos","linux"]}
---

# Selección Ponderada de Proceso Crítico (GMP Etapa 1 - Matriz Multicriterio Oficial)

Skill atómica especialista para la priorización y selección matemática del **Proceso Crítico** a intervenir en proyectos de Gestión y Mejora de Procesos (GMP). Aplica la matriz multicriterio formal de los **5 factores de cátedra** (SLI_U2_C01 y Planilla Oficial TPI) para transformar el relevamiento inicial en una decisión cuantitativa, justificada e incontestable.

---

## Límites de Autoridad y Reglas Invariables

1. **Persistencia Determinista Obligatoria:** El resultado debe persistirse obligatoriamente en el archivo Markdown `seleccion_proceso.md` en el directorio de trabajo actual.
2. **Los 5 Factores Normativos de Cátedra (SLI_U2_C01):** La evaluación multicriterio debe evaluar obligatoriamente y sin excepción los 5 factores normativos de cátedra:
   - **$C_1$: Impacto en la Estrategia** (peso sugerido $w_1 = 0.25$ / 25%): Elegir procesos que permitan alcanzar los objetivos organizacionales (oportunidades, competitividad y eficiencia).
   - **$C_2$: Tendencias del Entorno / Lógica Dominante del Servicio (SDL)** (peso sugerido $w_2 = 0.20$ / 20%): Elegir procesos vinculados a tendencias globales, de la industria o mercado que establezcan un diferencial competitivo y potencien la co-creación de valor / servitización.
   - **$C_3$: Problemas Identificados y Oportunidades de Mejora** (peso sugerido $w_3 = 0.25$ / 25%): Elegir procesos que impacten en la eficiencia, inversión, riesgos, fallas y costos operativos (mermas, retrabajos, cuellos de botella).
   - **$C_4$: Cliente** (peso sugerido $w_4 = 0.20$ / 20%): Elegir el proceso que permita satisfacer, mejorar o resolver requerimientos de clientes, cambios de preferencias y experiencia de servicio.
   - **$C_5$: Producto / Servicio** (peso sugerido $w_5 = 0.10$ / 10%): Evaluar si el producto/servicio central requiere rediseño, nuevas funcionalidades o representa la propuesta de valor sustantiva del negocio.
3. **Consistencia Matemática Estricta:**
   - La suma de los pesos debe ser exactamente igual a 1.00 ($\sum_{i=1}^5 w_i = 1.00$ o $100\%$).
   - Las calificaciones $C_i$ deben pertenecer al intervalo entero discreto $[1, 5]$.
   - El puntaje total de cada proceso candidato se calcula determinísticamente como:
     $$S_p = \sum_{i=1}^5 w_i \times C_{i,p}$$
   - El orden de prelación (ranking) debe derivarse estrictamente del valor decreciente de $S_p$.
4. **Mecanismo Objetivo de Desempate:** Si dos o más procesos obtienen idéntico puntaje ponderado total $S_p$, el desempate se resuelve por orden jerárquico de factores:
   - 1° Criterio de desempate: Mayor calificación en $C_3$ (problemas identificados, costos y riesgos).
   - 2° Criterio de desempate: Mayor calificación en $C_1$ (impacto en la estrategia).
   - 3° Criterio de desempate: Mayor calificación en $C_4$ (impacto en cliente).
5. **Trazabilidad a Evidencias del Caso (No Invención):** Toda puntuación debe estar sustentada en hechos, reclamos, costos, tiempos o metas estratégicas documentadas en el caso o relevamiento. Si faltan datos numéricos precisos, explicitar el supuesto y marcar como `TBD`.
6. **Singularidad de la Selección:** Debe seleccionarse exactamente un (1) proceso como el **Proceso Crítico Seleccionado** para ser objeto de delimitación, matriz SIPOC (`sipocBuilder`), modelado AS-IS (`bpmnExtractor`) y auditoría forense (`processAuditor`) en la Etapa 2 de GMP.

---

## Rúbrica de Calificación Oficial (Escala 1 a 5)

| Nivel | Descriptor Cualitativo | C1: Estrategia | C2: Tendencias / SDL | C3: Problemas / Costos | C4: Cliente | C5: Producto / Servicio |
|:---:|:---|:---|:---|:---|:---|:---|
| **1** | **Muy Bajo** | No incide en objetivos estratégicos ni ventaja competitiva. | Totalmente aislado de tendencias y sin potencial de co-creación de valor. | Operación fluida, costos insignificantes, sin reclamos ni cuellos de botella. | Proceso interno de soporte lejano al cliente final. | Proceso periférico ajeno al core business de la compañía. |
| **2** | **Bajo** | Alineación tangencial o indirecta con la estrategia. | Afectación marginal por tendencias tecnológicas o normativas. | Fricciones esporádicas y pérdidas económicas menores toleradas. | Contacto muy bajo o impacto diferido en la satisfacción del cliente. | Servicio accesorio o de soporte secundario. |
| **3** | **Medio** | Contribuye a objetivos operativos pero no a la diferenciación principal. | Impacto moderado de servitización; requiere adaptación estándar. | Fallas recurrentes conocidas; costos operativos moderados en retrabajo. | Impacta en plazos o calidad pero con tolerancia del cliente. | Parte de la entrega pero estandarizado o commoditizado. |
| **4** | **Alto** | Clave para sostener la promesa de marca o rentabilidad anual. | Alta presión del entorno por digitalización, trazabilidad o autoservicio. | Cuellos de botella crónicos, costos de no-calidad elevados, horas extras continuas. | Repercute directamente en reclamos, NPS, tiempos de espera o pérdida de clientes. | Vinculado directamente a atributos distintivos del producto/servicio. |
| **5** | **Muy Alto / Crítico** | Factor central e indispensable de supervivencia y liderazgo estratégico. | Disrupción inminente por Lógica Dominante del Servicio (SDL) o exigencias del mercado. | Fallas severas, riesgos legales/financieros, mermas críticas o paradas operativas. | El proceso define la lealtad o el rechazo inmediato del cliente ("momento de la verdad"). | Es la esencia misma de la propuesta de valor y del producto/servicio comercializado. |

---

## Flujo de Trabajo Paso a Paso

### Paso 1: Encuadre Estratégico y Mapeo de Candidatos
- Identificar la misión, visión y 2-4 objetivos estratégicos de la organización (Matriz 1 de Etapa 1 TPI).
- Relevar entre 3 y 5 procesos candidatos a partir del Mapa de Procesos institucional (clasificados en Estratégicos, Principales/Misionales y Soporte).
- Delimitar brevemente el alcance de cada candidato (evento disparador de inicio y evento de entrega final).

### Paso 2: Análisis Individual contra los 5 Factores de Cátedra
Para cada candidato, relevar la evidencia cualitativa y cuantitativa respondiendo a las preguntas metodológicas de cátedra:
- **$C_1$ (Estrategia):** ¿Permite alcanzar los objetivos organizacionales? ¿Qué impacto tiene en competitividad y eficiencia?
- **$C_2$ (Tendencias / SDL):** ¿Se vincula con tendencias de la industria, servitización o co-creación de valor que establezcan un diferencial competitivo?
- **$C_3$ (Problemas / Costos):** ¿Qué problemas particulares plantea? ¿Cómo impacta en costos de no-calidad, fallas, inversión, riesgos y cuellos de botella?
- **$C_4$ (Cliente):** ¿Permite satisfacer, mejorar o resolver requerimientos críticos y expectativas del cliente?
- **$C_5$ (Producto / Servicio):** ¿Requiere rediseño, nuevas funcionalidades o es el núcleo de la entrega del producto/servicio central?

### Paso 3: Asignación de Calificaciones y Cálculo Matemático
- Asignar a cada candidato una nota entera entre 1 y 5 en cada factor según la rúbrica oficial.
- Establecer los pesos $w_i$ (pesos estándar de cátedra: $0.25, 0.20, 0.25, 0.20, 0.10$, sumando $1.00$).
- Calcular para cada candidato el puntaje ponderado:
  $$S_p = (w_1 \times C_1) + (w_2 \times C_2) + (w_3 \times C_3) + (w_4 \times C_4) + (w_5 \times C_5)$$
- Ordenar los candidatos de mayor a menor puntaje ($S_p$). Aplicar regla de desempate ($C_3 \rightarrow C_1 \rightarrow C_4$) si existiera paridad.

### Paso 4: Justificación Cualitativa y Análisis de Sensibilidad
- Redactar la justificación formal del proceso ganador:
  - Argumentar por qué su selección maximiza el retorno de la intervención en GMP.
  - Trazar los vínculos directos entre el puntaje alto en $C_3$ (urgencia operativa) y $C_1$/$C_4$ (valor percibido y estrategia).
- Explicar sucintamente por qué los procesos descartados tienen menor urgencia relativa o menor apalancamiento estratégico inmediato.
- Definir el alcance inicial para la Etapa 2 de GMP (límites del BPD AS-IS: disparador, actores primarios, entregable al cliente).

### Paso 5: Generación y Validación del Entregable
- Utilizar la estructura de [templates/critical_selector_template.md](templates/critical_selector_template.md).
- Guardar el documento en el archivo `seleccion_proceso.md`.
- Ejecutar la validación matemática determinista mediante el script [scripts/validate_selection.py](scripts/validate_selection.py) sobre `seleccion_proceso.md`.
- Consultar un ejemplo completo validado en [examples/sample_seleccion_proceso.md](examples/sample_seleccion_proceso.md).

---

## Contrato de Salida

La skill genera y persiste deterministamente:
- **Archivo:** `seleccion_proceso.md`
- **Estructura Requerida:**
  1. **Encuadre Organizacional:** Misión, propuesta de valor y objetivos estratégicos.
  2. **Inventario de Procesos Candidatos:** Definición, clasificación en mapa de procesos y alcance preliminar.
  3. **Criterios de Ponderación Oficiales:** Pesos ($w_1..w_5$) y justificación de ponderaciones de cátedra.
  4. **Matriz Multicriterio de Selección Ponderada:** Tabla comparativa con notas $C_1..C_5$, cálculo del puntaje total ($S_p$), ranking y estatus de selección.
  5. **Justificación Cualitativa y Cuantitativa del Proceso Seleccionado:** Análisis multifactorial fundamentado en evidencias del caso.
  6. **Análisis de Procesos No Seleccionados:** Argumentación de descarte relativo.
  7. **Handoff Metodológico a Etapa 2 de GMP:** Fronteras iniciales para SIPOC y BPD AS-IS (`sipocBuilder`, `bpmnExtractor`, `processAuditor`).
