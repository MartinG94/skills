---
name: requirements-extractor
description: Extrae y normaliza requisitos trazables desde entrevistas, minutas, documentos, formularios o notas de relevamiento. Úsala para construir un registro de RF/RNF, reglas, historias de usuario opcionales y preguntas abiertas; no para inventar una solución ni diseñar casos de uso, dominio o arquitectura.
---

# Requirements Extractor

Convierte evidencia de relevamiento en un registro de requisitos verificable. El producto predeterminado es un **registro Markdown conciso**; genera una ERS, historias o JSON solo si el usuario lo pide.

## Modos

- **Registro** (predeterminado): extraer, clasificar y dejar trazabilidad y pendientes.
- **ERS**: organizar evidencia suficiente con la estructura institucional. Leer [templates/requirements_specification.template.md](templates/requirements_specification.template.md).
- **Historias**: preparar un backlog breve de historias de usuario solo si se solicita ese artefacto.
- **JSON**: serializar el modo Registro conforme a [templates/extracted_requirements.schema.json](templates/extracted_requirements.schema.json). El schema valida estructura; [scripts/validate_requirements_semantics.py](scripts/validate_requirements_semantics.py) comprueba unicidad y referencias internas. No añadir además Markdown salvo solicitud.

No describas casos de uso, modelo de dominio, arquitectura, interfaz ni pruebas completas dentro de esta skill.

## Entradas

Acepta una o varias fuentes: entrevistas, minutas, documentos, formularios, manuales, reportes, normas o descripción de un sistema existente.

Antes de extraer:

1. Asigna a cada fuente un ID estable (`SRC-01`) y conserva su título o descripción.
2. Usa el localizador disponible: página, párrafo, fila, sección o marca de tiempo. Si la fuente no permite localizar, indícalo; no inventes uno.
3. Delimita el sistema o producto cuando la fuente lo permita. Si el alcance es incierto, regístralo como pregunta abierta.

Para fuentes extensas, mixtas o contradictorias, lee [references/elicitation_heuristics.md](references/elicitation_heuristics.md).

## Reglas de evidencia

- Cada RF, RNF, regla, restricción y dependencia debe citar al menos una fuente y localizador.
- Marca el origen como `explícito` si la fuente lo declara o `derivado` si varias evidencias obligan a la conclusión. En este último caso explica la derivación y déjalo pendiente de validación.
- Una posibilidad razonable, práctica habitual o decisión de diseño no es un requisito: conviértela en hipótesis o pregunta.
- No inventes actores, prioridades, campos, métricas, umbrales, volúmenes, tecnologías, integraciones, normas ni excepciones.
- Usa `TBD` únicamente para un dato necesario que la evidencia no determina y acompáñalo con una pregunta concreta.
- Conserva contradicciones; no elijas una versión ni propongas una resolución como decisión tomada.

## Extracción y normalización

1. **Extraer hechos:** necesidades, servicios, información, restricciones, problemas observados y mejoras solicitadas.
2. **Separar tipos:**
   - `RF`: comportamiento o servicio que debe brindar el sistema. Redactar con verbo en infinitivo.
   - `RNF`: requisito de producto, organizacional o externo; puede imponer calidad, proceso de desarrollo, entorno, entrega o cumplimiento. Usar la taxonomía de cátedra de [references/furps_and_iso25010_taxonomy.md](references/furps_and_iso25010_taxonomy.md).
   - `RN`: política, condición o cálculo propio del negocio.
   - `RES`: hecho contextual que delimita el relevamiento o las alternativas, pero no constituye una obligación del producto, del desarrollo ni de la entrega.
   - `DEP`: elemento externo del que depende el cumplimiento.
   - `SUP`: supuesto explícito o hipótesis analítica que requiere validación.
3. **Estructurar RF:** distinguir `global` y `detallado`; un RF detallado referencia a su RF global. No completar una descomposición CRUD por costumbre.
4. **Precisar sin fabricar:** si un RNF dice “rápido”, “seguro” o similar, conserva la necesidad y registra la métrica como `TBD`. Para preguntas útiles lee [references/ambiguity_detection_lexicon.md](references/ambiguity_detection_lexicon.md).
5. **Consolidar duplicados:** fusiona solo enunciados equivalentes y conserva todas sus evidencias. Mantén separados objetivos, condiciones o alcances distintos.
6. **Registrar conflictos y pendientes:** enlázalos con los IDs afectados.

Si un límite impone una obligación verificable sobre producto, desarrollo, entorno,
entrega o cumplimiento, clasifícalo como `RNF` institucional; usa `RES` solo para un
hecho de contexto no normativo. Si una frase contiene ambos, sepárala y conserva la
misma evidencia; no dupliques el enunciado en dos categorías.

No asignes prioridad salvo que la fuente la establezca o el usuario solicite una priorización con un criterio acordado.

## Modo Historias

Representa cada necesidad validable como una tarjeta breve:

`Como <rol de usuario> deseo <función del sistema> para poder <valor de negocio>.`

- Conserva la traza a RF/evidencia y separa tarjeta, conversación pendiente y confirmación.
- Redacta criterios de aceptación observables solo desde reglas y ejemplos conocidos; usa `TBD` si falta un dato, sin convertirlo en Gherkin salvo pedido.
- Si no se conocen rol, función o valor, la historia no está lista: registra la pregunta y no completa el hueco por intuición.
- No asigna prioridad, valor, sprint, puntos, horas ni tareas técnicas sin decisión del Product Owner o fuente equivalente.
- No reemplaza una ERS o un CU cuando el encargo exige esos artefactos.

Salida:

| ID | Historia | RF / evidencia | Estado |
| --- | --- | --- | --- |

Después incluye únicamente las conversaciones pendientes y los criterios de aceptación
de cada historia. Finaliza cuando cada tarjeta tiene rol, función, valor y confirmación
trazables, o queda marcada como no lista con su pregunta.

## Salida predeterminada

```markdown
# Registro de requisitos — <producto o TBD>

## Fuentes y alcance
<fuentes, límites conocidos y vacíos>

## Requisitos funcionales
| ID | Nivel / padre | Enunciado | Origen | Derivación / validación | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- |

## Requisitos no funcionales
| ID | Categoría | Enunciado / medida | Alcance | Origen | Derivación / validación | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Reglas, restricciones y dependencias
| ID | Tipo | Enunciado | Origen | Derivación / validación | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- |

## Supuestos y preguntas abiertas
| ID | Tipo | Afecta a | Enunciado / pregunta | Base / evidencia | Acción y estado |
| --- | --- | --- | --- | --- | --- |

## Conflictos
| ID | Afecta a | Versiones incompatibles con su evidencia | Pregunta de decisión | Estado |
| --- | --- | --- | --- | --- |

## Control de cobertura
<fuentes sin explotar, elementos derivados y TBD que bloquean validación>
```

No rellenes tablas con ejemplos ficticios. Si una sección no tiene elementos, indica “No identificado en las fuentes revisadas”.

Estados: `confirmado` requiere ratificación o baseline aprobado; una declaración aislada
queda `pendiente de validación`. `TBD` indica un dato necesario todavía desconocido y
siempre se vincula con una pregunta.
Una `hipotesis_analista` permanece pendiente; al validarse debe registrarse la fuente
que la confirmó y reclasificarse, no conservar una confirmación sin evidencia.

En modo JSON, después del schema comprueba: IDs únicos; `source_id` existentes;
`parent_id` que apunten a RF globales existentes; `target_ids` y IDs de cobertura
existentes. `coverage_control.blocking_tbd_ids` enumera exactamente los `OPEN-*`
bloqueantes con estado `abierto` o `diferido`. El JSON Schema estándar no expresa por
sí solo estas referencias cruzadas.
Desde la raíz del repositorio ejecuta:

```powershell
python .\requirementsExtractor\scripts\validate_requirements_semantics.py .\registro.json
```

## Criterio de término

Finaliza cuando:

- cada RF, RNF, regla, restricción y dependencia tenga ID, redacción y evidencia; cada supuesto declare su base y, si proviene de una fuente, su evidencia;
- los RF detallados tengan un RF global padre válido;
- toda cifra o tecnología provenga de fuente identificada;
- los derivados, conflictos y `TBD` estén visibles;
- no se hayan convertido decisiones de análisis/diseño en requisitos;
- se haya generado solo el formato solicitado.

Consulta [examples/logistics_stakeholder_interview_case.md](examples/logistics_stakeholder_interview_case.md) únicamente si hace falta ver un ejemplo breve de trazabilidad y `TBD`.
