# Especificación de Historias de Usuario (Modo Historias)

**Producto / Módulo:** {{NOMBRE_PRODUCTO}}  
**Épica / Capacidad:** {{NOMBRE_EPICA}}  
**Fecha:** {{FECHA}}  

---

## 1. Tabla de Backlog de Historias de Usuario

| ID Historia | Narrativa (Como... Deseo... Para...) | RF / Capacidad Trazada | Prioridad MoSCoW | Estado |
|---|---|---|:---:|:---:|
| `US-01` | **Como** cliente registrado<br/>**Deseo** consultar el estado de mi envío en tiempo real<br/>**Para** planificar la recepción del paquete | `RF-04` | Must Have | Confirmada |
| `US-02` | **Como** analista de créditos<br/>**Deseo** visualizar el historial de moras del solicitante<br/>**Para** dictaminar el otorgamiento de líneas de crédito | `RF-08` | Should Have | Pendiente |

---

## 2. Fichas de Historia de Usuario

### `US-01`: {{Título de la Historia}}
- **Tarjeta de Negocio:**
  - **Como** {{Rol del usuario}}
  - **Deseo** {{Acción o capacidad requerida}}
  - **Para** {{Beneficio o valor de negocio esperado}}
- **Reglas de Negocio Asociadas:** `RN-02`, `RN-05`.
- **Criterios de Aceptación Observables:**
  - **Escenario 1 (Éxito):**
    - *Dado que* el usuario tiene un pedido confirmado con número de guía válido.
    - *Cuando* consulta el detalle del envío.
    - *Entonces* el sistema muestra la ubicación actual y el estado operativo del paquete.
  - **Escenario 2 (Error o excepción):**
    - *Dado que* la guía no existe o fue cancelada.
    - *Cuando* el usuario consulta el envío.
    - *Entonces* el sistema informa que la guía no se encuentra registrada sin exponer errores técnicos.
- **Conversaciones Pendientes y Puntos Abiertos:**
  - `OPEN-01`: {{Definir frecuencia de actualización de la ubicación GPS}}.
