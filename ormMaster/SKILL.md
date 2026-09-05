---
name: orm-master
description: >-
  Audita, diseña u optimiza el mapeo y el acceso a datos de un ORM existente, usando
  el framework, la base y los requisitos del proyecto. Diagnostica carga de grafos,
  N+1, transacciones y concurrencia con evidencia; genera configuración o código solo
  cuando el usuario pide implementación.
---

# Auditoría y optimización de persistencia ORM

## Responsabilidad y límites

Esta skill trabaja **después** de que existen un modelo de diseño, un esquema o una
implementación de persistencia. Su producto primario es un diagnóstico y una decisión
de mapeo verificable; no debe inventar entidades, límites de agregados, tablas ni
reglas de negocio.

Usar uno de estos modos según el pedido:

- **Auditoría**: localizar problemas y priorizarlos con evidencia.
- **Diseño de mapeo**: definir cómo materializar un modelo ya aprobado.
- **Diagnóstico de rendimiento**: explicar consultas o bloqueos observados.
- **Implementación**: modificar configuración/código solo cuando fue solicitada.

No usar esta skill para diseñar el modelo relacional desde cero; esa responsabilidad
corresponde a `relational-object-map`. No reemplazar decisiones de dominio de
`domain-design` por conveniencias del ORM.

## Entradas

Identificar antes de prescribir una solución:

- ORM, versión, lenguaje y convenciones del repositorio;
- motor y versión de base de datos;
- entidades/mapeos y esquema realmente vigentes;
- casos de uso y límites transaccionales;
- consultas, logs SQL, planes, métricas o fallo reproducible;
- volumen, cardinalidad, patrón de acceso y nivel de contención relevantes.

Si faltan stack o código, entregar una recomendación neutral y declarar qué debe
confirmarse. No producir anotaciones JPA, configuración EF Core, Prisma o SQLAlchemy
al azar. Las diferencias de ciclo de vida y seguimiento entre frameworks deben
tratarse con su terminología real, no mediante una equivalencia universal.

## Flujo de trabajo

### 1. Reconstruir el comportamiento observable

- Relacionar cada consulta o escritura con el caso de uso que la necesita.
- Determinar qué datos deben cargarse, en qué cantidad y durante cuánto tiempo viven.
- En auditorías de rendimiento, obtener o solicitar evidencia: número de consultas,
  SQL generado, plan de ejecución, tiempo, filas y memoria. No diagnosticar N+1 por
  la presencia de una relación `lazy` solamente.

### 2. Revisar mapeo y ciclo de vida

Comprobar identidad, nulabilidad, claves, conversiones, relaciones y ownership contra
el esquema aprobado. Distinguir instancias nuevas, seguidas, desvinculadas y marcadas
para eliminación según el ORM objetivo.

No asumir que:

- toda entidad seguida se guarda sin una operación explícita en cualquier ORM;
- una consulta sin tracking equivale a una transacción de solo lectura;
- acceder a una relación lazy fuera del contexto siempre produce la misma excepción;
- toda relación de dominio deba representarse como navegación bidireccional.

### 3. Elegir la estrategia de carga por consulta

| Estrategia | Útil cuando | Riesgo a revisar |
|---|---|---|
| proyección | se necesitan pocos campos o un modelo de lectura | duplicar reglas en la proyección |
| join/include/fetch graph | se requiere un grafo acotado | multiplicación de filas y memoria |
| consultas divididas o batch | hay colecciones grandes o múltiples | más viajes y consistencia entre lecturas |
| carga explícita | la relación es condicional | consultas accidentales en bucles |

No declarar un join único como solución óptima por defecto: puede excluir padres sin
hijos, producir un producto cartesiano o transferir datos innecesarios. Tampoco marcar
todas las colecciones como `LAZY` o `EAGER` universalmente; decidir por caso de uso y
verificar el SQL resultante.

### 4. Delimitar transacciones

- Ubicar la transacción alrededor de una unidad de trabajo coherente, normalmente en
  la capa de aplicación, respetando las convenciones del proyecto.
- Mantener fuera del bloqueo las operaciones remotas o lentas cuando la consistencia
  no exija lo contrario.
- Definir rollback, reintentos y aislamiento de acuerdo con el framework y la base.
- Tratar `AsNoTracking` y equivalentes como opciones de seguimiento/materialización,
  no como sustitutos de una transacción `read-only`.

No imponer `rollbackFor`, transacciones manuales ni una anotación concreta sin conocer
el mecanismo del stack.

### 5. Tratar concurrencia según el conflicto

Elegir control optimista, bloqueo pesimista, operación atómica u otra estrategia a
partir de frecuencia de colisión, costo de reintento y requisito de consistencia.
Agregar una columna de versión solo cuando el riesgo de actualización perdida lo
justifique y documentar la experiencia ante conflicto. No reintentar automáticamente
una operación con efectos externos sin idempotencia demostrada.

### 6. Respetar agregados y cascadas

- Mantener invariantes y mutaciones del dominio detrás de sus operaciones aprobadas.
- Configurar cascada y orphan removal solo cuando el ciclo de vida dependiente esté
  sustentado por el modelo y el esquema.
- Evitar cascadas de borrado entre agregados independientes.
- Revisar igualdad, hash e identidad con las reglas del lenguaje y del ORM elegido;
  no imponer una única estrategia de ID a todos los modelos.

### 7. Verificar la solución

En modo implementación, ejecutar pruebas enfocadas de mapeo/consulta y observar el
SQL. Usar una base representativa cuando la semántica dependa del motor. Comparar
antes/después con la misma carga cuando se afirma una mejora de rendimiento.

Revisar índices con el plan de ejecución, selectividad y patrón de escritura. Una FK
no necesita automáticamente un índice adicional en todos los motores y cargas.

## Implementación condicional

Antes de editar código, localizar la configuración y los patrones ya usados por el
proyecto. Aplicar el cambio mínimo coherente con ese stack. No generar simultáneamente
versiones JPA, EF Core, Prisma y SQLAlchemy; un ejemplo genérico no sustituye una
implementación compilable.

Cuando el usuario solo pide revisión, no mutar archivos ni crear migraciones. Señalar
la ubicación, el comportamiento observado, el impacto y una corrección propuesta.

## Contrato de salida

Por defecto entregar:

1. **Contexto confirmado**: ORM/base/versiones y evidencia usada.
2. **Hallazgos priorizados**: ubicación, causa, impacto y confianza.
3. **Decisiones**: estrategia elegida y alternativas descartadas.
4. **Cambios**: solo si se pidió implementación, con archivos afectados.
5. **Verificación**: pruebas, SQL/métricas comparables y límites pendientes.

Finalizar cuando cada afirmación importante esté respaldada por código, SQL, una
medición o un requisito explícito; no prometer que un patrón elimina N+1, bloqueos o
inconsistencias sin comprobar el caso concreto.
