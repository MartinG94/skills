# Matriz de Intensidad de Humanización

Define los niveles de intervención al procesar un texto o respuesta de IA, equilibrando fidelidad al borrador original y grado de inyección de voz humana.

---

## Tabla Resumen de Niveles

| Nivel | Nombre | Grado de Intervención | Cuándo Usarlo | Riesgo de Alteración |
|---|---|---|---|---|
| `light` | **Editorial Mínimo** | Bajo (5-15% del texto modificado) | Borradores ya avanzados, código documentado, textos donde la voz del autor debe respetarse estrictamente. | Muy bajo: no modifica estructura global. |
| `medium` | **Equilibrado (Predeterminado)** | Moderado (25-45% del texto modificado) | La mayoría de las salidas de IA: artículos, explicaciones técnicas, correos profesionales, resúmenes. | Bajo: reestructura oraciones monótonas sin alterar argumentos. |
| `aggressive` | **Reescritura Profunda** | Alto (50-80% del texto modificado) | Textos con alta concentración de clichés de IA, respuestas de chatbot excesivamente complacientes o textos estériles sin pulso. | Moderado: reconstruye cadencia, añade opiniones explícitas y altera el orden de exposición. |

---

## Detalle por Nivel

### 1. Nivel `light` (Intervención Quirúrgica)
- **Alcance**:
  - Elimina clichés evidentes de IA (*delve, tapestry, serves as a testament, pivotal role*).
  - Suprime muletillas de chatbot iniciales y finales (*¡Por supuesto!, ¡Espero que esto te sirva!*).
  - Elimina guiones largos excesivos y dobles negritas decorativas.
  - Corrige evasión de cópula (*"se erige como"* → *"es"*).
- **Conserva**:
  - Longitud global de párrafos.
  - Estructura general de secciones y argumentos.
  - Nivel de formalidad intacto.

### 2. Nivel `medium` (Intervención Estructural y Rítmica - Predeterminado)
- **Alcance**:
  - Aplica todo lo de `light`.
  - **Quiebre de monotonía (Burstiness)**: fusiona o divide oraciones para romper la uniformidad de 15-20 palabras.
  - **Eliminación de conectores mecánicos**: suprime o reemplaza *Además*, *Asimismo*, *Por otra parte* al inicio de frases.
  - **Sustitución de andamiaje abstracto**: cambia *"múltiples factores"* o *"en términos de"* por conceptos concretos.
  - **Tono sobrio y directo**: elimina paralelismos negativos (*"no es solo X, es Y"*) y fórmulas de regla de tres.
- **Resultado**: Prosa limpia, natural, fácil de leer y libre de sospechas estadísticas de IA.

### 3. Nivel `aggressive` (Reescritura de Autor con Voz y Pulso)
- **Alcance**:
  - Aplica todo lo de `medium`.
  - **Inyección de postura y opinión**: permite frases en primera persona si el género lo admite (*"En mi experiencia...", "El problema central radica en..."*).
  - **Contraste de ideas vivo**: expone tensiones, dudas razonables y matices humanos en lugar de balances tibios de relaciones públicas.
  - **Reorganización discursiva**: descarta secciones predecibles de "Desafíos" y reorganiza el flujo para liderar con el hallazgo o desenlace más potente.
  - **Cadencia conversacional inteligente**: permite frases cortas de 3 a 5 palabras para énfasis dramático, seguidas de desarrollos minuciosos.
- **Resultado**: Texto indistinguible de un ensayo, artículo o informe escrito por un profesional senior con estilo propio.
