# Guía de Movimiento, Microinteracciones y Física de Interfaz

Esta referencia técnica consolida las mejores prácticas de microinteracción moderna, animación física con resortes (*springs*), animaciones de texto CSS de cero sobrecarga (*zero-runtime*) y microinteracciones de puntero y cursor, sintetizando:
- `ibelick/motion-primitives` (física de resortes y transiciones compartidas),
- `Hyperiux-Immersion-Labs/hyperiux-components` (componentes inmersivos y morphing),
- `ui-layouts/cursify` (artesanía de cursor y botones magnéticos),
- `akaieuan/trickle-UI-kit` (animaciones tipográficas puras en CSS).

---

## 1. Física de Resortes y Transiciones de Layout (Motion Primitives)

Las interfaces modernas evitan curvas de tiempo rígidas (`ease-in-out` de duración fija) para elementos interactivos directos, prefiriendo simulaciones físicas basadas en resortes (*springs*):

### 1.1 Configuraciones Recomendadas de Resortes
| Caso de Uso | Rigidez (`stiffness`) | Amortiguación (`damping`) | Masa (`mass`) | Carácter Perceptivo |
|---|---|---|---|---|
| **Controles Rápidos (Snappy)**<br>Tooltips, switches, popovers, badges | `400` | `30` | `0.8` | Rápido, preciso, sin rebote perceptible. Ideal para productividad. |
| **Superficies Grandes (Gentle)**<br>Diálogos modales, hojas laterales (sheets) | `260` | `26` | `1.0` | Elegante, controlado, sensación de peso físico creíble. |
| **Énfasis Lúdico (Playful)**<br>Reacciones, favoritos, logros | `300` | `15` | `1.0` | Rebote controlado y elástico para retroalimentación positiva. |

### 1.2 Transiciones Compartidas de Layout (`layoutId` / Morphing)
Al expandir un elemento de una lista a una vista en detalle o modal:
- Usar identificadores de layout compartidos (`layoutId` en Framer Motion / Motion Primitives) para que el navegador interpole suavemente tamaño y posición sin saltos de layout (*zero layout shift*).
- **Regla:** Mantener los radios de curvatura coordinados durante el morphing para evitar que las esquinas se deformen durante la animación.

### 1.3 Números Animados (`SlidingNumber`)
Para contadores de métricas, balances o temporizadores:
- Animar cada dígito individualmente en un carril vertical (`translateY`) en lugar de recrear el texto completo.
- Requisito obligatorio: aplicar `font-variant-numeric: tabular-nums` para garantizar que todos los dígitos compartan el mismo ancho y evitar vibraciones horizontales del contenedor.

---

## 2. Animaciones de Texto Zero-Runtime en CSS Puro (Trickle UI Kit)

Cuando se requiere enriquecer encabezados, llamadas a la acción o estados de carga sin añadir librerías de JavaScript pesadas (SSR-safe, 0 KB de runtime JS):

### 2.1 Revelado Escalonado de Caracteres o Palabras
```css
/* Escalonamiento mediante variable CSS inyectada en markup */
.char-reveal {
  display: inline-block;
  opacity: 0;
  transform: translateY(10px) filter(blur(4px));
  animation: revealChar 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  animation-delay: calc(var(--char-index, 0) * 25ms);
}

@keyframes revealChar {
  to {
    opacity: 1;
    transform: translateY(0) filter(blur(0));
  }
}
```

### 2.2 Barrido de Brillo Tipográfico (Text Shimmer / Gradient Sweep)
```css
.text-shimmer {
  background: linear-gradient(
    90deg,
    currentColor 0%,
    rgba(255, 255, 255, 0.8) 50%,
    currentColor 100%
  );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: shimmerSweep 3s infinite linear;
}

@keyframes shimmerSweep {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

---

## 3. Artesanía de Puntero y Cursor (Cursify & Hyperiux)

Las microinteracciones que responden a la posición del cursor enriquecen la sensación de solidez táctil en interfaces de escritorio de alta gama.

### 3.1 Botón Magnético Amortiguado
El elemento se desplaza sutilmente hacia el cursor cuando este se encuentra dentro de su radio de atracción ($R \approx 40\text{px}$):
```typescript
// Lógica de desplazamiento relativo contenido
function onMouseMove(e: MouseEvent, target: HTMLElement) {
  const rect = target.getBoundingClientRect();
  const centerX = rect.left + rect.width / 2;
  const centerY = rect.top + rect.height / 2;
  // Factor de atracción contenido (máximo 6px a 10px de desplazamiento)
  const deltaX = (e.clientX - centerX) * 0.15;
  const deltaY = (e.clientY - centerY) * 0.15;
  target.style.transform = `translate3d(${deltaX}px, ${deltaY}px, 0)`;
}

function onMouseLeave(target: HTMLElement) {
  // Retorno elástico al origen con transición spring
  target.style.transform = 'translate3d(0, 0, 0)';
}
```

### 3.2 Compuertas Obligatorias de Accesibilidad y Rendimiento (Gates)
> [!IMPORTANT]
> Todo efecto de cursor personalizado o botón magnético debe estar estrictamente condicionado por dos compuertas:

1. **Compuerta de Puntero Preciso (`@media (pointer: fine) and (hover: hover)`):**
   - **Prohibido** ejecutar o escuchar eventos de cursor custom en dispositivos táctiles (teléfonos, tablets), donde el cursor no existe y los eventos táctiles generan saltos visuales rotos.
2. **Compuerta de Reducción de Movimiento (`prefers-reduced-motion`):**
   - Si el usuario tiene habilitada la preferencia de movimiento reducido en su sistema operativo, anular traslaciones magnéticas y transiciones elásticas:
   ```css
   @media (prefers-reduced-motion: reduce) {
     *, *::before, *::after {
       animation-duration: 0.01ms !important;
       animation-iteration-count: 1 !important;
       transition-duration: 0.01ms !important;
       transform: none !important;
     }
   }
   ```
3. **Aislamiento en Hilo de Composición:**
   - Realizar transformaciones exclusivamente con `transform` y `opacity` (usando `translate3d` o variables CSS). Nunca mutar `left`, `top`, `width` o `margin` dentro de un listener de mouse para evitar *layout thrashing*.
