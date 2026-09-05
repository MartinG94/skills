# Realización de diseño

Lee esta referencia sólo para `design-rcu`.

## Punto de partida

Una realización de diseño representa físicamente un escenario y debe concordar con el
DCD y los contratos disponibles. Puede incorporar clases sin contraparte conceptual,
como adaptadores o servicios técnicos, sólo si el escenario las necesita.

Para cada participante registra:

- clase/interfaz de diseño existente o propuesta;
- responsabilidad concreta;
- operación invocada y datos necesarios;
- forma de obtención de la referencia;
- restricción o requisito que justifica su presencia.

## Detalle y consistencia

- Usa la firma del DCD cuando está definida.
- Si la secuencia deliberadamente abrevia tipos, retornos o parámetros, indícalo; no
  declares una inconsistencia exacta por omisión gráfica.
- Si el DCD carece de una operación necesaria, propón el cambio por separado.
- No presupongas que una flecha de asociación sin navegabilidad explícita la concede.
- Comprueba precondiciones y transiciones contra el modelo de estados disponible.

## Patrones opcionales

Considera un patrón sólo ante una fuerza concreta, por ejemplo:

- algoritmos sustituibles → Strategy;
- comportamiento realmente distinto por estado → State;
- notificación uno-a-muchos → Observer;
- interfaz externa incompatible → Adapter;
- recorrido desacoplado de una estructura no trivial → Iterator.

Verifica alternativas más simples antes de introducirlo. Una enumeración, método
polimórfico existente, llamada directa o colección idiomática puede ser suficiente.
Cuando uses un patrón, identifica problema, participantes, colaboración y consecuencia;
no lo agregues sólo por coincidencia de nombre.

## Trazabilidad de diseño

| Paso CU | Mensaje | Receptor/operación DCD | Visibilidad | Estado |
|---|---|---|---|---|
| evidencia | llamada | clase::operación | atributo/parámetro/create/retorno | confirmado/propuesto/TBD |
