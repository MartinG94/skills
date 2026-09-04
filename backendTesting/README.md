# backend-testing

Skill downstream para diseñar, auditar o implementar pruebas automatizadas a partir
del comportamiento, los riesgos y el stack que realmente existen. El contrato
operativo completo está en [SKILL.md](SKILL.md).

## Qué decide

- qué riesgos y comportamientos necesitan cobertura;
- qué nivel ofrece la evidencia adecuada: unitario, integración, contrato o E2E;
- qué dobles de prueba reducen costo sin ocultar la integración que se quiere comprobar;
- qué verificación puede ejecutarse en el repositorio objetivo.

No presupone una pirámide con porcentajes fijos, un framework, una arquitectura, una
base de datos ni un tiempo máximo universal. Tampoco trata una prueba de contrato como
sinónimo de E2E.

## Entrada mínima

Se necesita al menos un comportamiento o riesgo identificable. Para implementar o
ejecutar pruebas también hacen falta el proyecto objetivo, su stack y sus comandos
reales. Si solo existe una especificación, la salida apropiada puede ser una estrategia
o matriz de cobertura, no código ficticio.

## Producto

Según el modo solicitado:

1. alcance, riesgos y evidencia disponible;
2. matriz comportamiento/riesgo → nivel → oráculo → estado;
3. hallazgos o pruebas implementadas;
4. comandos realmente ejecutados y resultado;
5. brechas, límites y próximos controles justificados.

Las convenciones AAA o Given–When–Then y la taxonomía de dobles de Meszaros se usan
cuando mejoran claridad; no son ceremonias obligatorias ni justifican sobre-mocking.
