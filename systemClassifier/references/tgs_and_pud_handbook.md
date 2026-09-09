# Criterios de clasificación, prefactibilidad y PUD

Consulta solo la sección correspondiente al modo activo.

## 1. Diagnóstico de SI

Modelo operativo mínimo:

```text
entradas -> transformación/proceso -> salidas
                         ^             |
                         +-- retroalimentación/control
```

Registra objetivo y límite antes de clasificar componentes. Personas, procedimientos, datos, hardware y software pueden formar parte del SI; la presencia de software no convierte al SI completo en una aplicación.

Preguntas discriminantes:

- ¿Qué información o recursos ingresan y de dónde?
- ¿Qué transformación relevante ocurre?
- ¿Qué resultado útil recibe quién?
- ¿Qué información permite corregir o controlar el proceso?
- ¿Qué parte es manual y cuál computarizada?

## 2. Tipos de SI

| Tipo | Evidencia fuerte | No basta por sí solo |
| --- | --- | --- |
| TPS | registro rutinario de operaciones, alto volumen, reglas estructuradas | que exista una base de datos |
| MIS | reportes regulares, resumen y control de gestión | cualquier listado operativo |
| DSS | análisis ad hoc, alternativas o modelos para decidir | un dashboard estático |
| ESS | información agregada y estratégica para dirección | que el usuario sea gerente |
| KMS | capturar, organizar, compartir o reutilizar conocimiento | repositorio documental sin uso descrito |
| AI/experto | inferencia, recomendación o explicación basada en conocimiento/modelo | automatización convencional |

Clasifica por capacidad. Explica qué evidencia satisface el criterio y qué falta.

## 3. Prefactibilidad

La evaluación inicial responde si vale la pena continuar estudiando o desarrollar el proyecto con los recursos y contexto conocidos.

- **Técnica:** disponibilidad/capacidad de equipamiento, tecnología base, integración y competencias.
- **Económica:** costos y beneficios, capacidad/disposición de inversión; separar datos de estimaciones.
- **Operativa:** aceptación, uso real, cambios de procedimiento, capacitación y resistencia.

Un riesgo no equivale a inviabilidad. Para `CONDICIONADA`, expresa condición, responsable de resolverla si consta y evidencia necesaria. Para `NO DETERMINADO`, indica el dato faltante sin estimarlo.

## 4. PUD

Conceptos:

- fase: tramo del ciclo con objetivos;
- iteración: recorrido acotado por los flujos de trabajo;
- flujo: actividades, roles y artefactos de un aspecto como requisitos, análisis o diseño;
- artefacto: resultado producido por un flujo.

Las fases se solapan con los flujos: requisitos, análisis, diseño, implementación y prueba pueden aparecer en cada iteración con distinta intensidad. No deduzcas porcentajes universales.

Antes de ubicar un elemento, pregunta si se está describiendo trabajo previsto, artefacto existente o criterio de decisión. La prefactibilidad puede aportar a Inicio, pero por sí sola no prueba que Inicio haya terminado.


## Fórmulas Financieras de Evaluación de Prefactibilidad Económica

Calcula estos indicadores únicamente cuando el usuario proporcione la tasa de descuento, el horizonte temporal y los flujos de fondos proyectados:

### 1. Valor Actual Neto (VAN / NPV)
Descuenta los flujos netos futuros a una tasa de oportunidad $k$ y resta la inversión inicial $I_0$:
$$\text{VAN} = \sum_{t=1}^n \frac{F_t}{(1 + k)^t} - I_0$$
- **Criterio de Aceptación:** $\text{VAN} > 0$ indica viabilidad económica (genera valor por encima de la tasa exigida).

### 2. Tasa Interna de Retorno (TIR / IRR)
Tasa de descuento $r$ que iguala el VAN a cero:
$$\text{VAN} = 0 \implies \sum_{t=1}^n \frac{F_t}{(1 + r)^t} - I_0 = 0$$
- **Criterio de Aceptación:** $\text{TIR} > k$ (la rentabilidad del proyecto supera la tasa de corte).

### 3. Período de Recupero de la Inversión (Payback)
Tiempo requerido para que la sumatoria acumulada de flujos netos cubra la inversión inicial $I_0$:
- **Payback Simple:** Sumatoria directa de flujos nominales $\sum F_t \ge I_0$.
- **Payback Descontado:** Sumatoria de flujos descontados $\sum \frac{F_t}{(1+k)^t} \ge I_0$.

### 4. Retorno sobre la Inversión (ROI)
$$\text{ROI} = \left( \frac{\sum_{t=1}^n \text{Beneficios Netos}}{\text{Inversión Total (CAPEX)}} \right) \times 100$$

---

## Hitos y Puertas de Aprobación del Proceso Unificado (PUD / RUP Gates)

| Fase PUD | Hito de Salida (Gate) | Criterios Formales de Aprobación | Artefactos Clave Evaluados |
|---|---|---|---|
| **Inicio (Inception)** | **LCO** (*Lifecycle Objectives*) | Consenso en el alcance; prefactibilidad aprobada; identificación del ~20% de casos de uso críticos. | Visión, Caso de Negocio, Modelo de CU Preliminar. |
| **Elaboración** | **LCA** (*Lifecycle Architecture*) | Arquitectura base ejecutable probada contra riesgos técnicos; especificación del ~80% de casos de uso. | Documento de Arquitectura (SAD/DAS), Prototipo ejecutable, Plan de Proyecto. |
| **Construcción** | **IOC** (*Initial Operational Capability*) | Sistema completo y funcional en versión Beta; listo para despliegue en entorno controlado de usuarios. | Código probado, Manuales de usuario, Suite de tests automatizados. |
| **Transición** | **PR** (*Product Release*) | Aceptación formal por el cliente/usuarios finales; migración de datos completada y sistema en producción. | Reporte UAT firmado, Acta de pase a producción, Métricas de estabilización. |

---

## Conceptos Avanzados de Teoría General de Sistemas (TGS)

- **Homeostasis:** Capacidad de autorregulación del sistema para mantener su equilibrio operativo ante perturbaciones del entorno (ej. Circuit breakers, autoscaling, colas de desborde).
- **Entropía:** Tendencia natural al desorden, degradación o pérdida de información (ej. Deuda técnica acumulada, desincronización de esquemas).
- **Negentropía:** Energía e información inyectada externamente para preservar el orden y vigencia del sistema (ej. Refactorización continua, linters, CI/CD).
- **Sinergia:** El valor generado por el sistema coordinado es cualitativamente superior a la suma aislada de sus componentes ($1 + 1 > 2$).
- **Equifinalidad:** Capacidad de alcanzar el mismo estado o resultado final a partir de condiciones iniciales distintas y a través de caminos diferentes.
