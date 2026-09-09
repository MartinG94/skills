# processWorkbench

Mesa de trabajo analítica y estratégica para las Etapas 1, 2 y 3 del marco metodológico de Gestión y Mejora de Procesos (GMP).

---

## 1. Propósito General

`processWorkbench` asiste al equipo de proyecto y a los analistas en la toma de decisiones metodológicas iniciales e intermedias. Conduce la secuencia lógica desde la selección justificada del proceso crítico hasta la definición de acciones de intervención viables:
- **Etapa 1 (Encuadre y Selección):** Vincula los objetivos del negocio y las tendencias de servitización (SDL) con la Cadena de Valor Virtual (Rayport & Sviokla) y aplica la matriz ponderada multicriterio oficial (Estrategia, Tendencias, Costos/Problemas, Cliente, Producto) para elegir objetivamente el proceso crítico.
- **Etapa 2 (Diagnóstico Estratégico):** Mapea los intereses y fricciones de los *Stakeholders* y construye la Matriz FODA alimentando las Debilidades directamente desde la evidencia forense provista por `processAuditor`.
- **Etapa 3 (Formulación de la Solución):** Genera los cruces estratégicos de la Matriz CAME, deriva las Acciones de Valor bajo el esquema EERR (Eliminar, Reducir, Incrementar, Crear) y somete cada iniciativa al **Filtro de Restricciones Operativas** (Plazos, Costos, Dependencia de TI y Resistencia Humana al Cambio).

---

## 2. Arquitectura Interna

```
processWorkbench/
├── SKILL.md                                # Contrato operacional consumido por el LLM
├── README.md                               # Documentación técnica y guía metodológica
├── templates/                              # Plantillas estructuradas de entrega
│   ├── stage1_framing_and_selection.md     # Encuadre y matriz de 5 criterios ponderados
│   ├── virtual_value_chain_matrix.md       # Cadena de Valor Virtual (5 etapas de información)
│   ├── stage2_stakeholders_foda.md         # Mapeo de partes interesadas y FODA del proceso
│   └── stage3_came_value_actions.md        # Cruces CAME, acciones EERR y filtro operativo
└── references/                             # Fundamentos teóricos y bibliografía de cátedra
```

---

## 3. Prerequisitos de Entorno

- No requiere librerías complejas ni compiladores; los cálculos ponderados se realizan de forma determinista mediante tablas Markdown.
- Se integra de forma natural con los diagnósticos de `processAuditor` y sirve como insumo de entrada para `processImprovementPlanner` y `kpiDesigner`.

---

## 4. Ejemplos de Invocación y Uso

### Selección Ponderada de Proceso (Etapa 1)
```markdown
Evaluación de candidatos en caso BioTrace:
- Candidato 1: Gestión de Despacho y Entrega Frigorífica -> Puntaje 4.70 (Seleccionado)
- Candidato 2: Compras de Insumos Descartables -> Puntaje 3.40
- Candidato 3: Mantenimiento Preventivo de Flota -> Puntaje 3.05
Justificación: Concentra el mayor impacto en SLAs de clientes y riesgo de pérdida por cadena de frío.
```

### Derivación de Acción de Valor CAME (Etapa 3)
```markdown
Cruce CAME: DO (Debilidad D2: remito papel demorado 48h + Oportunidad O1: apps móviles SaaS de bajo costo).
Acción EERR: CREAR app de chofer con firma digital en entrega.
Filtro de Viabilidad:
- Plazo: 8 semanas (Aprobado)
- Presupuesto: Suscripción por chofer (Aprobado)
- Dependencia TI: Integración API simple (Aprobado)
- Resistencia al Cambio: Mitigada con 2 talleres de capacitación práctica (Aprobado)
Dictamen: APROBADA para plan de implantación de Etapa 4.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Enunciado del caso de negocio o entrevista a la dirección de la empresa.
- Diagnóstico de debilidades y riesgos operativos generado por `processAuditor`.
- Restricciones organizacionales conocidas (presupuesto tope, plazos de entrega, stack tecnológico).

### Salidas (Outputs)
- Tablas estructuradas de Etapa 1: Encuadre, análisis SDL, matriz de la Cadena de Valor Virtual y matriz de selección de 5 criterios con cálculo ponderado.
- Tablas estructuradas de Etapa 2: Matriz de Stakeholders y Matriz FODA contextualizada al proceso crítico.
- Tablas estructuradas de Etapa 3: Matriz CAME, inventario de Acciones de Valor EERR, matriz del Filtro de Restricciones Operativas y mapeo de procesos afectados.
