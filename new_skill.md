---
name: quality-scenario-specifier
description: >-
  Convierte requisitos no funcionales en escenarios de calidad verificables sin
  inventar umbrales. Usa el formato de cátedra atributo–estímulo–respuesta por defecto
  y el escenario de seis partes sólo cuando el contexto lo requiere.
---

# Especificación de escenarios de calidad

Aclara qué cualidad se espera, ante qué condición y qué respuesta observable debe
producir el sistema. Especificar el requisito y diseñar su solución son tareas distintas.

## Elegir el perfil

- `course-3-field` — predeterminado para DSI/PPAI: atributo, estímulo, respuesta. Lee
  [references/scenario-profiles.md](references/scenario-profiles.md).
- `six-part` — úsalo si el usuario pide Bass/SEI, un escenario plenamente medible o si
  fuente, entorno y artefacto son necesarios para eliminar una ambigüedad. Lee la misma
  referencia y conserva `TBD` donde falte evidencia.
- `architecture-response` — sólo si el usuario pide tácticas, diseño o validación de
  arquitectura. Lee [references/tactics-and-validation.md](references/tactics-and-validation.md)
  después de especificar el escenario.

No conviertas automáticamente todos los escenarios de tres campos en seis partes.

## Entradas

Recopila únicamente lo disponible:

- texto del RNF, objetivo o preocupación del stakeholder;
- contexto/operación afectada y condiciones relevantes;
- atributo y modelo de calidad exigido por la consigna;
- umbral, unidad y método de medición aprobados;
- prioridad, justificación y carácter arquitectónicamente significativo si se conocen.

Una expresión como “rápido”, “siempre” o “seguro” es una ambigüedad que debe convertirse
en pregunta, no en un número ficticio.

## Flujo

1. Separa RNF de restricciones tecnológicas y requisitos funcionales.
2. Conserva la cita/paráfrasis del requisito original y su fuente.
3. Selecciona atributo/subcaracterística según el perfil solicitado.
4. Escribe estímulo y respuesta observable sin incluir la solución técnica.
5. Añade medida sólo si fue proporcionada, derivada de una política explícita o acordada.
6. Marca ambigüedades, conflictos y datos `TBD` con preguntas concretas.
7. Sólo en `architecture-response`, compara tácticas y propone cómo validar la respuesta.

## Reglas de evidencia

- No inventes latencia, disponibilidad, carga, cobertura, MTTR, tasa de error, RPO/RTO,
  presupuesto, número de usuarios ni porcentaje de éxito.
- No prometas valores absolutos, cero fallos, seguridad total ni pérdida nula sin un
  contrato que lo establezca y una estrategia de verificación apropiada.
- La `respuesta` describe comportamiento observable; productos, mecanismos y patrones
  son posibles tácticas, no respuestas.
- Si hay varias interpretaciones plausibles, conserva alternativas o pide decisión.
- Una prioridad o la etiqueta SPA debe tener justificación, no inferirse por el atributo.

## Modelo de calidad

En contexto de cátedra usa el perfil ISO/IEC 25010:2011 que figure en el material. No lo
presentes como edición vigente universal. Si el usuario pide la norma actual, confirma
la edición aplicable y no mezcles taxonomías silenciosamente.

## Producto predeterminado

1. `Inventario` — identificador, fuente y texto normalizado del RNF.
2. `Escenarios` — tabla atributo | estímulo | respuesta.
3. `TBD y preguntas` — medidas, entorno, prioridad o alcance faltantes.
4. `Conflictos` — escenarios que compiten entre sí o con restricciones.

Añade fuente/artefacto/entorno/medida, tácticas o plan de validación sólo para el perfil
que lo requiera. No generes arquitectura ni elijas tecnología como efecto colateral.

## Criterios de cierre

- Cada escenario se remonta a un requisito o supuesto explícito.
- Estímulo y respuesta son distinguibles y no contienen una solución disfrazada.
- Toda cifra tiene fuente, cálculo reproducible o estado `propuesto para acordar`.
- La taxonomía y su versión están declaradas.
- Las tácticas, si existen, incluyen alternativas, trade-offs y forma de validación.
