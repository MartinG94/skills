# Realización de análisis

Lee esta referencia sólo para `analysis-rcu`.

## Participantes

- `Actor`: rol externo que inicia o participa en el escenario.
- `Boundary`: frontera del sistema para la interacción; captura y presenta, sin reglas
  de negocio.
- `Control`: coordina el caso de uso o evento del sistema y distribuye trabajo.
- `Entity`: representa información y comportamiento del dominio del problema.

No introduzcas clases de framework, base de datos, API o infraestructura. Una boundary
puede ser abstracta (`interfaz del sistema`) cuando la tecnología no está decidida.

## Asignación con los cinco GRASP

| Guía | Pregunta de decisión | Señal de abuso |
|---|---|---|
| Experto | ¿Quién posee la información para cumplir la responsabilidad? | El control calcula todo con datos ajenos. |
| Creador | ¿Quién contiene, registra, usa estrechamente o posee los datos de inicio? | Se aplica como regla absoluta ignorando acoplamiento. |
| Bajo acoplamiento | ¿La colaboración introduce dependencias evitables? | Se agregan intermediarios sin beneficio. |
| Alta cohesión | ¿Las responsabilidades del participante tienen un propósito enfocado? | Gestor o entidad acumula tareas heterogéneas. |
| Controlador | ¿Quién representa el sistema o el caso/evento? | La boundary coordina dominio o una entidad controla toda la UI. |

Balancea las guías: no existe una elección mecánica basada en una sola condición.

## Visibilidad

Para cada mensaje entre objetos, explica una ruta disponible en ese momento:

- referencia persistente por atributo/asociación;
- colaborador recibido como parámetro;
- objeto creado localmente;
- objeto devuelto por un mensaje anterior.

No dibujes una asociación permanente sólo para justificar una referencia temporal.

## Escenarios

Modela el flujo principal y cada alternativa significativa como diagramas separados si
combinarlos perjudica la legibilidad. Mantén los mismos nombres y numeración del CU.
Una realización de análisis puede omitir tipos, visibilidad y detalles de transporte.

Salida estática complementaria, sólo si se pide: clases BCE participantes y relaciones
necesarias para entender la colaboración.
