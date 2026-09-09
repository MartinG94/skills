# Especificación de Descomposición de Servicios y Arquitectura

**Sistema / Iniciativa:** {{NOMBRE_DEL_SISTEMA}}  
**Perfil de Trabajo:** `professional-decomposition` / `course-architecture` / `distributed-workflow`  
**Decisión Base:** Monolito Modular vs. Microservicios Distribuidos  
**Fecha:** {{FECHA}}  

---

## 1. Contexto, Fuerzas y Matriz de Trade-offs (ISO 25010)

| Atributo de Calidad | Monolito Modular | Microservicios Distribuidos | Decisión / Racional Técnico |
|---|---|---|---|
| **Latencia de Red** | Mínima (llamadas en memoria) | Mayor (saltos de red, serialización) | {{Evaluación según volumen}} |
| **Consistencia Transaccional**| Fuerte (ACID en base unificada) | Eventual (Sagas, compensaciones) | {{Impacto en integridad}} |
| **Complejidad de Despliegue** | Baja (pipeline y artefacto único) | Alta (orquestación, service discovery, CI/CD independiente) | {{Madurez del equipo}} |
| **Radio de Explosión (Blast)**| Mayor (un fallo puede tumbar la app)| Menor (aislamiento por contenedor) | {{Criticidad de tolerancia a fallos}} |
| **Escalado Elástico** | Escala todo el bloque | Escala solo el servicio saturado | {{Perfil de demanda}} |

**Decisión Arquitectónica:** Se adopta {{Monolito Modular / Microservicios}} debido a {{Justificación basada en las fuerzas anteriores}}.

---

## 2. Mapa de Subdominios y Bounded Contexts
| Subdominio | Clasificación | Bounded Context | Estrategia de Inversión |
|---|:---:|---|---|
| {{Nombre}} | **Core Domain** | `{{Contexto}}` | Desarrollo a medida; ventaja competitiva |
| {{Nombre}} | **Supporting** | `{{Contexto}}` | Código propio complementario |
| {{Nombre}} | **Generic** | `{{Contexto}}` | Adopción de COTS / SaaS / Librería estándar |

---

## 3. Matriz de Fronteras de Servicio y Propiedad de Datos
| Servicio Propuesto | Bounded Context | Responsabilidades Principales | Almacén de Datos (Ownership) | Contrato / Protocolo Público |
|---|---|---|---|---|
| `ServicioA` | {{ContextoA}} | {{Capacidades que gobierna}} | Esquema/Base `db_servicio_a` | REST / OpenAPI |
| `ServicioB` | {{ContextoB}} | {{Capacidades que gobierna}} | Esquema/Base `db_servicio_b` | Eventos Asíncronos / REST |

---

## 4. Trazabilidad de Casos de Uso Arquitectónicamente Significativos (CUAS)
| ID CUAS | Denominación del Flujo | Servicios Intervinientes | Modo de Coordinación |
|---|---|---|---|
| `CUAS-01` | {{Flujo transaccional crítico}} | `ServicioA` $\to$ `ServicioB` | Síncrono HTTP con Circuit Breaker |
| `CUAS-02` | {{Procesamiento asíncrono}} | `ServicioA` $\to$ Broker $\to$ `ServicioB` | Publicación de eventos / Outbox |

---

## 5. Estrategia de Consistencia Distribuida (Saga)
| Paso | Servicio Origen | Transacción Local Realizada | Evento Publicado / Comando | Transacción Compensatoria (Rollback) |
|---|---|---|---|---|
| 1 | `ServicioPedidos` | Crear pedido en estado `Pendiente` | `PedidoCreadoEvent` | Marcar pedido como `Cancelado` |
| 2 | `ServicioPagos` | Autorizar cobro con pasarela | `PagoAprobadoEvent` | Reembolsar cargo en pasarela |
| 3 | `ServicioStock` | Reservar ítems en depósito | `StockReservadoEvent` | Liberar reserva de inventario |
