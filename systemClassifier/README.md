# systemClassifier

Herramienta de análisis sistémico, clasificación de sistemas empresariales, evaluación de prefactibilidad y ubicación de fases PUD.

---

## 1. Propósito General

`systemClassifier` herramienta de análisis sistémico, clasificación de sistemas empresariales, evaluación de prefactibilidad y ubicación de fases pud.

### Capacidades Principales:
- **Clasificación Funcional de Sistemas:** Identifica y clasifica subsistemas según su rol organizacional: TPS, MIS, DSS, ESS, KMS y AI.
- **Evaluación de Prefactibilidad Integral:** Evalúa viabilidad Técnica, Operativa y Económica mediante indicadores financieros (VAN, TIR, Payback y ROI).
- **Alineación con el Proceso Unificado (PUD):** Mapea hitos, artefactos y compuertas de decisión a través de las fases de Inicio, Elaboración, Construcción y Transición.
- **Diagnóstico según Teoría General de Sistemas (TGS):** Identifica límites, entorno, entradas, salidas, procesos y mecanismos de retroalimentación.

---

## 2. Arquitectura Interna

```
systemClassifier/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de reporte sistémico
│   └── prefeasibility_and_pud_report_template.md # Plantilla formal de prefactibilidad y PUD
└── references/                             # Manuales teóricos y metodológicos
    └── tgs_and_pud_handbook.md             # Manual de TGS, taxonomía de sistemas, métricas financieras y PUD
```

---

## 3. Prerequisitos de Entorno

- No requiere dependencias externas.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Estudio de Prefactibilidad y Clasificación
Entradas: Propuesta de incorporación de sistema automatizado de control de stock y presupuesto estimado.
Salida: Dictamen de factibilidad económica (tabla de flujos, VAN, TIR), clasificación como TPS/MIS y compuerta PUD.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Enunciados de proyectos de software o iniciativas organizacionales.
- Estimaciones de costos de desarrollo, costos operativos y beneficios proyectados.
- Planes de iteración o cronogramas de proyecto.

### Salidas (Outputs)
- Dictamen de Clasificación Funcional del Sistema (TPS/MIS/DSS/etc.).
- Informe formal de Prefactibilidad Técnica, Operativa y Económica con tabla de flujo de caja.
- Matriz de trazabilidad de fases e hitos del Proceso Unificado de Desarrollo (PUD).
