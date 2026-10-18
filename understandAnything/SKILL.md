---
name: understandAnything
description: "Comprensión profunda de codebases, extracción de modelos mentales y grafos arquitectónicos, trazabilidad de flujos de ejecución y onboarding acelerado de desarrolladores. Modos: map (mapeo de dominios, capas y puntos de entrada), explain (rastreo de flujos extremo a extremo con enlaces archivo:línea) y onboard (guías estructuradas de incorporación técnica con orden de lectura e invariantes). Se integra nativamente con codebase-memory MCP y graphify."
---

# understandAnything

Comprende en profundidad cualquier repositorio de software, reconstruye su modelo mental y arquitectónico, y genera guías de incorporación técnica sin inventar supuestos ni perderse en detalles irrelevantes.

---

## 1. Principios de Operación

1. **Evidencia Comprobable y Citas `file:line`:**
   Toda afirmación estructural o de flujo debe estar respaldada por una cita verificable en el código fuente utilizando enlaces en formato Markdown: `[archivo:línea](file:///ruta/al/archivo#LXX)`.
2. **Separación Estricta: Hechos vs. Inferencias:**
   - **Hecho comprobado:** Código visible, tipos declarados o tests ejecutables.
   - **Inferencia lógica:** Hipótesis sobre diseño o intención; debe marcarse explícitamente con `[Inferencia]`.
3. **Exploración Jerárquica y Eficiente (Graph First):**
   Antes de leer archivos masivos con grep o cat, consultar herramientas de grafo (`codebase-memory` MCP o `graphify`).

---

## 2. Modos de Uso y Selección de Modo

| Modo | Desencadenante / Pregunta | Entregable Proporcional |
|---|---|---|
| **`map`** | "¿Cómo está estructurado este proyecto?", "¿Cuáles son los módulos y capas principales?", "Mapear arquitectura" | Mapa de dominios, capas, puntos de entrada y diagrama Mermaid C4/LR (`CODEBASE_MAP.md`). |
| **`explain`** | "¿Cómo funciona el flujo X?", "¿Qué pasa cuando se llama a Y?", "Rastrear ciclo de vida de Z" | Trazabilidad de llamadas paso a paso, diagrama de secuencia y manejo de errores (`FLOW_TRACE.md`). |
| **`onboard`** | "Soy nuevo en el equipo, ¿por dónde empiezo?", "Guía de onboarding", "Mental model del repo" | Guía de 30 minutos: modelo mental, invariantes no negociables, orden de lectura y guía "¿dónde tocar para...?" (`ONBOARDING.md`). |

---

## 3. Integración con Servidores MCP y Herramientas

Antes de iniciar la exploración manual:

1. **Inspección de `graphify`:**
   - Comprobar si existe `graphify-out/graph.json` en la raíz del proyecto.
   - Si existe, usar las consultas de grafo o el reporte para acelerar la identificación de clusters y nodos centrales ("god nodes").
2. **Inspección de `codebase-memory` MCP:**
   - Si el servidor MCP `codebase-memory` o `codebase-memory-mcp` está disponible, utilizar:
     - `get_architecture`: para obtener las capas y módulos indexados.
     - `search_graph`: para ubicar conceptos o símbolos clave.
     - `trace_path`: para reconstruir rutas de llamadas entre dos módulos o componentes.
3. **Fallback Asistido por `rtk`:**
   - Si no hay grafos preindexados, usar comandos con prefijo `rtk` para localizar manifests y entrypoints:
     - Localizar manifests: `rtk find package.json`, `rtk find Cargo.toml`, `rtk find pyproject.toml`.
     - Localizar entrypoints: `rtk grep "listen\(" src/`, `rtk grep "main\(" src/`.

---

## 4. Protocolo Paso a Paso por Modo

### Modo 1: `map` (Mapeo Arquitectónico y de Dominios)
1. **Identificar el Corazón del Sistema:**
   - Localizar el archivo de configuración del proyecto (`package.json`, `go.mod`, etc.) para entender dependencias clave.
   - Localizar puntos de entrada (`main.ts`, `server.js`, `cmd/main.go`, `index.py`).
2. **Descubrir Capas y Delimitaciones:**
   - Identificar si sigue un patrón reconocible (Clean Architecture, Hexagonal, MVC, Feature-sliced design, Monorepo con workspaces).
   - Mapear carpetas a responsabilidades de dominio en una tabla estructurada.
3. **Generar Diagrama Mermaid:**
   - Producir un diagrama de bloques o arquitectura horizontal (`flowchart LR`) que muestre cómo interactúan los clientes, puntos de entrada, lógica de negocio e infraestructura (bases de datos, servicios externos).
4. **Persistencia:**
   - Guardar el análisis en `CODEBASE_MAP.md` siguiendo la plantilla en [references/comprehension-templates.md](references/comprehension-templates.md).

### Modo 2: `explain` (Rastreo de Flujos Extremo a Extremo)
1. **Identificar el Disparador (Trigger):**
   - Determinar dónde se origina el estímulo (ej. un evento HTTP, un mensaje en una cola AMQP, un comando CLI, un click de UI).
2. **Trazar la Cadena de Ejecución (Execution Trace):**
   - Seguir el flujo a través de routers, middlewares, controladores, servicios de aplicación y repositorios.
   - Anotar cada salto de función con su ruta de archivo y número de línea exacto: `[NombreArchivo:Línea](file:///...)`.
3. **Documentar Efectos Secundarios:**
   - Identificar mutaciones en base de datos, emisiones de eventos, escritura de archivos o llamadas a APIs externas.
4. **Mapear Invariantes y Fallbacks:**
   - ¿Qué validaciones ocurren? ¿Cómo se manejan errores y excepciones? ¿Hay transacciones con rollback?
5. **Persistencia:**
   - Generar el diagrama `sequenceDiagram` y guardar el reporte en `FLOW_TRACE.md`.

### Modo 3: `onboard` (Guía de Incorporación para Desarrolladores)
1. **Destilar el Modelo Mental:**
   - Resumir en 3-5 párrafos qué hace el sistema, quiénes son los usuarios y cómo fluye la información principal.
2. **Extraer Invariantes Críticos:**
   - Identificar reglas que un desarrollador nuevo NUNCA debe romper (ej. reglas de concurrencia, transacciones, convenciones de nombres de eventos, validación de tipos obligatoria).
3. **Determinar la Ruta de Lectura Óptima:**
   - Ordenar de 4 a 6 archivos clave que deben leerse en secuencia para entender el 80% de la lógica de negocio sin abrumarse.
4. **Construir la Matriz "¿Dónde Tocar para...?":**
   - Indicar archivos que deben modificarse para tareas frecuentes (crear endpoint, modificar modelo, conectar webhook).
5. **Persistencia:**
   - Guardar la guía en `ONBOARDING.md` usando la plantilla de [references/comprehension-templates.md](references/comprehension-templates.md).

---

## 5. Referencias y Recursos

- [references/comprehension-templates.md](references/comprehension-templates.md): Plantillas detalladas para mapas arquitectónicos, trazabilidad de flujos y manuales de onboarding.
