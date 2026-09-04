# Decisiones de mapeo relacional

## Matriz base

| Elemento OO | Pregunta | Resultado relacional posible |
|---|---|---|
| Clase persistente | ¿Tiene identidad y ciclo de vida persistente? | tabla o parte de estrategia de herencia |
| Atributo simple | ¿Dominio, precisión, longitud, opcionalidad? | columna con tipo/restricción por decidir |
| Objeto de valor | ¿Se consulta/reutiliza por separado? | columnas embebidas o tabla dependiente |
| 1:1 | ¿Quién depende de quién y es opcional? | FK única en el lado adecuado o tabla compartida |
| 1:N | ¿Cuál es el lado dependiente? | FK en el lado N, con nulabilidad conocida |
| N:M | ¿El vínculo tiene datos/identidad? | tabla puente o entidad asociativa |
| Herencia | ¿Qué consultas e invariantes dominan? | TPH, TPT, TPC o composición alternativa |

No decidas por la forma visual solamente. Una asociación conceptual puede requerir una
entidad asociativa y una composición puede conservar historial después de terminar la
relación en memoria.

## Identidad

Separa:

- identidad del dominio;
- clave candidata/natural;
- clave técnica/surrogada;
- claves externas provenientes de otros sistemas.

No reemplaces automáticamente la identidad del dominio con una clave técnica. Si se usa
una clave surrogada, conserva las restricciones únicas que protegen la regla de negocio.

## Tipos

Primero describe el dominio lógico: texto, entero, decimal con precisión, fecha civil,
instante temporal, booleano, binario, enumeración, identificador. La traducción a un
tipo físico depende del motor y versión.

Preguntas que no deben resolverse por defecto:

- longitud máxima y soporte Unicode;
- precisión/escala monetaria;
- zona horaria y semántica de fecha/instante;
- representación y evolución de enumeraciones;
- formato de identificadores;
- cifrado, hashing o clasificación de datos sensibles.

## Herencia

| Estrategia | Ventaja típica | Coste típico |
|---|---|---|
| TPH / tabla única | consultas polimórficas simples | columnas opcionales y restricciones por subtipo difíciles |
| TPT / tabla por tipo | estructura normalizada por nivel | joins y escrituras más complejas |
| TPC / tabla concreta | lectura de subtipo independiente | duplicación y consultas polimórficas costosas |

También considera reemplazar herencia por composición si el modelo de objetos lo admite;
no alteres el dominio sólo para acomodar una preferencia de base de datos.

## Integridad e índices

Traduce a restricciones sólo reglas confirmadas: PK, FK, UNIQUE, CHECK y nulabilidad.
Una regla que cruza filas/tablas puede requerir transacción o lógica de aplicación; marca
la limitación.

Propón índices desde consultas, ordenamientos, joins, unicidad y selectividad conocidas.
Registra coste de escritura/almacenamiento y no afirmes rendimiento sin plan/medición.

## Trazabilidad

| Fuente DCD/regla | Tabla/columna/restricción | Transformación | Estado |
|---|---|---|---|
| elemento o evidencia | destino | directa, embebida, normalizada, derivada | confirmado/propuesto/TBD |
