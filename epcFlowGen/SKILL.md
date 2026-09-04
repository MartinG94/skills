---
name: epc-flow-gen
description: >-
  Analiza y coordina la resolución de Ejercicios Prácticos Complementarios (EPC) de
  Análisis o Diseño de Sistemas: descompone la consigna, identifica los artefactos
  pedidos, selecciona las skills especializadas y ensambla una entrega trazable sin
  inventar datos. Usar cuando el usuario aporte o mencione un EPC académico; no usar
  para diseñar interfaces ni diagramas Event-driven Process Chain.
---

# Orquestador de Ejercicios Prácticos Complementarios (EPC)

## Alcance

En el material de ASI/DSI, **EPC significa Ejercicio Práctico Complementario**. Es una
consigna académica integradora cuyo contenido cambia entre ejercicios: puede pedir
modelos de análisis, DTE, DSD, DCD, patrones, persistencia o vistas de arquitectura.
La carpeta heredada `epcFlowGen` se conserva por compatibilidad; el nombre invocable
es `epc-flow-gen`. La skill no define una notación propia ni una secuencia fija de
artefactos.

Usar esta skill para:

- convertir una consigna EPC en un plan de resolución verificable;
- ejecutar o coordinar únicamente los artefactos que la consigna exige;
- mantener trazabilidad entre cada ítem, la evidencia del caso y su entregable;
- ensamblar y revisar la entrega sin duplicar la labor de las skills especialistas.

No usarla para inferir flujos de pantalla, campos, botones o controladores. Si una
consigna pide explícitamente una interfaz o prototipo, derivar esa parte a
`design-ux-ui`. Si la sigla EPC es ambigua y el documento no identifica la materia ni
el tipo de ejercicio, pedir una aclaración breve antes de elegir el significado.

## Fuentes e información necesaria

Aplicar esta prioridad cuando haya diferencias:

1. instrucciones explícitas del usuario;
2. consigna, versión y criterios de evaluación del EPC entregado;
3. descripción del dominio y anexos asociados al mismo EPC;
4. material de la cátedra aplicable a ese artefacto;
5. convenciones generales, solo cuando no contradigan las fuentes anteriores.

Entrada mínima: la consigna o una reproducción fiel de sus ítems. Registrar, cuando
estén disponibles, materia, nombre, versión, objetivo, contenidos evaluados, dominio,
criterios de evaluación y formato solicitado. No detener todo el trabajo por un dato
ausente: resolver los ítems sustentados y marcar el resto como pendiente.

Primero leer la identificación, el objetivo, la consigna y los criterios. Después
leer solo los fragmentos del dominio y las referencias necesarios para los artefactos
seleccionados; no recorrer indiscriminadamente todo el material académico.

## Flujo de trabajo

### 1. Inventariar la consigna

- Conservar la numeración y los subítems originales (`1`, `2.a`, `2.b`).
- Separar cada verbo de entrega: construir, listar, justificar, comparar, modelar o
  explicar. No fusionar productos distintos en una respuesta genérica.
- Identificar restricciones de notación, escenario, patrón, vista y nivel
  análisis/diseño. No sustituir el artefacto pedido por otro más moderno o cómodo.

### 2. Crear la matriz de cobertura antes de modelar

Usar esta estructura compacta:

| Ítem | Artefacto o respuesta exigida | Evidencia necesaria | Skill responsable | Estado |
|---|---|---|---|---|
| `1` | `[entregable literal]` | `[fuente/sección]` | `[skill]` | `pendiente` |

Estados permitidos: `pendiente`, `en curso`, `resuelto`, `parcial` y `no aplica`.
Justificar siempre los dos últimos. Cada ítem debe aparecer una sola vez. La matriz es
un control de cobertura, no un segundo desarrollo del contenido.

### 3. Enrutar únicamente los artefactos pedidos

| Pedido de la consigna | Skill primaria |
|---|---|
| Relevamiento, RF/RNF, historias de usuario o reglas de negocio | `requirements-extractor` |
| Clasificación del sistema, alcance, viabilidad o PUD | `system-classifier` |
| BPMN o ficha de proceso | `bpmn-extractor` |
| Modelo o descripción de caso de uso | `use-case-extractor` |
| RCU de análisis, clases BCE, DSD o responsabilidades GRASP | `grasp-sequence-realizer` |
| Modelo o diagrama de clases de análisis/dominio | `domain-model-gen` |
| Matriz CRUD o cobertura entidad–caso de uso | `crud-validator` |
| Escenario de calidad | `quality-scenario-specifier` |
| DTE o matriz de transición de estados | `mermaid-diagram-gen` |
| Consideración o patrón GoF | `gof-adviser` |
| DCD o estructura de clases de diseño | `domain-design` |
| Mapeo relacional o DDL | `relational-object-map` |
| Arquitectura, subdominios, microservicios o C4 | `microservice-decomposer` |
| Consistencia entre modelos ya producidos | `uml-consistency` |
| Interfaz o prototipo pedido de forma explícita | `design-ux-ui` |

Una fila puede requerir dos skills solo cuando la consigna combina explícitamente
dos productos, por ejemplo DSD más patrón GoF. No cargar ni invocar el catálogo
completo por defecto. Las skills de API, ORM, frontend o testing son downstream y
solo corresponden si la consigna solicita esos productos.

### 4. Resolver con trazabilidad

- Etiquetar cada sección de la entrega con el ítem de consigna que satisface.
- Para cada decisión no trivial, registrar la fuente como archivo y página, sección
  o fragmento identificable. Una cita respalda un dato; la decisión de modelado debe
  explicitar además su derivación.
- Reutilizar los mismos nombres, identificadores y reglas entre diagramas. Introducir
  un alias solo si se documenta la equivalencia.
- Producir una sola notación de diagrama, salvo que la consigna o el usuario pidan
  más de una.
- Cuando una skill especialista ofrezca productos adicionales, omitirlos si no
  satisfacen ningún ítem.

### 5. Validar y ensamblar

Revisar primero cada artefacto con sus criterios propios y después verificar:

- cobertura: todos los ítems están resueltos o tienen un estado pendiente explícito;
- nivel: análisis y diseño no se mezclan ni se reemplazan entre sí;
- consistencia: actores, clases, mensajes, estados, reglas e identificadores coinciden;
- justificación: cada patrón o decisión responde a una consideración de la consigna;
- formato: se respetan notación, escenario, vistas y medio de entrega pedidos.

Usar `uml-consistency` únicamente cuando existan varios modelos que realmente deban
compararse. No inventar artefactos auxiliares solo para ejecutar una validación.

## Control de no invención

Distinguir siempre entre:

- **dato fuente**: expresado en la consigna o el dominio;
- **derivación**: consecuencia necesaria y explicable del dato fuente;
- **supuesto propuesto**: alternativa no confirmada, nunca presentada como hecho;
- **pendiente**: información indispensable que no está disponible.

No completar por conveniencia actores, casos de uso, estados, transiciones,
multiplicidades, atributos, métodos, métricas, infraestructura, tecnologías o reglas
de negocio. No copiar soluciones de otro EPC ni convertir ejemplos docentes en
requisitos del caso actual. Si falta un dato que cambia materialmente la solución,
marcar el punto como pendiente, explicar su impacto y formular una pregunta concreta;
continuar con los demás ítems.

No aplicar un patrón, una arquitectura distribuida o una tecnología porque aparezca
en una skill. Usarlos solo cuando la consigna los exige o la evidencia del problema
justifica la decisión, dejando explícito el razonamiento.

## Contrato de salida

Adaptar el formato al solicitado por el usuario. Si no se especifica, entregar:

1. **Identificación y alcance**: EPC, versión/fuente y escenario resuelto.
2. **Matriz de cobertura**: ítem → artefacto → evidencia → skill → estado.
3. **Resolución por ítem**: los artefactos en el orden de la consigna.
4. **Supuestos y pendientes**: solo los que afecten el resultado.
5. **Control final**: cobertura y consistencia, con discrepancias concretas.

Finalizar cuando cada ítem tenga un entregable verificable o un pendiente justificado.
No añadir teoría de la materia, prototipos, código ni artefactos no solicitados.
