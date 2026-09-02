# FICHA DE PROCESO DE NEGOCIO: {{NOMBRE_DEL_PROCESO}}

## 1. Identificación y Alcance
| Atributo | Especificación |
| :--- | :--- |
| **Nombre del Proceso** | {{NOMBRE_PROCESO_INFINITIVO}} |
| **Dueño del Proceso (Owner)** | {{ROL_DUEÑO_DE_PROCESO}} |
| **Tipo de Proceso** | {{TIPO_PROCESO: Clave / Operativo / De Negocio | Estratégico | De Apoyo / Soporte}} |
| **Objetivo** | {{OBJETIVO_DE_NEGOCIO_Y_VALOR_GENERADO}} |
| **Disparador (Trigger)** | {{EVENTO_INICIAL_O_SOLICITUD}} |
| **Límite Inicial** | {{PRIMER_EVENTO_O_ACTIVIDAD}} |
| **Límite Final** | {{RESULTADO_FINAL_EXITOSO_O_ANOMALO}} |
| **Cliente(s) del Proceso** | {{CLIENTE_EXTERNO_O_INTERNO}} |
| **Productos / Salidas** | {{BIENES_SERVICIOS_O_RESULTADOS_ENTREGADOS}} |

---

## 2. Matriz de Proveedores e Insumos (SIPOC)
| Proceso / Entidad Proveedora | Insumo / Información Suministrada | Propósito en el Proceso |
| :--- | :--- | :--- |
| `{{PROVEEDOR_1}}` | `{{INSUMO_1}}` | `{{PROPOSITO_1}}` |
| `{{PROVEEDOR_2}}` | `{{INSUMO_2}}` | `{{PROPOSITO_2}}` |

---

## 3. Recursos del Proceso
* **Recursos Humanos (Roles / Lanes)**:
  - `{{ROL_1}}`: Responsable de {{TAREAS_ROL_1}}.
  - `{{ROL_2}}`: Responsable de {{TAREAS_ROL_2}}.
* **Recursos Tecnológicos / Sistemas de Soporte**:
  - `{{SISTEMA_1}}`: Módulos de soporte para registro, persistencia y control.
* **Recursos Físicos / Materiales**:
  - `{{RECURSOS_MATERIALES_O_INFRAESTRUCTURA}}`.

---

## 4. Formularios, Registros e Información
* **Formularios Estructurados**:
  - `{{FORMULARIO_1: ej. F-01 Nota de Pedido}}`.
* **Registros de Datos**:
  - `{{REGISTRO_1: ej. Datos del Cliente, Datos de la Transacción}}`.
* **Información Consumida / Emitida**:
  - Consumida: `{{INFO_CONSUMIDA: ej. Listado de Precios, Historial Crediticio}}`.
  - Emitida: `{{INFO_EMITIDA: ej. Factura Electrónica, Comprobante de Entrega}}`.

---

## 5. Reglas de Negocio (RN)
| Código | Denominación | Enunciado Formal de la Regla (Modo Imperativo) |
| :---: | :--- | :--- |
| **RN-01** | {{NOMBRE_RN_01}} | {{ACCION_O_RESTRICCION}} si {{CONDICION_EVALUADA}}. |
| **RN-02** | {{NOMBRE_RN_02}} | Para {{ACCION}}, es obligatorio que {{CONDICION}}. |

---

## 6. Restricciones Normativas y Legales
* `{{RESTRICCION_LEGAL_1: ej. Normativa Impositiva / Resolución AFIP}}`.
* `{{RESTRICCION_LEGAL_2: ej. Marco Regulatorio Sectorial / Normas IRAM}}`.

---

## 7. Indicadores de Desempeño del Proceso (KPIs)
| Identificador | Nombre del Indicador | Fórmula de Cálculo / Métrica | Frecuencia | Meta / Umbral Esperado |
| :---: | :--- | :--- | :---: | :---: |
| **KPI-01** | {{NOMBRE_KPI_01}} | `{{FORMULA_CALCULO_01}}` | {{FRECUENCIA_01}} | `{{META_01}}` |
| **KPI-02** | {{NOMBRE_KPI_02}} | `{{FORMULA_CALCULO_02}}` | {{FRECUENCIA_02}} | `{{META_02}}` |
