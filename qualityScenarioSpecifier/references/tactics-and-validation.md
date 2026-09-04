# Tácticas y validación arquitectónica

Lee esta referencia únicamente cuando el usuario pida diseño, tácticas o evaluación de
arquitectura. Primero debe existir un escenario suficientemente claro.

## Registro de respuesta arquitectónica

| Escenario | Alternativa/táctica | Mecanismo | Trade-offs | Evidencia requerida |
|---|---|---|---|---|
| ID o enlace | decisión candidata | cómo influye en la respuesta | atributos/coste afectados | prueba, análisis, prototipo o medición |

No hay correspondencia uno-a-uno entre atributo y tecnología. Compara una solución
simple con las alternativas plausibles y respeta las restricciones existentes.

Familias de tácticas que pueden orientar la búsqueda, sin prescribir productos:

- disponibilidad/fiabilidad: detección, recuperación, redundancia, degradación y
  prevención de fallos;
- rendimiento: demanda de recursos, concurrencia, priorización y gestión de recursos;
- seguridad: identificación, autorización, confidencialidad, integridad, detección,
  respuesta y auditoría;
- modificabilidad: localización de cambios, abstracción, cohesión y reducción de
  dependencias;
- interoperabilidad: contratos, mediación y gestión de evolución;
- usabilidad: prevención/recuperación de errores y soporte a tareas del usuario.

Una táctica no garantiza por sí sola el escenario. Por ejemplo, redundancia puede
introducir demora o inconsistencia; retries pueden duplicar efectos; cache puede servir
datos obsoletos; asincronía puede dificultar confirmación y trazabilidad.

## Elegir validación

- revisión basada en escenarios: para rastrear decisiones y trade-offs;
- análisis/modelo: cuando existe una relación calculable y supuestos conocidos;
- prueba automatizada: cuando hay sistema o componente ejecutable;
- prototipo/PoC: cuando la incertidumbre técnica domina;
- observación en operación: cuando el entorno real determina la medida.

No fijes herramientas, carga o umbrales. Expresa entorno, datos, procedimiento, medida
y criterio de aceptación con valores proporcionados o `TBD`.

## Cierre

Una propuesta está lista cuando cada decisión se vincula a un escenario, muestra al
menos un coste y tiene una forma proporcional de validar la hipótesis. Si faltan datos,
presenta la incertidumbre; no aumentes la confianza con cifras inventadas.
