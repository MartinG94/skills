# Ficha Técnica y Diccionario de Indicadores de Desempeño (KPIs)

## 1. Estructura Estándar de Ficha de KPI

| Campo de Gobernanza | Especificación / Regla | Ejemplo Diligenciado |
|---|---|---|
| **ID del Indicador** | Código alfanumérico único (`[DOMINIO]-[NUM]`) | `KPI-OPS-01` |
| **Nombre Técnico** | Nombre formal sin ambigüedades | `Tiempo de Ciclo de Entrega (Lead Time de Pedido)` |
| **Dominio** | `Operaciones` \| `Negocio` \| `Software_DevOps` \| `Producto_UX` | `Operaciones` |
| **Clasificación Funcional** | `Resultado / Eficacia (O1)` \| `Proceso / Eficiencia (O2)` | `Proceso / Eficiencia (O2)` |
| **Objetivo SMART** | `[Verbo] + [Variable] + [de Base a Meta] + [Plazo]` | `Reducir el tiempo medio de despacho de pedidos de 48h a 4h para el 31 de diciembre de 2026` |
| **Fórmula Matemática** | Expresión dimensional explícita con unidades | $\frac{\sum (\text{FechaHora\_Entrega} - \text{FechaHora\_Pedido})\,[\text{horas}]}{\text{Total de Pedidos Despachados}\,[\text{pedidos}]}$ |
| **Unidad de Medida** | Unidad dimensional física, temporal o porcentual | `Horas / Pedido` |
| **Línea Base (AS-IS)** | Valor histórico observado antes de la mejora | `48.2 horas` |
| **Meta Cuantitativa (TO-BE)** | Valor objetivo acordado en el proyecto | `\le 4.0 horas` |
| **Umbrales Semafóricos** | Verde (Objetivo) / Amarillo (Alerta) / Rojo (Crítico) | Verde: $\le 4\text{h}$; Amarillo: $4.1\text{h} - 8\text{h}$; Rojo: $> 8\text{h}$ |
| **Polaridad** | `Negativa (Menos es mejor)` \| `Positiva (Más es mejor)` | `Negativa` |
| **Frecuencia de Medición** | Diaria / Semanal / Mensual / Tiempo Real | `Diaria` |
| **Fuente Primaria (Data Provenance)** | Sistema, tabla o log exacto de captura | `ERP_Logistica.tb_despachos (campo: fecha_confirmacion_cliente - fecha_orden)` |
| **Responsable / Dueño** | Rol o cargo que rinde cuentas por el indicador | `Jefe de Logística y Distribución` |

---

## 2. Catálogo de Presets por Dominio

### A. Dominio Operaciones y Procesos (GMP / Lean / Six Sigma)
- **O1 (Resultado / Eficacia):**
  - `OTIF (On-Time In-Full):` $\frac{\text{Pedidos Entregados a Tiempo y Completos}}{\text{Total de Pedidos Solicitados}} \times 100\,[\%]$.
  - `NPS Operativo / Tasa de Quejas:` $\frac{\text{Reclamos por Error de Despacho}}{\text{Total de Entregas}} \times 100\,[\%]$.
- **O2 (Proceso / Eficiencia):**
  - `Lead Time de Pedido:` Tiempo transcurrido entre la colocación del pedido y la recepción conforme [horas o días].
  - `Cycle Time:` Tiempo de valor añadido en que el producto está siendo activamente procesado [minutos u horas].
  - `Tasa de Merma / Scrap:` $\frac{\text{Unidades Descartadas o Vencidas}}{\text{Total Unidades Ingresadas}} \times 100\,[\%]$.
  - `OEE (Overall Equipment Effectiveness):` $\text{Disponibilidad} \times \text{Rendimiento} \times \text{Calidad} \times 100\,[\%]$.

### B. Dominio Negocio y Estrategia (Balanced Scorecard / OKRs)
- **Perspectiva Financiera:** EBITDA, Retorno de la Inversión en Procesos ($\text{ROI} = \frac{\text{Ahorro Anual} - \text{Inversión}}{\text{Inversión}} \times 100$).
- **Perspectiva Clientes:** Cuota de Mercado, Costo de Adquisición de Clientes (CAC), Valor de Vida del Cliente (LTV).
- **Perspectiva Procesos Internos:** Reducción de costos operativos unitarios, tiempo de ciclo de aprovisionamiento.
- **Perspectiva Aprendizaje y Crecimiento:** Horas de capacitación por empleado, índice de rotación voluntaria de talento.

### C. Dominio Software & DevOps (DORA / SRE)
- **Métricas DORA:**
  - `Deployment Frequency (DF):` Frecuencia con que el código se despliega a producción con éxito [despliegues / semana o día].
  - `Lead Time for Changes (LTC):` Tiempo desde el commit de código hasta su ejecución en producción [horas].
  - `Change Failure Rate (CFR):` $\frac{\text{Despliegues que Causaron Fallas en Producción}}{\text{Total de Despliegues}} \times 100\,[\%]$.
  - `Time to Restore Service (MTTR):` Tiempo medio de recuperación ante un incidente en producción [minutos].
- **Métricas SRE:**
  - `SLI (Service Level Indicator):` $\frac{\text{Peticiones HTTP Exitosas (2xx/3xx)}}{\text{Total de Peticiones Válidas}} \times 100\,[\%]$.
  - `SLO (Service Level Objective):` Meta acordada (ej. $99.9\%$ mensual).
  - `Error Budget:` $100\% - \text{SLO}$ ($0.1\%$ de margen para incidentes y despliegues).

### D. Dominio Producto y Experiencia (HEART Framework)
- **Happiness:** CSAT (Customer Satisfaction Score), facilidad percibida en tareas clave.
- **Engagement:** Frecuencia de uso por usuario semanal, promedio de sesiones activas.
- **Adoption:** Nuevos usuarios que completan el onboarding en los primeros 7 días.
- **Retention:** Tasa de retención de cohortes a 30, 60 y 90 días (inversa al Churn Rate).
- **Task Success:** Tasa de éxito de finalización de checkout o registro, tiempo medio por tarea.
