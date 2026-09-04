# Integración y consistencia distribuidas

Lee esta referencia sólo para flujos que realmente cruzan límites desplegables.

## Selección de interacción

Usa comunicación síncrona cuando el llamador necesita la respuesta para continuar y el
presupuesto de latencia/disponibilidad lo permite. Usa mensajería cuando se necesita
desacoplamiento temporal, distribución de hechos o procesamiento diferido. No conviertas
toda interacción en eventos ni toda consulta en llamada remota.

Para cada interacción registra:

- semántica del comando/consulta/evento;
- propietario del contrato y política de evolución;
- expectativa de latencia/disponibilidad, si fue proporcionada;
- semántica de entrega y duplicados;
- idempotencia y tratamiento de reordenamiento;
- observabilidad y datos sensibles;
- comportamiento ante fallo o indisponibilidad.

## Resiliencia contextual

- Timeout: deriva del presupuesto extremo a extremo y del trabajo remoto; no uses un
  valor universal.
- Retry: sólo para fallos transitorios y operaciones seguras/idempotentes, con límite y
  presupuesto. Puede amplificar carga o duplicar efectos.
- Circuit breaker: útil ante fallos repetidos de una dependencia; requiere política de
  recuperación y comportamiento visible.
- Bulkhead: aísla recursos cuando la contención compartida es un riesgo demostrado.

Ninguno es obligatorio por el mero hecho de usar HTTP/gRPC.

## Consistencia

Una Saga coordina transacciones locales y compensaciones semánticas. La compensación no
borra necesariamente la historia ni restaura exactamente el estado anterior; debe ser
una operación de negocio válida, idempotente y auditable.

Usa Saga sólo si un proceso de negocio cruza límites y acepta esa semántica. Compara con:

- rediseñar el límite para mantener una transacción local;
- aceptar confirmación diferida;
- reservar/expirar recursos;
- coordinación manual;
- un protocolo transaccional, evaluando sus costes y soporte real.

No describas 2PC como “violación de CAP”. Analiza disponibilidad, bloqueo, latencia,
soporte de participantes y modelo de fallo concretos.

Transactional Outbox coordina cambio local y publicación, pero normalmente produce
entrega al menos una vez; consumidores y relay deben tolerar duplicados. No garantiza
exactly-once extremo a extremo.

## Validación

Prueba los caminos parciales, duplicados, mensajes fuera de orden, expiraciones y
compensaciones con valores del contexto. Si no hay entorno ejecutable, presenta las
hipótesis y fallos a simular en vez de afirmar resiliencia.
