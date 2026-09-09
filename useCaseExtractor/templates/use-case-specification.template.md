# Especificación Detallada de Caso de Uso

**Identificador:** `CU-{{NUMERO}}`  
**Nombre:** {{Verbo en Infinitivo + Objeto Directo}} (ej. Registrar Pedido)  
**Módulo / Subsistema:** {{NOMBRE_SUBSISTEMA}}  
**Tipo de Ejecución:** En línea (Síncrono) / Asíncrono / Batch programado  
**Frecuencia de Uso:** Alta (Diaria) / Media / Baja (Eventual)  
**Requisitos Trazados:** `RF-{{NUM}}`, `RF-{{NUM2}}`  
**Fecha:** {{FECHA}}  

---

## 1. Actores y Disparador
- **Actor Principal:** {{Rol que inicia la interacción para cumplir su meta de negocio}}.
- **Actores Secundarios / Pasivos:** {{Sistemas externos o roles receptores de notificaciones}}.
- **Disparador (Trigger):** {{Evento observable o decisión del actor que inicia el flujo}}.

---

## 2. Precondiciones y Garantías (Cockburn)
- **Precondiciones:** {{Estado necesario y verificado del sistema antes de iniciar}}.
- **Garantía de Éxito (Postcondición Primaria):** {{Estado final consistente y comprobantes persistidos tras la finalización exitosa}}.
- **Garantía Mínima (Postcondición de Cancelación / Fallo):** {{Estado preservado y compensaciones ante cancelación o error sin corromper datos}}.

---

## 3. Relaciones y Puntos de Extensión
- **Inclusiones (`<<include>>`):** `CU-XX` {{Nombre del caso de uso incluido obligatorio}}.
- **Extensiones (`<<extend>>`):**
  - Caso de Uso Extendido: `CU-YY`
  - **Punto de Extensión (Extension Point):** En el paso {{N}} del flujo principal.
  - **Condición de Extensión:** {{Condición bajo la cual se desvía la extensión}}.

---

## 4. Flujo Principal de Eventos (Curso Normal)

| Paso | Acción del Actor | Respuesta Observable del Sistema | Regla de Negocio |
|:---:|---|---|:---:|
| 1 | El actor solicita registrar un nuevo pedido. | El sistema valida permisos y presenta el formulario con número provisorio. | - |
| 2 | El actor selecciona el cliente y agrega productos con cantidades. | El sistema verifica stock disponible y calcula subtotales en pantalla. | `RN-01` |
| 3 | El actor confirma la operación. | El sistema valida el crédito disponible, persiste el pedido y emite confirmación. | `RN-02` |

---

## 5. Flujos Alternativos y de Excepción

### Flujo Alternativo 2a: Stock Insuficiente
- **Condición de Activación:** En el paso 2, la cantidad solicitada supera el stock disponible.
- **Acciones:**
  1. El sistema informa el stock máximo disponible para el producto.
  2. El actor puede modificar la cantidad o desestimar el ítem.
  3. El flujo retorna al paso 2 del curso normal.

### Flujo de Excepción 3a: Límite de Crédito Superado
- **Condición de Activación:** En el paso 3, el saldo del cliente es inferior al total.
- **Acciones:**
  1. El sistema bloquea la confirmación y emite mensaje de rechazo crediticio.
  2. El sistema preserva el pedido en estado `Borrador` sin comprometer inventario.
  3. El caso de uso finaliza preservando la Garantía Mínima.

---

## 6. Catálogo de Reglas de Negocio Asociadas
| Código | Enunciado Lógico de la Regla | Severidad | Mensaje de Error Asociado |
|---|---|:---:|---|
| `RN-01` | La cantidad solicitada de un ítem debe ser un entero positivo mayor a cero. | Bloqueante | "La cantidad mínima permitida es 1." |
| `RN-02` | El cliente no debe registrar facturas vencidas con más de 30 días de mora. | Bloqueante | "Cliente inhabilitado por mora preexistente." |

---

## 7. Criterios de Aceptación BDD (Opcional / Gherkin)
```gherkin
Escenario: Registro exitoso de pedido con stock y crédito disponible
  Dado que el cliente "C-100" no registra facturas vencidas
  Y el producto "P-200" tiene stock disponible de 50 unidades
  Cuando el vendedor confirma un pedido de 5 unidades de "P-200" para el cliente "C-100"
  Entonces el sistema emite el pedido en estado "Confirmado"
  Y el stock disponible de "P-200" se actualiza a 45 unidades
```
