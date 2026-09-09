# Matriz de Diálogo Pantalla — Gestor (Estándar DSI)

Esta referencia estandariza la especificación formal del flujo de diálogo entre la interfaz de usuario (Boundary) y el controlador GRASP (Gestor de Caso de Uso) en la materia Diseño de Sistemas de Información.

---

## 1. Estructura de la Matriz de Diálogo

| Paso CU | Fase Interacción | Control Visual de Entrada | Evento UI Disparador | Método Invocado en Gestor | Control de Salida / Feedback | Validaciones & Heurísticas |
|---|:---:|---|---|---|---|---|
| 1 | Entrada | Botón / Menú Principal | `Click()` | `opcionRegistrarPedido()` | Pantalla se habilita; Grilla de clientes | H5: Habilitación controlada |
| 2 | Entrada | Grilla `dgvClientes` | `CellClick(fila)` | `tomarSeleccionCliente(id)` | Panel de productos visible; Ficha cliente | H1: Visibilidad de estado |
| 3 | Entrada | Selector `cboProductos` + `txtCantidad` | `Click(btnAgregar)` | `tomarProductoYCantidad(prodId, cant)` | Grilla `dgvItems` actualizada con subtotal | Validación: cantidad > 0 |
| 4 | Proceso | Botón `btnConfirmar` | `Click()` | `confirmarPedido()` | Diálogo modal de confirmación con total | Confirmación explícita |
| 5 | Consulta | Diálogo modal | `Click(btnAceptar)` | `procesarConfirmacion()` | Toaster éxito; Impresión comprobante | H1: Feedback de cierre |

---

## 2. Reglas de Desacoplamiento Arquitectónico

1. **La Interfaz es Pasiva:** La pantalla (`Boundary`) solo captura eventos de usuario (`Click`, `TextChange`) y delega inmediatamente al `Gestor`.
2. **Cero Lógica de Negocio en la UI:** La pantalla jamás calcula subtotales, totales, comisiones ni valida saldos crediticios; esas responsabilidades corresponden al dominio coordinado por el Gestor.
3. **Cero Acceso Directo a Persistencia:** La interfaz no invoca repositorios, DAOs ni ejecuta consultas a base de datos.
