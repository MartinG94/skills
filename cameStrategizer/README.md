# cameStrategizer

Skill atómica para la construcción, estructuración, auditoría y validación de la **Matriz CAME** (Corregir, Afrontar, Mantener, Explotar) en la Etapa 3 de Gestión y Mejora de Procesos (GMP). Formula cruces estratégicos rigurosos entre factores internos y externos bajo las reglas de oro de cátedra (*SLI_U3_C04* y *PlanillaMATRICES-TPI 2026 - Etapa 3 Matriz 1*) y genera de forma determinista el entregable `came.md`.

---

## 1. Propósito General

En la metodología de Gestión y Mejora de Procesos (ciclo PDCA), la Matriz CAME constituye la **hoja de ruta metodológica donde el diagnóstico se convierte en intervención** (*FODA: ¿Dónde estamos? ➔ CAME: ¿Qué vamos a hacer?*).

`cameStrategizer` resuelve la desconexión metodológica habitual donde las propuestas de mejora surgen de forma intuitiva o desconectada de la auditoría. Asegura que:
- **Toda estrategia tenga procedencia comprobable:** Cada decisión nace de un cruce formal explícito entre factores internos ($F, D$) y factores del entorno ($O, A$) con citación obligatoria de IDs (ej. `F2 x O3`).
- **Se cubran los cuatro cuadrantes canónicos:** 
  - **FO (Ofensiva):** Mantener Fortalezas + Explotar Oportunidades (posicionamiento y ventajas competitivas).
  - **FA (Defensiva):** Mantener Fortalezas + Afrontar Amenazas (gestión de riesgos y blindaje operativo).
  - **DO (Reorientación):** Corregir Debilidades + Explotar Oportunidades (inversión, digitalización y reingeniería).
  - **DA (Supervivencia):** Corregir Debilidades + Afrontar Amenazas (control de daños y mitigación de crisis).
- **Se formulen propuestas de valor con procesos involucrados:** Cada cruce define su enunciado estratégico, su iniciativa operativa concreta (con palancas de cambio: Automatizar/Digitalizar, Eliminar/Simplificar, Modificar/Rediseñar, Crear/Incorporar), los procesos impactados y la expectativa del stakeholder que satisface (puente directo hacia `valueActionsBuilder` y `processImprovementPlanner`).
- **El entregable sea determinista:** Genera invariablemente el archivo `came.md`.

---

## 2. Arquitectura Interna

```
cameStrategizer/
├── SKILL.md                              # Contrato operativo para el agente inteligente
├── README.md                             # Documentación técnica para el desarrollador y analista
├── templates/                            # Plantillas estandarizadas de entrega
│   └── came_matrix_template.md           # Estructura canónica del entregable came.md
├── scripts/                              # Herramientas auxiliares de verificación
│   └── validate_came.py                  # Validador determinista CLI de matrices CAME
└── tests/                                # Pruebas unitarias automatizadas
    └── test_came_strategizer.py          # Suite de verificación de reglas de cátedra
```

---

## 3. Prerequisitos de Entorno

- **Runtime:** Python 3.10 o superior (para ejecutar el validador CLI `validate_came.py` y los tests).
- **Librerías estándar:** No requiere paquetes externos (`pip`), utiliza únicamente módulos estándar (`re`, `sys`, `json`, `argparse`, `pathlib`, `unittest`).
- **Visor Markdown:** Compatible con cualquier visor estándar (VS Code, Obsidian, GitHub, GitLab).

---

## 4. Ejemplos de Invocación y Uso

### Invocación Rápida desde el Agente
```markdown
Usuario: "Toma la matriz FODA elaborada para el proceso de Admisión y genera la matriz CAME estratégica con sus cruces formales."

Acción del Agente:
1. Lee foda.md e identifica los factores F1..Fn, D1..Dn, O1..On, A1..An.
2. Construye los cruces para FO, FA, DO y DA asociando los IDs exactos.
3. Guarda el entregable deterministamente en came.md.
4. Ejecuta: python cameStrategizer/scripts/validate_came.py came.md
```

### Ejemplo de Cruce y Salida Generada (Basado en Caso de Cátedra)

A partir de los factores de la institución:
- `F2`: Infraestructura tecnológica y edilicia adecuada y moderna.
- `D1`: Control manual de requisitos y carga de datos duplicada en admisiones.
- `O3`: Demanda creciente de educación superior continua y trayectos cortos flexibles.
- `A1`: Competidores low-cost y plataformas educativas 100% online.

Se formulan los cruces canónicos:

| Tipo CAME | Cruce IDs | Enunciado Estratégico | Propuesta de Valor / Acción Concreta | Procesos Involucrados | Alineación / Stakeholder |
|---|---|---|---|---|---|
| **FO (Ofensiva)** | `F2 x O3` | Ampliar la oferta académica desarrollando programas innovadores y atractivos adaptados a la demanda creciente | CREAR: Estructuración y despliegue de Trayectos de Especialización Cortos con matriculación digital | Académica, Admisiones, Calidad | Objetivo: Crecimiento de matrícula. Stakeholder: Alumnos (flexibilidad) |
| **DO (Reorientación)** | `D1 x O3` | Erradicar la carga manual de inscripciones adoptando una pasarela digital de cobro y validación automática | AUTOMATIZAR: Portal de auto-enrolamiento con validación en tiempo real de documentación | Admisiones, Sistemas, Cobranzas | Objetivo: Reducción de costos de enrolamiento. Stakeholder: Aspirantes |
| **FA (Defensiva)** | `F2 x A1` | Diferenciarse frente a plataformas virtuales low-cost destacando el valor de los laboratorios físicos | INCREMENTAR: Talleres prácticos híbridos con certificación presencial de competencias | Extensión, Docencia, Marketing | Objetivo: Posicionamiento de calidad. Stakeholder: Empresas empleadoras |
| **DA (Supervivencia)** | `D1 x A1` | Agilizar los tiempos de respuesta de inscripción para frenar la deserción hacia competidores ágiles | ELIMINAR: Control manual de legajos y verificación física de aranceles en ventanilla | Mesa de Entradas, Tesorería | Objetivo: Tasa de conversión de inscritos. Stakeholder: Dirección Financiera |

### Validación CLI Determinista
```bash
# Validar el archivo came.md generado:
python cameStrategizer/scripts/validate_came.py came.md

# Salida esperada:
# [OK] Archivo 'came.md' verificado exitosamente.
# [OK] Cuadrante FO: 2 cruces detectados.
# [OK] Cuadrante FA: 2 cruces detectados.
# [OK] Cuadrante DO: 2 cruces detectados.
# [OK] Cuadrante DA: 2 cruces detectados.
# [OK] Total de estrategias válidas: 8. Citación de IDs: 100% conforme.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entrada (Input)
- Archivo `foda.md` o sección FODA de un informe de auditoría:
  - Factores clasificados en Fortalezas ($F$), Debilidades ($D$), Oportunidades ($O$) y Amenazas ($A$).
  - Identificadores alfanuméricos asignados (`F1`, `F2`, `D1`, `D2`, `O1`, `O2`, `A1`, `A2`).

### Salida (Output)
- Archivo canónico obligatorio: `came.md`.
- Secciones requeridas:
  1. `Encuadre y Metadatos`: Proceso analizado, fecha, equipo, documento fuente.
  2. `Registro de Factores de Entrada`: Tabla normalizada de $F, D, O, A$ con descripción fáctica.
  3. `Matriz Conceptual CAME`: Cuadrantes 2x2 (*SLI_U3_C04*).
  4. `Matriz CAME Consolidada`: Tabla formal con columnas: ID Estrategia, Tipo CAME, Cruce de Factores (IDs), Descripción de Factores, Enunciado Estratégico, Acción de Mejora Concreta (Propuesta de Valor), Procesos Involucrados y Alineación Estratégica.
  5. `Síntesis y Handoff`: Balance cuantitativo de cuadrantes y canalización hacia la matriz EERR (`acciones_valor.md`).

---

## 6. Compuertas de Calidad y Reglas de Oro de Cátedra

| Criterio | Pregunta de Verificación | Estado Requerido |
|---|---|:---:|
| **Determinismo de Archivo** | ¿El archivo se guardó exactamente con el nombre `came.md`? | Obligatorio |
| **Exhaustividad de Cuadrantes** | ¿Están representados los 4 cuadrantes (FO, FA, DO, DA)? | Mínimo 1 cruce por cuadrante |
| **Citación Explícita de IDs** | ¿Cada estrategia cita los IDs exactos de los factores cruzados (ej. `F1 x O2`)? | 100% de los cruces |
| **Doble Formulación** | ¿Cada fila contiene tanto la directriz táctica como la acción operativa tangible? | Requerido |
| **Procesos Involucrados** | ¿Se especifican los procesos directos o de soporte afectados por la intervención? | Requerido |
| **Trazabilidad Downstream** | ¿Las acciones concretas alimentan el inventario EERR de `valueActionsBuilder`? | Requerido |
