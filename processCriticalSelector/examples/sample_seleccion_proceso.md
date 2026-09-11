# Matriz de Selección Ponderada del Proceso Crítico (GMP Etapa 1)

## 1. Encuadre Organizacional y Contexto Estratégico

- **Organización / Empresa:** BioTrace Logística S.A.
- **Sector / Rubro / Actividad:** Operador Logístico Farmacéutico y Distribución de Cadena de Frío
- **Ámbito / Alcance del Negocio:** Regional y Nacional (Centros de distribución en Córdoba, Rosario y Buenos Aires)
- **Tipo / Modelo de Negocio / Estructura:** Empresa privada de servicios B2B, estructura matricial con Dirección de Operaciones, Logística y Calidad Farmacéutica (GMP/ANMAT).
- **Misión:** Garantizar la custodia térmica ininterrumpida y trazabilidad de extremo a extremo para medicamentos biológicos, vacunas y reactivos críticos.
- **Visión:** Ser el operador logístico de referencia en Argentina por confiabilidad, innovación tecnológica y co-creación de valor bajo la Lógica Dominante del Servicio (SDL).
- **Propuesta de Valor:** Distribución y cross-docking refrigerado con trazabilidad IoT en tiempo real, alertas preventivas y certificación de cadena de frío.
- **Objetivos Estratégicos Relevantes:**
  - **OE-1:** Reducir incidentes de desvío térmico y mermas a menos del 0.05% anual.
  - **OE-2:** Brindar visibilidad y alertas tempranas en tiempo real al 100% de los clientes farmacéuticos para co-crear valor (SDL).
  - **OE-3:** Optimizar tiempos de ciclo en picking y despacho reduciendo el tiempo de preparación a menos de 40 minutos por orden.
- **Propósito de la Intervención GMP:** Eliminar cuellos de botella y descontrol de temperatura en el proceso clave de preparación y despacho para recuperar la satisfacción del cliente y reducir penalizaciones.

---

## 2. Inventario de Procesos Candidatos

| ID | Proceso Candidato | Clasificación en Mapa de Procesos | Evento Disparador (Inicio) | Resultado Entregado (Fin) | Responsable / Área Líder |
|:---:|:---|:---:|:---|:---|:---|
| **P1** | Recepción y Almacenamiento Frigorífico | Proceso Principal (Misional) | Arribo de camión térmico del laboratorio | Lote verificado e ingresado a cámara matriz | Almacén Central |
| **P2** | Preparación de Pedidos (Picking) y Despacho Urgente | Proceso Principal (Misional) | Orden de entrega confirmada en sistema | Pedido entregado conforme en destino con planilla térmica | Operaciones y Despacho |
| **P3** | Compras y Reposición de Envases Térmicos | Proceso de Soporte | Punto de reorden de insumos alcanzado | Cajas térmicas y geles calificados en stock | Compras y Suministros |
| **P4** | Facturación y Conciliación de Cobranzas | Proceso de Soporte | Remito conformado digitalizado | Cobro imputado y cuenta corriente actualizada | Administración y Finanzas |

---

## 3. Factores de Evaluación Normativos de Cátedra y Ponderación

**Escala de Calificación:** 1 (Muy Bajo / Impacto insignificante) a 5 (Muy Alto / Impacto Crítico).

| Código | Factor de Cátedra (SLI_U2_C01) | Peso ($w_i$) | Porcentaje | Justificación del Peso en el Negocio |
|:---:|:---|:---:|:---:|:---|
| **C1** | **Impacto en la Estrategia** | `0.25` | 25% | Prioriza procesos clave para cumplir OE-1, OE-2 y OE-3, ventaja competitiva y supervivencia. |
| **C2** | **Tendencias del Entorno / Lógica Dominante del Servicio (SDL)** | `0.20` | 20% | Evalúa la servitización, integración IoT y co-creación de valor donde el cliente monitorea su envío. |
| **C3** | **Problemas Identificados y Oportunidades de Mejora** | `0.25` | 25% | Mide la urgencia operativa por costos de no-calidad, mermas de frío, demoras y reclamos. |
| **C4** | **Cliente** | `0.20` | 20% | Refleja la visibilidad directa, cumplimiento de SLAs prometidos y percepción de calidad del destinatario. |
| **C5** | **Producto / Servicio** | `0.10` | 10% | Valora la centralidad del proceso en la oferta nuclear de logística térmica especializada. |
| **Total** | **Suma de Ponderaciones ($\sum w_i$)** | **`1.00`** | **100%** | **Condición matemática de cierre estricto cumplida.** |

---

## 4. Matriz Multicriterio de Selección Ponderada

| ID | Proceso Candidato | C1: Estrategia ($w=0.25$) | C2: Tendencias/SDL ($w=0.20$) | C3: Problemas/Costos ($w=0.25$) | C4: Cliente ($w=0.20$) | C5: Producto ($w=0.10$) | Puntaje Ponderado Total ($S_p$) | Ranking | Decisión Metodológica |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P2** | Preparación de Pedidos y Despacho Urgente | 5 | 4 | 5 | 5 | 5 | 4.80 | **#1** | **SELECCIONADO (Proceso Crítico)** |
| **P1** | Recepción y Almacenamiento Frigorífico | 4 | 3 | 4 | 3 | 4 | 3.60 | **#2** | No Seleccionado |
| **P4** | Facturación y Conciliación de Cobranzas | 3 | 3 | 3 | 3 | 2 | 2.90 | **#3** | No Seleccionado |
| **P3** | Compras y Reposición de Envases Térmicos | 3 | 2 | 3 | 1 | 3 | 2.40 | **#4** | No Seleccionado |

*Nota de Cálculo:* $S_p = (0.25 \times C_1) + (0.20 \times C_2) + (0.25 \times C_3) + (0.20 \times C_4) + (0.10 \times C_5)$.

---

## 5. Justificación Cualitativa y Cuantitativa del Proceso Seleccionado

### Proceso Crítico Elegido: Preparación de Pedidos (Picking) y Despacho Urgente (Puntaje Total: 4.80)

- **Sustento en C1 (Impacto en la Estrategia - Nota: 5):**
  Alineado directamente con los tres objetivos estratégicos OE-1, OE-2 y OE-3. Representa la promesa nuclear de entrega urgente garantizada; una falla aquí compromete directamente la continuidad comercial de BioTrace.
- **Sustento en C2 (Tendencias del Entorno / SDL - Nota: 4):**
  La servitización farmacéutica exige telemetría continua de temperatura y co-creación de valor donde clínicas y laboratorios consultan la ubicación del vehículo y el estado térmico en tiempo real.
- **Sustento en C3 (Problemas Identificados y Oportunidades de Mejora - Nota: 5):**
  Concentra el 82% de las pérdidas operativas del último ejercicio: rotura de empaques térmicos por manipulación apresurada, cuellos de botella en la zona de pre-cámara con demoras de hasta 120 minutos y costos anuales de $48,000 USD por productos descalificados.
- **Sustento en C4 (Cliente - Nota: 5):**
  Genera el 88% de los reclamos formales y amenazas de rescisión contractual por parte de sanatorios y laboratorios debido a arribos fuera de ventana horaria o remitos discordantes.
- **Sustento en C5 (Producto / Servicio - Nota: 5):**
  Constituye la esencia misma del servicio brindado: la entrega confiable y calificada de medicamentos biológicos bajo estricta cadena de frío.

**Conclusión de Priorización:**
Preparación de Pedidos y Despacho Urgente alcanza el puntaje más alto (4.80/5.00), superando por 1.20 puntos al proceso más cercano. Su optimización en el marco de GMP producirá el mayor impacto en la calidad del servicio, reducción de costos ocultos y retención de clientes.

---

## 6. Análisis Comparativo y Razones de Descarte Relativo

| ID | Proceso Descartado | Puntaje ($S_p$) | Brecha vs. Seleccionado ($\Delta$) | Criterio Determinante de Descarte Relativo |
|:---:|:---|:---:|:---|:---|
| **P1** | Recepción y Almacenamiento Frigorífico | 3.60 | -1.20 | Aunque relevante, sus protocolos de descarga y control de temperatura son estables y presentan baja tasa de reclamos. |
| **P4** | Facturación y Conciliación | 2.90 | -1.90 | Proceso administrativo transaccional de soporte sin impacto directo en la mercadería física ni urgencia médica. |
| **P3** | Compras y Reposición de Envases | 2.40 | -2.40 | Proceso interno de aprovisionamiento de soporte sin visibilidad ante el cliente externo final. |

---

## 7. Delimitación de Fronteras y Handoff a Etapa 2 de GMP

El proceso seleccionado pasa formalmente a la **Etapa 2 (Diagnóstico AS-IS y Modelado)**:

- **Nombre Institucional del Proceso:** Preparación de Pedidos (Picking) y Despacho Urgente
- **Frontera Inicial (Disparador / Input inicial):** Confirmación y liberación de la orden de pedido en el sistema WMS/ERP.
- **Frontera Final (Entregable / Output final):** Medicamento biológico entregado en punto de destino con remito conformado y registro de temperatura firmado conforme por el director técnico de la farmacia/clínica.
- **Unidades / Roles Involucrados:** Operador de Picking Frío, Verificador de Calidad Térmica, Chofer de Reparto Frigorífico, Encargado de Expedición.
- **Artefactos Inmediatos a Desarrollar en Etapa 2:**
  1. `sipoc.md`: Matriz SIPOC con requisitos de entrada/salida (`sipocBuilder`).
  2. `diagramStudio` / `bpmnExtractor`: BPD AS-IS descriptivo/operacional en BPMN 2.0.
  3. `processAuditor`: Auditoría forense de los 4 ejes (Control Interno COSO, Formularios/Ruta documental, Factores Humanos, Silos TI).
