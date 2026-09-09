# processAuditor

Herramienta analítica y de auditoría forense para procesos operativos de negocio en la Etapa 2 de Gestión y Mejora de Procesos (GMP), basada en los 4 ejes de la guía oficial `GUI_U2`.

---

## 1. Propósito General

`processAuditor` permite a analistas y consultores de procesos diagnosticar de forma estructurada las fallas operativas de un proceso actual (AS-IS). Transforma entrevistas no estructuradas y relevamientos de campo en evidencias fácticas agrupadas en cuatro dimensiones críticas:
1. **Control Interno (Marco COSO):** Salvaguarda de inventarios y activos, autorización multinivel, doble registro y segregación de funciones incompatibles (SoD).
2. **Formularios y Ruta Documental:** Normalización de comprobantes, copias justificadas, legibilidad y ciclo de vida del archivo.
3. **Factores Humanos y Condiciones Laborales:** Ergonomía física y cognitiva, tiempos muertos y sobrecarga de tareas burocráticas.
4. **Soporte Informático y Silos TI:** Erradicación de recapturas manuales, integración de software desconectado y trazabilidad de accesos.

Las salidas de esta auditoría constituyen la evidencia primaria para fundamentar las **Debilidades** en la Matriz FODA de la Etapa 2.

---

## 2. Arquitectura Interna

```
processAuditor/
├── SKILL.md                               # Contrato operativo para el agente inteligente
├── README.md                              # Guía metodológica para el desarrollador/analista
├── templates/                             # Plantillas estandarizadas de matrices y checklists
│   ├── risk_control_matrix_template.md    # Matriz de Riesgos y Controles (RCM)
│   ├── segregation_of_duties_matrix.md    # Matriz de Segregación de Funciones (SoD)
│   ├── document_routing_checklist.md      # Diagnóstico de comprobantes y rutas físicas
│   ├── human_factors_checklist.md         # Evaluación ergonómica y laboral
│   └── it_silos_checklist.md              # Auditoría de integración y brechas de software
└── references/                            # Documentación y marcos teóricos de apoyo
```

---

## 3. Prerequisitos de Entorno

- No requiere runtime de código ni dependencias externas; opera sobre procesamiento de lenguaje natural estructurado y razonamiento encadenado.
- Los artefactos se entregan íntegramente en formato Markdown (`.md`) tabular estándar.

---

## 4. Ejemplos de Invocación y Uso

### Caso 1: Detección de incompatibilidad de funciones (SoD)
```markdown
Entrada: "El encargado de depósito recibe las cajas del camión y luego ingresa en el sistema el comprobante de recepción para actualizar las existencias."
Diagnóstico processAuditor:
- Conflicto SoD Crítico: Custodia Física (recepción) + Registro Contable (alta de stock en ERP).
- Riesgo: Ocultamiento de faltantes o mermas mediante ajustes unilaterales de inventario.
- Control propuesto: Separación de la recepción física (marcado de bultos) de la confirmación administrativa de stock por parte de Compras/Administración mediante escaneo ciego.
```

### Caso 2: Auditoría de Silos TI y Recapturas
```markdown
Entrada: "El área de ventas recibe los pedidos de clientes por correo en PDF y una secretaria los transcribe manualmente al sistema de facturación antes del mediodía."
Diagnóstico processAuditor:
- Brecha Eje 4: Silo informático y recaptura manual propensa a error humano.
- Control propuesto: Implementación de portal web de autogestión de pedidos B2B o ingesta automática de pedidos por API.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Transcripciones de entrevistas a participantes del proceso.
- Minutas de relevamiento, narrativas de casos prácticos (ej. BioTrace Logística).
- Reglamentos internos o descripciones de puestos de trabajo.

### Salidas (Outputs)
- **Matriz RCM:** Tabla con cálculo de severidad inherente ($P \times I$) y recomendaciones de control preventivo/detectivo.
- **Matriz SoD:** Mapeo de incompatibilidades de custodia, registro, autorización y conciliación.
- **Checklists de los Ejes 2, 3 y 4:** Diagnósticos temáticos con evidencias textuales.
- **Enunciados FODA:** Lista de debilidades fácticas normalizadas para consumo directo por `processWorkbench`.
