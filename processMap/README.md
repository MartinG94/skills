# processMap

Habilidad atómica especialista para la construcción, estructuración, diagramación visual y validación del **Mapa de Procesos Institucional** y la **Selección Multicriterio del Proceso Crítico**, correspondiente a la **Etapa 1 (Situación Actual y Encuadre)** de la metodología de **Gestión y Mejora de Procesos (GMP)**.

Basada estrictamente en los materiales oficiales de cátedra:
- `SLI_U1_C03_Mapa_de_Procesos.pdf` (Arquitectura institucional de procesos en 3 niveles).
- `SLI_U2_C01_Seleccion_Proceso.pdf` (Matriz multicriterio de los 5 factores normativos).
- `PlanillaMATRICES-TPI 2026 con ejemplo.xlsx` (Hoja *'Etapa 1 Situación actual'*, Matriz 2).

---

## 1. Propósito General

En la Etapa 1 de GMP, la organización bajo estudio debe mapear sus procesos de negocio para comprender su arquitectura operacional y el flujo de valor, y simultáneamente seleccionar con rigor analítico y cuantitativo cuál es el **proceso crítico** que debe ser intervenido y rediseñado en las siguientes etapas.

`processMap` consolida de forma integral ambas tareas en un único flujo de trabajo cohesivo:
1. **Identificar y categorizar los procesos en 3 niveles canónicos:**
   - **Procesos Estratégicos (`PE-XX`):** Dirección, políticas, planificación y gobierno.
   - **Procesos Operativos / Misionales / Clave (`PO-XX`):** Cadena de valor primaria que crea valor directo para el cliente.
   - **Procesos de Soporte / Apoyo (`PS-XX`):** Habilitadores de recursos humanos, tecnológicos, edilicios y financieros.
2. **Definir objetivos específicos y dueños:** Cada proceso documenta su objetivo individual formal con verbo en infinitivo y su área o rol responsable.
3. **Mapear el flujo de valor:** Conecta las necesidades y requisitos del cliente (a la izquierda) con la entrega de satisfacción y valor co-creado (a la derecha).
4. **Generar el diagrama visual integrado:** Produce el código Mermaid in-line estructurado por subgrafos horizontales, destacando visualmente el proceso crítico seleccionado.
5. **Evaluar con la matriz multicriterio de los 5 factores:** Aplica los factores normativos de cátedra ($C_1$ Estrategia, $C_2$ Tendencias/SDL, $C_3$ Problemas/Costos, $C_4$ Cliente, $C_5$ Producto/Servicio), con pesos sumando 1.00, escala 1 a 5 y regla de desempate jerárquico.
6. **Dictaminar el Proceso Crítico y documentar el Porqué:** Emite la justificación técnica exhaustiva basada en causas raíz, evidencias del caso, dolores del cliente y retorno de inversión metodológica.

---

## 2. Contrato de Entrada y Salida

### Entradas (Inputs)
- Descripción de la organización, rubro, actividad principal, misión, visión y objetivos SMART (desde `organizationAnalysis`).
- Relevamiento de áreas funcionales, actividades operativas y servicios prestados.
- Requisitos normativos, dolores operativos, costos de no-calidad y demandas de los clientes/usuarios.

### Salida Determinista (Output)
La skill genera y persiste obligatoriamente el entregable en el archivo canónico:
```text
mapa_procesos.md
```
*(Soporta la exportación complementaria a `seleccion_proceso.md` en caso de invocaciones específicas o retrocompatibilidad).*

---

## 3. Arquitectura Interna del Módulo

```text
processMap/
├── SKILL.md                               # Contrato operacional consumido por el LLM (YAML Frontmatter + Flujo v2.0)
├── README.md                              # Documentación para desarrolladores y usuarios humanos
├── references/
│   ├── process_classification_guide.md    # Guía taxonómica de procesos estratégicos, misionales y de soporte
│   └── critical_factors_framework.md      # Marco normativo de los 5 factores de selección, rúbrica y desempate
├── templates/
│   └── process_map_template.md            # Plantilla institucional normalizada para mapa_procesos.md
├── examples/
│   └── mapa_procesos_ejemplo.md           # Caso canónico de cátedra validado (Universidad Privada)
├── scripts/
│   └── validate_process_map.py            # Validador determinista CLI en Python
└── tests/
    └── test_validate_process_map.py       # Suite completa de pruebas unitarias automatizadas (9 tests)
```

---

## 4. Uso del Validador CLI

Para auditar la conformidad metodológica de cualquier archivo `mapa_procesos.md`:

```bash
# Validación con informe legible en consola
python skills/processMap/scripts/validate_process_map.py ruta/hacia/mapa_procesos.md

# Validación con volcado JSON estructurado para pipelines
python skills/processMap/scripts/validate_process_map.py ruta/hacia/mapa_procesos.md --json
```

### Reglas Verificadas por el Validador:
1. Presencia de las 5 secciones canónicas obligatorias.
2. Diagrama visual Mermaid estructurado en 3 niveles con nodos de clientes y resaltado del proceso crítico.
3. Existencia de procesos en los 3 niveles canónicos (`PE-XX`, `PO-XX`, `PS-XX`) con objetivos definidos.
4. Cierre matemático de los pesos de evaluación ($\sum w_i = 1.00 \pm 0.001$).
5. Calificaciones discretas en rango $[1..5]$ y cálculo verificado de $S_p = \sum w_i C_i$.
6. Declaración unívoca del Proceso Crítico Seleccionado coincidente con el ganador del ranking.
7. Justificación técnica exhaustiva con sustento multifactorial ($\ge 80$ palabras).

---

## 5. Ejecución de Pruebas Unitarias

Para ejecutar la batería de tests unitarios automatizados:

```bash
python -m unittest discover -s skills/processMap/tests -p "test_*.py"
```

---

## 6. Retrocompatibilidad y Aliases

Esta skill unificada responde tanto a los comandos propios de mapa de procesos como a las invocaciones históricas de selección de proceso crítico registradas en `skill-aliases.json`:
- `/processMap`, `/process-map`, `/processMapBuilder`, `/mapaProcesos`
- `/processCriticalSelector`, `/process-critical-selector`, `/criticalSelector`, `/seleccionProceso`
