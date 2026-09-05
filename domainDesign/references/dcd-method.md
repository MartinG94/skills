# Método para DCD de cátedra

Lee esta referencia sólo en modo `course-dcd`.

## Límite entre análisis y diseño

El modelo de análisis describe una solución lógica en el dominio del problema. El
modelo de diseño describe una solución física/específica en el dominio de la solución.
Por eso una clase conceptual no se copia mecánicamente: puede refinarse, dividirse o
ser acompañada por clases sin contraparte conceptual.

Artefactos de entrada frecuentes:

- casos de uso y escenarios;
- clases de análisis `boundary`, `control` y `entity`;
- realizaciones de casos de uso de análisis;
- modelo de dominio, estados y reglas;
- requisitos no funcionales y restricciones de tecnología.

Artefactos de diseño frecuentes:

- clases e interfaces suficientemente especificadas para implementación;
- realización de caso de uso de diseño para un escenario concreto;
- organización en paquetes, subsistemas o componentes cuando sea necesaria;
- arquitectura y despliegue sólo en el grado que el sistema requiera.

No todos los sistemas ni todas las consignas necesitan todas las vistas.

## Derivación operativa

Para cada mensaje relevante de la realización:

1. identifica el receptor que posee la información o responsabilidad;
2. define la operación en ese receptor;
3. determina cómo el emisor obtiene visibilidad: atributo/asociación, parámetro,
   creación local o retorno previo;
4. registra parámetros y resultado conocidos;
5. añade tipos y visibilidad con las convenciones del lenguaje sólo si están definidos;
6. verifica que los flujos alternativos no contradigan precondiciones o estados.

La clase de diseño debe indicar, cuando sea relevante, nombre, estereotipo/rol,
atributos con tipos, operaciones con parámetros y retorno, visibilidad, relaciones y
multiplicidades. Una ficha textual puede completar lo que el renderer no expresa bien.

## Responsabilidades

- Usa Experto para ubicar comportamiento donde está la información necesaria.
- Usa Creador como guía, balanceado con cohesión, acoplamiento y restricciones de ciclo
  de vida; no es una condición bicondicional.
- Un controlador coordina el evento del sistema, pero no debe absorber reglas que
  pertenecen a entidades u otros colaboradores.
- Pura Fabricación es válida cuando una responsabilidad técnica no pertenece de manera
  natural a una entidad, siempre que reduzca acoplamiento o mejore cohesión.

## Trazabilidad mínima

| Evidencia | Elemento de diseño | Responsabilidad | Estado |
|---|---|---|---|
| paso/escenario del CU | clase u operación | qué resuelve | confirmado/propuesto/TBD |

Marca como `TBD` multiplicidades, tipos o visibilidad que el material no permita
determinar. No rellenes el modelo para que “parezca completo”.

Base curricular: PUD/RUP de diseño, clases de diseño y realizaciones de CU de diseño.
