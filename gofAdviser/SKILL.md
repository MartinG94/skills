---
name: gof-adviser
description: >-
  Evalúa si un problema de diseño justifica un patrón GoF y compara alternativas y
  consecuencias. Úsala para asesorar o refactorizar diseño existente; no para añadir
  patrones automáticamente a toda clase o caso de uso.
---

# Asesor de patrones GoF

Selecciona patrones desde las fuerzas del problema, no desde una palabra clave o smell
aislado. La respuesta correcta puede ser una mejora simple o `ningún patrón GoF`.

Cuando necesites comparar patrones o mapear participantes, lee
[references/pattern-selection.md](references/pattern-selection.md). No cargues el
catálogo completo si el usuario ya eligió un patrón y sólo pide explicarlo.

## Entradas

Obtén, en lo posible:

- comportamiento que debe variar o responsabilidad problemática;
- diseño/código actual y ejemplos de cambio esperado;
- restricciones de compatibilidad, rendimiento y complejidad;
- stack y alcance, sólo si se solicita implementación;
- perfil académico o profesional.

Si sólo hay una etiqueta como “God Class” o “muchos if”, inspecciona el contexto antes
de recomendar. Un síntoma no determina por sí mismo un patrón.

## Método

1. Formula el problema y qué aspecto se espera que cambie.
2. Identifica fuerzas: acoplamiento, cohesión, identidad, orden, cardinalidad,
   extensibilidad, ciclo de vida y costes operativos.
3. Establece una alternativa base sin patrón.
4. Compara como máximo tres candidatos pertinentes.
5. Descarta candidatos cuya intención o coste no encaje.
6. Si uno aporta valor neto, mapea participantes al dominio y explica consecuencias.
7. Valida la propuesta contra el diseño existente y los cambios previstos.

En contexto DSI/cátedra prioriza State, Strategy, Observer, Adapter e Iterator, sin
forzarlos. El catálogo GoF completo sigue disponible cuando el problema lo requiere.

## Límites

- No equipares `switch` con Strategy o State sin distinguir tipo de variación.
- No uses Observer para dividir cualquier clase grande; primero separa responsabilidades.
- No reemplaces colecciones idiomáticas por Iterator personalizado sin necesidad.
- No introduzcas Singleton para compartir estado o acceso a infraestructura por defecto.
- No combines varios patrones para demostrar cobertura académica.
- No prometas desacoplamiento total: todo patrón intercambia unas dependencias por otras.
- No afirmes mejora de rendimiento, mantenibilidad o testabilidad sin una consecuencia
  observable o una forma de validarla.

## Producto predeterminado

1. `Diagnóstico` — evidencia y fuerza de cambio.
2. `Opciones` — solución simple y patrones candidatos.
3. `Decisión` — patrón elegido o ninguno, con motivo.
4. `Participantes` — sólo si se elige patrón.
5. `Consecuencias` — beneficios, costes y riesgos en este contexto.
6. `Validación` — ejemplo de cambio futuro o comprobación estructural.

Un diagrama es opcional. Si aporta valor, usa Mermaid por defecto o el renderer pedido,
nunca dos representaciones equivalentes. Código y diffs sólo cuando el usuario solicite
implementación; usa el lenguaje, versión, convenciones y pruebas del proyecto.

## Criterios de cierre

- La intención del patrón coincide con el problema, no sólo con el vocabulario.
- Existe una comparación con una alternativa más simple.
- Los participantes tienen nombres y responsabilidades del dominio inspeccionado.
- Las consecuencias negativas y migración están visibles.
- No se generó código, infraestructura ni dependencias fuera del alcance.
