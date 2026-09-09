# microserviceDecomposer

Herramienta de análisis arquitectónico para la descomposición de sistemas en microservicios o modularización de monolitos basada en DDD e ISO 25010.

---

## 1. Propósito General

`microserviceDecomposer` herramienta de análisis arquitectónico para la descomposición de sistemas en microservicios o modularización de monolitos basada en ddd e iso 25010.

### Capacidades Principales:
- **Evaluación Monolito vs Microservicios:** Analiza la viabilidad y conveniencia de descomposición evaluando madurez de equipo, frecuencia de despliegue y costos operativos.
- **Delimitación por Contextos Delimitados (DDD):** Define fronteras de servicios alineadas con Subdominios Core, de Soporte y Genéricos.
- **Análisis de Atributos de Calidad (ISO 25010):** Cuantifica el impacto en escalabilidad, disponibilidad, mantenibilidad, latencia y consistencia de datos.
- **Patrones de Integración y Consistencia:** Diseña transacciones distribuidas mediante Sagas (Orquestación vs Coreografía) y consultas CQRS/Event Sourcing.

---

## 2. Arquitectura Interna

```
microserviceDecomposer/
├── SKILL.md                                # Contrato operacional del agente
├── README.md                               # Documentación técnica de la skill
├── templates/                              # Plantillas de descomposición de sistemas
│   └── service-decomposition-spec.md       # Plantilla de especificación con trade-offs y matriz de servicios
└── references/                             # Guías de patrones distribuidos y modelado
    ├── decomposition-and-views.md          # Métodos de particionamiento y vistas C4 Container
    └── distributed-patterns.md             # Patrones de mensajería, Sagas y compensaciones transaccionales
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Ejemplo de Invocación
```markdown
Modo: Descomposición Arquitectónica de Servicios
Entradas: Monolito de Comercio Electrónico y requerimiento de escalar Checkout independientemente del Catálogo.
Salida: Especificación de Bounded Contexts, matriz de trade-offs ISO 25010 y diagrama C4 Container en Mermaid.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Arquitectura actual del sistema y stack tecnológico.
- Modelo de dominio y casos de uso de negocio.
- Requisitos de atributos de calidad (disponibilidad, tolerancia a fallos, latencia).

### Salidas (Outputs)
- Especificación formal de Descomposición de Microservicios.
- Matriz de evaluación de trade-offs ISO 25010.
- Diagrama C4 Container en Mermaid o draw.io.
- Estrategia de transacciones distribuidas y compensación de fallos.
