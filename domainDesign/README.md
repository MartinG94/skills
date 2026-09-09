# domainDesign

Herramienta para la transformación de modelos de análisis y realizaciones de casos de uso en Diagramas de Clases de Diseño (DCD) trazables.

---

## 1. Propósito General

`domainDesign` herramienta para la transformación de modelos de análisis y realizaciones de casos de uso en diagramas de clases de diseño (dcd) trazables.

### Capacidades Principales:
- **Construcción de DCD:** Especifica clases de diseño completas con visibilidad (+, -, #), tipos de datos de implementación, multiplicidades y navegabilidad direccional.
- **Design Class Cards:** Documenta cada clase de diseño desglosando responsabilidades, colaboradores, métodos con firmas formales y atributos.
- **Patrones de Arquitectura de Dominio:** Diseña agregados, entidades, objetos de valor y servicios de dominio evitando el antipatrón de Modelo de Dominio Anémico.
- **Auditoría de Olores de Diseño:** Detecta dependencias circulares, acoplamiento excesivo, falta de cohesión y clases dios.

---

## 2. Arquitectura Interna

```
domainDesign/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de especificación de diseño
│   └── dcd-specification-template.md       # Plantilla DCD con Design Class Cards y diagrama
└── references/                             # Principios metodológicos de diseño de clases
    ├── dcd-method.md                       # Método de construcción y notación UML formal
    └── rich-domain.md                      # Patrones de dominio rico y catálogo de olores de diseño
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Especificación de Diagrama de Clases de Diseño (DCD)
Entradas: Modelo de Dominio de Análisis y Realizaciones de CU Registrar Pedido.
Salida: Documento DCD con Design Class Cards, diagrama UML en Mermaid y justificación de visibilidades.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Modelo de Dominio Conceptual de Análisis.
- Diagramas de Secuencia y Realizaciones de Casos de Uso (RCU).
- Restricciones y contratos del lenguaje de programación objetivo.

### Salidas (Outputs)
- Especificación formal de Diagrama de Clases de Diseño (DCD).
- Fichas técnicas de clases de diseño (Design Class Cards).
- Diagrama UML estructural en Mermaid o draw.io.
