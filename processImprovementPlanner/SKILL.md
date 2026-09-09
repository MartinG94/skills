---
name: processImprovementPlanner
description: >-
  Orquesta la metodología completa de Gestión y Mejora de Procesos (GMP / ciclo PDCA) integrando
  las 4 etapas del proyecto sin dependencia de hojas de cálculo de Excel. Compila el Informe Técnico Maestro
  en Markdown (.md), construye el cronograma de implantación con diagramas de Gantt en Mermaid y genera
  la Matriz de Trazabilidad Integral de Extremo a Extremo (E1 Encuadre y Criterios ➔ E2 Auditoría y FODA ➔
  E3 CAME y Acciones de Valor ➔ E4 TO-BE, KPIs y Gantt).
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.0.0","category":"orchestrator","platforms":["windows","macos","linux"]}
---

# Process Improvement Planner & PDCA Orchestrator

Orquestador metodológico del ciclo de mejora de procesos organizacionales. Asegura la continuidad lógica y la trazabilidad integral de punta a punta entre las 4 etapas de cátedra, compilando la entrega final en documentos Markdown versionables y diagramas de Gantt visuales listos para publicación.

---

## Principios y Restricciones Metodológicas

1. **Cero Dependencia de Excel:** Todas las matrices, ponderaciones, cronogramas y trazabilidades se construyen directamente en tablas Markdown limpias y código de diagrama Mermaid (`gantt`), eliminando macros, archivos binarios y dependencias propietarias.
2. **Gobernanza Secuencial de Etapas:**
   - No se modela el AS-IS de Etapa 2 sin haber justificado la selección del proceso en Etapa 1.
   - No se formula el CAME de Etapa 3 sin los hallazgos de auditoría de Etapa 2.
   - No se diseña el TO-BE de Etapa 4 sin que las Acciones de Valor hayan superado el Filtro de Restricciones Operativas.
3. **Invariante de Trazabilidad Total ($E_1 \rightarrow E_2 \rightarrow E_3 \rightarrow E_4$):**
   Todo cambio introducido en el proceso TO-BE debe rastrearse inequívocamente hacia una Acción de Valor (E3), originada en un cruce CAME (E3), justificada por una debilidad de auditoría (E2) y alineada a los criterios estratégicos (E1).

---

## Orquestación del Ecosistema de Skills

`processImprovementPlanner` coordina la intervención de las skills especialistas según la fase del proyecto:

```
[Etapa 1: Encuadre & Selección] ────> processWorkbench
                                             │
[Etapa 2: Diagnóstico AS-IS]    ────> processAuditor + bpmnExtractor
                                             │
[Etapa 3: CAME & Acciones]      ────> processWorkbench
                                             │
[Etapa 4: TO-BE, KPIs & Plan]   ────> bpmnExtractor + kpiDesigner + diagramStudio
                                             │
                                             ▼
                      [Informe Maestro Consolidado & Gantt]
```

---

## Flujo de Trabajo para el Entregable Final

1. **Validación de Entradas Previas:**
   - Comprobá la disponibilidad de las matrices de Etapas 1, 2 y 3.
2. **Generación del Cronograma Gantt (Mermaid):**
   - Utilizá [templates/gantt_template.mmd](templates/gantt_template.mmd).
   - Estructurá las fases canónicas: 1) Diseño Detallado; 2) Configuración TI; 3) Piloto & Capacitación; 4) Despliegue General; 5) Medición de KPIs y Cierre.
   - Definí hitos de control claros (`milestone`).
3. **Construcción de la Matriz de Trazabilidad Integral:**
   - Utilizá [templates/e1_e4_traceability_matrix.md](templates/e1_e4_traceability_matrix.md).
   - Auditá que no existan eslabones rotos ni acciones huérfanas.
4. **Ensamblado del Informe Maestro:**
   - Compilá las secciones siguiendo [templates/master_report_template.md](templates/master_report_template.md).

---

## Contrato de Salida

El orquestador produce:
1. `Informe Técnico Consolidado`: Documento maestro en `.md` que reúne las 4 etapas con formato ejecutivo formal.
2. `Diagrama de Gantt Mermaid`: Bloque de código ```mermaid de tipo `gantt` renderizable en cualquier visualizador Markdown.
3. `Matriz de Trazabilidad E1 ➔ E4`: Tabla Markdown completa con verificación de consistencia.
