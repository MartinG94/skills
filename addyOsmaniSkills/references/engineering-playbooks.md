# Playbooks de Ingeniería de Producción, Rendimiento Web y Desarrollo Guiado por Especificación

Este documento contiene los manuales técnicos y playbooks de referencia de la skill `addyOsmaniSkills`, basados en los estándares de ingeniería de software para producción formulados por Addy Osmani (`addyosmani/agent-skills`).

---

## 1. Playbook de Desarrollo Guiado por Especificación (Spec-Driven Development)

El desarrollo guiado por especificación establece que antes de escribir código de producción, el diseño del sistema, los contratos y los casos borde deben articularse y validarse en un documento vivo de especificación (`SPEC.md`).

### 1.1. Estructura Canónica de `SPEC.md`

Un documento de especificación completo y riguroso debe estructurarse obligatoriamente con las siguientes secciones:

```markdown
# SPEC-[ID]: [Título Técnico de la Funcionalidad / Módulo]

## 1. Contexto y Objetivos
- **Problema de Negocio / Técnico:** Qué dolor o deficiencia se está resolviendo.
- **Objetivos de Éxito:** Métricas cuantitativas o criterios observables que definirán el éxito.
- **Fuera de Alcance (Non-Goals):** Límites explícitos de lo que NO se resolverá en esta iteración.

## 2. Modelos de Datos y Contratos de Entidades
- Definición de tipos estáticos (TypeScript / Python Dataclasses / Rust Structs).
- Validaciones e invariantes de dominio (ej. esquemas Zod o Pydantic).

## 3. Contratos de API e Interfaces de Integración
- Endpoints HTTP, métodos RPC o eventos emitidos/consumidos.
- Estructura de peticiones, respuestas y códigos de error (RFC 9457).

## 4. Máquina de Estados Finita (FSM)
- Estados posibles del componente o entidad (ej. `idle` | `loading` | `success` | `error`).
- Eventos desencadenantes y transiciones válidas.
- Manejo de estados de carrera y reintentos.

## 5. Matriz de Casos Borde y Escenarios de Falla
- Comportamiento ante fallos de conectividad, payloads gigantes o malformados, concurrencia simultánea y límites de tasa (rate limiting).

## 6. Plan de Verificación y Criterios de Aceptación
- Lista de tests unitarios, de integración y rendimiento que deben pasar al 100%.
```

---

## 2. Playbook de Core Web Vitals y Rendimiento Web de Alto Impacto

El rendimiento web no es una tarea accesoria de pulido final; es una restricción arquitectónica fundamental. Las tres métricas de Core Web Vitals (CWV) deben cumplirse de forma estricta:

```
┌────────────────────────────┬────────────────────────────┬────────────────────────────┐
│   LCP (Largest Paint)      │   INP (Interaction Paint)  │   CLS (Layout Shift)       │
│   Objetivo: < 2.5 segundos │   Objetivo: < 200 ms       │   Objetivo: < 0.1          │
└────────────────────────────┴────────────────────────────┴────────────────────────────┘
```

### 2.1. Optimización de Largest Contentful Paint (LCP < 2.5s)

1. **Priorización de Recursos Críticos:**
   - Asignar `fetchpriority="high"` al elemento hero visualmente principal (imagen o banner superior).
   - Pre-cargar fuentes críticas y la imagen de cabecera en el `<head>` del HTML:
     ```html
     <link rel="preload" as="image" href="/hero.avif" fetchpriority="high" />
     <link rel="preload" as="font" href="/fonts/inter.woff2" type="font/woff2" crossorigin />
     ```
2. **Formato y Compresión de Medios:**
   - Utilizar formatos modernos AVIF o WebP con compresión adaptativa según la resolución del cliente (`<picture>` con `srcset`).
3. **Eliminación de Bloqueos de Renderizado:**
   - Evitar hojas de estilo CSS o scripts síncronos sin `defer` o `type="module"` antes de la etiqueta del LCP.
   - Entregar el HTML inicial mediante Server-Side Rendering (SSR) o streaming con las secciones críticas renderizadas.

### 2.2. Optimización de Interaction to Next Paint (INP < 200ms)

1. **Fragmentación de Tareas Largas (Long Tasks > 50ms):**
   - El hilo principal de JavaScript nunca debe bloquearse por más de 50ms durante una interacción del usuario.
   - Interrumpir bucles pesados de procesamiento cediendo el control al planificador del navegador:
     ```typescript
     async function yieldToMain() {
       if ('scheduler' in window && 'yield' in (window as any).scheduler) {
         await (window as any).scheduler.yield();
       } else {
         await new Promise(resolve => setTimeout(resolve, 0));
       }
     }
     ```
2. **Optimización de Handlers de Eventos:**
   - Aplicar *debounce* o *throttle* riguroso a eventos de alta frecuencia (`scroll`, `resize`, `input`).
   - Evitar leer propiedades de diseño (`offsetHeight`, `getBoundingClientRect`) inmediatamente después de modificar estilos en el mismo tick (previene el *Forced Synchronous Layout* o *Layout Thrashing*).
3. **Delegación de Renderizado Complejo:**
   - Usar `requestAnimationFrame` para animaciones visuales continuas o Web Workers para cómputos criptográficos/analíticos intensivos.

### 2.3. Eliminación de Cumulative Layout Shift (CLS < 0.1)

1. **Dimensionamiento Explícito de Contenedores:**
   - Toda etiqueta `<img>`, `<video>` o `<iframe>` debe declarar obligatoriamente atributos `width` y `height`, o la propiedad CSS `aspect-ratio`:
     ```css
     .card-banner {
       width: 100%;
       aspect-ratio: 16 / 9;
     }
     ```
2. **Espacio Reservado para Contenido Dinámico:**
   - Reservar contenedores con altura mínima (`min-height`) para anuncios, banners de cookies o componentes que cargan asíncronamente.
3. **Prevención de Saltos por Fuentes Web (FOUT/FOIT):**
   - Emplear `font-display: optional` para fuentes web donde el rendimiento sea crítico, o calcular métricas de reemplazo tipográfico (*Font Metric Overrides*):
     ```css
     @font-face {
       font-family: 'FallbackFont';
       src: local('Arial');
       ascent-override: 90%;
       descent-override: 22%;
       size-adjust: 105%;
     }
     ```

---

## 3. Presupuesto de Rendimiento y Carga de Paquetes (Bundle Budgeting)

- **Presupuesto Inicial:** Máximo $100\text{ KB}$ de JavaScript comprimido (Brotli/Gzip) en la carga inicial de cualquier ruta de usuario.
- **División de Código (Code-Splitting):** Cargar componentes pesados (gráficos, editores enriquecidos, visores 3D) bajo demanda mediante importación dinámica (`React.lazy()`, `import()`).
- **Arquitectura de Islas e Hidratación Selectiva:** Priorizar HTML estático generado en el servidor, hidratando únicamente las pequeñas islas interactivas que lo requieran.

---

## 4. Protocolo de Entrevista Técnica (`interview-me`)

Cuando se solicita el modo `interview-me` para clarificar un requerimiento antes de codificar, el agente debe formular una serie estructurada de 4 a 6 preguntas de alto calibre técnico orientadas a:

1. **Volumetría y Escala:** ¿Cuál es la concurrencia esperada (RPS) y el volumen diario de registros en la base de datos?
2. **Políticas de Consistencia y Fallo:** Si el servicio externo de procesamiento cae, ¿se bloquea la operación síncronamente o se encola con reintentos en segundo plano?
3. **Manejo de Estados de Borde:** ¿Qué sucede si el usuario cancela la operación a la mitad de la transacción?
4. **Idempotencia y Concurrencia:** ¿Cómo se identifican transacciones duplicadas generadas por doble clic o pérdida de conexión?
5. **Restricciones de Rendimiento y Latencia:** ¿Cuál es el SLA de respuesta tolerable para el usuario final en redes móviles lentas (3G/4G)?
