---
name: api-design
description: >-
  Diseña o audita contratos HTTP/REST y especificaciones OpenAPI a partir de casos de
  uso y requisitos aprobados. Define recursos, operaciones, errores, idempotencia y
  compatibilidad sin inventar el stack. Implementa controladores o handlers solo
  cuando el usuario lo pide y existe un proyecto objetivo.
---

# Diseño y auditoría de contratos HTTP/REST

## Responsabilidad

El producto primario de esta skill es un **contrato de integración** verificable:
OpenAPI, decisiones HTTP y hallazgos de auditoría. Es una actividad downstream del
análisis y del diseño del sistema; no debe crear casos de uso, reglas de negocio,
entidades de dominio ni una arquitectura para poder completar el contrato.

Modos de trabajo:

- **Diseño**: producir o completar el contrato solicitado.
- **Auditoría**: revisar un contrato existente y reportar problemas con ubicación,
  impacto y corrección propuesta.
- **Implementación**: generar o modificar código en el stack existente únicamente si
  el usuario lo solicita. El contrato aprobado sigue siendo la referencia.

No convertir automáticamente una API RPC, GraphQL, gRPC o basada en eventos a REST.
Si el estilo está decidido, respetarlo; si la elección forma parte del pedido,
comparar alternativas según consumidores, semántica y restricciones observadas.

## Entradas y decisiones pendientes

Usar lo que exista de:

- casos de uso, operaciones y reglas de negocio aprobadas;
- consumidores, límites de confianza y requisitos de seguridad;
- recursos y esquemas ya publicados;
- política de compatibilidad/versionado;
- requisitos de reintento, concurrencia, volumen y observabilidad;
- contrato o código actual y stack del proyecto.

No suponer autenticación, proveedor, framework, base de datos, formato de IDs,
moneda, estados, límites de paginación ni SLA. Cuando falte una decisión que cambie la
interfaz pública, marcarla como pendiente y formular una pregunta concreta. Puede
avanzarse con las partes independientes.

## Flujo de diseño

### 1. Fijar el alcance del contrato

Enumerar las capacidades solicitadas y sus consumidores. Relacionar cada operación
con un caso de uso o necesidad explícita. No exponer mecánicamente cada clase o método
del DCD.

### 2. Modelar recursos y operaciones

- Usar URIs estables orientadas a recursos cuando el dominio lo permita.
- Representar comandos de negocio como creación de recursos, transición explícita o
  endpoint de acción solo cuando esa forma comunique mejor la semántica.
- Usar query parameters para filtros y paginación; elegir el esquema de paginación de
  acuerdo con estabilidad, volumen y necesidades del consumidor.
- Evitar anidamiento que replique todo el grafo interno. No imponer una profundidad
  numérica universal.
- Mantener las convenciones y la política de versión ya publicadas. Un prefijo como
  `/v1` es una opción, no un requisito automático.

### 3. Aplicar semántica HTTP

| Método | Propiedad relevante | Uso habitual |
|---|---|---|
| `GET`, `HEAD` | seguros e idempotentes | leer una representación o metadatos |
| `PUT` | idempotente | crear o reemplazar el estado de una URI conocida |
| `PATCH` | puede diseñarse idempotente, pero no lo es por definición | modificación parcial |
| `POST` | sin garantía general de idempotencia | crear bajo una colección o ejecutar un comando |
| `DELETE` | idempotente en su efecto previsto | eliminar o solicitar eliminación |

Seleccionar códigos de estado según el resultado observable. Documentar, entre
otros, éxito, entrada inválida, autenticación/autorización cuando aplique, ausencia,
conflicto, límites y fallos del servicio. No forzar `201`, `204`, `404` o `422` sin
considerar la operación y las convenciones existentes.

### 4. Definir esquemas y compatibilidad

- Separar representaciones públicas de detalles internos cuando reduzca acoplamiento.
- Expresar campos requeridos, nulabilidad, formatos, enums, límites y ejemplos solo
  con evidencia del dominio o del contrato existente.
- No introducir valores de ejemplo que puedan interpretarse como reglas reales.
- Identificar cambios incompatibles: eliminación o renombre de campos/operaciones,
  restricciones más fuertes y cambios de significado o tipo.
- Elegir la versión OpenAPI soportada por el proyecto o solicitada por el usuario; no
  cambiar de versión como efecto lateral de una auditoría.

### 5. Estandarizar errores

Usar Problem Details (`application/problem+json`) cuando el contrato adopte RFC 9457
o deba ofrecer errores HTTP estructurados. Definir al menos `type`, `title`, `status`
y, cuando aporte valor, `detail` e `instance`. Las extensiones como errores de campo o
identificadores de trazabilidad deben ser estables y no revelar secretos, datos
personales ni detalles internos.

No es obligatorio convertir toda respuesta `4xx/5xx` de infraestructura en el mismo
cuerpo si un intermediario no lo controla; documentar las excepciones observables.

### 6. Decidir idempotencia y concurrencia

Exigir una clave de idempotencia solo para operaciones reintentables cuyo efecto no
pueda duplicarse de forma segura, como un cobro o una reserva. Si se adopta:

- marcar el header como requerido en esas operaciones;
- definir alcance, formato, vencimiento y comportamiento ante reutilización con un
  payload diferente;
- documentar qué respuesta se reproduce y cómo se evita una carrera.

La persistencia concreta de la clave es una decisión de implementación. No prescribir
Redis, una base de datos ni una ventana fija sin contexto. Para actualizaciones
concurrentes, documentar la política elegida (`ETag`/`If-Match`, versión u otra) solo
si el requisito existe.

## Implementación condicional

No generar handlers, controladores, DTOs ni middleware durante un pedido de diseño o
auditoría. Cuando se pida implementación:

1. detectar lenguaje, framework, convenciones y generadores ya presentes;
2. implementar la mínima superficie necesaria para satisfacer el contrato;
3. no cambiar el contrato silenciosamente para acomodar el framework;
4. ejecutar las validaciones y pruebas disponibles del proyecto.

## Validación

Validar el documento con una herramienta compatible con su versión cuando esté
disponible y revisar además:

- cada operación tiene propósito, identificador, entradas, respuestas y seguridad
  aplicable;
- referencias y esquemas resuelven correctamente;
- métodos, caché e idempotencia coinciden con la semántica declarada;
- errores y cambios incompatibles están documentados;
- no aparecen requisitos, datos ni tecnologías no sustentados.

El Modelo de Madurez de Richardson puede describir el estilo observado; no es una
meta obligatoria. Incorporar hipermedia solo si los consumidores necesitan descubrir
transiciones mediante enlaces.

## Contrato de salida

Entregar únicamente lo solicitado. Por defecto:

1. alcance, fuentes y decisiones pendientes;
2. contrato OpenAPI nuevo/modificado o hallazgos de auditoría;
3. tabla breve de decisiones HTTP relevantes;
4. resultado de validación y riesgos abiertos.

Incluir código de implementación y pruebas solo en modo Implementación.

Finalizar cuando todas las operaciones del alcance tengan entradas, respuestas y
decisiones públicas definidas, el contrato pase la validación disponible y cualquier
incertidumbre incompatible quede explícita. No ampliar el alcance para “completar” la
API.
