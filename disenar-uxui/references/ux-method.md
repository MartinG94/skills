# Método UX proporcional

Lee esta referencia cuando el pedido defina una experiencia nueva, cambie un flujo o deje decisiones importantes abiertas. El objetivo es tomar mejores decisiones de implementación, no producir ceremonias o entregables de investigación que nadie usará.

## 1. Construir el brief de experiencia

Separa hechos, restricciones, hipótesis y preguntas. Resume:

- objetivo de usuario y resultado de negocio;
- usuarios principales, capacidades, contexto y dispositivos;
- tarea crítica y frecuencia;
- contenido, datos, permisos y reglas;
- plataforma, marca, idioma y restricciones técnicas;
- qué conducta observable indicará éxito.

No completes datos desconocidos con una persona ficticia presentada como investigación. Si falta evidencia, usa un escenario o proto-perfil explícitamente hipotético y registra qué debería validarse.

## 2. Usar evidencia que cambie una decisión

Revisa primero el material disponible: producto actual, analytics compartidos, tickets, entrevistas, documentación, contenido, capturas y patrones del dominio. Elige una técnica adicional solo si puede resolver una incertidumbre concreta.

Ejemplos de relación decisión-evidencia:

| Incertidumbre | Evidencia útil | Decisión que informa |
|---|---|---|
| Los usuarios no encuentran contenido | inventario, tree test o card sorting | agrupación, rótulos y navegación |
| Un proceso se abandona | funnel, observación o prueba de tarea | pasos, fricción y recuperación |
| Hay dos conceptos de audiencia | entrevistas o datos de uso | prioridades y variantes del flujo |
| El vocabulario genera errores | consultas, soporte o test de comprensión | microcopy y términos de dominio |

No inventes muestras, citas, métricas ni resultados. Cuando no sea posible investigar, diseña la versión reversible de menor riesgo.

## 3. Arquitectura de información

Antes del layout visual:

1. inventaría contenido y acciones;
2. agrupa por tarea y modelo mental, no por estructura interna del sistema;
3. usa rótulos concretos en el lenguaje del usuario;
4. establece jerarquía, navegación, búsqueda y orientación solo donde aporten;
5. dibuja el recorrido feliz y las alternativas: cancelar, volver, corregir, reintentar y recuperar;
6. verifica que cada pantalla responda dónde estoy, qué puedo hacer y qué ocurrirá después.

Aplica revelado progresivo cuando reduzca carga sin ocultar información necesaria. No lo actives por un número fijo de opciones o campos.

## 4. Interacción y feedback

Para cada acción relevante define:

- disparador y resultado esperado;
- affordance o señal visible;
- feedback inmediato y estado persistente;
- prevención de error y forma de recuperación;
- foco posterior y anuncio no visual cuando corresponda;
- comportamiento con mouse, touch y teclado según el patrón.

Usa consistencia para reducir aprendizaje, pero conserva convenciones del dominio y de la plataforma. La familiaridad no justifica copiar un patrón que contradice la tarea.

Distingue el artefacto que necesitas: un task/user flow modela acciones y decisiones para completar una tarea; un journey map agrega etapas, canales, necesidades, emociones, fricciones y oportunidades. No produzcas ambos si uno no cambiará la implementación.

## 5. Contenido y confianza

- Escribe primero el contenido crítico y diseña alrededor de él.
- Usa verbos específicos en acciones y títulos que ayuden a decidir.
- Explica errores con qué ocurrió, qué se conserva y cómo continuar.
- Evita culpa, jerga interna, códigos técnicos y confirmaciones ambiguas.
- Considera expansión de texto, formatos locales, nombres largos y traducción cuando el producto los requiera.
- No presentes datos simulados como reales ni prometas una operación de backend inexistente.

## 6. Ética, privacidad y control

- Minimiza datos y permisos; pide cada dato sensible en contexto y explica finalidad y consecuencia.
- Mantén visibles y comparables consentimiento, rechazo, cancelación y baja.
- Evita opt-ins escondidos o preseleccionados, urgencia o escasez falsas, confirmshaming y recorridos deliberadamente asimétricos.
- No optimices clics, conversión o tiempo de uso a costa de comprensión, bienestar o libertad.
- No incorpores analytics, tracking, permisos del dispositivo ni transmisión de datos reales sin pedido y autorización.

## 7. Evaluación proporcional

Convierte el brief en escenarios comprobables. Prioriza efectividad, eficiencia y satisfacción para la tarea real. Usa SUS, HEART u otras métricas solo cuando el usuario pide investigación o instrumentación y existen población, método y tratamiento de datos definidos.

Antes de implementar, deja una nota de decisión breve con:

- usuario y tarea primaria;
- flujo y estados críticos;
- dirección visual;
- supuestos y riesgos;
- criterios de aceptación.
