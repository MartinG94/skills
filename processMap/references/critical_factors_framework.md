# Marco Conceptual de Cátedra: Selección Multicriterio de Proceso Crítico (GMP Etapa 1)

Fundamentado en los materiales oficiales de la cátedra de Gestión y Mejora de Procesos (GMP):
- `SLI_U1_C03_Mapa_de_Procesos.pdf` (Arquitectura institucional de procesos en 3 niveles).
- `SLI_U2_C01_Seleccion_Proceso.pdf` (Criterios normativos de priorización y selección).
- `PlanillaMATRICES-TPI 2026 con ejemplo.xlsx` (Hoja *'Etapa 1 Situación actual'*, Matriz 2).

---

## 1. El Rol de la Selección del Proceso Crítico en Etapa 1

Una organización opera a través de decenas de procesos interrelacionados en sus 3 niveles (Estratégicos, Operativos y de Soporte). Sin embargo, un proyecto de mejora y rediseño de procesos no puede ni debe abarcar simultáneamente toda la empresa debido a:
- Limitaciones de presupuesto, recursos y tiempo.
- Resistencia al cambio y fatiga organizacional.
- Ley de Pareto (80/20): aproximadamente el 20% de los procesos concentra el 80% de los costos de no-calidad, insatisfacción de clientes y oportunidades de diferenciación competitiva.

Por ello, inmediatamente después de mapear e inventariar la red de procesos institucionales, se debe aplicar una **Matriz de Decisión Multicriterio Ponderada** para seleccionar objetiva, transparente e incontestablemente el **Proceso Crítico** que será intervenido en las siguientes etapas.

---

## 2. Los 5 Factores Normativos de Cátedra

Cada proceso candidato (típicamente del nivel Operativo / Clave / Misional) es calificado en una escala discreta de **1 a 5** en los siguientes cinco factores:

### Factor 1 ($C_1$): Impacto en la Estrategia (Peso sugerido: $w_1 = 0.25$ / 25%)
- **Definición de Cátedra:** Evalúa en qué medida el proceso permite alcanzar los objetivos estratégicos organizacionales (OE), sostener la promesa de marca y asegurar la competitividad y eficiencia de largo plazo.
- **Rúbrica:**
  - `1`: Sin incidencia en metas estratégicas.
  - `2`: Alineación tangencial o indirecta.
  - `3`: Contribuye a metas operativas anuales estándar.
  - `4`: Muy relevante para el cumplimiento de objetivos estratégicos clave (ej. expansión, rentabilidad, calidad).
  - `5`: Proceso central e indispensable para la supervivencia y el liderazgo estratégico de la institución.

### Factor 2 ($C_2$): Tendencias del Entorno / Lógica Dominante del Servicio (SDL) (Peso sugerido: $w_2 = 0.20$ / 20%)
- **Definición de Cátedra:** Mide cómo el proceso responde a las macrotendencias del sector (digitalización, autoservicio, inmediatez, sostenibilidad) y su potencial para la **co-creación de valor** según la Lógica Dominante del Servicio (Vargo & Lusch).
- **Rúbrica:**
  - `1`: Proceso estático, insensible a cambios tecnológicos o sociales.
  - `2`: Afectación marginal por tendencias del mercado.
  - `3`: Requiere adaptación digital básica; impacto moderado de servitización.
  - `4`: Alta presión por trazabilidad, autoservicio móvil y agilidad digital.
  - `5`: Disrupción inminente; el proceso representa el eje de transformación hacia la co-creación de valor en tiempo real.

### Factor 3 ($C_3$): Problemas Identificados, Costos y Riesgos (Peso sugerido: $w_3 = 0.25$ / 25%)
- **Definición de Cátedra:** Cuantifica la magnitud de las fricciones operativas actuales: costos de no-calidad, mermas, retrabajos, demoras crónicas, cuellos de botella, riesgos de control interno y horas hombre improductivas.
- **Rúbrica:**
  - `1`: Operación fluida, costos insignificantes, sin reclamos ni cuellos de botella.
  - `2`: Fricciones esporádicas y pérdidas económicas menores toleradas.
  - `3`: Fallas recurrentes conocidas; demoras moderadas asumidas como "normales".
  - `4`: Cuellos de botella crónicos, costos de retrabajo elevados, horas extras continuas.
  - `5`: Crisis operativa severa: mermas críticas, riesgos de pérdida de clientes, fallas de control interno graves o paradas operativas.

### Factor 4 ($C_4$): Cliente y Experiencia de Servicio (Peso sugerido: $w_4 = 0.20$ / 20%)
- **Definición de Cátedra:** Mide la sensibilidad del cliente externo ante el desempeño de este proceso: satisfacción, volumen de quejas, tiempos de espera percibidos y fidelización ("momento de la verdad").
- **Rúbrica:**
  - `1`: Proceso interno sin visibilidad ni contacto con el cliente externo.
  - `2`: Contacto muy bajo; el cliente apenas percibe demoras leves.
  - `3`: Impacta en tiempos o calidad pero con tolerancia moderada del cliente.
  - `4`: Repercute directamente en insatisfacción, reclamos formales, caída de NPS o riesgo de abandono.
  - `5`: Proceso crítico en el "viaje del cliente"; define la lealtad o el rechazo inmediato de la organización.

### Factor 5 ($C_5$): Producto / Servicio (Peso sugerido: $w_5 = 0.10$ / 10%)
- **Definición de Cátedra:** Analiza la relevancia del proceso en la entrega de los atributos diferenciales del producto o servicio sustantivo y la necesidad de rediseño funcional o técnico.
- **Rúbrica:**
  - `1`: Proceso periférico o accesorio ajeno al producto/servicio nuclear.
  - `2`: Servicio complementario estándar.
  - `3`: Parte de la prestación habitual pero comoditizada.
  - `4`: Vinculado a atributos distintivos de la propuesta de valor comercial.
  - `5`: Constituye el núcleo sustantivo y diferenciador del producto o servicio entregado.

---

## 3. Modelo Matemático y Condición de Cierre

El vector de ponderación $W = [w_1, w_2, w_3, w_4, w_5]$ debe satisfacer estrictamente:
$$\sum_{i=1}^{5} w_i = 1.00 \quad (100\%)$$

Para cada proceso candidato $p$, su puntaje ponderado total $S_p$ se calcula como:
$$S_p = \sum_{i=1}^{5} w_i \times C_{i,p}$$
Donde $C_{i,p} \in \{1, 2, 3, 4, 5\}$.

El ranking de prioridad se ordena de mayor a menor según $S_p$.

---

## 4. Mecanismo Objetivo de Desempate Jerárquico

Si dos o más procesos obtienen idéntico puntaje total $S_p$, el conflicto se dirime mediante la siguiente prelación objetiva de factores:
1. **1° Criterio de Desempate:** Mayor calificación en $C_3$ (urgencia operativa, costos de no-calidad y cuellos de botella).
2. **2° Criterio de Desempate:** Mayor calificación en $C_1$ (impacto directo en la estrategia organizacional).
3. **3° Criterio de Desempate:** Mayor calificación en $C_4$ (impacto directo en el cliente y experiencia de servicio).
4. **4° Criterio de Desempate:** Mayor calificación en $C_5$ (relevancia para el producto/servicio nuclear).
5. **5° Criterio de Desempate:** Mayor calificación en $C_2$ (tendencias del entorno / SDL).

---

## 5. Estándar de la Justificación Técnica ("El Porqué")

La justificación no puede ser un resumen vago de calificaciones; debe articular:
1. **Alineación Estratégica ($C_1$):** Cómo el proceso apalanca las metas SMART institucionales.
2. **Respuesta a Tendencias ($C_2$):** Cómo habilita la co-creación de valor y supera la obsolescencia.
3. **Evidencia Forense y Cuantitativa de Dolores ($C_3$):** Cifras concretas de mermas, horas perdidas, costos de retrabajo y cuellos de botella documentados en el caso.
4. **Impacto en el Cliente ($C_4$):** Métricas de insatisfacción, reclamos, tiempos de respuesta y fricciones perceptibles.
5. **Esencia de la Propuesta de Valor ($C_5$):** Por qué optimizar este proceso genera el mayor retorno de inversión metodológica para el proyecto.
