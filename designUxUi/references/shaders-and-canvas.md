# Arquitectura de Shaders, WebGL y Superficies Canvas

Esta guía proporciona directivas técnicas y de diseño para integrar fondos y efectos generativos en WebGL, WebGPU y Canvas 2D (`paper-design/shaders` y `DavidHDev/canvas-ui`) por debajo de árboles DOM interactivos, asegurando máximo rendimiento, cero interferencia interactiva y accesibilidad garantizada.

---

## 1. Arquitectura de Capas Desacopladas (Layering Pattern)

Todo fondo visual computado mediante Canvas o Shaders debe aislarse completamente del árbol de interacción de la interfaz de usuario:

```
┌────────────────────────────────────────────────────────┐
│ Capa 3: UI Interactiva (Z-index: 10)                  │
│ Botones, Formularios, Texto, Navegación                │
├────────────────────────────────────────────────────────┤
│ Capa 2: Velo de Contraste Semántico (Z-index: 5)       │
│ Overlay CSS (gradiente oscuro/claro para WCAG AA)      │
├────────────────────────────────────────────────────────┤
│ Capa 1: Superficie de Shaders / Canvas (Z-index: 0/-1) │
│ WebGL / WebGPU / Canvas 2D (pointer-events: none)      │
└────────────────────────────────────────────────────────┘
```

### Código Base de Contenedor Aislado:
```html
<div class="hero-container" style="position: relative; overflow: hidden;">
  <!-- Capa 1: Canvas / Shaders -->
  <div class="shader-canvas-host"
       aria-hidden="true"
       style="position: absolute; inset: 0; pointer-events: none; z-index: 0;">
    <canvas id="bg-shader"></canvas>
  </div>

  <!-- Capa 2: Velo de Contraste Protector -->
  <div class="contrast-overlay"
       aria-hidden="true"
       style="position: absolute; inset: 0; background: rgba(9, 9, 11, 0.65); backdrop-filter: blur(8px); z-index: 1;">
  </div>

  <!-- Capa 3: Contenido Interactivo y Accesible -->
  <div class="hero-content" style="position: relative; z-index: 10;">
    <h1>Título Nítido con Contraste Garantizado</h1>
    <p>Texto legible sin degradación por variación de color del shader.</p>
    <button class="btn-primary">Acción Principal</button>
  </div>
</div>
```

---

## 2. Catálogo de Shaders y Superficies Generativas

### 2.1 Shaders de Paper Design (`@paper-design/shaders-react`)
1. **`MeshGradient`**:
   - Degradado de malla multieje con interpolación fluida de colores en fragment shader. Ideal para hero sections de alto impacto visual y fondos ambientales en tarjetas principales.
2. **`DotOrbit`**:
   - Constelación de puntos o partículas en órbitas sutiles. Aporta dinamismo geométrico controlado para productos técnicos y SaaS de infraestructura.
3. **`NeuroNoise` / `SimplexNoise`**:
   - Ruido procedimental orgánico que evoca fluidos, nubes o bioluminiscencia. Debe ejecutarse con baja velocidad (`speed <= 0.2`) para evitar distracción cognitiva.
4. **`SmokeRing`**:
   - Vórtice radial tenue que crea un punto focal luminoso detrás de capturas de producto o llamadas a la acción clave.

### 2.2 Lienzos Interactivos de Canvas UI (`DavidHDev/canvas-ui`)
- Simulaciones físicas de partículas y fluidos bidimensionales optimizados para renderizado continuo a 60 FPS con mínimo consumo de memoria en el hilo principal.

---

## 3. Compuertas Obligatorias de Rendimiento y Accesibilidad

> [!CAUTION]
> Queda terminantemente prohibido incorporar lienzos Canvas o WebGL sin implementar las siguientes 5 compuertas:

### 3.1 Aislamiento Total de Puntero (`pointer-events: none`)
El elemento `<canvas>` o su contenedor anfitrión debe tener obligatoriamente `pointer-events: none`. Jamás debe interceptar clics, selecciones de texto o eventos de arrastre dirigidos a controles de la UI.

### 3.2 Neutralidad para Tecnologías Asistivas (`aria-hidden="true"`)
Toda capa gráfica generativa es meramente decorativa. Debe contener `aria-hidden="true"` y `role="presentation"` para que lectores de pantalla ignoren el nodo por completo.

### 3.3 Pausa Automática Fuera de Viewport (`IntersectionObserver`)
No consumir ciclos de GPU en áreas no visibles de la página. El bucle de animación (`requestAnimationFrame`) debe suspenderse cuando el elemento salga de pantalla:

```typescript
let animationFrameId: number;
let isVisible = false;

const observer = new IntersectionObserver(([entry]) => {
  isVisible = entry.isIntersecting;
  if (isVisible) {
    renderLoop();
  } else {
    cancelAnimationFrame(animationFrameId);
  }
}, { threshold: 0.1 });

observer.observe(canvasElement);

// Pausa adicional si el usuario cambia de pestaña en el navegador
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    cancelAnimationFrame(animationFrameId);
  } else if (isVisible) {
    renderLoop();
  }
});
```

### 3.4 Fallback Estático para Movimiento Reducido (`prefers-reduced-motion`)
Si el usuario tiene activada la preferencia de movimiento reducido:
- Detener por completo la actualización de tiempo del shader (renderizar un único frame estático).
- O bien ocultar el canvas y mostrar un fondo degradado estático equivalente en CSS:
```css
@media (prefers-reduced-motion: reduce) {
  .shader-canvas-host {
    display: none !important;
  }
  .hero-container {
    background: radial-gradient(circle at 50% 30%, #1e1b4b 0%, #09090b 100%) !important;
  }
}
```

### 3.5 Garantía de Contraste de Texto sobre Shaders Dinámicos
Dado que los shaders alternan colores y brillos en tiempo real:
- **Nunca** colocar texto directamente sobre el canvas sin un velo de contraste (`overlay`).
- El contraste entre el texto y el punto más brillante del shader (sumado al velo) debe cumplir siempre la norma **WCAG 2.2 AA (mínimo 4.5:1 para texto normal, 3:1 para texto grande)**.
