# gofAdviser

Herramienta de evaluación, asesoramiento y auditoría de aplicación de patrones de diseño GoF (Gang of Four) en arquitecturas orientadas a objetos.

---

## 1. Propósito General

`gofAdviser` herramienta de evaluación, asesoramiento y auditoría de aplicación de patrones de diseño gof (gang of four) en arquitecturas orientadas a objetos.

### Capacidades Principales:
- **Diagnóstico de Justificación:** Determina si un problema de diseño realmente justifica la introducción de un patrón GoF o si introduce complejidad accidental innecesaria.
- **Mapeo Síntomas / Smells a Patrones:** Asocia olores de código y diseño (violaciones OCP, condicionales polimórficos, acoplamiento a clases concretas) a patrones específicos.
- **Comparativa de Alternativas:** Evalúa ventajas y desventajas entre patrones afines (ej. Strategy vs State, Decorator vs Composite, Factory Method vs Abstract Factory).
- **Diseño de Solución:** Modela las clases, interfaces y relaciones de colaboración del patrón adaptadas al contexto específico del problema.

---

## 2. Arquitectura Interna

```
gofAdviser/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de evaluación técnica
│   └── gof-assessment-template.md          # Plantilla de dictamen técnico con matriz de trade-offs
└── references/                             # Catálogos de selección y principios
    └── pattern-selection.md                # Matriz de Olores de Diseño -> Patrones GoF y árbol de decisión
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Dictamen de Selección GoF
Entradas: Necesidad de soportar múltiples algoritmos de cálculo de comisiones con cambios frecuentes en runtime.
Salida: Evaluación técnica justificando el patrón Strategy frente a herencia rígida o State, con diagrama UML.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Descripción de la variación o punto de extensión del sistema.
- Diagrama de clases o fragmento de código actual a refactorizar.
- Atributos de calidad priorizados (mantenibilidad, extensibilidad, rendimiento).

### Salidas (Outputs)
- Dictamen técnico de evaluación GoF con matriz comparativa de alternativas.
- Diagrama UML de la solución propuesta (participantes y colaboraciones).
- Balance de trade-offs y consecuencias arquitectónicas.
