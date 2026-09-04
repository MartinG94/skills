---
name: domain-model-gen
description: Genera un modelo conceptual del dominio en UML a partir de requisitos, procesos o relatos del negocio, con clases, atributos, responsabilidades y relaciones trazables. Úsala para comprender el problema y aplicar patrones de dominio ASI cuando correspondan; no para diseñar tablas, servicios, controladores ni arquitectura.
---

# Domain Model Generator

Modela los objetos importantes, las “cosas” y los eventos del entorno del sistema para crear vocabulario común. El producto predeterminado es **un diagrama conceptual y un registro breve de evidencia**.

## Entrada

- alcance o problema de negocio;
- requisitos, entrevistas, procesos o casos de uso disponibles;
- reglas que determinen relaciones, cantidades, vigencias o cálculos.

Asigna IDs de fuente y conserva página, sección, párrafo o marca de tiempo. Si el alcance o una regla estructural no está determinado, usa `TBD` y formula una pregunta.

## Límites

- Una clase de dominio representa un concepto del problema, no una pantalla, tabla, endpoint, servicio técnico o “sistema gestor”.
- No inventes clases, atributos, identificadores, estados, fechas, multiplicidades, métodos ni restricciones.
- Distingue `explícito` de `derivado`; toda derivación incluye evidencia, justificación y estado pendiente de validación.
- Los patrones son ayudas para descubrir una estructura, no plantillas que deban aplicarse siempre.

## Procedimiento

1. **Delimitar:** registrar objetivo, fuentes y conceptos fuera de alcance.
2. **Descubrir candidatos:** buscar objetos relevantes, eventos/transacciones, participantes, lugares, ítems, planes y agrupaciones. No conviertas automáticamente cada sustantivo en clase.
3. **Definir clases:** asignar propósito y evidencia. Un concepto meramente descriptivo puede ser atributo; sepáralo como clase solo si tiene identidad, propiedades, comportamiento o relaciones propias relevantes.
4. **Asignar atributos:** conservar información intrínseca respaldada. Los identificadores propios —número de pedido, código de artículo, patente, ISBN— son válidos. Evita únicamente representar como atributo una clave foránea que duplica una asociación conceptual.
5. **Aplicar patrones:** cuando el problema coincida con una estructura recurrente, leer [references/asi_domain_patterns.md](references/asi_domain_patterns.md), declarar patrón, evidencia y consecuencias. No reemplazar el lenguaje del dominio por nombres genéricos del patrón.
6. **Relacionar:** establecer asociación, agregación, composición o generalización y sus multiplicidades a partir de reglas del negocio. Si una multiplicidad no puede justificarse, omitirla del diagrama y registrarla como `TBD`.
7. **Asignar responsabilidades:** usar operaciones conceptuales como crear, mostrar, conocer, calcular o cambiar solo cuando las fuentes o el patrón las sustenten. Evitar firmas técnicas, repositorios, persistencia y tipos de implementación.
8. **Revisar:** comprobar vocabulario, trazabilidad, duplicados, ciclos de vida y consistencia con requisitos/CU.

## Decisiones estructurales

- **Transacción–detalle:** no fuerces composición ni `1..*`. Determina si el detalle existe independientemente y si una transacción puede iniciarse sin detalles.
- **Agregación/composición:** usa composición solo con dependencia fuerte de ciclo de vida explícita; agregación cuando la relación todo–parte no implica destrucción conjunta; asociación simple si solo se conoce el vínculo.
- **Ítem–ítem específico:** separa descripción compartida e instancia individual únicamente si el dominio distingue ambas.
- **Clase de asociación:** créala si el vínculo tiene datos, vigencia o responsabilidades propias.
- **Estado:** un atributo o clase de estado puede ser suficiente. Crea historial con fechas/responsable solo si se exige conservar cambios o vigencias. No confundas historial de negocio con el patrón de diseño Estado.
- **Plan/ejecución:** separa definición y ocurrencia real solo si ambas existen en la fuente.

## Notación

Usa la notación solicitada. Si no hay preferencia, genera un único `classDiagram` de Mermaid y decláralo como representación, no como UML interoperable. Si se requiere fidelidad UML, usa la herramienta correspondiente. No añadas visibilidad ni tipos de lenguaje: si se pide ese perfil, deriva el trabajo a `domain-design` en vez de mezclar niveles.

Incluye en el diagrama solo elementos sustentados.

## Salida predeterminada

```markdown
# Modelo de dominio — <problema o TBD>

## Alcance, fuentes y supuestos

## Catálogo de clases
| Clase | Propósito | Atributos / responsabilidades conceptuales | Patrón | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- |

## Patrones aplicados (solo si existen)
| Patrón | Clases en sus roles | Evidencia | Consecuencia de aplicarlo | Estado |
| --- | --- | --- | --- | --- |

## Diagrama conceptual
<un único diagrama>

## Relaciones y multiplicidades
| Origen | Relación | Destino | Multiplicidad | Justificación / evidencia | Estado |
| --- | --- | --- | --- | --- | --- |

## TBD y preguntas
| ID | Elemento afectado | Dato faltante / conflicto | Pregunta de validación |
| --- | --- | --- | --- |
```

## Criterio de término

- Cada clase y relación tiene propósito y evidencia.
- Cada multiplicidad y tipo de relación puede justificarse; lo demás es `TBD` fuera del diagrama.
- Los identificadores intrínsecos se conservan y no aparecen FK duplicadas.
- Las responsabilidades son conceptuales y coherentes con el nivel de análisis.
- Los patrones aplicados coinciden con el catálogo ASI y su contexto.
- No se introdujeron persistencia, UI, arquitectura ni tecnología.
- Se produjo una sola representación, salvo solicitud explícita.
