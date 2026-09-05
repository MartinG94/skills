# Heurísticas de elicitación y proveniencia

Lee esta referencia cuando haya varias fuentes, material heterogéneo o contradicciones. No la uses para completar el dominio con prácticas habituales.

## Mapa mínimo de fuentes

| Tipo de fuente | Qué puede aportar | Precaución |
| --- | --- | --- |
| Persona o taller | objetivos, necesidades, problemas y prioridades declaradas | distinguir opinión individual de acuerdo validado |
| Formulario o registro | datos usados y secuencia observable | un campo existente no prueba que siga siendo necesario |
| Manual o procedimiento | reglas y flujo prescripto | contrastar lo prescripto con lo que realmente se hace |
| Reporte | salidas e información de decisión | no inferir origen, frecuencia o destinatario ausente |
| Norma o contrato | restricciones externas | registrar versión, alcance y texto aplicable |
| Sistema existente | comportamiento actual | no convertir una limitación heredada en requisito futuro |

## Orden de trabajo

1. Inventariar fuentes con ID y localizador.
2. Extraer declaraciones sin reinterpretarlas.
3. Agrupar por objetivo, información, comportamiento, regla o restricción.
4. Contrastar coincidencias y contradicciones entre fuentes.
5. Normalizar solo después de conservar la evidencia original.

## Nivel de inferencia

- **Explícito:** la fuente declara directamente el elemento.
- **Derivado:** varias evidencias obligan lógicamente a la conclusión. Documentar las evidencias y la derivación; estado `pendiente_validacion`.
- **Hipótesis:** explicación plausible pero no necesaria. No crear un requisito; registrar `SUP` o pregunta.

Indicios débiles como “muchos usuarios”, “se usa Excel”, “a veces no hay red” o “se cobra con tarjeta” no autorizan por sí solos arquitectura offline, exportaciones, proveedores de pago, cifrado específico ni requisitos regulatorios. Pregunta por la necesidad y el contexto.

## Contradicciones y vacíos

- Conserva cada versión con su fuente.
- Enlaza el conflicto con los elementos afectados.
- Formula una pregunta neutral y señala si bloquea el alcance o la verificación.
- No decidas por autoridad aparente salvo que la fuente establezca formalmente esa autoridad.

## Cobertura

Al cerrar, indica:

- fuentes revisadas y fuentes no disponibles;
- fragmentos relevantes aún no clasificados;
- elementos derivados;
- decisiones, métricas o límites pendientes.
