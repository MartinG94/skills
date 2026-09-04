# Revisión de enunciados que sustentan una matriz CRUD

Usa esta referencia solo si se pide revisar la calidad de RF/CU además de construir la matriz. Es una revisión heurística: no certifica cumplimiento con IEEE, ISO ni INCOSE.

## Comprobaciones

| Aspecto | Pregunta | Tratamiento |
| --- | --- | --- |
| Identidad | ¿El enunciado tiene un ID estable? | registrar ausencia; no renumerar sin autorización |
| Alcance | ¿Se sabe qué sistema o CU asume el comportamiento? | usar `TBD` y preguntar |
| Responsabilidad | ¿Puede distinguirse actor, sistema y elemento de dominio? | pedir aclaración si afecta la celda CRUD |
| Acción observable | ¿Se entiende qué información se crea, usa, cambia o finaliza? | no deducir una operación por una palabra aislada |
| Condiciones | ¿Las condiciones y alternativas relevantes están expresadas? | registrar el flujo o condición faltante |
| Consistencia | ¿Otros RF/CU usan el concepto con el mismo significado? | conservar versiones y exponer conflicto |
| Verificabilidad | ¿Existe un resultado observable? | formular criterio pendiente sin inventar métrica |
| Trazabilidad | ¿Existe fuente/localizador? | marcar el hallazgo como no sustentado |

## Límites de las heurísticas

- Una conjunción no demuestra que el requisito no sea atómico; revisa si expresa una sola capacidad inseparable.
- La voz pasiva no es un defecto si la responsabilidad queda inequívoca en el contexto.
- No sustituyas automáticamente `debe`, `debería` o `puede`; conserva la intención y consulta cuando la obligatoriedad sea ambigua.
- Palabras como “rápido” o “adecuado” requieren criterio observable, pero el valor debe provenir de una decisión válida.
- Una reescritura propuesta es una sugerencia separada del requisito aprobado.

## Salida opcional

| Artefacto | Observación | Evidencia | Efecto sobre CRUD | Pregunta / propuesta | Estado |
| --- | --- | --- | --- | --- | --- |

No agregues una puntuación global ni un umbral de aprobación sin un método acordado por el usuario.
