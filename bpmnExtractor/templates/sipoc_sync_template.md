# Matriz de Sincronización SIPOC ↔ BPD (sipoc-sync)

| Componente SIPOC | Ítem SIPOC | Elemento BPD Correspondiente | Tipo de Elemento BPMN | Cobertura / Estado | Evidencia / Observación |
|---|---|---|---|---|---|
| **S** (Supplier) | `S1: Proveedor Externo` | Pool Externa o Lane | `Participant / Lane` | Conforme | Envía insumo mediante message flow |
| **I** (Input) | `I1: Factura / Remito` | Objeto de Datos o Evento Inicial | `DataObject / MessageEvent` | Conforme | Ingresa al inicio del proceso |
| **P** (Process) | `P1: Registrar Recepción` | Tarea de Proceso | `userTask` en Lane Almacén | Conforme | Mapeo 1:1 con macroactividad |
| **P** (Process) | `P2: Control de Calidad` | Subproceso o Tarea | `manualTask` en Lane Calidad | Conforme | Incluye gateway de rechazo |
| **O** (Output) | `O1: Acta de Recepción` | Objeto de Datos o Mensaje Saliente | `DataObject` | Conforme | Generado al finalizar inspección |
| **C** (Customer) | `C1: Contabilidad / Cuentas a Pagar` | Lane Interna o Pool Destino | `Lane` o `Participant` | Conforme | Recibe acta y factura conformada |

## Diagnóstico de Brechas (Gaps)
- **Insumos Huérfanos:** Elementos de SIPOC que no ingresan a ninguna tarea del BPD.
- **Salidas No Producidas:** Resultados declarados en SIPOC sin actividad productora en el BPD.
- **Fronteras Incompatibles:** Discrepancias entre las macroactividades de SIPOC y los límites de inicio/fin del BPD.
