# Clasificación de requisitos no funcionales

La clasificación primaria sigue el enfoque de Análisis de Sistemas de la cátedra. Lee esta referencia al clasificar RNF o preparar una ERS.

## Taxonomía primaria

| Categoría | Uso operativo | Subcategorías habituales |
| --- | --- | --- |
| **Producto** | cualidades o restricciones del producto entregado | eficiencia/rendimiento, fiabilidad, seguridad, usabilidad |
| **Organizacional** | políticas y condiciones de la organización que desarrolla u opera | operacionales, de desarrollo, de entorno |
| **Externo** | obligaciones originadas fuera de la organización o proyecto | regulatorias, legislativas, éticas |

Clasifica por el origen y efecto del requisito, no por palabras clave. Una misma frase puede contener más de un requisito; sepáralos si tienen criterios de verificación diferentes.

## Especificación mínima

Todo RNF debe indicar, cuando la evidencia lo permita:

- comportamiento o restricción requerida;
- alcance: producto global o CU/función afectada;
- condición de observación;
- escala y criterio de aceptación;
- evidencia y estado de validación.

Si falta una medida, conserva el RNF, usa `TBD` en el dato faltante y formula una pregunta. No inventes un SLA o valor objetivo.

## Mapeos opcionales

FURPS+ o ISO/IEC 25010 pueden añadirse cuando el usuario lo solicite o cuando un contrato exija esa clasificación. Son vistas secundarias y no reemplazan la categoría institucional.

Mapea por significado y deja `TBD` ante duda. No atribuyas conformidad con una norma por usar sus nombres y no conviertas una categoría de calidad en una tecnología concreta.
