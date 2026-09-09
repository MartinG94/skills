# Anti-Patrones Clásicos en ORMs y Checklist de Calidad

Esta referencia consolida las patologías recurrentes en el mapeo y acceso a datos y provee un marco de revisión para pull requests.

---

## 1. Catálogo de los 6 Anti-Patrones Clásicos

| Anti-Patrón | Síntoma en Producción | Causa Raíz en el ORM | Solución Canónica |
|---|---|---|---|
| **Problema N+1** | Cientos de consultas SQL emitidas para satisfacer una sola vista o endpoint; latencia que escala linealmente con el volumen. | Carga perezosa (*Lazy Loading*) navegada dentro de un bucle iterativo o serializador. | Emplear `JOIN FETCH`, proyecciones DTO específicas o `EntityGraph`. |
| **Explosión Cartesiana** | Consumo exponencial de memoria RAM en el servidor y transferencia masiva de datos redundantes. | Múltiples `JOIN FETCH` simultáneos sobre dos o más colecciones independientes ($1:N$). | Dividir en consultas separadas (*Split Queries*) o cargar colecciones secundarias mediante batching. |
| **Open Session in View (OSIV)** | Agotamiento del pool de conexiones de la base de datos bajo concurrencia moderada. | Mantener la conexión JDBC/SQL abierta durante todo el renderizado de la vista o serialización JSON. | Desactivar OSIV; cargar todos los datos necesarios en la capa de servicio/aplicación antes de retornar el DTO. |
| **Mutación Asimétrica de Grafos** | Inconsistencia de estado en memoria: el objeto hijo referencia al padre pero la lista del padre no contiene al hijo. | Mapeo bidireccional sin métodos helper de sincronización mutua en el agregado. | Implementar métodos defensivos en la entidad raíz (ej. `agregarItem(item) { items.add(item); item.setPadre(this); }`). |
| **Falta de Control de Concurrencia** | Sobrescritura silenciosa de datos (*Lost Updates*) cuando dos usuarios modifican el mismo registro. | Ausencia de atributo de versión o token de concurrencia optimista. | Incorporar atributo `@Version` (JPA) o `[Timestamp] / IsRowVersion` (EF Core) con control de excepciones. |
| **Fuga de Entidades hacia la API** | Errores de LazyInitializationException al serializar JSON o exposición accidental de columnas privadas. | Retornar entidades gestionadas directamente desde los controladores HTTP. | Proyectar siempre DTOs o ViewModels inmutables dedicados a la interfaz pública. |

---

## 2. Checklist Operativo de Revisión de Mapeo y Persistencia

- [ ] **Relaciones To-Many:** ¿Están configuradas como Lazy por defecto para evitar cargas masivas accidentales?
- [ ] **Índices en Claves Foráneas:** ¿Las columnas FK que participan habitualmente en JOINs cuentan con índice en base de datos?
- [ ] **Consultas en Loops:** ¿Se auditó que ningún método ejecute queries dentro de un `foreach` o `for`?
- [ ] **Proyecciones de Solo Lectura:** ¿Las consultas de reporte o lectura pura utilizan `AsNoTracking()` o proyecciones directas?
- [ ] **Delimitación Transaccional:** ¿Las operaciones mutadoras están delimitadas por transacciones atómicas con manejo de rollback?
