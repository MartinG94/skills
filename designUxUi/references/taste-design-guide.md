# Guía de dirección visual para productos sin sistema existente

## Cuándo usarla

Consultar esta guía solo para definir una dirección visual nueva cuando no existen
marca, sistema de diseño ni referencias suficientes. Las decisiones del usuario, la
identidad existente, el contenido y la accesibilidad tienen prioridad. Estas son
heurísticas para evitar una propuesta genérica, no prohibiciones universales.

No usarla para rediseñar por iniciativa propia una interfaz existente ni para
convertir una auditoría funcional en un cambio estético.

## Calibrar la dirección

Definir explícitamente tres ejes antes de elegir tokens:

1. **Densidad**
   - espaciosa: contenido editorial, presentación o tarea simple;
   - equilibrada: productos cotidianos y formularios;
   - densa: monitoreo, tablas y herramientas expertas.
2. **Composición**
   - regular: comparación rápida, familiaridad y previsibilidad;
   - desplazada/asimétrica: énfasis editorial o jerarquía deliberada.
3. **Movimiento**
   - mínimo: tareas frecuentes, información crítica o preferencia de movimiento
     reducido;
   - expresivo: transiciones que aclaran continuidad o identidad de marca.

Elegir un punto por eje y justificarlo con audiencia, tarea y contenido. No usar una
escala numérica si no aporta una decisión comprobable.

## Color

- Partir de la paleta de marca o de las funciones semánticas necesarias: superficie,
  texto, acción, foco, éxito, advertencia y error.
- Usar uno o varios acentos según jerarquía y marca; limitar colores compitiendo por
  atención, no por una cifra fija.
- Negro puro, blancos, grises cálidos o fríos y colores saturados son opciones
  válidas si el contraste, la reproducción y la identidad lo justifican.
- Evitar gradientes o resplandores usados como sustituto de jerarquía. Mantenerlos si
  son parte intencional de la marca y no degradan legibilidad.
- Verificar contraste en estados normal, hover, focus, disabled y selected. No
  deducir conformidad de una descripción del color.

## Tipografía

- Reutilizar primero las fuentes ya disponibles y autorizadas en el proyecto.
- Elegir por legibilidad, cobertura de caracteres, rendimiento, licencia e identidad.
  `Inter`, fuentes de sistema, serif o monospace pueden ser correctas según el caso.
- Crear jerarquía con una combinación contenida de tamaño, peso, espaciado y color.
- Ajustar el largo de línea al tipo de contenido; alrededor de 45–75 caracteres suele
  ser cómodo para prosa, pero tablas, código y etiquetas tienen otras necesidades.
- No declarar una fuente remota si el artefacto no puede cargarla o no hay fallback.

## Composición y componentes

- La acción y la información principal deben dominar antes que la decoración.
- Una grilla simétrica favorece comparación; una composición asimétrica favorece
  narrativa o énfasis. Elegir por tarea, no para evitar un cliché.
- Repetir tarjetas cuando representan elementos equivalentes. Variar tamaños solo si
  existe una diferencia real de prioridad.
- Diseñar primero con contenido representativo o placeholders explícitos para revelar
  desbordes, estados vacíos y variación de longitud.
- Usar iconos, ilustraciones o emojis si son comprensibles, accesibles y coherentes con
  el producto. No usarlos como único nombre de una acción ambigua.
- Preferir imágenes proporcionadas o placeholders locales estables. No introducir
  URLs aleatorias o assets de terceros como contenido final.

## Movimiento y feedback

- Cada animación debe comunicar estado, continuidad, causalidad o jerarquía.
- Evitar movimiento continuo decorativo en tareas de concentración.
- Respetar `prefers-reduced-motion` y conservar una experiencia comprensible sin
  animación.
- Elegir duración y curva según plataforma y componente; no copiar parámetros físicos
  fijos en todos los proyectos.

## Señales de una propuesta poco sustentada

Revisar y corregir cuando aparezcan sin respaldo:

- métricas, testimonios, logos, nombres o estadísticas inventadas;
- copy genérico que no explica la tarea;
- secciones decorativas sin función ni contenido real;
- controles inertes, links rotos o acciones que simulan estar conectadas;
- jerarquía basada solo en tamaño extremo, brillo o saturación;
- el mismo patrón de hero, tres tarjetas y CTA aplicado a cualquier producto;
- cursores personalizados, loaders o efectos que empeoran uso o rendimiento;
- layout que desborda en móvil o depende de una altura de viewport rígida;
- texto sobre imágenes sin contraste robusto;
- una dirección visual que contradice el sistema existente.

Estas señales requieren evaluación, no reemplazo automático. Una estructura común
puede ser la mejor opción si el contenido y la tarea la justifican.

## Salida de la decisión visual

Registrar de forma breve:

- propósito y audiencia;
- dirección elegida en densidad, composición y movimiento;
- decisiones de color y tipografía con su fuente o carácter provisional;
- componentes y estados prioritarios;
- riesgos de accesibilidad o contenido pendiente.

No crear métricas, claims comerciales ni datos de ejemplo presentados como reales.
