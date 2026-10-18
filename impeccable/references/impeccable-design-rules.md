# Catálogo de Reglas de Precisión Óptica y Auditoría Anti-Slop (Impeccable)

Este documento reúne el catálogo exhaustivo de anti-patrones visuales generados por IA ("AI Slop Detector") y las reglas matemáticas y ópticas de refinamiento para alcanzar un acabado de interfaz de nivel artesanal (*impeccable craft*).

---

## 1. Catálogo de Anti-patrones Visuales ("AI Slop Detector")

Los modelos de lenguaje suelen recurrir por defecto a un conjunto predecible de clichés estéticos que delatan una interfaz genérica y descuidada. La auditoría debe detectar y marcar activamente estos 8 anti-patrones:

### 1.1 Gradiente Violeta/Índigo Genérico (*The Purple Haze*)
- **Síntoma:** Uso indiscriminado de `bg-gradient-to-r from-purple-600 to-indigo-600` o acentos violeta brillante sobre fondos oscuros sin justificación de marca.
- **Por qué falla:** Es el cliché por excelencia de demos de IA; desgasta la identidad del producto y reduce el contraste percibido.
- **Corrección:** Usar una paleta intencional derivada de la función o la marca; preferir monocromo con acento de alta especificidad o luminancias sutiles.

### 1.2 Sombras Sucias y Desenfocadas (*Muddy Shadows*)
- **Síntoma:** Sombras difusas de color negro puro con gran radio de desenfoque: `box-shadow: 0 20px 40px rgba(0,0,0,0.4)`.
- **Por qué falla:** En superficies oscuras o de color genera un halo grisáceo "sucio" (desaturación perceptiva) y carece de dirección física creíble.
- **Corrección:** Usar sombras de dos capas (luz de ambiente + luz directa/key) entintadas sutilmente con el tono del fondo:
  ```css
  /* Sombra limpia y física en modo claro */
  box-shadow:
    0 1px 2px -1px rgb(0 0 0 / 0.08),
    0 3px 6px -2px rgb(0 0 0 / 0.12);
  ```

### 1.3 Violación de Radios Concéntricos (*The Nested Radius Clash*)
- **Síntoma:** Un contenedor con `border-radius: 16px` contiene un elemento interno con el mismo radio (`16px`) separado por un `padding: 12px`.
- **Por qué falla:** Las esquinas se "pellizcan" visualmente, produciendo un espacio en blanco irregular y distorsionado en las diagonales.
- **Corrección:** Aplicar la **Ley de Radios Concéntricos**:
  $$R_{outer} = R_{inner} + Padding$$
  $$R_{inner} = \max(0, R_{outer} - Padding)$$

### 1.4 Ritmo Espacial Roto y Escala Arbitraria
- **Síntoma:** Mezcla de márgenes y paddings no modulares (`7px`, `11px`, `23px`, `38px`) sin grilla base.
- **Por qué falla:** Destruye la coherencia de lectura y el orden visual; la interfaz se percibe inestable y caótica.
- **Corrección:** Respetar estrictamente la escala modular de 4px / 8px (`4, 8, 12, 16, 24, 32, 48, 64px`).

### 1.5 Sobrecarga de Contenedores Anidados (*Card Inception*)
- **Síntoma:** Tarjetas dentro de tarjetas dentro de tarjetas, cada una con su propio borde, sombra y fondo diferenciado.
- **Por qué falla:** Añade ruido visual innecesario, consume padding horizontal valioso y divide la atención del usuario en compartimentos redundantes.
- **Corrección:** Destilar (*distill*): eliminar bordes y cajas redundantes; usar espaciado y tipografía para agrupar.

### 1.6 Emojis como Iconos de Sistema
- **Síntoma:** Emplear emojis de Unicode (🚀, 💡, ⚡, 🎯) como iconos de navegación o botones de acción.
- **Por qué falla:** Varían drásticamente de apariencia según el sistema operativo (Apple vs. Android vs. Windows), no admiten colores de tema (`currentColor`) y lucen poco profesionales en aplicaciones B2B o herramientas de productividad.
- **Corrección:** Usar una biblioteca de iconos vectoriales SVG consistente (Lucide, Heroicons, Radix Icons, Phosphor).

### 1.7 Falta de `tabular-nums` en Datos Numéricos
- **Síntoma:** Números, contadores, precios y tablas que bailan o tiemblan horizontalmente cuando las cifras cambian de valor o al alinear columnas.
- **Por qué falla:** Los glifos tipográficos estándar son proporcionales; el número `1` es más estrecho que el `8`, lo que provoca vibración visual (*jitter*).
- **Corrección:** Aplicar `font-variant-numeric: tabular-nums` (o clase Tailwind `tabular-nums`) a todas las métricas, precios y tablas.

### 1.8 Huérfanos Tipográficos y Títulos Desequilibrados
- **Síntoma:** Títulos grandes donde una sola palabra queda aislada en la segunda o tercera línea.
- **Por qué falla:** Arruina la armonía compositiva y la velocidad de lectura.
- **Corrección:** Aplicar `text-wrap: balance` a encabezados ($H1-H4$) y `text-wrap: pretty` a párrafos explicativos.

---

## 2. Reglas Matemáticas y de Precisión Óptica

### 2.1 Ley del Borde de Luminancia de 1px (Subtle 1px Borders)
En interfaces oscuras o modernas, las sombras solas no delimitan con nitidez las superficies.
- **Regla:** Todo contenedor elevado o flotante debe poseer un borde sutil de 1px con opacidad calibrada sobre el color de superficie:
  ```css
  /* Superficie Dark Mode */
  background: #121214;
  border: 1px solid rgba(255, 255, 255, 0.08); /* Luz reflejada */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
  ```

### 2.2 Compensación Óptica de Alineación (Icons & Badges)
- **Problema:** Un icono centrado matemáticamente con `align-items: center` suele verse caído o desalineado respecto al texto adyacente debido a la línea base y la altura de las mayúsculas (Cap-Height).
- **Regla:** Aplicar un ajuste óptico de `-0.5px` a `-1px` vertical o usar `display: inline-flex; align-items: center;` con cajas viewBox normalizadas (`20x20` o `24x24`).

### 2.3 Contraste de Superficies Escalonado
En temas oscuros (Dark UI), la profundidad no se logra oscureciendo sino aclarando las capas a medida que se acercan al usuario:
- Nivel 0 (Fondo base / Canvas): `#09090b`
- Nivel 1 (Superficie / Sidebar / Card): `#121214` o `#18181b`
- Nivel 2 (Popover / Dropdown / Modal): `#27272a`
- Nivel 3 (Hover / Estado activo): `#3f3f46`

---

## 3. Protocolo de Modos de Refinamiento

### Modo `detect` (Auditoría Anti-Slop)
Escanea el archivo o componente y genera una lista de hallazgos clasificados:
- 🔴 **Crítico:** Falta de contraste accesible, violación de radios concéntricos, jitter numérico.
- 🟡 **Advertencia:** Sombras sucias, degradados genéricos, emojis en navegación, card inception.
- 🟢 **Sugerencia:** Falta de `text-wrap: balance`, micro-alineación de iconos.

### Modo `polish` (Micro-refinamiento de Precisión)
Aplica correcciones quirúrgicas en CSS/Tailwind:
1. Inyecta `tabular-nums` en contadores y métricas.
2. Recalcula radios internos según $R_{inner} = R_{outer} - Padding$.
3. Reemplaza sombras sucias por sombras de doble capa entintadas.
4. Agrega bordes sutiles de luminancia de 1px.
5. Aplica `text-wrap: balance` a encabezados.

### Modo `distill` (Depuración y Poda de Ruido)
1. Identifica y disuelve contenedores decorativos superfluos.
2. Elimina fondos duplicados y bordes que compiten entre sí.
3. Transforma una grilla abarrotada de tarjetas en una lista limpia o tabla minimalista si la tarea lo requiere.

### Modo `animate` (Coreografía Natural)
1. Duraciones contenidas: entre 120ms y 240ms para microinteracciones de interfaz; nunca más de 300ms en herramientas cotidianas.
2. Curvas de aceleración: entrada rápida con desaceleración suave (`cubic-bezier(0.16, 1, 0.3, 1)`).
3. Respeto incondicional: envolver toda animación en `@media (prefers-reduced-motion: no-preference)`.
