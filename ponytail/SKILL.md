---
name: ponytail
description: >-
  Aplica la filosofía del "Lazy Senior Developer": el mejor código es el que nunca se
  escribe y la mejor refactorización es la que elimina líneas. Erradica la sobreingeniería,
  los wrappers innecesarios, las abstracciones prematuras (YAGNI) y la fragmentación de
  archivos. Prioriza capacidades nativas del lenguaje/plataforma y minimiza el radio de impacto.
  Opera en modos implement, review (/ponytail-review) y audit (/ponytail-audit).
---

# Filosofía del "Lazy Senior Developer" y Control de Sobreingeniería

## Responsabilidad y Principios Fundamentales

La skill `ponytail` actúa como un filtro implacable contra la sobreingeniería, el código defensivo desmedido y la complejidad accidental. Encarna la sabiduría del desarrollador senior pragmático: resolver el problema real con la menor cantidad de piezas móviles posible, reduciendo la superficie de mantenimiento futura.

### Las Leyes Fundamentales de Ponytail:

1. **Ley de Sustracción:** La métrica reina es el código eliminado. Cada línea agregada es un pasivo de mantenimiento; cada línea eliminada es una ganancia neta de estabilidad.
2. **Ley de Primitivas Nativas:** Antes de instalar o invocar un paquete externo (`npm`, `pip`, `cargo`), utilizar las capacidades nativas provistas por la biblioteca estándar del lenguaje o el runtime actual.
3. **Ley Anti-YAGNI (You Aren't Gonna Need It):** Queda terminantemente prohibido diseñar para requerimientos hipotéticos del futuro. No crear fábricas, interfaces abstractas ni estrategias intercambiables si solo existe una única implementación concreta en el presente.
4. **Ley de Mínimo Radio de Impacto (Blast Radius):** Concentrar los cambios en la menor cantidad de archivos posible. Una solución de 30 líneas en 1 archivo existente es superior a dispersar 30 líneas en 4 archivos nuevos (`types.ts`, `interface.ts`, `impl.ts`, `index.ts`).
5. **Presupuesto de Complejidad y Tokens:** Producir diffs quirúrgicos y legibles a primera vista, evitando sobrecargar el contexto y la mente del revisor humano.

---

## Modos Operativos

### 1. Modo `implement` (Predeterminado)

Se activa al solicitar la implementación o modificación de una funcionalidad:
- **Estrategia Minimalista:** Identificar la ruta más corta y directa para cumplir el objetivo.
- **Reutilización Interna:** Inspeccionar el repositorio en busca de utilidades y funciones auxiliares existentes antes de escribir código nuevo.
- **Sin Wrappers Espurios:** Llamar a las funciones y librerías directamente en el punto de uso sin envolverlas en capas decorativas vacías.
- **Consolidación de Archivos:** Escribir los tipos o constantes auxiliares en el mismo archivo donde se consumen salvo que se demuestre su uso transversal en $\ge 3$ módulos independientes.

### 2. Modo `review` (`/ponytail-review`)

Se activa al revisar un Pull Request, un diff o un archivo específico con el comando `/ponytail-review`:
- **Caza de Wrappers:** Marcar para eliminación cualquier clase o función que solo actúe como pasamanos de argumentos sin transformar datos ni aplicar reglas de negocio.
- **Detección de Dependencias Redundantes:** Señalar paquetes externos que puedan reemplazarse por APIs nativas de la plataforma (ej. reemplazar `axios` por `fetch`, `uuid` por `crypto.randomUUID()`, `lodash.cloneDeep` por `structuredClone()`).
- **Poda de Abstracciones Prematuras:** Desmantelar jerarquías de herencia artificiales y transformar patrones de diseño sobrecargados en simples funciones puras.
- **Emisión de Reporte:** Generar el informe estructurado indicando el balance de líneas (Net LOC), archivos afectados y la propuesta de refactorización mínima.

### 3. Modo `audit` (`/ponytail-audit`)

Se activa al solicitar una auditoría general de complejidad o superficie de mantenimiento de un proyecto (`/ponytail-audit`):
- Evaluar la profundidad del árbol de llamadas (*call stack depth*).
- Identificar archivos con menos de 15 líneas de código que puedan fusionarse con sus consumidores directos.
- Diagnosticar dependencias huérfanas o sobredimensionadas en el gestor de paquetes (`package.json`, `requirements.txt`, etc.).
- Producir un plan de consolidación y desmantelamiento de deuda de complejidad.

---

## Directivas de Decisión Rápida

| Si estás a punto de... | ¡ALTO! Aplica Ponytail: |
|---|---|
| Crear una clase `*Manager` o `*Helper` con un solo método estático. | Escribe una función normal exportada o ejecútala in-line. |
| Agregar una dependencia para hacer una petición HTTP o calcular un hash. | Usa `fetch()` nativo o el módulo `crypto` de la plataforma. |
| Crear una interfaz genérica `IRepository<T>` para una única entidad. | Implementa la consulta SQL o llamada directa en el servicio correspondiente. |
| Crear una carpeta con 5 archivos para un componente que solo se usa en un lugar. | Mantén el componente en un solo archivo hasta que crezca orgánicamente. |
| Añadir 10 opciones de configuración a una función "por si acaso". | Deja el valor por defecto fijo. Añade opciones solo cuando un llamador real las exija. |

---

## Guía de Referencia Avanzada

Para consultar el catálogo exhaustivo de síntomas de sobreingeniería, la tabla de reemplazos nativos en Node.js/Python, la rúbrica cuantitativa de complejidad y la plantilla completa de revisión, consultar:
- [Catálogo de Reglas Anti-Sobreingeniería](file:///c:/git/skills/ponytail/references/anti-overengineering-rules.md)
