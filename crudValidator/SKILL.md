---
name: crud-validator
description: Construye una matriz de trazabilidad CRUD entre clases de dominio y casos de uso o requisitos, mostrando evidencia, cobertura y vacíos. Úsala como diagnóstico de consistencia; no presupone que toda clase necesite C, R, U y D ni genera requisitos o casos de uso para completar la matriz.
---

# CRUD Validator

Contrasta el modelo de dominio con el comportamiento especificado. La matriz es una ayuda de validación, no una prueba automática de completitud del sistema.

## Entrada mínima

- alcance del análisis;
- inventario de clases o entidades conceptuales;
- casos de uso descritos o requisitos funcionales con evidencia.

Si falta el modelo de dominio o el comportamiento, declara el resultado **parcial/no determinable**. No reconstruyas el artefacto ausente por intuición.

## Semántica

- `C` — se establece una nueva instancia o registro conceptual.
- `R` — se consulta o utiliza información existente.
- `U` — se modifica información o estado registrado.
- `D` — se elimina o finaliza una vigencia cuando esa semántica está expresada.
- `N/A` — la operación no corresponde y existe justificación.
- `EXT` — la información se origina o mantiene fuera del alcance.
- `?` — la evidencia no permite determinar la operación.

No traduzcas automáticamente estas letras a `INSERT`, `SELECT`, `UPDATE` o `DELETE`: las clases son conceptos del dominio, no tablas. “Baja” puede significar desactivación, fin de vigencia o eliminación; conserva la expresión de la fuente.

## Evidencia

- Cada celda con operación debe referenciar el paso de CU, RF o fragmento que la sustenta.
- Si una operación se deriva, marca `derivada`, explica la inferencia y déjala pendiente de validación.
- No infieras CRUD por el nombre del CU. Usa sus pasos o un RF descriptivo; si no están disponibles, marca `?` y registra la evidencia faltante.
- No inventes persistencia, actores, pantallas, estados, campos, seguridad, auditoría ni CU correctivos.

## Procedimiento

1. Normaliza IDs sin renombrar los artefactos fuente.
2. Delimita qué clases y CU/RF están dentro del alcance.
3. Recorre cada flujo o RF y registra las operaciones sustentadas.
4. Usa `N/A`, `EXT` o `?` en vez de forzar una letra.
5. Contrasta la matriz con afirmaciones explícitas del alcance.
6. Registra hallazgos y preguntas; no alteres los artefactos de entrada.

## Diagnósticos válidos

Un patrón solo es hallazgo si afecta el alcance o contradice evidencia:

- **Origen no identificado:** una clase es leída o modificada pero no se conoce cómo ingresa al alcance. Puede ser externa, precargada o faltar comportamiento.
- **Uso no identificado:** se crean datos pero no se observa uso posterior dentro del alcance. Puede existir retención, auditoría o un consumidor fuera del recorte.
- **Clase sin trazabilidad:** ninguna operación la conecta con los CU/RF analizados. Puede ser conceptual, derivada o estar fuera del alcance.
- **Operación esperada ausente:** la fuente exige explícitamente una capacidad y no existe traza correspondiente.
- **Inconsistencia:** CU, RF y modelo asignan significados incompatibles al mismo concepto.

No llames “fantasma”, “agujero negro”, “huérfana” o “balanceada” a una clase como conclusión definitiva sin resolver estas alternativas. La ausencia de `D` o de cualquier otra letra no es defecto por sí misma.

## Salida

Usa [templates/crud-matrix-report-template.md](templates/crud-matrix-report-template.md). El producto predeterminado contiene:

1. alcance e integridad de entradas;
2. matriz con evidencia por celda;
3. hallazgos y preguntas;
4. trazabilidad RF/CU–clase–operación;
5. límites del diagnóstico.

No añadas especificaciones de CU, reescritura de requisitos ni métricas porcentuales salvo petición explícita y método acordado.

Si el usuario solicita revisar además la calidad de los enunciados que alimentan la matriz, lee [references/ieee29148-quality-rules.md](references/ieee29148-quality-rules.md) y presenta esa revisión como sección opcional, no como certificación normativa.

## Criterio de término

- Toda celda no vacía tiene evidencia o una marca explícita de inferencia/incertidumbre.
- `N/A` y `EXT` incluyen justificación.
- Los hallazgos distinguen defecto confirmado, riesgo y dato faltante.
- No se exige cobertura CRUD uniforme.
- Las preguntas identifican la decisión necesaria y los artefactos afectados.
- El informe no agrega comportamiento inexistente a las fuentes.
