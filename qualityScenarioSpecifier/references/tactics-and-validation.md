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


## Catálogo de Tácticas Arquitectónicas SEI (Bass, Clements & Kazman)

### 1. Disponibilidad / Fiabilidad
- **Detección de Fallos:**
  - *Heartbeat / Ping-Echo:* Monitoreo periódico de vida entre nodos o servicios.
  - *Liveness & Readiness Probes:* Comprobaciones del orquestador antes de enrutar tráfico.
  - *Timeouts:* Interrupción de esperas indefinidas ante caídas de red.
- **Recuperación de Fallos:**
  - *Redundancia Activa (Hot Standby):* Nodos replicados procesando en paralelo para absorción inmediata.
  - *Redundancia Pasiva (Warm/Cold Standby):* Nodo secundario que se inicializa o promueve ante fallo.
  - *Circuit Breaker:* Apertura de circuito ante umbral de fallos para evitar saturación en cascada.
  - *Retry con Exponential Backoff y Jitter:* Reintentos espaciados con aleatoriedad para evitar tormentas de reconexión.
  - *Degradación Elegante (Fallback):* Respuesta con datos cacheados o funcionalidad reducida ante caída externa.
- **Prevención de Fallos:**
  - *Bulkhead (Mamparos):* Aislamiento de pools de hilos o recursos para que un fallo no arrastre a todo el sistema.

### 2. Rendimiento / Desempeño
- **Control de Demanda:**
  - *Rate Limiting / Throttling:* Limitación de tasa de solicitudes con algoritmos Token Bucket o Leaky Bucket.
  - *Colas con Prioridad:* Procesamiento preferente de transacciones VIP o de facturación sobre reportes.
- **Gestión de Recursos:**
  - *Concurrencia y Asincronía:* Liberación de hilos de atención mediante arquitecturas orientadas a eventos.
  - *Caching Multinivel:* Almacenamiento en caché en memoria o distribuido para lecturas intensivas.
  - *Pool de Conexiones (Connection Pooling):* Reutilización de canales abiertos de base de datos.

### 3. Seguridad
- **Resistir Ataques:**
  - *Autenticación y Autorización Robusta:* MFA, RBAC, ABAC y tokens de corta duración con rotación.
  - *Validación y Sanitización:* Inspección defensiva de entradas en las fronteras públicas.
  - *Cifrado:* TLS 1.3 en tránsito y AES-256 en reposo.
- **Detectar y Recuperar:**
  - *Audit Trail Inmutable:* Bitácora append-only protegida contra mutación.
  - *Bloqueo por Fuerza Bruta:* Inhabilitación temporal de accesos ante intentos fallidos reiterados.

### 4. Modificabilidad / Mantenibilidad
- **Reducción del Acoplamiento:**
  - *Inversión de Dependencias (DIP) y Puertos/Adaptadores:* Desacoplamiento del dominio frente a infraestructura.
  - *Ocultamiento de Información:* Encapsulamiento estricto de invariantes tras contratos estables.
- **Diferir el Enlace (*Defer Binding*):**
  - *Inyección de Dependencias (IoC):* Resolución de colaboradores en tiempo de arranque.
  - *Feature Flags:* Habilitación dinámica de capacidades en producción sin redespliegue.
