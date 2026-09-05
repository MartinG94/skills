---
name: design-ux-ui
description: >-
  Diseña, audita o implementa experiencias e interfaces web a partir de requisitos y
  contexto visual aprobados. Respeta el stack y sistema de diseño existentes, ajusta
  el artefacto al alcance pedido y valida accesibilidad y comportamiento; no crea por
  defecto un DESIGN.md, un prototipo, un servidor ni un widget embebido.
---

# Diseño e implementación UX/UI proporcional

## Responsabilidad y límites

Esta skill convierte necesidades de usuario ya identificadas en uno de estos
productos, según el pedido:

- **especificación UX**: tareas, arquitectura de información, flujos y estados;
- **dirección visual o tokens**: decisiones reutilizables de presentación;
- **prototipo**: artefacto acotado para explorar o validar una interacción;
- **implementación**: cambios en el frontend existente;
- **auditoría**: hallazgos de usabilidad, accesibilidad o consistencia sin mutaciones.

No inferir que un Ejercicio Práctico Complementario (EPC) es un flujo de interfaz.
Diseñar UI para un EPC solo si la consigna la pide. No crear requisitos, casos de uso,
contenido de negocio ni contratos de API para rellenar una pantalla.

## Autoridad y entradas

Respetar, en este orden:

1. instrucciones y alcance del usuario;
2. comportamiento y contenido aprobados;
3. sistema de diseño, componentes y convenciones del proyecto;
4. marca y referencias visuales proporcionadas;
5. heurísticas de esta skill como apoyo, no como identidad impuesta.

Identificar audiencia, tarea principal, plataformas/viewports, estados y datos reales,
restricciones de accesibilidad, stack, componentes disponibles y artefacto de salida.
Si falta información visual, puede proponerse una dirección explícitamente marcada
como propuesta. Si falta una regla funcional, dejar el estado pendiente o preguntar;
no inventarla.

## Elegir el modo antes de producir archivos

| Situación | Producto proporcional |
|---|---|
| se pide entender o corregir un flujo | especificación UX o wireflow |
| se pide una propuesta visual sin código | dirección visual/tokens o mockup |
| existe una aplicación y se piden cambios | implementación en su stack |
| se pide una demo aislada | prototipo autocontenido mínimo |
| se pide revisar | informe priorizado; no editar |

No entregar simultáneamente especificación, sistema de diseño, prototipo y aplicación
completa salvo que el usuario los haya solicitado. No cambiar de framework ni añadir
Tailwind por preferencia de la skill.

## Flujo de trabajo

### 1. Definir la experiencia observable

- Enumerar tareas y resultados esperados, no pantallas decorativas.
- Modelar estados relevantes: inicial, carga, vacío, error, éxito, deshabilitado y
  permisos cuando el producto los necesite.
- Mantener trazabilidad con requisitos/CU mediante sus IDs existentes, sin exigir una
  correspondencia uno-a-uno entre cada control y cada paso del caso de uso.
- Resolver navegación, jerarquía, feedback y recuperación antes del detalle estético.

Para investigación, arquitectura de información o flujos complejos, leer
[references/ux-method.md](references/ux-method.md).

### 2. Reutilizar antes de crear

En un proyecto existente, inspeccionar tokens, CSS, componentes, rutas y patrones de
interacción. Preservar su lenguaje visual y corregir solo lo necesario. Leer
[references/extract-code-guide.md](references/extract-code-guide.md) únicamente si se
deben extraer tokens desde código.

Crear o actualizar `DESIGN.md` solo cuando el usuario lo pida o cuando el proyecto
necesite realmente una fuente de tokens mantenible. Para ese caso, leer
[references/design-tokens-spec.md](references/design-tokens-spec.md) y elegir una sola
plantilla proporcional en `resources/templates/`. No reemplazar un sistema de diseño
existente por esas plantillas.

Si se diseña un producto nuevo sin marca ni referencias, puede consultarse
[references/taste-design-guide.md](references/taste-design-guide.md) y usar
`DESIGN-taste.template.md` como punto de partida editable, nunca como norma universal.

### 3. Diseñar la interfaz

- Priorizar contenido, orden de lectura y acción principal.
- Usar componentes familiares cuando reducen aprendizaje; introducir una variante
  solo con una razón funcional o de marca.
- Diseñar responsive a partir del contenido, no mediante un layout fijo aplicado a
  todos los productos.
- Incluir copy real provisto por las fuentes. Usar placeholders explícitos para
  nombres, imágenes o métricas que falten.
- No prometer acciones que el prototipo o la implementación no realizan.

Para decisiones de layout, controles, responsive y contraste, leer
[references/interface-craft.md](references/interface-craft.md) solo en trabajos de
diseño visual o implementación.

### 4. Implementar solo cuando corresponde

En modo Implementación:

1. localizar el stack, comandos, design system y convenciones del repositorio;
2. reutilizar componentes y dependencias existentes;
3. implementar el menor conjunto de archivos que complete la tarea;
4. conectar acciones a comportamiento real o declarar claramente el alcance de demo;
5. no iniciar servidores ni abrir previews si no aportan a la verificación solicitada.

Un HTML autocontenido es apropiado para una demo aislada, no el valor por defecto de
todo frontend. Los mecanismos de incrustación y las URLs de assets dependen del host;
confirmar que estén disponibles antes de usarlos.

Leer [references/preview-and-runtime.md](references/preview-and-runtime.md) solo si se
debe ejecutar una vista previa. Leer [references/designmd-cli.md](references/designmd-cli.md)
solo si el proyecto usa `DESIGN.md` y hay que validarlo o exportarlo.

### 5. Validar proporcionalmente

Para una implementación, comprobar como mínimo lo afectado por el cambio:

- navegación por teclado, foco visible, nombres accesibles y orden semántico;
- contraste aplicable y estados que no dependan solo del color;
- reflow, overflow y legibilidad en viewports relevantes;
- carga, vacío, error y éxito que formen parte del flujo;
- acciones principales y ausencia de controles inertes;
- lint, types y pruebas existentes relacionadas.

WCAG 2.2 AA es la referencia por defecto cuando no existe otra exigencia, pero no
afirmar conformidad completa a partir de un único chequeo automático. Informar qué se
verificó y qué requiere revisión manual. Para un cierre de implementación amplio,
leer [references/quality-gates.md](references/quality-gates.md).

## Control de no invención

- No fabricar testimonios, usuarios, estadísticas, precios, rendimiento ni logos.
- No asumir que una referencia visual autoriza copiar su marca o sus assets.
- No convertir preferencias como tipografía, asimetría, color o animación en vetos
  universales; el contexto, la marca y la accesibilidad deciden.
- No presentar un prototipo como producción ni una auditoría automática como prueba
  total de accesibilidad.
- No rediseñar áreas fuera del alcance para homogeneizar el proyecto.

## Contrato de salida

Entregar únicamente el artefacto solicitado y un resumen breve con:

1. alcance y fuentes/restricciones usadas;
2. decisiones UX/UI que afectan la tarea;
3. archivos o artefactos creados/modificados, si los hubo;
4. verificaciones ejecutadas y resultado real;
5. pendientes que cambien materialmente la experiencia.

Una URL local, un embed, tokens exportados o `DESIGN.md` aparecen solo cuando forman
parte del producto pedido y fueron comprobados en el entorno disponible.

Finalizar cuando las tareas y estados dentro del alcance estén representados, el
artefacto solicitado haya superado las verificaciones aplicables y los pendientes que
cambian la experiencia estén declarados. No extender el rediseño a áreas vecinas.
