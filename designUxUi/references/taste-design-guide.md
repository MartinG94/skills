# Guía de Principios Estéticos y Anti-Slop (Taste Design)

Esta guía condensa la filosofía visual para erradicar las interfaces genéricas producidas comúnmente por inteligencia artificial y establecer un estándar de diseño editorial, riguroso y con carácter.

---

## 1. El Espectro del Buen Gusto (3 Diales de Atmósfera)

Antes de definir tokens, calibra estos tres diales según la naturaleza del producto:

1. **Densidad (1 a 10):**
   - `1 - 3 (Art Gallery Airy):` Grandes áreas de respiración, tipografía protagonista, márgenes masivos (>32px). Ideal para portfolios, marcas de lujo y editoriales.
   - `4 - 7 (Daily App Balanced):` Densidad estándar para productos digitales cotidianos, SaaS y comercio electrónico.
   - `8 - 10 (Cockpit Dense):` Máxima densidad de información, tablas complejas, paneles de trading y monitoreo técnico. Espaciados compactos (4px/8px) y tipografía monospace para cifras.
2. **Varianza y Asimetría (1 a 10):**
   - `1 - 3 (Symmetric Predictable):` Estructuras clásicas centradas.
   - `4 - 7 (Offset Asymmetric):` Columnas divididas asimétricamente (ej. 60/40), márgenes desalineados intencionales.
   - `8 - 10 (Artsy Chaotic):` Composiciones vanguardistas y de choque visual controlado.
3. **Movimiento y Micro-interacción (1 a 10):**
   - `1 - 3 (Static Restrained):` Transiciones de estado limpias sin animación continua.
   - `4 - 7 (Fluid Spring CSS):` Físicas de resorte (`stiffness: 100, damping: 20`) en hovers, aperturas de modales y tooltips.
   - `8 - 10 (Cinematic):` Revelaciones escalonadas (*staggered waterfall*), micro-bucles sutiles y transiciones de página coreografiadas.

---

## 2. Reglas Estrictas de Color
- **Máximo 1 color de acento principal.** Saturación estricta por debajo del 80%.
- **Bases neutras puras:** Zinc, Slate o Charcoal.
- **Prohibido el negro puro (`#000000`):** Usa siempre un negro con matiz, como Zinc-950 (`#09090B`) u Off-Black (`#121214`).
- **Coherencia térmica:** No mezcles grises fríos con grises cálidos en la misma pantalla.
- **Eliminación del 'AI Purple/Neon':** Prohibidos los botones violetas con gradientes neón o sombras de resplandor exterior brillante.

---

## 3. Arquitectura Tipográfica con Carácter
- **Prohibido `Inter` en contextos de marca o diseño de autor:** `Inter` es la firma por defecto de la IA. Emplea tipografías con personalidad geométrica o editorial:
  - Sans modernas: `Geist`, `Cabinet Grotesk`, `Outfit`, `Satoshi`, `Plus Jakarta Sans`.
  - Serifs de autor (solo para contextos editoriales o de moda, nunca en dashboards técnicos): `Fraunces`, `Gambarino`, `Editorial New`, `Instrument Serif`.
  - Monospace (para cifras, métricas o código): `JetBrains Mono`, `Geist Mono`, `Space Mono`.
- **Jerarquía sin gritar:** Genera contraste mediante el peso (`font-semibold` / `font-medium`) y el color de texto, en lugar de recurrir a tamaños gigantescos desmedidos.
- **Largo de línea:** Máximo 65 caracteres por línea en texto corrido para asegurar descanso ocular.

---

## 4. Diseño del Hero Section y Composiciones
- **Prohibidos los héroes centrados aburridos:** En varianzas mayores a 4, usa división en pantalla partida (Split Screen) o alineación asimétrica a la izquierda con generoso espacio negativo.
- **Micro-imágenes tipográficas inline:** Incrusta fotografías contextuales redondeadas entre palabras clave del titular como puntuación visual.
- **Prohibida la fila genérica de "3 tarjetas iguales":** Reemplázala por zig-zag de 2 columnas, cuadrículas asimétricas de bento-box o scroll horizontal controlado.

---

## 5. El Catálogo de los 19 Anti-Patrones Prohibidos (Banned AI Clichés)

1. ❌ **Cero emojis en la interfaz:** No utilices emojis como iconos ni decoraciones en botones, tarjetas o títulos.
2. ❌ **Cero fuentes genéricas sin calibrar:** No uses `Inter` puro ni serifs tradicionales como `Times New Roman` o `Georgia`.
3. ❌ **Cero negro puro (`#000000`):** Usa `#09090B`, `#121214` o `#18181B`.
4. ❌ **Cero gradientes neón o resplandores exteriores (outer glows).**
5. ❌ **Cero acentos sobresaturados (>80% saturación).**
6. ❌ **Cero texto con degradado excesivo en titulares grandes.**
7. ❌ **Cero cursores de mouse personalizados extravagantes.**
8. ❌ **Cero solapamiento sucio de texto sobre imágenes.**
9. ❌ **Cero filas simétricas de 3 tarjetas idénticas.**
10. ❌ **Cero nombres genéricos inventados:** ("John Doe", "Acme Corp", "Nexus AI").
11. ❌ **Cero métricas o estadísticas inventadas:** ("99.99% Uptime", "124ms response", "18.5k deployments"). Si no hay datos reales, utiliza placeholders explícitos como `[métrica]`.
12. ❌ **Cero secciones falsas de estadísticas:** ("BY THE NUMBERS", "KEY SYSTEM METRICS") con números ficticios.
13. ❌ **Cero formato de etiqueta artificial:** No uses `LABEL // 2025` o `SYSTEM // V1`.
14. ❌ **Cero clichés de redacción de IA:** ("Elevate", "Seamless", "Unleash", "Next-Gen", "Cutting-edge").
15. ❌ **Cero textos de relleno en UI:** ("Scroll to explore", "Swipe down", flechas que rebotan).
16. ❌ **Cero enlaces de imagen rotos:** Usa SVGs embebidos o `picsum.photos`.
17. ❌ **Cero loaders de spinner circular genérico:** Diseña skeletons a la medida de la tarjeta.
18. ❌ **Cero alturas `h-screen`:** Usa `min-h-[100dvh]` para evitar saltos bruscos en navegadores móviles.
19. ❌ **Cero desbordamiento horizontal en móvil:** En anchos menores a 768px, toda cuadrícula colapsa ordenadamente a una sola columna.
