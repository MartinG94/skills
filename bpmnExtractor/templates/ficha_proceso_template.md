# Ficha Descriptiva del Proceso de Negocio

## 1. Identificación y Alcance
| Atributo | Definición / Contenido | Evidencia / Cita |
|---|---|---|
| **Nombre del Proceso** | {{Verbo infinitivo + Objeto + Contexto}} | {{EV-01}} |
| **Código / ID** | `PRC-{{CODIGO}}` | {{EV-01}} |
| **Dueño del Proceso (Owner)** | {{Rol organizacional responsable de extremo a extremo}} | {{EV-02}} |
| **Tipo de Proceso** | Estratégico / Operativo (Clave) / Soporte | {{EV-03}} |
| **Disparador (Trigger)** | {{Evento o solicitud que da inicio a la ejecución}} | {{EV-04}} |
| **Límite Inicial** | {{Primera actividad observable al recibir el disparador}} | {{EV-05}} |
| **Límite Final** | {{Resultado final observable o entrega al cliente}} | {{EV-06}} |
| **Cliente del Proceso** | {{Destinatario del producto o servicio generado}} | {{EV-07}} |
| **Producto / Valor Entregado** | {{Resultado concreto que satisface la necesidad del cliente}} | {{EV-08}} |

---

## 2. Recursos del Proceso
| Categoría de Recurso | Detalle de Recursos Requeridos | Responsabilidad en el Proceso |
|---|---|---|
| **Humanos (Roles / Lanes)** | {{Lista de roles organizacionales intervinientes}} | {{Responsabilidad asignada}} |
| **Tecnológicos / Sistemas** | {{Sistemas ERP, CRM, bases de datos o servicios web}} | {{Interacción o soporte brindado}} |
| **Físicos / Infraestructura** | {{Depósitos, talleres, terminales móviles, equipamiento}} | {{Uso físico en el flujo}} |

---

## 3. Formularios, Registros e Información (FRI)
| Tipo | Código / Nombre | Propósito en el Proceso | Soporte / Persistencia |
|---|---|---|---|
| **Formulario (Captura)** | `F-{{NRO}}` {{Nombre Formulario}} | Captura de datos iniciales o transaccionales | Físico / Digital / Web UI |
| **Registro (Persistencia)** | `REG-{{NRO}}` {{Nombre Registro}} | Registro persistido de la transacción en sistema | Base de Datos / ERP |
| **Información (Consumida/Emitida)** | `INF-{{NRO}}` {{Nombre Información}} | Documentos, comprobantes o estados consultados | Comprobante fiscal / Reporte |

---

## 4. Reglas de Negocio Formalizadas
| Código | Denominación | Enunciado Lógico (Acción obligatoria + Condición) | Fuente / Evidencia |
|---|---|---|---|
| `RN-01` | {{Nombre de la regla}} | El sistema/rol DEBE {{acción}} SI {{condición de negocio}}. | {{EV-09}} |
| `RN-02` | {{Nombre de la regla}} | No se autorizará {{acción}} CUANDO {{condición de bloqueo}}. | {{EV-10}} |

---

## 5. Restricciones Normativas y de Cumplimiento
- **Restricción 1:** {{Leyes, normativas de AFIP/ARCA, ISO, GDPR o políticas internas aplicables}}.
- **Restricción 2:** {{Políticas de seguridad o auditoría obligatorias}}.

---

## 6. Indicadores Clave de Desempeño (KPIs)
| ID KPI | Nombre del Indicador | Fórmula de Cálculo | Frecuencia | Meta / Umbral Esperado |
|---|---|---|---|---|
| `KPI-01` | Lead Time del Proceso | $\text{FechaHoraFin} - \text{FechaHoraInicio}$ | Mensual | $\le 24$ horas |
| `KPI-02` | Tasa de Rechazo / Desvíos | $(\text{Rechazos} / \text{TotalSolicitudes}) \times 100$ | Semanal | $\le 3\%$ |

---

## 7. Secuencia de Actividades y Tratamiento de Excepciones
| ID Actividad | Carril / Rol | Tipo de Tarea | Descripción Operativa | Regla Asociada | Salida / Estado |
|---|---|---|---|---|---|
| `ACT-01` | {{Rol}} | `userTask` | {{Descripción de la acción}} | `RN-01` | Solicitud Registrada |
| `ACT-02` | {{Sistema}} | `serviceTask` | {{Verificación automática}} | `RN-02` | Score Obtenido |
