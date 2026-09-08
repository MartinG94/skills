# Taxonomía ISO/IEC 25010:2011 usada por el perfil de cátedra

Lee esta referencia cuando un requisito de calidad deba clasificarse y la fuente no
traiga ya la categoría. Este catálogo identifica conceptos; no prueba conformidad con
la norma ni aporta métricas o umbrales reutilizables.

## Calidad del producto

| Característica | Subcaracterísticas del perfil 2011 | Pregunta discriminante |
|---|---|---|
| Adecuación funcional | completitud, corrección, pertinencia | ¿Las funciones cubren las tareas y producen el resultado correcto y útil? |
| Eficiencia de desempeño | comportamiento temporal, utilización de recursos, capacidad | ¿Qué tiempo, recursos o volumen límite debe observarse? |
| Compatibilidad | coexistencia, interoperabilidad | ¿Debe compartir entorno o intercambiar y usar información con otro producto? |
| Usabilidad | reconocimiento de adecuación, aprendizaje, operabilidad, protección frente a errores, estética de UI, accesibilidad | ¿Qué usuario debe reconocer, aprender u operar qué tarea y bajo qué condición? |
| Fiabilidad | madurez, disponibilidad, tolerancia a fallos, recuperabilidad | ¿Qué servicio debe continuar o recuperarse ante qué fallo o período de operación? |
| Seguridad | confidencialidad, integridad, no repudio, responsabilidad, autenticidad | ¿Qué activo o acción debe protegerse, frente a quién o qué amenaza, y qué resultado es verificable? |
| Mantenibilidad | modularidad, reusabilidad, analizabilidad, modificabilidad, testabilidad | ¿Qué cambio, diagnóstico o prueba debe realizarse y con qué esfuerzo observable? |
| Portabilidad | adaptabilidad, instalabilidad, reemplazabilidad | ¿A qué entorno debe adaptarse, instalarse o sustituir otro producto? |

## Calidad en uso

Usa calidad en uso sólo cuando el requisito describe el resultado que personas o
grupos obtienen al utilizar el producto en un contexto definido:

- **eficacia:** exactitud y completitud con que alcanzan objetivos;
- **eficiencia:** recursos usados en relación con esos resultados;
- **satisfacción:** utilidad, confianza, agrado o comodidad observables;
- **libertad de riesgo:** reducción de riesgos económicos, de salud/seguridad o
  ambientales;
- **cobertura del contexto:** desempeño en los contextos especificados y flexibilidad
  fuera del contexto inicialmente previsto.

No confundas `eficiencia` de calidad en uso con `eficiencia de desempeño` del
producto: la primera relaciona resultados del usuario con recursos; la segunda mide
comportamiento temporal, recursos técnicos o capacidad del sistema.

## Regla de clasificación

1. Conserva el texto y la fuente del RNF.
2. Identifica el objeto evaluado: producto o resultado de uso.
3. Elige la característica por significado, no por palabra clave.
4. Selecciona subcaracterística sólo si la evidencia permite discriminarla; de lo
   contrario deja la característica y marca la subcategoría `TBD`.
5. Si encajan varias categorías, separa requisitos con respuestas o medidas distintas,
   o conserva las alternativas pendientes de validación.

No reutilices cifras del material didáctico. Toda medida debe provenir del caso,
política aplicable o acuerdo explícito.
