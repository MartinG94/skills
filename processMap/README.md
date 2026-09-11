# processMap

Habilidad atómica especialista para la construcción, estructuración, diagramación y validación del **Mapa de Procesos Institucional**, correspondiente a la **Etapa 1 (Situación Actual y Encuadre)** de la metodología de **Gestión y Mejora de Procesos (GMP)**.

Basada estrictamente en la diapositiva oficial de cátedra `SLI_U1_C03_Mapa_de_Procesos.pdf` y la Matriz 2 de la hoja *'Etapa 1 Situación actual'* de la `PlanillaMATRICES-TPI 2026 con ejemplo.xlsx`.

---

## 1. Propósito General

En la Etapa 1 de GMP, la organización bajo estudio debe mapear sus procesos de negocio para comprender su arquitectura operacional y el flujo de valor antes de abordar la selección y el diagnóstico del proceso crítico.

`processMap` permite:
1. **Identificar y categorizar los procesos:** Clasifica el inventario completo en los **3 niveles canónicos de cátedra**:
   - **Procesos Estratégicos (`PE-XX`):** Dirección, políticas, planificación y gobierno.
   - **Procesos Operativos / Misionales / Clave (`PO-XX`):** Cadena de valor primaria que crea valor directo para el cliente.
   - **Procesos de Soporte / Apoyo (`PS-XX`):** Habilitadores de recursos humanos, tecnológicos, edilicios y financieros.
2. **Definir objetivos específicos alineados:** Cada proceso documenta su objetivo individual formal con verbo en infinitivo, estableciendo su aporte al propósito organizacional.
3. **Mapear el flujo de valor:** Conecta las necesidades y requisitos del cliente (a la izquierda) con la entrega de satisfacción y valor co-creado (a la derecha).
4. **Generar el diagrama visual integrado:** Produce el código Mermaid in-line estructurado por subgrafos horizontales, compatible con la exportación y edición avanzada en diagrams.net a través de `diagramStudio`.
5. **Preseleccionar los candidatos críticos:** Suministra los procesos operativos candidatos para su pase a la Matriz Multicriterio de Decisión Ponderada (`processCriticalSelector`).

---

## 2. Contrato de Entrada y Salida

### Entradas (Inputs)
- Descripción de la organización, rubro, actividad principal y modelo de negocio (desde `organizationAnalysis`).
- Relevamiento de áreas funcionales, actividades operativas y servicios prestados.
- Requisitos normativos y demandas de los clientes/usuarios.

### Salida Determinista (Output)
La skill genera y persiste obligatoriamente el entregable en el archivo canónico:
```text
mapa_procesos.md
```
Ubicado en la raíz del proyecto o directorio de trabajo del usuario.

---

## 3. Arquitectura Interna del Módulo

```text
processMap/
├── SKILL.md                               # Contrato operacional consumido por el LLM (YAML Frontmatter + Flujo)
├── README.md                              # Documentación para desarrolladores y usuarios humanos
├── references/
│   └── process_classification_guide.md    # Guía taxonómica de procesos estratégicos, misionales y de soporte
├── templates/
│   └── process_map_template.md            # Plantilla institucional normalizada para mapa_procesos.md
├── examples/
│   └── mapa_procesos_ejemplo.md           # Caso canónico de cátedra validado (Universidad Privada)
├── scripts/
│   └── validate_process_map.py            # Validador determinista CLI en Python
└── tests/
    └── test_validate_process_map.py       # Suite de pruebas unitarias automatizadas
```

---

## 4. Validación Determinista (CLI)

Para auditar la conformidad de cualquier entregable `mapa_procesos.md`:

```bash
# Validación estándar por consola
python "skills/processMap/scripts/validate_process_map.py" "ruta/hacia/mapa_procesos.md"

# Validación estructurada en JSON
python "skills/processMap/scripts/validate_process_map.py" "ruta/hacia/mapa_procesos.md" --json
```

### Reglas Validadas por el Script
1. Presencia de las 5 secciones obligatorias de cátedra.
2. Inclusión de bloque de diagrama visual en Mermaid (`flowchart`) con subgrafos.
3. Existencia de al menos 2 procesos por cada nivel canónico (`PE-XX`, `PO-XX`, `PS-XX`).
4. Especificación de objetivos para cada proceso individual.
5. Presencia de nodos de requisitos de entrada y satisfacción de salida.
6. Enlace a la preselección de procesos para `seleccion_proceso.md`.

---

## 5. Ejecución de Pruebas Unitarias

```bash
python "skills/processMap/tests/test_validate_process_map.py"
```
Todas las pruebas unitarias deben reportar `OK`.
