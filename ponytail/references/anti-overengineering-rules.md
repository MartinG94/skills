# Catálogo de Reglas Anti-Sobreingeniería y Filosofía del "Lazy Senior Developer"

Este documento contiene la guía de referencia y los criterios de evaluación de la skill `ponytail`, inspirada en la filosofía de ingeniería pragmática de `DietrichGebert/ponytail`: *"El mejor código es el código que nunca escribiste; la segunda mejor opción es el código que pudiste eliminar"*.

---

## 1. Catálogo de Síntomas de Sobreingeniería (Overengineering Smells)

| Código | Síntoma / Antipadrón | Manifestación Típica | Corrección Mandatoria (Ponytail) |
|---|---|---|---|
| **OES-01** | **Wrapperitis Aguda** | Clases o funciones intermediarias de un solo uso que solo delegan una llamada (`class Service { get(id) { return this.repo.get(id); } }`). | Eliminar el wrapper intermediario y llamar directamente a la fuente. |
| **OES-02** | **Generalización Especulativa (YAGNI)** | Creación de interfaces genéricas, jerarquías de herencia, fábricas abstractas o builders para entidades que solo tienen una única implementación concreta hoy. | Implementar el caso concreto en una función o clase plana. No abstraer hasta tener al menos 3 casos reales diferentes. |
| **OES-03** | **Fragmentación de Archivos (File Sprawl)** | Dividir una lógica simple de 40 líneas en 5 o 6 archivos independientes (`types.ts`, `interfaces.ts`, `constants.ts`, `service.ts`, `factory.ts`, `index.ts`). | Colocar la lógica y sus tipos asociados juntos en un único archivo autocontenido. |
| **OES-04** | **Arquitectura Astronauta** | Introducir Event Sourcing, CQRS, Message Brokers o arquitectura hexagonal estricta en aplicaciones o servicios con baja concurrencia o lógica CRUD directa. | Usar arquitectura modular sencilla basada en funciones y servicios directos con límites claros. |
| **OES-05** | **Dependencia Compulsiva (NPM/PyPI Bloat)** | Instalar librerías externas pesadas para operaciones que la biblioteca estándar o las APIs modernas de la plataforma resuelven nativamente. | Reemplazar paquetes por primitivas nativas del lenguaje o entorno de ejecución. |
| **OES-06** | **Configurabilidad Prematura** | Crear 20 opciones de configuración, flags o variables de entorno para comportamientos que nunca cambian en la práctica. | Hardcodear constantes sensatas con nombres claros. Extraer a configuración únicamente lo que varíe por entorno (dev/staging/prod). |

---

## 2. Catálogo de Reemplazos Nativos de Bloat Común

### 2.1. Ecosistema JavaScript / TypeScript / Node.js

| Paquete Externo / Bloat | Reemplazo Nativo Moderno | Beneficio |
|---|---|---|
| `axios`, `got`, `node-fetch`, `request` | `fetch()`, `AbortController` (Global en Node 18+) | Cero dependencias, soporte de streaming nativo, interoperabilidad web. |
| `uuid` | `crypto.randomUUID()` (Global en Node 19+ y navegadores) | Nativo en C++, sin dependencias, criptográficamente seguro. |
| `lodash.clonedeep` | `structuredClone()` (Global en Node 17+ y navegadores) | Copia profunda nativa sin serialización JSON defectuosa. |
| `lodash.isequal` | Comparación por campos o `URLSearchParams` según contexto | Elimina miles de líneas de código reflexivo. |
| `chalk`, `colors` | `util.styleText()` (Node 22+) o códigos ANSI directos | Sin riesgo de vulnerabilidades ni dependencias de terminal. |
| `dotenv` | `node --env-file=.env` (Node 20.6+) o `process.env` nativo | Lectura nativa antes de la inicialización de módulos. |
| `glob`, `rimraf`, `mkdirp` | `fs.globSync()`, `fs.rmSync({ recursive: true })` (Node 22+) | Primitivas del sistema de archivos optimizadas. |
| `moment`, `date-fns` (casos básicos) | `Intl.DateTimeFormat`, APIs nativas de `Date` | Ahorro masivo de bundle size y tiempo de inicio. |

### 2.2. Ecosistema Python

| Paquete Externo / Bloat | Reemplazo Nativo Moderno | Beneficio |
|---|---|---|
| `requests` (para scripts o llamadas simples) | `urllib.request` con `json.loads` | Scripts completamente portables sin `pip install`. |
| Clases manuales con `__init__`, `__repr__` | `@dataclass(frozen=True)` o `NamedTuple` | Inmutabilidad declarativa y código conciso. |
| Librerías complejas de parsing CLI | `argparse` nativo | Soporte oficial, validación y autogeneración de ayuda. |
| Manipulación de rutas con `os.path` | `pathlib.Path` | Sintaxis orientada a objetos moderna y multiplataforma. |

---

## 3. Rúbrica de Auditoría de Complejidad (`/ponytail-audit`)

Toda revisión o auditoría bajo la skill `ponytail` debe evaluar la solución contra esta matriz cuantitativa:

| Criterio | Puntuación Excelente (Verde) | Advertencia (Amarillo) | Rechazo por Sobreingeniería (Rojo) |
|---|---|---|---|
| **Balance de Líneas (Net LOC)** | Reducción neta ($\Delta < 0$) o adición mínima justificada ($\Delta < 50$). | $+50$ a $+150$ LOC para una tarea puntual. | $> 150$ LOC adicionales para una función simple. |
| **Radio de Impacto (Blast Radius)** | 1 a 2 archivos modificados. | 3 a 4 archivos tocados. | $\ge 5$ archivos tocados para un cambio funcional localizado. |
| **Nuevas Dependencias** | 0 paquetes agregados (`package.json`, `requirements.txt`). | 1 paquete crítico sin alternativa nativa viable. | $\ge 2$ dependencias introducidas para tareas rutinarias. |
| **Capas de Indirección** | Llamada directa o 1 salto de delegación. | 2 saltos de delegación justificados. | $\ge 3$ saltos (Controlador ➔ Fachada ➔ Servicio ➔ Adaptador ➔ Repositorio). |
| **Presupuesto de Tokens** | Diff compacto, fácil de revisar en un vistazo ($< 100$ líneas de diff). | Diff moderado ($100$ a $300$ líneas). | Diff masivo ($> 300$ líneas) saturando la ventana de contexto. |

---

## 4. Plantilla de Salida Estandarizada (`/ponytail-review`)

Al invocar una revisión de código bajo el modo `/ponytail-review`, el reporte debe estructurarse con la siguiente plantilla:

```markdown
### Reporte de Revisión Ponytail: [Nombre de la Tarea / Módulo]

- **Veredicto:** [APROBADO | ALERTA DE COMPLEJIDAD | RECHAZADO POR SOBREINGENIERÍA]
- **Métricas Clave:**
  - Archivos Afectados: [X] (Límite sugerido: <= 2)
  - Balance de Líneas: [+A / -B / Balance Neto: C]
  - Dependencias Nuevas: [0 | Lista de paquetes agregados]
  - Profundidad de Indirección: [N niveles]

#### 1. Abstracciones y Wrappers Podados / Podables
- *[Archivo:Línea]*: [Descripción de la abstracción innecesaria y propuesta de eliminación].

#### 2. Reemplazos Nativos Disponibles
- *[Código actual]* ➔ *[Primitiva nativa del lenguaje]* (Elimina dependencia de `[paquete]`).

#### 3. Violaciones del Principio YAGNI
- *[Elemento especulativo]*: Diseñado para futuras extensiones no solicitadas. Recomendación: Simplificar a implementación directa.

#### 4. Propuesta de Refactorización Mínima (Diff Sugerido)
```diff
- // Código con 3 capas de indirección
+ // Solución directa en 5 líneas
```
```
