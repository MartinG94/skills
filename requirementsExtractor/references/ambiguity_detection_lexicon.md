# Ambigüedad y preguntas de clarificación

Lee esta referencia cuando una necesidad no pueda verificarse tal como está expresada. Detectar una palabra no basta para declarar un defecto: considera la oración y su contexto.

| Patrón | Falta por conocer | Pregunta útil |
| --- | --- | --- |
| rápido, inmediato, en tiempo real | operación, población, carga y límite tolerable | ¿Qué operación se mide, bajo qué condiciones y cuál es el tiempo máximo aceptable? |
| fácil, intuitivo, amigable | usuarios, tarea, experiencia previa y criterio observable | ¿Qué usuario debe completar qué tarea y cómo se comprobará que puede hacerlo? |
| seguro, confiable, robusto | activo o servicio protegido, amenaza/fallo y resultado esperado | ¿Qué debe protegerse o continuar funcionando, frente a qué situación y con qué criterio de aceptación? |
| muchos, frecuente, a veces | volumen, período y pico | ¿Cuál es el volumen habitual y máximo en un período definido? |
| según corresponda, adecuado | condiciones de decisión | ¿Qué condiciones determinan cada alternativa y dónde están documentadas? |
| y/o, etc., entre otros | conjunto cerrado o combinación permitida | ¿Cuáles son las alternativas completas y pueden combinarse? |
| se registra, se autoriza, se informa | responsable y destinatario | ¿Qué rol o sistema realiza la acción y quién recibe el resultado? |

## Métricas

No reemplaces una expresión vaga por un número de ejemplo. Si la fuente no provee el valor:

```text
Escala: TBD
Condiciones de medición: TBD
Objetivo o límite: TBD
Pregunta: <una pregunta que permita completar los tres datos>
```

Puedes sugerir familias de medida —tiempo por tarea, tasa de error, disponibilidad, tiempo de recuperación— solo como opciones de clarificación. No nombres herramientas, algoritmos, proveedores, percentiles ni umbrales salvo que la fuente o el usuario los establezca.

## Preguntas

- Una pregunta por decisión relevante; evita cuestionarios exhaustivos.
- No ofrezcas alternativas que sesguen al stakeholder hacia una solución técnica.
- Indica qué requisito o validación queda bloqueado.
- Mantén el texto original hasta obtener respuesta.
