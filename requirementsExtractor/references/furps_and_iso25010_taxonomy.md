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


## Familias de Escalas de Medición para Desambiguación de RNF

Al elicitar y desambiguar requerimientos no funcionales (Planguage / ISO 25010), orienta las preguntas `OPEN-XXX` hacia escalas verificables:

| Dimensión de Calidad | Expresión Ambigua Habitual | Familia de Escala Observable | Métrica / Unidad Típica |
|---|---|---|---|
| **Usabilidad** | *"El sistema debe ser intuitivo y fácil de usar"* | Tiempo de inducción / Tasa de error | Tiempo en tarea $\le X\text{ min}$; Éxito en primer intento $\ge 90\%$; Escala SUS $\ge 80$. |
| **Rendimiento** | *"El sistema debe responder rápidamente"* | Comportamiento temporal percentilar | Latencia $\le X\text{ ms en P95}$; Rendimiento $\ge X\text{ transacciones/seg}$. |
| **Fiabilidad** | *"El sistema no debe caerse nunca"* | Disponibilidad y tolerancia a fallos | Uptime $\ge 99.9\%$ mensual; MTBF $\ge 720\text{ h}$; MTTR $\le 15\text{ min}$. |
| **Seguridad** | *"El sistema debe ser completamente seguro"* | Protección de accesos y confidencialidad | Cifrado TLS 1.3 / AES-256; MFA obligatorio; Registro de auditoría inmutable de accesos. |
| **Capacidad** | *"El sistema debe soportar muchos datos"* | Volumen y concurrencia nominal | Almacenamiento hasta $X\text{ TB}$; Concurrencia de $X\text{ usuarios simultáneos}$. |
