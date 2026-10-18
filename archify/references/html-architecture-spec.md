# Especificación de Documentos de Arquitectura Interactivos en HTML Autónomo

Esta referencia define el estándar y la plantilla base para generar documentos de arquitectura interactivos y autónomos (zero-dependency standalone HTML) mediante la skill `archify`.

---

## 1. Principios del Documento Autónomo

1. **Autonomía Total (Zero-Dependency Standalone):**
   - El archivo generado (`architecture.html` o `<proyecto>-architecture.html`) debe poder abrirse directamente en cualquier navegador moderno mediante doble clic o `file:///`, sin necesidad de un servidor web local (`http-server`), Node.js o bundlers.
   - Todo el CSS y JavaScript interactivo reside dentro de bloques `<style>` y `<script>` embebidos en el propio documento.
   - Para visualización de diagramas Mermaid, se incluye un fallback de SVG renderizado o bien la carga condicional de la librería Mermaid vía CDN con soporte offline elegante si no hay conectividad.

2. **Diseño y Ergonomía Visual:**
   - Soporte nativo para temas Claro / Oscuro (`dark` / `light`) respetando la preferencia del sistema (`prefers-color-scheme`) y con botón de alternancia persistente (`localStorage`).
   - Tipografía moderna basada en fuentes de sistema (`Inter`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto`).
   - Esquema de colores de alta legibilidad y contraste accesible (WCAG 2.2 AA).

3. **Capacidades Interactivas Clave:**
   - **Búsqueda y Filtrado en Tiempo Real:** Barra de búsqueda para filtrar módulos, servicios, endpoints o entidades por nombre, etiqueta o capa.
   - **Filtro por Capas (Layer Toggles):** Casillas o botones para aislar o destacar capas específicas (ej. *Frontend / Clientes*, *API / Gateway*, *Lógica de Dominio*, *Persistencia / Infraestructura*, *Servicios Externos*).
   - **Panel de Detalle / Inspector:** Al hacer clic en un nodo o componente del diagrama, el panel lateral muestra:
     - Nombre y tipo de componente.
     - Responsabilidad principal.
     - Puntos de entrada / interfaces expuestas.
     - Dependencias directas e inversas.
     - Enlaces a archivos fuente locales (`file:///...`).
   - **Vistas Múltiples Paginadas o por Pestañas:**
     1. *Vista Estructural (Arquitectura C4 / Bloques)*
     2. *Flujo de Datos y Eventos (Data Flow)*
     3. *Matriz de Dependencias (Dependency Matrix)*
     4. *Diagramas de Secuencia (Sequence Flows)*

---

## 2. Estructura del Modelo de Datos Embebido

El documento almacena los metadatos de los componentes en un bloque JSON estructurado dentro del `<head>` o al final del `<body>`:

```html
<script id="arch-data" type="application/json">
{
  "system": {
    "name": "Sistema de Ejemplo",
    "version": "1.0.0",
    "updatedAt": "2026-10-18",
    "description": "Arquitectura modular para procesamiento de transacciones y pagos."
  },
  "layers": [
    { "id": "clients", "name": "Clientes y Consumidores", "color": "#3b82f6" },
    { "id": "gateway", "name": "API & Ingress", "color": "#8b5cf6" },
    { "id": "services", "name": "Servicios de Dominio", "color": "#10b981" },
    { "id": "storage", "name": "Persistencia & Datos", "color": "#f59e0b" }
  ],
  "components": [
    {
      "id": "web-spa",
      "name": "Portal Web (Next.js)",
      "layer": "clients",
      "summary": "Aplicación web SPA para usuarios finales.",
      "path": "frontend/src/app",
      "dependencies": ["api-gateway"],
      "tags": ["frontend", "react", "typescript"]
    },
    {
      "id": "api-gateway",
      "name": "API Gateway (FastAPI)",
      "layer": "gateway",
      "summary": "Punto de entrada único HTTP; valida JWT y enruta peticiones.",
      "path": "backend/src/gateway",
      "dependencies": ["order-service", "auth-service"],
      "tags": ["backend", "python", "http"]
    },
    {
      "id": "order-service",
      "name": "Servicio de Órdenes",
      "layer": "services",
      "summary": "Gestiona ciclo de vida de compras, inventario y facturación.",
      "path": "backend/src/services/orders",
      "dependencies": ["orders-db"],
      "tags": ["core", "business-logic"]
    },
    {
      "id": "orders-db",
      "name": "Base de Datos de Órdenes",
      "layer": "storage",
      "summary": "PostgreSQL 16 particionado con réplicas de lectura.",
      "path": "infrastructure/postgres",
      "dependencies": [],
      "tags": ["database", "sql"]
    }
  ]
}
</script>
```

---

## 3. Plantilla Base de Documento HTML Autónomo

```html
<!DOCTYPE html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arquitectura del Sistema - Documento Interactivo</title>
  <style>
    :root {
      --bg: #0f172a;
      --bg-surface: #1e293b;
      --bg-surface-hover: #334155;
      --border: #334155;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --radius: 8px;
      --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    [data-theme="light"] {
      --bg: #f8fafc;
      --bg-surface: #ffffff;
      --bg-surface-hover: #f1f5f9;
      --border: #e2e8f0;
      --text: #0f172a;
      --text-muted: #64748b;
      --primary: #0284c7;
      --primary-hover: #0369a1;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font);
      background-color: var(--bg);
      color: var(--text);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }
    header {
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }
    .header-title { font-size: 1.1rem; font-weight: 600; display: flex; align-items: center; gap: 8px; }
    .header-controls { display: flex; align-items: center; gap: 12px; }
    .search-input {
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 6px 12px;
      border-radius: var(--radius);
      font-size: 0.9rem;
      outline: none;
      width: 240px;
    }
    .search-input:focus { border-color: var(--primary); }
    .btn {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 6px 12px;
      border-radius: var(--radius);
      cursor: pointer;
      font-size: 0.85rem;
      transition: background 0.15s;
    }
    .btn:hover { background: var(--bg-surface-hover); }
    .btn-active { background: var(--primary); color: #fff; border-color: var(--primary); }
    main {
      display: flex;
      flex: 1;
      overflow: hidden;
    }
    aside.sidebar {
      width: 320px;
      background: var(--bg-surface);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      overflow-y: auto;
    }
    .sidebar-section { padding: 16px; border-bottom: 1px solid var(--border); }
    .sidebar-section h3 { font-size: 0.8rem; text-transform: uppercase; color: var(--text-muted); margin-bottom: 8px; letter-spacing: 0.5px; }
    .layer-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.8rem;
      margin-bottom: 4px;
      cursor: pointer;
      user-select: none;
    }
    .component-list-item {
      padding: 10px 12px;
      border-radius: var(--radius);
      cursor: pointer;
      margin-bottom: 4px;
      border: 1px solid transparent;
      transition: all 0.15s;
    }
    .component-list-item:hover { background: var(--bg-surface-hover); }
    .component-list-item.selected { border-color: var(--primary); background: var(--bg-surface-hover); }
    .viewport {
      flex: 1;
      display: flex;
      flex-direction: column;
      background: var(--bg);
      overflow: hidden;
      position: relative;
    }
    .tabs-bar {
      display: flex;
      gap: 8px;
      padding: 12px 20px;
      border-bottom: 1px solid var(--border);
      background: var(--bg-surface);
    }
    .diagram-container {
      flex: 1;
      padding: 24px;
      overflow: auto;
      display: flex;
      justify-content: center;
      align-items: flex-start;
    }
    aside.inspector {
      width: 340px;
      background: var(--bg-surface);
      border-left: 1px solid var(--border);
      padding: 20px;
      overflow-y: auto;
      display: none;
    }
    aside.inspector.open { display: block; }
    .inspector h2 { font-size: 1.2rem; margin-bottom: 8px; }
    .inspector p { font-size: 0.9rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 16px; }
    .inspector-meta { font-size: 0.85rem; margin-bottom: 12px; }
    .inspector-meta strong { color: var(--text); }
  </style>
</head>
<body>
  <header>
    <div class="header-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3h7v7H3zM14 3h7v7h-7zM14 14h7v7h-7zM3 14h7v7H3z"/></svg>
      <span id="title-text">Arquitectura del Sistema</span>
    </div>
    <div class="header-controls">
      <input type="text" class="search-input" id="search-box" placeholder="Buscar componente o etiqueta...">
      <button class="btn" id="theme-toggle" title="Cambiar tema">🌓 Tema</button>
    </div>
  </header>
  <main>
    <aside class="sidebar">
      <div class="sidebar-section">
        <h3>Filtro por Capas</h3>
        <div id="layer-filters"></div>
      </div>
      <div class="sidebar-section" style="flex:1;">
        <h3>Componentes (<span id="comp-count">0</span>)</h3>
        <div id="component-list"></div>
      </div>
    </aside>
    <section class="viewport">
      <div class="tabs-bar">
        <button class="btn btn-active" data-view="c4">Arquitectura C4</button>
        <button class="btn" data-view="dataflow">Flujo de Datos</button>
        <button class="btn" data-view="matrix">Matriz de Dependencias</button>
      </div>
      <div class="diagram-container" id="diagram-mount">
        <!-- El diagrama Mermaid o SVG interactivo se monta aquí -->
      </div>
    </section>
    <aside class="inspector" id="inspector-panel">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <span style="font-size:0.75rem; text-transform:uppercase; color:var(--primary); font-weight:700;" id="ins-layer">Capa</span>
        <button class="btn" style="padding:2px 8px;" id="close-inspector">✕</button>
      </div>
      <h2 id="ins-name">Componente</h2>
      <p id="ins-summary">Descripción detallada del componente y su rol en el sistema.</p>
      <div class="inspector-meta">
        <div><strong>Ubicación:</strong> <span id="ins-path">src/...</span></div>
        <div style="margin-top:6px;"><strong>Dependencias:</strong> <span id="ins-deps">Ninguna</span></div>
        <div style="margin-top:6px;"><strong>Etiquetas:</strong> <span id="ins-tags">-</span></div>
      </div>
    </aside>
  </main>

  <script>
    // Inicialización de temas y listeners interactivos
    const themeBtn = document.getElementById('theme-toggle');
    themeBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('archify-theme', next);
    });
    const savedTheme = localStorage.getItem('archify-theme');
    if (savedTheme) document.documentElement.setAttribute('data-theme', savedTheme);

    // Inspector controller
    const inspector = document.getElementById('inspector-panel');
    document.getElementById('close-inspector').addEventListener('click', () => {
      inspector.classList.remove('open');
    });

    function selectComponent(comp) {
      document.getElementById('ins-name').textContent = comp.name;
      document.getElementById('ins-layer').textContent = comp.layer;
      document.getElementById('ins-summary').textContent = comp.summary;
      document.getElementById('ins-path').textContent = comp.path;
      document.getElementById('ins-deps').textContent = comp.dependencies.length > 0 ? comp.dependencies.join(', ') : 'Ninguna';
      document.getElementById('ins-tags').textContent = comp.tags.join(', ');
      inspector.classList.add('open');
    }
  </script>
</body>
</html>
```

---

## 4. Convenciones de Generación

1. **Orientación Horizontal por Defecto:**
   Los diagramas de arquitectura, flujo de datos y dependencias deben usar orientación `flowchart LR` o `graph LR` para optimizar pantallas apaisadas de escritorio.
2. **Identificadores Limpios:**
   Usar IDs en kebab-case (`order-service`, `auth-gateway`, `redis-cache`) consistentes en el JSON y en los nodos del diagrama.
3. **Generación Determinista:**
   El entregable debe guardarse en `architecture.html` dentro de la carpeta del proyecto o en la ruta indicada por el usuario, acompañado de un resumen en Markdown.
