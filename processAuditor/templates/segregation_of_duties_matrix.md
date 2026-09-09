# Matriz de Segregación de Incompatibilidad de Funciones (Segregation of Duties - SoD)

La segregación de funciones garantiza que ningún empleado o rol tenga el control total sobre todas las fases de una transacción operativa crítica (Custodia, Registro, Autorización, Conciliación).

---

## 1. Mapa de Incompatibilidades Teóricas

| Dimensión de Función | Custodia Física de Activos | Registro en Sistema / Contable | Autorización / Aprobación | Conciliación / Control Independiente |
|---|---|---|---|---|
| **Custodia Física** | — | **INCOMPATIBLE** | **INCOMPATIBLE** | **INCOMPATIBLE** |
| **Registro en Sistema** | **INCOMPATIBLE** | — | **INCOMPATIBLE** | **INCOMPATIBLE** |
| **Autorización** | **INCOMPATIBLE** | **INCOMPATIBLE** | — | Condicional |
| **Conciliación** | **INCOMPATIBLE** | **INCOMPATIBLE** | Condicional | — |

---

## 2. Matriz Operativa de Conflicto de Roles Observada

| Rol Evaluado | Funciones Combinadas Observadas | Naturaleza del Conflicto (SoD) | Nivel de Riesgo | Evidencia en el Caso | Acción Correctiva Propuesta |
|---|---|---|---|---|---|
| Responsable de Almacén | Recibe mercadería física (Custodia) y da de alta el stock en ERP (Registro) | Custodia + Registro contable | Crítico | Entrevista Almacén: "El jefe de depósito recibe y carga el remito directo" | Separar la recepción física del ingreso administrativo en sistema |
| Tesorero | Confecciona cheques (Ejecución) y concilia cuentas bancarias (Conciliación) | Ejecución + Conciliación | Crítico | Minuta Administración: "Tesorería concilia los extractos mensuales" | Transferir la conciliación a Contaduría o Auditoría Interna |
| Ejecutivo de Compras | Selecciona proveedor, adjudica compra y aprueba factura | Autorización + Adjudicación + Aprobación | Alto | Relevamiento Compras: "El comprador valida la factura para pago" | Aprobar compras mediante Comité o Gerencia y validar recepción en Almacén |
