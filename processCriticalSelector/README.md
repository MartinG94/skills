# processCriticalSelector

Skill atómica especialista para la evaluación multicriterio, priorización matemática y selección determinista del **Proceso Crítico** a intervenir en la Etapa 1 del marco metodológico de Gestión y Mejora de Procesos (GMP).

---

## 1. Propósito General

En la metodología de Gestión y Mejora de Procesos (GMP), la intervención no puede dispersarse en múltiples áreas simultáneamente sin diluir recursos y foco. La selección del proceso crítico debe basarse en un análisis formal, cuantitativo y fundado en hechos fácticos.

`processCriticalSelector` implementa la matriz de decisión multicriterio oficial basada en los **5 factores de cátedra** (documentados en `SLI_U2_C01_Analisis_de_Proceso.pdf` y la Matriz 2 de Etapa 1 de la Planilla TPI 2026). Transforma el relevamiento inicial y la narrativa de la organización en una matriz ponderada con calificaciones objetivas, cálculo matemático estricto, orden de mérito justificado y delimitación de fronteras operativas.

### Principio de Atomicidad y Componibilidad
- **Como Skill Atómica (Building Block Especialista):** Puede ejecutarse de forma 100% aislada e independiente para priorizar procesos en cualquier empresa u organización, exigiendo únicamente una lista de procesos candidatos y el encuadre estratégico básico.
- **En Workbenches y Orquestadores:** Se integra en la Etapa 1 de `processWorkbench` y transfiere su entregable canónico (`seleccion_proceso.md`) a `processImprovementPlanner` para el Informe Técnico Maestro, y a `sipocBuilder`, `bpmnExtractor` y `processAuditor` para la apertura de la Etapa 2 (Diagnóstico AS-IS).

---

## 2. Arquitectura Interna del Paquete

- [`SKILL.md`](SKILL.md): Contrato operacional del agente (YAML frontmatter + progressive disclosure).
- [`README.md`](README.md): Documentación técnica y guía metodológica para desarrolladores/usuarios.
- [`templates/critical_selector_template.md`](templates/critical_selector_template.md): Plantilla canónica institucional para `seleccion_proceso.md`.
- [`scripts/validate_selection.py`](scripts/validate_selection.py): Validador CLI determinista de consistencia matemática, desempate y estructura.
- [`tests/test_validate_selection.py`](tests/test_validate_selection.py): Batería de 14 pruebas unitarias automatizadas del validador.
- [`examples/sample_seleccion_proceso.md`](examples/sample_seleccion_proceso.md): Ejemplo representativo validado (BioTrace Logística S.A.).

```
processCriticalSelector/
├── SKILL.md                                 # Contrato operacional del agente (YAML frontmatter + progressive disclosure)
├── README.md                                # Documentación técnica y guía metodológica para desarrolladores/usuarios
├── templates/
│   └── critical_selector_template.md        # Plantilla canónica institucional para 'seleccion_proceso.md'
├── scripts/
│   └── validate_selection.py                # Validador CLI determinista de consistencia matemática y estructura
├── tests/
│   └── test_validate_selection.py           # Batería de pruebas unitarias automatizadas del validador
└── examples/
    └── sample_seleccion_proceso.md          # Ejemplo representativo validado
```

---

## 3. Fundamento Metodológico y los 5 Criterios de Cátedra

La evaluación se estructura sobre los 5 factores normativos establecidos por la cátedra de Gestión y Mejora de Procesos (SLI_U2_C01):

| Factor | Denominación Oficial | Peso Normativo ($w_i$) | Porcentaje | Fundamento Metodológico (Cátedra GMP) |
|:---:|:---|:---:|:---:|:---|
| **$C_1$** | **Impacto en la Estrategia** | `0.25` | 25% | Elegir procesos que permitan alcanzar los objetivos organizacionales (oportunidades, competitividad, eficiencia). |
| **$C_2$** | **Tendencias del Entorno / Lógica Dominante del Servicio (SDL)** | `0.20` | 20% | Elegir procesos vinculados a tendencias globales, del sector y del mercado que establezcan un diferencial competitivo y potencien la servitización / co-creación de valor. |
| **$C_3$** | **Problemas Identificados y Oportunidades de Mejora** | `0.25` | 25% | Elegir procesos que impacten en la eficiencia, inversión, riesgos y costos de la organización (mermas, fallas, tiempos muertos, cuellos de botella). |
| **$C_4$** | **Cliente** | `0.20` | 20% | Elegir el proceso que permita satisfacer, mejorar o resolver requerimientos del cliente, cambios de preferencias y experiencia de servicio. |
| **$C_5$** | **Producto / Servicio** | `0.10` | 10% | Evaluar si el producto/servicio requiere rediseño, nuevas funcionalidades o es el núcleo de la entrega comercial de la organización. |
| **Total** | **Suma de Ponderaciones ($\sum w_i$)** | **`1.00`** | **100%** | **Cierre matemático estricto.** |

### Formulación Matemática
Para cada proceso candidato $p \in \{1, \dots, m\}$ evaluado en los criterios $i \in \{1, \dots, 5\}$ con calificaciones $C_{i,p} \in [1, 5]$:

$$S_p = \sum_{i=1}^{5} w_i \times C_{i,p}$$

Donde:
- $S_p$: Puntaje ponderado total del proceso candidato $p$.
- $w_i$: Ponderación del criterio $i$ ($\sum w_i = 1.00$).
- $C_{i,p}$: Calificación discreta entera (1 a 5) otorgada según la rúbrica oficial.

### Regla Objetiva de Desempate
En caso de empate en el puntaje total ($S_a = S_b$), la prioridad se resuelve mediante el siguiente orden jerárquico estricto:
1. Mayor puntaje en **$C_3$** (Problemas identificados y costos operativos: mayor urgencia de intervención).
2. Mayor puntaje en **$C_1$** (Impacto en la estrategia del negocio).
3. Mayor puntaje en **$C_4$** (Impacto directo en el cliente).

---

## 4. Prerequisitos de Entorno

- **Runtime de Validación:** Python 3.8 o superior (no requiere librerías externas de terceros; usa exclusivamente módulos de la biblioteca estándar `re`, `sys`, `pathlib`, `unittest`).
- **Compatibilidad de Plataformas:** Totalmente compatible con Windows (PowerShell / cmd), macOS y Linux.
- **Entorno Agéntico:** Compatible con Google Antigravity, Claude Code, Cursor y Windsurf.

---

## 5. Ejemplos de Invocación y Uso

### Caso Práctico: Distribuidora Logística "BioTrace Logística S.A."

**Contexto:** Empresa de logística farmacéutica con problemas en despacho de biológicos y mermas por ruptura de cadena de frío.

**Procesos Candidatos:**
1. P1: Recepción y Cuarentena Frigorífica
2. P2: Preparación de Pedidos (Picking) y Despacho Urgente
3. P3: Compras y Reposición de Envases Térmicos
4. P4: Facturación y Cobranzas

**Matriz Resultante:**

| ID | Proceso Candidato | C1 ($w=0.25$) | C2 ($w=0.20$) | C3 ($w=0.25$) | C4 ($w=0.20$) | C5 ($w=0.10$) | Puntaje Total ($S_p$) | Ranking | Decisión |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P2** | **Preparación de Pedidos y Despacho** | 5 | 4 | 5 | 5 | 5 | **4.80** | **#1** | **SELECCIONADO (Proceso Crítico)** |
| **P1** | Recepción y Cuarentena Frigorífica | 4 | 3 | 4 | 3 | 4 | **3.60** | #2 | No Seleccionado |
| **P4** | Facturación y Cobranzas | 3 | 3 | 3 | 3 | 2 | **2.90** | #3 | No Seleccionado |
| **P3** | Compras de Envases Térmicos | 3 | 2 | 3 | 1 | 3 | **2.40** | #4 | No Seleccionado |

**Cálculo de P2:**
$$S_{P2} = (0.25 \times 5) + (0.20 \times 4) + (0.25 \times 5) + (0.20 \times 5) + (0.10 \times 5) = 1.25 + 0.80 + 1.25 + 1.00 + 0.50 = 4.80$$

### Validación Automatizada del Entregable
Para verificar la consistencia matemática, desempate y estructura del archivo generado:

```bash
# Validar el entregable generado
python scripts/validate_selection.py seleccion_proceso.md

# Ejecutar el conjunto de pruebas unitarias automatizadas (14 tests)
python -m unittest tests/test_validate_selection.py
```

---

## 6. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs Requeridos)
- Perfil institucional de la organización (misión, visión, objetivos estratégicos).
- Inventario preliminar de 3 a 5 procesos candidatos clasificados en el Mapa de Procesos.
- Evidencias de fallas operativas, quejas de clientes, costos y oportunidades de digitalización/SDL.

### Salida Determinista Canónica (Output Contract)
- **Nombre de archivo unívoco:** `seleccion_proceso.md`
- **Contenido obligatorio:**
  1. Encuadre organizacional y contexto estratégico (Matriz 1 de Etapa 1 TPI).
  2. Inventario de procesos candidatos clasificados en Estratégicos, Principales/Misionales y Soporte.
  3. Factores normativos de cátedra y justificación del vector de ponderación.
  4. Matriz multicriterio ponderada con cálculo explícito de $S_p$ y ranking.
  5. Justificación detallada cuali-cuantitativa del proceso seleccionado.
  6. Análisis comparativo y justificación de descarte relativo de los demás procesos.
  7. Delimitación de fronteras y handoff formal a Etapa 2 de GMP (SIPOC, BPMN AS-IS, Auditoría).

---

## 7. Integración en el Pipeline GMP

```
[Etapa 1: Situación Actual]
       │
       ├── organizationAnalysis     ──> cadena_valor_virtual.md
       └── processCriticalSelector ──> seleccion_proceso.md
                                              │
       ┌──────────────────────────────────────┴──────────────────────────────────────┐
       ▼                                      ▼                                      ▼
[Etapa 2: SIPOC]                      [Etapa 2: BPMN AS-IS]                  [Etapa 2: Auditoría]
 sipocBuilder                          bpmnExtractor                          processAuditor
 ──> sipoc.md                          ──> bpd_as_is.bpmn                     ──> auditoria_as_is.md
```
