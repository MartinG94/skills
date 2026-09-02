# Guía de Referencia Técnica: Taxonomía BPMN 2.0 y Motor de Edición Incremental

Esta guía complementa la skill `bpmnExtractor` con especificaciones operativas detalladas sobre la taxonomía de elementos BPMN 2.0, el árbol JSON canónico (BPMN-IR), la gramática formal de edición y el catálogo completo de anti-patrones.

---

## 1. Taxonomía de Tareas BPMN 2.0

Cada tarea debe modelar una unidad atómica de trabajo. La asignación del tipo de tarea determina su nivel de automatización y semántica de ejecución:

| Tipo (`type`) | Icono / Semántica | Criterio de Selección | Ejemplo Práctico |
| :--- | :---: | :--- | :--- |
| `userTask` | 👤 | Tarea realizada por un ser humano con asistencia de una aplicación informática o ERP. | `Confeccionar Cotización`, `Aprobar Solicitud` |
| `serviceTask` | ⚙️ | Tarea 100% automatizada ejecutada por un servicio web, microservicio, daemon o base de datos. | `Solicitar CAE a AFIP`, `Calcular Impuestos` |
| `sendTask` | ✉️➡️ | Tarea automatizada que despacha un mensaje, notificación o documento a un participante externo. | `Enviar Factura por Email`, `Publicar Webhook` |
| `receiveTask` | ✉️⬅️ | Tarea que bloquea el proceso hasta recibir un mensaje o señal de un participante externo. | `Esperar Confirmación de Pago`, `Recibir Webhook` |
| `businessRuleTask`| 📋 | Tarea que delega la decisión a un motor de reglas de negocio (ej. Drools, Camunda DMN). | `Evaluar Score Crediticio`, `Determinar Descuento` |
| `manualTask` | ✋ | Tarea física realizada por un operador humano sin interacción de sistemas de software. | `Cargar Bultos en Camión`, `Armar Pallet` |
| `scriptTask` | 📜 | Tarea que ejecuta un script o fragmento de código interpretado por el propio motor BPMN. | `Formatear Cadena JSON`, `Calcular Hash` |
| `task` | ◻️ | Tarea genérica. Usar únicamente cuando no se dispone de suficiente información de automatización. | `Realizar Trámite` |

---

## 2. Taxonomía de Eventos y Disparadores

Los eventos modelan sucesos que ocurren durante el ciclo de vida del proceso:

| Elemento | `type` | `eventDefinition` | Comportamiento |
| :--- | :--- | :--- | :--- |
| **Start Event (Genérico)** | `startEvent` | `null` | Disparo manual o sin trigger específico. |
| **Message Start Event** | `startEvent` | `messageEventDefinition` | El proceso arranca al recibir un mensaje/documento externo. |
| **Timer Start Event** | `startEvent` | `timerEventDefinition` | El proceso arranca según un cronograma periódico (ej. medianoche). |
| **Intermediate Catch Timer**| `intermediateCatchEvent`| `timerEventDefinition` | El flujo se pausa durante un lapso de tiempo o hasta una fecha/hora. |
| **Intermediate Catch Message**| `intermediateCatchEvent`| `messageEventDefinition` | El flujo espera la llegada de un mensaje específico. |
| **Intermediate Throw Message**| `intermediateThrowEvent`| `messageEventDefinition` | El proceso emite un mensaje y continúa inmediatamente. |
| **End Event (Genérico)** | `endEvent` | `null` | Cierre normal y natural de la ruta de ejecución. |
| **Message End Event** | `endEvent` | `messageEventDefinition` | Finaliza la ruta emitiendo un mensaje/comprobante de cierre. |

---

## 3. Motor de Edición y Refactorización Incremental (BPMN Change Engine)

Cuando un usuario solicita modificar un proceso existente, el analista/agente aplica una o más de las **5 funciones de mutación atómica**:

```
add_element(element, before_id=None, after_id=None)
delete_element(element_id)
update_element(new_element)
move_element(element_id, before_id=None, after_id=None)
redirect_branch(branch_condition, next_id)
```

### 3.1. `add_element`
Inserta un nuevo elemento atómico o una compuerta completa (con sus ramas) antes o después de un nodo existente.
- **Regla**: Debe especificarse exactamente uno de `before_id` o `after_id`.
- **Payload JSON**:
```json
{
  "function": "add_element",
  "arguments": {
    "element": {
      "type": "serviceTask",
      "id": "task_validar_cuit",
      "label": "Validar CUIT en padrón AFIP",
      "lane": "Lane_Ventas"
    },
    "before_id": "task_draft_quote"
  }
}
```

### 3.2. `delete_element`
Elimina un elemento del proceso por su ID.
- **Eliminación en Cascada**: Si se elimina una compuerta (`exclusiveGateway`, `inclusiveGateway`, `parallelGateway`), se eliminan automáticamente todos los elementos contenidos en sus ramas internas.
- **Payload JSON**:
```json
{
  "function": "delete_element",
  "arguments": {
    "element_id": "task_cancel_quote"
  }
}
```

### 3.3. `update_element`
Reemplaza los metadatos (label, type, lane, eventDefinition) de un elemento manteniendo su ID y posición.
- **Payload JSON**:
```json
{
  "function": "update_element",
  "arguments": {
    "new_element": {
      "type": "businessRuleTask",
      "id": "task_eval_credit",
      "label": "Evaluar matriz de riesgo DMN",
      "lane": "Lane_Creditos"
    }
  }
}
```

### 3.4. `move_element`
Reubica un nodo existente a una nueva posición en el flujo de secuencia sin alterar sus propiedades internas.
- **Payload JSON**:
```json
{
  "function": "move_element",
  "arguments": {
    "element_id": "task_check_stock",
    "after_id": "start_solicitud"
  }
}
```

### 3.5. `redirect_branch`
Modifica el destino del flujo saliente de una rama condicional para crear un bucle (loopback) o dirigir hacia una tarea anterior o posterior.
- **Payload JSON**:
```json
{
  "function": "redirect_branch",
  "arguments": {
    "branch_condition": "Documentación incompleta",
    "next_id": "task_solicitar_doc"
  }
}
```

---

## 4. Detección de Intención Conversacional

Antes de ejecutar mutaciones, clasificar la solicitud del usuario:
1. **`intent: "modify"`**:
   - Descripciones de procesos nuevos ("Crea el proceso de compras...").
   - Comandos imperativos directos sobre un proceso existente ("Agrega un paso de validación", "Elimina el rechazo", "Si no paga, reintentar").
2. **`intent: "talk"`**:
   - Preguntas conceptuales ("¿Qué es un gateway inclusivo?").
   - Consultas de análisis sobre el proceso actual ("¿Quién es responsable de facturar?").
   - Solicitudes de explicación ("Describe el camino feliz del diagrama").

---

## 5. Catálogo Extendido de Anti-Patrones de Calidad (AP-01 a AP-12)

| Código | Anti-Patrón | Descripción | Corrección Obligatoria |
| :---: | :--- | :--- | :--- |
| **AP-01** | *Sequence Flow entre Pools* | Flecha sólida cruzando el límite exterior de una Pool hacia otra. | Reemplazar por **Message Flow** (`-.->`). |
| **AP-02** | *Message Flow intra-Pool* | Flecha discontinua conectando elementos dentro de una misma Pool o entre Lanes. | Reemplazar por **Sequence Flow** (`-->`). |
| **AP-03** | *Compuerta Huérfana / Asimétrica* | Compuerta de bifurcación abierta sin convergencia correspondiente o con cierre desbalanceado. | Incorporar nodo Join explícito (`has_join: true`) o cerrar con End Event en cada rama. |
| **AP-04** | *Nombres Ambiguos en Actividades* | Tareas con verbos vagos ("Procesar", "Gestión", "Datos"). | Renombrar con fórmula imperativa: `[Verbo Infinitivo] + [Objeto Directo]`. |
| **AP-05** | *Condiciones Ocultas en XOR* | Salidas de compuerta exclusiva sin etiquetas de condición booleanas. | Etiquetar cada flujo saliente con la condición excluyente evaluada. |
| **AP-06** | *Sumidero Negro (Deadlock)* | Flujo que ingresa a una rama sin compuerta de unión ni End Event. | Toda rama terminal debe culminar en un End Event específico. |
| **AP-07** | *Confusión Rol vs Organización* | Crear una Pool para cada empleado o puesto interno. | La organización es una única Pool; los puestos son **Lanes**. |
| **AP-08** | *Rama Paralela Vacía* | Definir una rama en `parallelGateway` sin tareas ni eventos ejecutables. | Todo camino paralelo debe contener al menos un elemento ejecutable. |
| **AP-09** | *Redirección / Bucle Colgante* | Un atributo `next` en una rama apunta a un ID de elemento que no existe. | Verificar que el ID referenciado exista previamente en el modelo. |
| **AP-10** | *Ambigüedad Tarea Manual vs Servicio* | Modelar tareas de software como manuales o tareas físicas como servicios. | Validar contra la matriz de automatización de la Sección 1. |
| **AP-11** | *Compuerta Inclusiva sin Default* | Compuerta OR sin rama predeterminada (`is_default: true`) arriesgando bloqueo si ninguna condición evalúa a True. | Definir una ruta default de contingencia sin condición. |
| **AP-12** | *Omisión de Evento de Fin en Excepción* | Rama de rechazo o error en XOR que no finaliza formalmente en un `endEvent`. | Agregar un `endEvent` etiquetado (ej. `Fin: Operación Cancelada`). |
