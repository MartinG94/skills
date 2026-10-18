# understandAnything

Skill para comprensión profunda de repositorios de software, extracción de modelos mentales, trazabilidad de flujos de ejecución y generación de guías de onboarding técnico.

Inspirada en `Egonex-AI/Understand-Anything`, esta skill proporciona un enfoque estructurado para que desarrolladores y agentes de IA comprendan rápidamente bases de código complejas sin suposiciones infundadas ni lecturas masivas innecesarias.

---

## 1. Propósito General

`understandAnything` transforma un repositorio de código desconocido en un modelo mental claro y accionable mediante tres capacidades clave:
- **Mapeo Arquitectónico (`map`):** Identificación de dominios, capas, puntos de entrada y diagramas estructurales C4/Mermaid en orientación horizontal (`LR`).
- **Trazabilidad de Flujos (`explain`):** Reconstrucción determinista de cadenas de ejecución paso a paso con enlaces verificables `archivo:línea` y diagramas de secuencia.
- **Onboarding Técnico (`onboard`):** Creación de guías de incorporación en 30 minutos con orden de lectura optimizado, invariantes críticos no negociables y matriz "¿dónde tocar para...?".

---

## 2. Arquitectura Interna

```
understandAnything/
├── SKILL.md                                # Contrato operativo del agente (YAML frontmatter + directivas)
├── README.md                               # Documentación para desarrolladores humanos
└── references/                             # Guías, heurísticas y plantillas
    └── comprehension-templates.md          # Plantillas de mapas de dominio, flujos y onboarding
```

---

## 3. Prerequisitos e Integraciones

- **Integración con Servidores MCP de Grafo:**
  - `codebase-memory` / `codebase-memory-mcp`: Permite consultar `get_architecture`, `search_graph` y `trace_path` para evitar escaneos textuales masivos.
  - `graphify`: Reutiliza grafos preexistentes en `graphify-out/graph.json` para saltar directamente a consultas de comunidades y nodos centrales.
- **Optimización de Consola:**
  - Uso automático de `rtk` (`rtk find`, `rtk grep`, `rtk ls`) para minimizar consumo de tokens en exploraciones terminales.

---

## 4. Modos Operativos y Ejemplos de Invocación

### Modo 1: `map`
**Cuándo usar:** Al ingresar por primera vez a un repositorio o al documentar la arquitectura general de un sistema.
```markdown
/understandAnything map
```
*Pregunta equivalente:* "¿Cómo está estructurado este proyecto y cuáles son sus puntos de entrada principales?"

### Modo 2: `explain`
**Cuándo usar:** Para auditar, depurar o entender la lógica completa de una mutación, endpoint o proceso de negocio.
```markdown
/understandAnything explain "Proceso de checkout y confirmación de pago"
```
*Pregunta equivalente:* "¿Cómo viaja la petición desde que entra por la API hasta que se guarda en la base de datos y se envían las notificaciones?"

### Modo 3: `onboard`
**Cuándo usar:** Para incorporar a un desarrollador nuevo al equipo o al iniciar una sesión de trabajo sobre un subsistema desconocido.
```markdown
/understandAnything onboard
```
*Pregunta equivalente:* "Genera una guía de onboarding para un desarrollador nuevo con los archivos clave a leer y los invariantes que no debe romper."

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Código fuente local del repositorio (`C:\git\<repo>`).
- Especificaciones técnicas, esquemas de bases de datos o rutas HTTP del sistema.
- Consultas de lenguaje natural sobre módulos o flujos específicos.

### Salidas (Outputs)
- `CODEBASE_MAP.md`: Mapa de capas, límites de dominio, puntos de entrada y diagrama Mermaid horizontal C4 (`flowchart LR`).
- `FLOW_TRACE.md`: Trazabilidad detallada de llamadas con enlaces a código `[archivo:línea](file:///...)`, diagramas de secuencia y gestión de excepciones.
- `ONBOARDING.md`: Guía de incorporación técnica, checklist de invariantes, orden cronológico de lectura y matriz de tareas comunes.
