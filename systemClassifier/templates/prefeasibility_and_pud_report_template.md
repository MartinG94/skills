# Informe de [modo] — [Proyecto o sistema]

**Alcance:** [alcance o TBD]<br>
**Fuentes:** [SRC-01, ...]<br>
**Estado:** Borrador / En validación

> Conserva únicamente la sección del modo solicitado. No completes celdas con cifras, tecnología, fechas o actores de ejemplo.

## A. Diagnóstico de sistema de información

| Elemento | Origen | Evidencia | Interpretación / derivación | Estado |
| --- | --- | --- | --- | --- |
| Objetivo | | | | |
| Entradas | | | | |
| Proceso / transformación | | | | |
| Salidas | | | | |
| Retroalimentación | | | | |
| Componentes y límite | | | | |

## B. Clasificación de capacidades

| Capacidad | Tipo(s) TPS/MIS/DSS/ESS/KMS/AI | Nivel o decisión si consta | Origen | Evidencia | Justificación / derivación | Estado |
| --- | --- | --- | --- | --- | --- | --- |

## C. Prefactibilidad

### C.1 Técnica

| Origen | Evidencia disponible | Brecha o riesgo | Derivación | Dato faltante | Dictamen |
| --- | --- | --- | --- | --- | --- |

### C.2 Económica

### C.2.1 Cuadro Condicional de Flujo de Fondos Proyectado
*(Completar únicamente si el usuario aportó horizonte temporal, tasa y valores de inversión)*

| Concepto Financiero | Año 0 (Inversión) | Año 1 | Año 2 | Año 3 |
|---|:---:|:---:|:---:|:---:|
| **Inversión Inicial (CAPEX)** | -{{$INVERSION}} | - | - | - |
| **Costos Operativos (OPEX)** | - | -{{$OPEX_1}} | -{{$OPEX_2}} | -{{$OPEX_3}} |
| **Beneficios Brutos Obtenidos** | - | +{{$BENEF_1}} | +{{$BENEF_2}} | +{{$BENEF_3}} |
| **Flujo de Fondos Neto ($F_t$)** | **-{{$INVERSION}}** | **{{$NETO_1}}** | **{{$NETO_2}}** | **{{$NETO_3}}** |
| **Flujo Neto Descontado (Tasa $k$)** | **-{{$INVERSION}}** | **{{$DESC_1}}** | **{{$DESC_2}}** | **{{$DESC_3}}** |

**Indicadores Financieros Calculados:**
- **VAN ($k = {{TASA}}\%$):** `$ {{VALOR_VAN}}` $\to$ {{Viable / No viable}}
- **TIR:** `{{VALOR_TIR}}\%` $\to$ {{Mayor / Menor que la tasa de corte}}
- **Período de Recupero (Payback):** `{{ANIOS}}` años
- **ROI:** `{{VALOR_ROI}}\%`


| Costo/beneficio | Tipo | Valor y moneda si constan | Origen | Fuente | Derivación / estado |
| --- | --- | --- | --- | --- | --- |

[Incluir cálculos financieros solo si fueron pedidos y existen datos suficientes.]

### C.3 Operativa

| Origen | Evidencia disponible | Impacto/aceptación | Derivación | Dato faltante | Dictamen |
| --- | --- | --- | --- | --- | --- |

### C.4 Dictamen consolidado

`FAVORABLE / CONDICIONADA / DESFAVORABLE / NO DETERMINADO`

Justificación: [traza a los tres dictámenes].

Condiciones o información necesaria: [lista].

## D. Contexto PUD

| Elemento o artefacto | Fase / flujo | Origen | Evidencia | Derivación / estado | Falta para decidir |
| --- | --- | --- | --- | --- | --- |

No incluir un cronograma salvo que el usuario lo pida y provea restricciones de calendario y estimaciones.

## Preguntas y límites

| ID | Afecta a | Pregunta o conflicto | Por qué importa | Estado |
| --- | --- | --- | --- | --- |

- Fuentes no disponibles: [lista o ninguna].
- Conclusiones derivadas pendientes: [lista o ninguna].
- Aspectos fuera de alcance: [lista].
