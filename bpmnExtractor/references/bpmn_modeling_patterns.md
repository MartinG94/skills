# Patrones de Modelado BPMN 2.0 y Manejo de Excepciones

Esta guía técnica complementa la taxonomía BPMN y detalla patrones de modelado para colaboraciones complejas y flujos con eventos.

---

## 1. Colaboración entre Piscinas (Pools): White-Box vs. Black-Box

1. **Piscinas Cerradas (Black-Box):**
   - Representan entidades externas (clientes, proveedores, entes reguladores como AFIP/bancos) cuyo proceso interno no controlamos ni modelamos en detalle.
   - **Regla:** No llevan lanes ni actividades en su interior; solo son el destino/origen de flechas de mensaje.
2. **Piscina Abierta (White-Box):**
   - Representa a la organización o proceso bajo análisis; contiene carriles (lanes), compuertas, actividades y eventos.
3. **Reglas Estrictas de Flujos de Mensaje (`Message Flow`):**
   - Se dibujan con línea de trazos y extremos circulares/flechas abiertas.
   - **Jamás** pueden conectar dos elementos situados dentro de la **misma** Pool.
   - **Jamás** un `Sequence Flow` (línea continua) puede cruzar la frontera entre dos Pools distintas.

---

## 2. Manejo de Tiempos y Esperas: Eventos Intermedios de Temporizador

### A. Temporizador en Línea (Catch Intermediate Timer Event)
- Se sitúa en la secuencia normal para modelar un retardo planificado o una ventana de espera (ej. "Aguardar 48 horas por respuesta").
- **Flujo:** La actividad precedente finaliza $\to$ el token queda retenido en el timer hasta que transcurre el tiempo programado $\to$ la secuencia continúa.

### B. Temporizador de Límite (Boundary Timer Event)
- Se acopla a la frontera de una actividad o subproceso para gestionar SLAs o caducidad.
- **Interrupción:** Si es *interrupting* (línea sólida doble), cancela la actividad activa y desvía el flujo a la rama de excepción. Si es *non-interrupting* (línea discontinua doble), dispara una acción paralela (ej. alerta o recordatorio) sin abortar la tarea.

---

## 3. Ciclo de Vida de Objetos de Datos (Data Objects)

BPMN permite modelar cómo los artefactos de información cambian de estado a lo largo del proceso:
- Sintaxis textual: `NombreObjeto [Estado]` (ej. `Solicitud [Borrador]`, `Solicitud [Verificada]`, `Contrato [Firmado]`).
- Se asocian a las tareas mediante asociaciones de datos (`Data Input Association` y `Data Output Association`).

---

## 4. Corrección de Anti-Patrones Estructurales Frecuentes

| Anti-Patrón | Descripción del Fallo | Corrección Inmediata |
|---|---|---|
| **Compuerta XOR sin rama Default** | Compuerta exclusiva donde ninguna condición se cumple con ciertos datos válidos, provocando que el token quede bloqueado. | Marcar explícitamente una de las salidas con el conector de barra oblicua (`Default Flow`). |
| **Compuerta AND asimétrica** | Una compuerta paralela de divergencia abre 3 ramas pero se cierra con una compuerta que espera 2, o se sincroniza con una compuerta XOR. | Toda divergencia AND debe cerrarse con una convergencia AND que espere el mismo número de ramas activas. |
| **Deadlock en Ciclos (Loopbacks)** | Una rama de reintento entra aguas arriba de una compuerta paralela de unión que todavía está esperando otro token. | Reingresar los flujos de reintento a compuertas de unión exclusivas (XOR) previas a la tarea a reintentar. |
| **Actividad Fantasma post-excepción** | Tras una bifurcación de error, la rama queda sin conector a un evento de fin, dejando el proceso colgado. | Todo camino alternativo o de error debe culminar en un `End Event` (de terminación, error o fin normal). |
