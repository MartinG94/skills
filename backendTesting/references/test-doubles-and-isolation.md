# Guía Técnica: Dobles de Prueba (Test Doubles) y Pruebas Deterministas

Esta referencia consolida la taxonomía de Gerard Meszaros y patrones para erradicar pruebas intermitentes (*flaky tests*) en cualquier stack tecnológico.

---

## 1. Taxonomía de Dobles de Prueba (Gerard Meszaros)

| Tipo de Doble | Propósito Principal | Cuándo Utilizarlo | Señal de Mal Uso / Anti-Patrón |
|---|---|---|---|
| **Dummy** | Relleno para satisfacer la firma de un método/constructor; nunca se invoca ni se lee. | Parámetro obligatorio que el flujo del test no utiliza. | Usar un Mock completo con expectativas cuando el método jamás se llama. |
| **Stub** | Provee respuestas enlatadas preprogramadas ante llamadas entrantes. | Simular lecturas de datos externos (ej. cotización de moneda, consulta de usuario). | Verificar cuántas veces se invocó el stub (convertirlo en un mock innecesario). |
| **Spy** | Stub que además registra internamente las invocaciones y parámetros recibidos para ser auditados. | Auditar si una llamada colateral ocurrió sin alterar su comportamiento base. | Depender de contadores internos en lugar de evaluar el resultado observable. |
| **Mock** | Objeto preconfigurado con expectativas sobre qué llamadas debe recibir; falla la prueba si no se cumplen. | **Verificar efectos secundarios externos** (ej. envío de email, publicación de evento en cola, cobro en pasarela). | **Over-Mocking:** Mockear entidades de dominio, DTOs o clases de datos que pueden usarse reales. |
| **Fake** | Implementación liviana y completamente funcional en memoria (ej. `InMemoryRepository`, base SQLite). | Reemplazar dependencias de infraestructura pesadas manteniendo lógica real sin simular cada método. | Introducir lógica compleja o dependencias de red en el fake. |

---

## 2. Regla de Oro: Evitar el Over-Mocking de Dominio

> [!WARNING]
> **Dominio Siempre Real:** Nunca mockees Entidades, Value Objects, DTOs ni colecciones del dominio. Úsalos con sus constructores o fábricas reales. Reserva los Mocks exclusivamente para fronteras de infraestructura (I/O, llamadas de red, APIs de terceros, colas de mensajería).

---

## 3. Aislamiento de Fuentes No Deterministas (Erradicación de Flakiness)

Las pruebas intermitentes degradan la confianza del equipo. Aplica estas tres reglas de aislamiento:

### A. Abstracción del Tiempo (Reloj del Sistema)
- **Anti-patrón:** Invocar directamente `DateTime.UtcNow`, `new Date()` o `datetime.now()` dentro de la lógica.
- **Solución Canónica:** Inyectar un proveedor de tiempo o reloj abstracto (`Clock`, `TimeProvider`, interfaz equivalente) configurable en el test.

### B. Control del Azar y UUIDs
- **Anti-patrón:** Generar `UUID.randomUUID()` dentro de métodos cuya salida se compara contra un valor fijo.
- **Solución Canónica:** Inyectar el generador de identificadores o fijar la semilla del generador pseudoaleatorio (`seed`).

### C. Concurrencia y Esperas Asíncronas
- **Anti-patrón:** Usar esperas fijas (`Thread.sleep(2000)`, `time.sleep(2)`).
- **Solución Canónica:** Usar esperas activas por condición (*polling*) con timeout máximo (ej. Awaitility en Java, Polly en .NET, o `wait_for` en Python).

---

## 4. Checklist de Calidad para Suites de Pruebas

- [ ] ¿Los tests son completamente independientes entre sí (se pueden ejecutar en paralelo y en cualquier orden)?
- [ ] ¿Se limpian los datos compartidos o se usa aislamiento por transacción en cada prueba de integración?
- [ ] ¿Toda prueba contiene al menos una aserción explícita sobre el resultado o una verificación de excepción?
- [ ] ¿Los nombres de los tests comunican claramente `Condición/Acción -> ResultadoEsperado`?
- [ ] ¿Se eliminaron los sleeps fijos en favor de aserciones asíncronas con timeout?
