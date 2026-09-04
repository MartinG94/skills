# Diagnóstico de trazabilidad CRUD — [Sistema o alcance]

## 1. Alcance e integridad de entrada

- Clases analizadas: [IDs/nombres].
- CU o RF analizados: [IDs].
- Fuentes: [IDs/localizadores].
- Artefactos faltantes o incompletos: [lista o ninguno].
- Estado del diagnóstico: Completo para el alcance / Parcial / No determinable.

## 2. Matriz CRUD con evidencia

Use `C`, `R`, `U`, `D`, `N/A`, `EXT` o `?`. Cada operación debe incluir traza y origen (`explícita`/`derivada`); si es derivada, añada justificación y estado pendiente.

| Clase \ CU o RF | [CU-01] | [CU-02] | Cobertura observada | Observación |
| --- | --- | --- | --- | --- |
| [Clase] | C explícita [CU-01 paso 4] | R derivada [CU-02 paso 2; justificación; pendiente] | C, R | [sin interpretación no sustentada] |

## 3. Hallazgos y preguntas

| ID | Tipo | Clase / artefactos | Evidencia observada | Qué no se conoce | Impacto | Pregunta o acción de validación | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |

Tipos sugeridos: origen no identificado, uso no identificado, clase sin trazabilidad, operación esperada ausente, inconsistencia.

## 4. Trazabilidad consolidada

| RF | CU / paso | Clase | Operación | Origen | Derivación | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Revisión opcional de enunciados

[Incluir solo si fue solicitada. Registrar observación, evidencia, efecto sobre la matriz y pregunta; no certificar conformidad.]

## 6. Límites del diagnóstico

- `?` pendientes: [lista o ninguno].
- Elementos `EXT` y su fuente externa: [lista o ninguno].
- Recortes de alcance: [lista].
- Conclusiones que requieren validación: [lista o ninguna].
