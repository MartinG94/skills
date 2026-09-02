# Manual de Referencia Teórica: TGS, Taxonomía de SI, Prefactibilidad y PUD

Este documento consolida las bases conceptuales, epistemológicas y metodológicas de la ingeniería de sistemas y de software utilizadas en la skill `systemsFeasibilityAndPudClassifier`.

---

## 1. Fundamentos de la Teoría General de Sistemas (TGS)

La Teoría General de Sistemas fue formulada en la década de 1950 por el biólogo **Ludwig von Bertalanffy** como un marco interdisciplinario para comprender las propiedades de totalidades complejas que no pueden explicarse por la mera suma de sus componentes aislados (reduccionismo mecanicista).

### 1.1. Principios Sistémicos Aplicados al Software
1. **Totalidad y Sinergia:** El sistema es una totalidad no descomponible sin pérdida de funcionalidad. En software empresarial, un ERP ofrece capacidades de trazabilidad y consistencia que superan exponencialmente la suma de módulos aislados de compras, inventario y facturación.
2. **Límite y Permeabilidad:** Los sistemas de software son sistemas abiertos caracterizados por fronteras semipermeables a través de las cuales intercambian DTOs, llamadas RPC, payloads HTTP y eventos de mensajería con su entorno.
3. **Homeostasis y Control:** Los sistemas vivos y organizacionales se autorregulan mediante bucles de retroalimentación negativa que detectan desviaciones respecto a una meta u óptimo de operación y activan mecanismos correctores (ej. control de cuotas, limitadores de tasa de llamadas, escalado elástico).
4. **Entropía y Negentropía:** La segunda ley de la termodinámica aplicada a los sistemas de información indica que los datos y el software tienden naturalmente al desorden, la incoherencia y la deuda técnica (entropía positiva). La organización contrarresta esto mediante negentropía: auditorías, refactorización continua, tareas periódicas de depuración y reentrenamiento.
5. **Equifinalidad y Multifinalidad:** La equifinalidad postula que un sistema puede alcanzar el mismo estado objetivo partiendo de diferentes condiciones iniciales y por múltiples rutas operativas (ej. omnicanalidad en compras electrónicas).

---

## 2. Taxonomía de Sistemas de Información Organizacionales

La estructura piramidal de **Robert Anthony** clasifica las actividades y decisiones de las organizaciones en tres estratos:

```
Nivel Estratégico (Directorio, C-Level)  --> Decisiones No Estructuradas (Largo Plazo, Incertidumbre)
Nivel Táctico (Gerencias, Jefaturas)    --> Decisiones Semiestructuradas (Control de Gestión, Resúmenes)
Nivel Operativo (Supervisores, Operarios)--> Decisiones Estructuradas (Reglas Determinísticas, Transacciones)
```

### 2.1. Mapeo Taxonómico
- **TPS (Transaction Processing Systems):** Procesan el flujo diario de eventos y transacciones elementales indispensables para la operatoria (ej. cobros, despachos, órdenes de producción). Garantizan propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad).
- **MIS (Management Information Systems):** Proveen reportes periódicos y consolidados a mandos medios para monitorear el desempeño frente a presupuestos y metas estándar.
- **DSS (Decision Support Systems):** Herramientas analíticas interactivas que combinan datos transaccionales con modelos matemáticos y de simulación para evaluar alternativas de decisión complejas.
- **EIS / ESS (Executive Information / Support Systems):** Tableros de control ejecutivos que presentan KPIs consolidados de alto nivel, gráficos multidimensionales y datos del contexto macroeconómico.
- **Sistemas Empresariales Integrados (ERP, CRM, SCM, KMS):** Suprimen los silos funcionales mediante bases de datos corporativas unificadas y procesos de negocio integrados de punta a punta.

---

## 3. Estudio de Prefactibilidad: Dimensiones y Fórmulas Financieras

El estudio de prefactibilidad responde a la pregunta fundamental: *¿Debe llevarse a cabo el proyecto?*

### 3.1. Fórmulas Financieras
- **Valor Actual Neto (VAN / NPV):**
  $$\text{VAN} = \sum_{t=1}^{n} \frac{F_t}{(1+k)^t} - I_0$$
  Donde $I_0$ es la inversión inicial en el Año 0, $F_t$ es el flujo neto en el año $t$, y $k$ es la tasa de descuento o costo de oportunidad del capital. Criterio de aceptación: $\text{VAN} > 0$.
- **Tasa Interna de Retorno (TIR / IRR):** Es la tasa $r$ que satisface $\text{VAN}(r) = 0$. Criterio: $\text{TIR} > k$.
- **Periodo de Recupero (Payback):** Tiempo exacto en el que la suma acumulada de flujos netos recupera la inversión inicial.
- **Retorno de la Inversión (ROI):**
  $$\text{ROI} = \left( \frac{\sum \text{Beneficios Netos}}{\text{Inversión Total}} \right) \times 100$$

---

## 4. El Proceso Unificado de Desarrollo (PUD / RUP)

El PUD (creado por **Ivar Jacobson, Grady Booch y James Rumbaugh**) es un marco de desarrollo de software formal para el paradigma orientado a objetos utilizando **UML**.

### 4.1. Pilares Fundamentales
1. **Dirigido por Casos de Uso:** Los casos de uso guían la captura de requerimientos, la arquitectura, el diseño de clases, la codificación y los planes de prueba.
2. **Centrado en la Arquitectura:** La arquitectura se concibe tempranamente para estructurar el sistema en capas, componentes e interfaces robustas antes de la codificación masiva.
3. **Iterativo e Incremental:** Cada iteración representa un ciclo de desarrollo completo (análisis, diseño, código, pruebas) que culmina en un release ejecutable.

### 4.2. Hitos Formales de Fase
- **LCO (Lifecycle Objectives) - Fin de Inicio:** Acuerdo formal sobre el alcance, caso de negocio, prefactibilidad y requerimientos clave (~20%).
- **LCA (Lifecycle Architecture) - Fin de Elaboración:** Validación de la arquitectura ejecutable mediante un prototipo que mitiga los riesgos técnicos críticos y especificación de ~80% de requerimientos.
- **IOC (Initial Operational Capability) - Fin de Construcción:** Sistema completamente funcional (versión Beta) con capacidad operativa para despliegue inicial en entorno controlado.
- **PR (Product Release) - Fin de Transición:** Sistema en producción (Golden Master) aceptado formalmente por los usuarios finales.
