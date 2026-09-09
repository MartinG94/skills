# Guía de Heurísticas de Inferencia CRUD desde Casos de Uso

Esta guía proporciona las reglas sistemáticas para deducir de forma objetiva las operaciones **C (Create)**, **R (Read)**, **U (Update)** y **D (Delete)** sobre las clases de dominio analizando las secciones de un Caso de Uso o especificación funcional.

---

## 1. Mapeo Sistemático por Sección del Caso de Uso

| Sección del Caso de Uso | Operación Inferida | Clases Típicas Afectadas | Justificación y Evidencia Requerida |
|---|:---:|---|---|
| **Precondición** | **R** | Clases maestras, catálogos, estados previos | El sistema debe consultar y validar el estado o existencia previa de la entidad (ej. "El Cliente está activo"). |
| **Paso de Búsqueda / Selección** | **R** | Catálogos, entidades transaccionales | El actor visualiza una lista, busca por filtros o selecciona una opción de una grilla. |
| **Evaluación de Regla de Negocio** | **R** | Parámetros, políticas, límites de crédito | El sistema lee umbrales o valores de configuración para validar la viabilidad del flujo. |
| **Confirmación de Transacción** | **C** | Comprobantes, solicitudes, detalles | El sistema materializa y persiste una nueva entidad en el dominio (ej. nuevo Pedido, nueva Factura). |
| **Actualización Colateral de Estado** | **U** | Saldos, stock, estados de ciclo de vida | El flujo muta atributos de entidades preexistentes (ej. descontar stock en Depósito, cambiar estado a Pagado). |
| **Flujo de Cancelación / Desistimiento**| **U** o **D** | Transacciones en curso, reservas temporales | Muta estado a Cancelado (U) o remueve una reserva efímera en memoria (D). |
| **Postcondición Observable** | **C** o **U** | Entidades transaccionales y colaterales | Declara el estado persistido final alcanzado tras la finalización exitosa del flujo. |

---

## 2. Árbol de Indagación de Brechas (Preguntas de Negocio)

Cuando una entidad presente en el Modelo de Dominio carezca de operaciones en la matriz, el agente debe formular la pregunta de negocio adecuada en lugar de calificarla con términos dramáticos:

### A. Si la clase carece de Creación (Sin C)
- ¿Es una entidad de datos semilla (*Seed Data*) precargada en la inicialización del sistema?
- ¿Proviene de una sincronización externa o webhook desde otro sistema (`EXT`)?
- ¿Falta elicitar o está fuera de alcance el Caso de Uso de administración o alta de este catálogo?

### B. Si la clase carece de Lectura (Sin R)
- ¿Es un log de auditoría o tabla append-only que solo se consulta ante incidentes o inspecciones legales externas?
- ¿El reporte o pantalla que consume este dato pertenece a un módulo táctico/estratégico de una fase posterior?
- ¿Se trata de un requerimiento superfluo (*Gold Plating*) que no aporta valor a ningún actor?

### C. Si la clase carece de Actualización o Baja (Sin U / Sin D)
- ¿La entidad es conceptualmente inmutable (ej. Comprobante contable cerrado, historial de auditoría)? Si es inmutable, marcar como `N/A`.
- ¿La política de retención del negocio prohíbe el borrado físico de datos por exigencia legal o impositiva?
