# Matriz de Trazabilidad Integral de Punta a Punta ($E_1 \rightarrow E_2 \rightarrow E_3 \rightarrow E_4$)

Esta matriz audita que no existan eslabones rotos en el proyecto de mejora de procesos: todo problema diagnosticado debe tener una acción de intervención aprobada, un cambio en el proceso TO-BE, una métrica de verificación (KPI) y una tarea en el cronograma Gantt.

| E1: Encuadre / Criterio | E2: Evidencia Forense / Debilidad FODA | E3: Cruce CAME | E3: Acción de Valor (EERR) y Filtro | E4: Modificación en BPD TO-BE | E4: Indicador de Control (KPI) | E4: Tarea en Cronograma Gantt | Estado |
|---|---|---|---|---|---|---|---|
| `C1: Estrategia` / Reducción de costos por errores de despacho | `D2: Ruta Documental` / Demora de 48h por remito físico papel | `DO (D2 + O1)` / Digitalización con app móvil | `AV-01 (Crear)` / App chofer con remito digital (Viabilidad: APROBADA) | Eliminación de tarea manual de archivo físico; alta automática por API | `KPI-OPS-01`: Reducir Lead Time de 48h a 4h | `T-03`: Despliegue piloto de app choferes | Conforme |
| `C3: Problemas Operativos` / Falla SoD en recepción de almacén | `D1: Control Interno` / Operario recibe y da de alta stock sin control | `DA (D1 + A1)` / Segregación de roles y control ciego | `AV-03 (Reducir)` / Reasignación de roles y doble verificación | Split de actividades: Lane Depósito recibe; Lane Compras valida | `KPI-OPS-03`: 0% de discrepancias en inventario físico | `T-02`: Actualización de perfiles ERP y manual | Conforme |
| `C4: Cliente` / Falta de visibilidad de estado de entrega | `D3: Silos TI` / Sistema de tracking no dialoga con ERP | `DO (D3 + O2)` / Integración por APIs y webhooks | `AV-04 (Crear)` / Portal de seguimiento en tiempo real | Emisión de evento Kafka/Webhook al cambiar estado de viaje | `KPI-OPS-02`: Aumentar OTIF de 74% a 95% | `T-04`: Integración API de seguimiento vehicular | Conforme |

---

## Verificación de Integridad de la Cadena de Trazabilidad
1. **Regla de Cobertura Cero-Huérfanos:** Ninguna debilidad crítica de Etapa 2 puede quedar sin una Acción de Valor en Etapa 3.
2. **Regla de Viabilidad:** Toda Acción de Valor que ingrese a la Etapa 4 debe contar con el dictamen de **APROBADA** en el Filtro de Restricciones Operativas.
3. **Regla de Verificabilidad:** Toda Acción de Valor debe estar asociada al menos a un KPI (O1 o O2) y a una tarea programada con responsable en el Gantt.
