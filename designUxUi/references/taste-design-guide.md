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
   - desplazada/asimétrica: énfasis editorial o jerarquía deliberada (flujo tipo Canvas de Superdesign).
3. **Movimiento**
   - mínimo: tareas frecuentes, información crítica o preferencia de movimiento
     reducido;
   - expresivo: transiciones que aclaran continuidad o identidad de marca.

Para perfiles estéticos canónicos de referencia (Linear, Vercel/Geist, Stripe, Supabase, Apple HIG, Notion), consultar [references/design-systems-catalog.md](design-systems-catalog.md).

## Protocolo Anti-AI-Slop (Auditoría Estética Crítica)

Al diseñar o auditar interfaces generadas por modelos de lenguaje, erradicar activamente los clichés estéticos no justificados:

1. **Eliminar el degradado violeta/índigo genérico:** No inyectar `from-purple-600 to-indigo-600` o violetas sobre negro salvo que la identidad de marca aprobada lo exija explícitamente.
2. **Desterrar las tres tarjetas idénticas como plantilla universal:** No resolver todo layout con una fila de 3 cards repetitivas; variar jerarquías según la relevancia del contenido.
3. **Erradicar emojis como iconos de sistema:** Usar sets vectoriales SVG consistentes y accesibles (Lucide, Heroicons, Radix) en lugar de emojis en navegación y acciones.
4. **Reemplazar sombras sucias (*muddy shadows*):** No usar halos oscuros con gran desenfoque (`blur > 30px`) en negro puro; aplicar sombras de dos capas (ambiente + luz directa) entintadas sutilmente.

## Matemática Espacial y Precisión Óptica

- **Ley de Radios Concéntricos:** Al anidar contenedores con bordes redondeados, calcular el radio exterior en función del interior y el padding:
  $$R_{outer} = R_{inner} + Padding$$
  $$R_{inner} = \max(0, R_{outer} - Padding)$$
  Evita el pinzamiento visual de las esquinas interiores.
- **Bordes de Luminancia de 1px:** En modo oscuro o interfaces de alta definición, delimitar superficies elevadas con un borde sutil de 1px (`rgba(255, 255, 255, 0.08)` o `oklch`), sustituyendo sombras pesadas.
- **Estabilidad Numérica:** Aplicar obligatoriamente `font-variant-numeric: tabular-nums` (o clase `tabular-nums`) en contadores, precios, tablas y métricas para prevenir vibraciones horizontales (*jitter*).
- **Equilibrio Tipográfico:** Aplicar `text-wrap: balance` a encabezados ($H1-H4$) para evitar palabras huérfanas, y `text-wrap: pretty` a párrafos de lectura.

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
- Para animaciones físicas con resortes, textos sin runtime JS o microinteracciones de cursor, consultar [references/motion-and-microinteractions.md](motion-and-microinteractions.md).
- Para integración de WebGL, lienzos y shaders generativos, consultar [references/shaders-and-canvas.md](shaders-and-canvas.md).

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
