---
name: kpiDesigner
description: >-
  Diseña, estructura, estandariza y audita sistemas de medición, métricas e Indicadores Clave de
  Desempeño (KPIs) en cualquier dominio técnico u organizacional: Operaciones y Procesos (GMP, Lean, Six Sigma,
  O1 Eficacia vs O2 Eficiencia, Lead Time, Scrap, OEE), Negocio y Estrategia (Balanced Scorecard, OKRs, ROI, EBITDA),
  Ingeniería de Software y DevOps (DORA, SRE/SLO/SLI, Error Budgets) y Producto/UX (HEART, North Star, Churn, LTV).
  Estandariza la sintaxis SMART obligatoria, consistencia dimensional matemática y trazabilidad a la fuente primaria del dato.
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.0.0","category":"metrics","platforms":["windows","macos","linux"]}
---

# KPI & Metrics Designer (Universal Measurement Studio)

Diseña, formula y audita indicadores de desempeño y tableros de control con rigor matemático, gobernanza de datos y alineación estratégica. Aplica en proyectos de optimización de procesos (Etapa 4 de GMP), arquitectura de software, ingeniería de confiabilidad (SRE) y gestión de producto.

---

## Principios de Rigor Metodológico

1. **Sintaxis SMART Canónica Obligatoria:**
   Todo objetivo de indicador debe formularse con la estructura:
   $$[\text{Verbo en Infinitivo}] + [\text{Variable/Métrica}] + [\text{de Línea Base a Meta}] + [\text{Plazo o Fecha Límite}]$$
2. **Consistencia Dimensional de Fórmulas:**
   Toda fórmula matemática debe declarar explícitamente sus unidades en numerador y denominador (ej. horas/pedido, fallas/despliegue, USD/cliente).
3. **Trazabilidad a Fuente Primaria (Data Provenance):**
   Ningún KPI es válido sin declarar el evento, log, tabla de base de datos o transacción exacta donde se origina el dato en origen.
4. **Distinción Funcional O1 vs. O2:**
   - **O1 (Resultado / Eficacia):** Mide el impacto final sobre el cliente o el negocio (ej. OTIF, NPS, Churn).
   - **O2 (Proceso / Eficiencia):** Mide el flujo interno, velocidad, desperdicio y costo (ej. Lead Time, Scrap, MTTR).

---

## Catálogo de Dominios Soportados

| Dominio | Marcos Metodológicos | Indicadores Canónicos |
|---|---|---|
| **Operaciones y Procesos** | GMP, Lean Manufacturing, Six Sigma | Lead Time, Cycle Time, OTIF, Tasa de Merma (Scrap), First Pass Yield, OEE, Takt Time |
| **Negocio y Estrategia** | Balanced Scorecard (Kaplan & Norton), OKRs | ROI, EBITDA, Margen Operativo, CAC, LTV, Horas de Capacitación, Cumplimiento de Metas OKR |
| **Software & DevOps** | DORA Metrics, Google SRE | Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR, SLI/SLO/SLA, Error Budget |
| **Producto y UX** | HEART Framework (Google), Growth | CSAT, NPS, Adopción de Onboarding, Retención por Cohortes (30/60/90 días), Éxito de Tareas, North Star |

---

## Flujo de Trabajo

1. **Definir el Propósito de Medición:** Vincular el KPI con una Acción de Valor (`processWorkbench`), un atributo de calidad o un driver de negocio.
2. **Redactar el Objetivo SMART:** Redactar la meta siguiendo la fórmula canónica.
3. **Construir la Ficha Técnica:** Completar los campos de [templates/kpi_dictionary_template.md](templates/kpi_dictionary_template.md).
4. **Validar la Especificación:**
   Ejecutá el script de validación determinista:
   ```bash
   python3 kpiDesigner/scripts/validate_kpi.py catalogo_kpis.json
   # O probar un objetivo SMART individual:
   python3 kpiDesigner/scripts/validate_kpi.py --test-smart "Reducir el Lead Time de 48h a 4h para el 31 de diciembre"
   ```

---

## Contrato de Salida

Entregá para cada indicador diseñado:
1. `Ficha Técnica del KPI`: Tabla estructurada con ID, nombre, dominio, clasificación (O1/O2), objetivo SMART, fórmula dimensional, unidad, polaridad, línea base, meta, frecuencia y fuente primaria.
2. `Justificación y Alineación`: Explicación de cómo el indicador tracciona el objetivo y mitiga el riesgo detectado.
3. `Protocolo de Gobernanza`: Responsable/dueño del dato y contingencia en caso de desvío (umbrales semafóricos).
