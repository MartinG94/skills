---
name: impeccable
description: "Auditoría visual anti-slop y refinamiento de alta precisión para interfaces de usuario web y landing pages. Modos: detect (identifica y audita clichés de IA, desalineaciones ópticas, sombras sucias, radios no concéntricos y saltos numéricos), polish (micro-refinamiento quirúrgico: bordes de luminancia de 1px, tabular-nums, compensación de iconos, radios concéntricos matemáticos), distill (poda de cajas redundantes y reducción de ruido visual) y animate (coreografía de microinteracciones con física y curvas naturales)."
---

# impeccable

Eleva interfaces web al nivel de artesanía digital de alta gama (*impeccable craft*), eliminando los anti-patrones estéticos genéricos de la IA ("AI slop") mediante precisión óptica, proporciones matemáticas rigurosas y coreografía de movimiento natural.

Inspirada en la filosofía y herramientas de `pbakaus/impeccable`.

---

## 1. Modos de Operación

| Modo | Comando / Gatillo | Propósito y Salida |
|---|---|---|
| **`detect`** | `/impeccable detect <archivo>` o "auditar diseño visual" | Escanea el componente y genera un informe de auditoría priorizado (Crítico, Advertencia, Sugerencia) señalando anti-patrones de AI-slop y desajustes ópticos. |
| **`polish`** | `/impeccable polish <archivo>` o "pulir UI al detalle" | Aplica micro-refinamientos quirúrgicos en el código: bordes sutiles de 1px, `tabular-nums`, radios concéntricos $R_{outer} = R_{inner} + Padding$ y alineación óptica. |
| **`distill`** | `/impeccable distill <archivo>` o "limpiar ruido visual" | Elimina cajas anidadas innecesarias ("card inception"), simplifica fondos y bordes en competencia, y restaura el aire tipográfico. |
| **`animate`** | `/impeccable animate <archivo>` o "añadir movimiento sutil" | Integra transiciones y microinteracciones de entrada y salida con física natural (resortes y curvas de aceleración), respetando siempre `prefers-reduced-motion`. |

---

## 2. Flujo de Trabajo por Modo

### 2.1 Modo `detect` (Auditoría Anti-Slop)
1. **Inspección de Clichés y Defectos:**
   - ¿Hay degradados violetas/índigos no justificados sobre fondos oscuros?
   - ¿Las sombras son manchas negras difusas y desaturadas (*muddy shadows*)?
   - ¿Los radios de cajas contenedoras e internas entran en conflicto? ($R_{inner} \ne R_{outer} - Padding$).
   - ¿Los números o contadores tiemblan al cambiar por falta de `tabular-nums`?
   - ¿Hay tarjetas metidas dentro de tarjetas sin jerarquía clara (*card inception*)?
   - ¿Se usan emojis en lugar de un set coherente de iconos vectoriales SVG?
2. **Entrega del Informe:**
   - Presentar el diagnóstico claro sin aplicar cambios automáticos, clasificando cada hallazgo por severidad y citando las líneas afectadas.

### 2.2 Modo `polish` (Refinamiento Quirúrgico)
1. **Corrección Matemática de Radios:**
   - Calcular $R_{inner} = \max(0, R_{outer} - Padding)$ para eliminar el pellizco en esquinas anidadas.
2. **Bordes de Luminancia de 1px:**
   - Reemplazar bordes oscuros o sombras pesadas en modo oscuro por bordes de un pixel con opacidad controlada (`rgba(255, 255, 255, 0.08)` o `oklch`).
3. **Estabilidad Tipográfica y Numérica:**
   - Añadir `tabular-nums` (`font-variant-numeric: tabular-nums`) en todas las columnas de métricas, contadores, timestamps y tablas.
   - Aplicar `text-wrap: balance` a titulares y títulos de tarjetas para evitar palabras huérfanas.
4. **Compensación Óptica de Iconos:**
   - Ajustar el alineamiento vertical de iconos con el texto contiguo (típicamente `translateY(-0.5px)` o normalización de `viewBox`).

### 2.3 Modo `distill` (Poda de Ruido Visual)
1. **Desmantelar Contenedores Redundantes:**
   - Retirar contenedores wrappers que solo aportan un borde adicional o un fondo gris sobre otro fondo gris.
2. **Priorizar Espacio en Blanco (White Space):**
   - Sustituir líneas divisorias y separadores agresivos por un espaciado modular limpio (múltiplos de 8px: `gap-4`, `gap-6`, `gap-8`).

### 2.4 Modo `animate` (Coreografía Natural)
1. **Curvas y Tiempos de Microinteracción:**
   - Mantener duraciones breves: 150ms a 220ms para botones, menus desplegables y toggles; 250ms a 320ms para modales o paneles laterales.
   - Usar curvas con entrada enérgica y desaceleración orgánica: `cubic-bezier(0.16, 1, 0.3, 1)`.
2. **Protección de Accesibilidad:**
   - Envolver las animaciones en `@media (prefers-reduced-motion: no-preference)` y proveer transiciones de opacidad instantáneas o nulas para usuarios sensibles al movimiento.

---

## 3. Heurísticas y Catálogo de Reglas

Para conocer las especificaciones matemáticas detalladas, ejemplos en CSS y clases de Tailwind CSS correspondientes, consultar:
- [references/impeccable-design-rules.md](references/impeccable-design-rules.md): Catálogo completo de anti-patrones y reglas de refinamiento visual.
