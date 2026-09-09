# graspSequenceRealizer

Herramienta para el diseño y auditoría de Realizaciones de Casos de Uso (RCU) mediante diagramas de secuencia trazables y patrones de asignación de responsabilidades GRASP.

---

## 1. Propósito General

`graspSequenceRealizer` herramienta para el diseño y auditoría de realizaciones de casos de uso (rcu) mediante diagramas de secuencia trazables y patrones de asignación de responsabilidades grasp.

### Capacidades Principales:
- **RCU de Análisis (BCE):** Modela la interacción colaborativa utilizando el patrón Boundary-Control-Entity sin asumir infraestructura de software.
- **RCU de Diseño (GRASP):** Asigna responsabilidades orientadas a objetos aplicando los patrones Experto en Información, Creador, Controlador, Bajo Acoplamiento, Alta Cohesión, Fabricación Pura, Polimorfismo, Indirección y Variaciones Protegidas.
- **Diagramas de Secuencia Trazables:** Genera especificaciones en Mermaid con líneas de vida tipadas, mensajes síncronos/asíncronos y fragmentos combinados (`opt`, `alt`, `loop`).
- **Auditoría de Olores en Secuencias:** Detecta mensajes huérfanos, controladores inflados (fat controller), llamadas circulares y violaciones de la ley de Demeter.

---

## 2. Arquitectura Interna

```
graspSequenceRealizer/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de realizaciones de casos de uso
│   ├── rcu-analysis-template.md            # Plantilla de RCU conceptual bajo arquitectura BCE
│   └── rcu-design-template.md              # Plantilla de RCU técnica con asignación formal GRASP
└── references/                             # Manuales y guías de patrones de responsabilidad
    ├── advanced-grasp-and-smells.md        # Patrones GRASP avanzados, sinergia GoF y antipatrones
    ├── analysis-realization.md             # Guía metodológica para realizaciones de análisis
    └── design-realization.md               # Guía metodológica para realizaciones de diseño
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: RCU de Diseño con Patrones GRASP
Entradas: CU-04 Confirmar Reserva y Diagrama de Clases de Diseño preliminar.
Salida: Documento RCU de diseño con diagrama de secuencia en Mermaid y tabla de responsabilidades GRASP.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Especificación del Caso de Uso (flujo principal y alternativos).
- Modelo de Dominio Conceptual (para Análisis) o DCD (para Diseño).
- Decisiones arquitectónicas de comunicación y persistencia.

### Salidas (Outputs)
- Documento formal de Realización de Caso de Uso (Análisis o Diseño).
- Diagrama de Secuencia estructurado en Mermaid o draw.io.
- Matriz de justificación de patrones de asignación de responsabilidades GRASP.
