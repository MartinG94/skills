# Criterios de interfaz

Lee esta referencia cuando vayas a establecer o modificar la forma visual e interactiva del frontend. Adapta cada criterio al sistema existente y al contexto; no copies una paleta, escala o componente universal.

## Dirección visual

Define antes de estilizar:

- propósito y tono del producto;
- densidad de información;
- jerarquía y punto focal;
- lenguaje de forma, color, tipografía e imagen;
- nivel de expresividad permitido por el dominio;
- rasgo distintivo que evita una plantilla genérica.

La estética debe sostener la tarea. Evita el uso automático de tarjetas, gradientes, glassmorphism, sombras, esquinas redondeadas o animaciones. Conserva el design system y los assets existentes salvo que el pedido incluya cambiarlos.

## Layout, grilla y responsive

- Diseña desde el contenido y las prioridades. Usa grilla, alineación, proximidad, espacio y región común para comunicar relaciones.
- Prefiere dimensiones fluidas, `min()`, `max()`, `clamp()`, flexbox, grid y container queries cuando sean compatibles con el proyecto.
- Elige breakpoints donde el contenido deja de funcionar, no por una lista fija de dispositivos.
- Decide qué debe reordenarse, resumirse, desplazarse o cambiar de patrón; responsive no significa solo reducir tamaños.
- Verifica zoom, texto ampliado, orientación, altura reducida, teclado virtual, safe areas y scroll anidado cuando sean pertinentes. Un panel `sticky` o `fixed` no debe volver inaccesible su propia acción.
- No fuerces la acción primaria a una “thumb zone” si contradice la plataforma, el flujo o la accesibilidad.

Modela la plataforma mediante ejes concretos —viewport y densidad, touch/mouse/teclado/voz, navegador o app, sistema operativo, movilidad, conectividad, capacidades y tecnologías de asistencia— en vez de asumir que “web”, “móvil” y “escritorio” son categorías excluyentes.

## Navegación y contexto móvil

- Elige bottom navigation, tabs, barra superior/lateral, menú o búsqueda según arquitectura, frecuencia, cantidad de destinos y espacio; ninguno es un default universal.
- No escondas una acción esencial en un hamburger ni uses un icono ambiguo sin etiqueta o nombre accesible.
- Mantén ubicación, comportamiento de volver, foco, scroll y filtros cuando la tarea lo requiera.
- Gestos, drag, swipe, pull-to-refresh e infinite scroll necesitan una alternativa visible y operable; preserva historial, foco y posición.
- Considera teclado virtual, orientación, interrupciones, conexión lenta, batería y reanudación. Usa cámara, ubicación, biometría, sensores o notificaciones solo si aportan a la tarea y con permisos pedidos en contexto.
- Para objetivos nativos consulta la guía vigente de la plataforma; no mezcles CSS px, puntos y dp.

## Tipografía y contenido

- Mantén una jerarquía perceptible sin depender solo del tamaño.
- Usa medidas legibles, altura de línea suficiente y longitudes de línea coherentes con el contenido.
- Evita alturas fijas que recorten texto, tamaños diminutos y truncado de información esencial.
- Prueba nombres, cantidades, fechas y traducciones largas; no optimices únicamente para el texto de muestra.
- Usa fuentes existentes o del sistema por defecto. No descargues tipografías sin necesidad, licencia y autorización.

## Color y tokens

- Reutiliza tokens del proyecto. Si no existen, crea el conjunto semántico mínimo que reduzca repetición real: superficies, texto, borde, acción, foco, feedback, espacio y movimiento.
- Separa propósito de valor para permitir temas y cambios de marca, pero no construyas tres capas de tokens si una página pequeña no las necesita.
- Comprueba cada par de primer plano/fondo real. No deduzcas conformidad a partir del nombre del token.
- No uses color como única señal de estado; combina texto, icono, forma o posición según corresponda.
- Prueba estados hover, focus, active, disabled, selected y feedback sobre la superficie donde aparecen.

## Componentes y estados

Empieza por HTML nativo. Añade ARIA solo para completar semántica o patrones que HTML no cubre. Revisa los patrones WAI-ARIA aplicables antes de crear widgets compuestos.

Para cada componente implementado, cubre únicamente los estados que el flujo puede alcanzar. Un estado “disabled” no sustituye una explicación; un loader no debe borrar el nombre accesible de la acción; una transición no debe esconder feedback.

Cuando una acción expanda contenido o reconstruya una región, comunica la relación y el estado con la semántica aplicable, conserva un foco útil y garantiza que el siguiente paso sea visible sin imponer desplazamientos sorpresivos.

Los modales requieren como mínimo nombre accesible, foco inicial deliberado, contenido de fondo realmente inerte, ciclo de Tab contenido, cierre coherente, retorno de foco y una acción visible para cerrar. Cuando el elemento `<dialog>` encaje y el soporte del proyecto lo permita, evalúalo antes de reconstruir el patrón.

## Formularios y errores

- Usa label visible y asociación programática; placeholder no sustituye label.
- Elige el control nativo y `autocomplete`, `inputmode` o tipo de entrada apropiados.
- Conserva la entrada del usuario tras un error y señala campos, resumen y próximo paso según la complejidad.
- Asocia ayudas y errores al control con `aria-describedby` cuando aporten contexto; sincroniza `aria-invalid`, el mensaje inline y el resumen al aparecer y también al resolverse el problema.
- Valida las restricciones que realmente promete la interfaz —incluidos rango, formato, longitud, dependencias y límites inclusivos— aunque el control quede fuera del `form` o el envío sea gestionado con JavaScript.
- Cada enlace de un resumen de errores debe llevar a un objetivo enfocable que exista en ese estado. Si falta un control dependiente, dirige al prerrequisito que permite crearlo.
- Valida en el momento que ayude: demasiado pronto puede interrumpir; solo al final puede aumentar retrabajo.
- No impongas máscaras, wizards o selects por cantidad de campos. Decide según formato, dependencia, riesgo y tarea.
- Anuncia cambios dinámicos sin duplicar `role="alert"` y `aria-live`, y evita anuncios agresivos para mensajes no urgentes.
- Para acciones destructivas o irreversibles, explica consecuencias y ofrece deshacer cuando sea viable.

## Accesibilidad verificable

Usa WCAG 2.2 AA como baseline salvo otro requisito. Como mínimo:

- estructura semántica, landmarks, título y orden de encabezados coherente;
- nombre, rol, valor y descripción accesibles;
- nombres accesibles que distingan controles repetidos por acción y objeto —por ejemplo, “Elegir Sala Norte”—, no una colección de botones homónimos sin contexto;
- orden de foco lógico, foco visible y sin trampas involuntarias;
- preservación o restauración deliberada del foco cuando una interacción vuelve a renderizar o elimina el nodo activo;
- interacción de teclado acorde al componente;
- alternativas de texto y subtítulos cuando el contenido los requiera;
- contraste de texto de al menos 4.5:1, o 3:1 para texto grande según la definición WCAG;
- contraste no textual de 3:1 donde el criterio 1.4.11 aplique;
- targets de puntero que cumplan 2.5.8: 24 × 24 CSS px o una excepción aplicable, incluido el espaciado; apunta a áreas mayores en controles importantes cuando el contexto lo permita;
- reflow, zoom y preferencias como `prefers-reduced-motion`, `forced-colors` y esquemas de color cuando sean relevantes;
- feedback que no dependa de color, hover, sonido o tiempo limitado.

Cuando el diseño responsive acorte u oculte texto visual, conserva el nombre y el contexto accesibles con una técnica apropiada; `display: none` también elimina el contenido del árbol de accesibilidad. Usa `aria-pressed` únicamente para un control que pueda alternar de verdad entre ambos estados.

Un scanner automatizado no prueba conformidad. Combínalo con teclado, zoom, inspección visual y, cuando el riesgo lo justifique, tecnología asistiva o revisión humana especializada.

## Movimiento y rendimiento percibido

- Anima para explicar relación, continuidad o estado; no por decoración automática.
- Respeta reducción de movimiento y evita `transition: all`.
- Mantén estable el layout durante carga. Elige skeleton, placeholder, spinner, progreso o texto según duración conocida, cantidad de contenido y riesgo de distracción.
- Optimiza imágenes, fuentes y JavaScript. Revisa que el acabado visual no degrade interacción, carga o batería.

## Calibración de heurísticas

Las leyes de Fitts, Hick, Gestalt, consistencia y carga cognitiva son lentes para revisar decisiones, no mandatos numéricos. Documenta la razón contextual de una decisión importante y valida el resultado observable.
