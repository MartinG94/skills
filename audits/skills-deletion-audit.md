# Auditoría de eliminaciones y compatibilidad de Skills

**Fecha:** 2026-09-08  
**Repositorio:** `D:\Proyectos-mg\skills`  
**Branch de auditoría:** `codex/skills-deletion-audit`  
**Estado del árbol al iniciar:** limpio  
**Alcance primario:** `1db737a..a039b86` (integrado en `main` por `35239db`)  
**Antecedentes revisados:** `449f64e` y `0739617`

## 1. Resumen ejecutivo

La refactorización principal reescribió 19 de las 22 skills existentes. Sus
`SKILL.md` pasaron de 76.729 a 16.733 palabras (reducción de 78,2 %) y de 11.451 a
2.250 líneas (reducción de 80,4 %). El tamaño de la reducción justificaba revisar la
secuencia de commits y los recursos auxiliares, no sólo el resultado actual.

La conclusión general es **riesgo moderado y corregible**. La mayor parte del texto
eliminado era teoría extensa, ejemplos completos, código ligado a frameworks,
duplicación de formatos o prescripciones no sustentadas. Su retiro mejoró el foco y,
en varios casos, evitó que un agente inventara arquitectura, tecnología o datos. No se
encontró una pérdida funcional P0 ni una razón técnica para restaurar masivamente las
versiones anteriores.

La clasificación primaria por paquete/identidad es la siguiente. La categoría indica
el efecto dominante de la eliminación; una transferencia a un recurso auxiliar puede
coexistir con cualquiera de ellas.

| Categoría | Cantidad | Paquetes o identidades |
|---|---:|---|
| A — Eliminación correcta | 15 | `backend-testing`, `bpmn-extractor`, `crud-validator`, `design-ux-ui`, `domain-design`, `domain-model-gen`, `epc-flow-gen`, `gof-adviser`, `grasp-sequence-realizer`, `microservice-decomposer`, `orm-master`, `relational-object-map`, `requirements-extractor`, `system-classifier`, `uml-consistency` |
| B — Correcta pero demasiado agresiva | 2 | `api-design`, `use-case-extractor` |
| C — Eliminación riesgosa | 3 | catálogo de rutas de `mermaid-diagram-gen`, taxonomía de `quality-scenario-specifier`, identidad eliminada `design-md` |
| D — Eliminación incorrecta comprobada | 0 | No se comprobó una pérdida funcional que obligue a restaurar íntegramente un bloque eliminado. |
| E — Información trasladada | 14 | 13 skills reescritas enlazan recursos locales; además, los recursos de `design-md` ya estaban duplicados byte a byte dentro de `designUxUi` antes de borrar la carpeta. |

Estas cifras no incluyen como “incorrecta” una incompatibilidad transversal: en
`a039b86` cambiaron los 19 nombres invocables de camelCase a kebab-case sin alias ni
período de deprecación. El contenido sigue existiendo, pero el contrato de invocación
externo puede romperse. Este punto afecta a los 19 paquetes y es el hallazgo de mayor
prioridad.

### Principales conclusiones

- La estrategia correcta fue conservar en `SKILL.md` responsabilidad, entradas,
  decisiones, límites, validación y contrato de salida, y mover detalle condicional a
  `references/`, `templates/` o `scripts/`.
- Los 43 enlaces locales presentes en los 19 entrypoints resuelven correctamente. No
  se detectaron referencias Markdown rotas.
- Los validadores nuevos son reales: pasaron 16 pruebas de BPMN y 11 de requisitos.
  Los JSON y XML versionados también se parsean correctamente.
- La reducción fue especialmente valiosa donde retiró código C#/Java/T-SQL genérico,
  ejemplos de dominio tratados como plantillas y reglas universales falsas.
- El ahorro fue excesivo cuando eliminó un índice necesario para descubrir recursos,
  una taxonomía requerida para decidir o una estructura mínima de salida que no quedó
  externalizada.
- Para modelos intermedios o menores, el principal riesgo no es la brevedad por sí
  sola: es exigir que infieran alias, encuentren archivos no ruteados, recuerden una
  taxonomía o resuelvan el ejecutable correcto sin una regla explícita.

## 2. Hallazgos críticos

### P1 — Los 19 nombres invocables cambiaron sin compatibilidad hacia atrás

**Evidencia:** commit `a039b86`, línea `name:` de los 19 `SKILL.md`. El cambio fue:

| Antes | Después |
|---|---|
| `apiDesign` | `api-design` |
| `backendTesting` | `backend-testing` |
| `bpmnExtractor` | `bpmn-extractor` |
| `crudValidator` | `crud-validator` |
| `designUxUi` | `design-ux-ui` |
| `domainDesign` | `domain-design` |
| `domainModelGen` | `domain-model-gen` |
| `epcFlowGen` | `epc-flow-gen` |
| `gofAdviser` | `gof-adviser` |
| `graspSequenceRealizer` | `grasp-sequence-realizer` |
| `mermaidDiagramGen` | `mermaid-diagram-gen` |
| `microserviceDecomposer` | `microservice-decomposer` |
| `ormMaster` | `orm-master` |
| `qualityScenarioSpecifier` | `quality-scenario-specifier` |
| `relationalObjectMap` | `relational-object-map` |
| `requirementsExtractor` | `requirements-extractor` |
| `systemClassifier` | `system-classifier` |
| `umlConsistency` | `uml-consistency` |
| `useCaseExtractor` | `use-case-extractor` |

`README.md` explica que el frontmatter prevalece y que las carpetas camelCase se
mantienen por compatibilidad de ruta. Eso no preserva prompts, configuraciones, handoffs
o catálogos externos que invoquen el nombre anterior. Un modelo de frontera puede
inferir la equivalencia; un runtime que despacha por coincidencia exacta o un modelo
menor no tiene por qué hacerlo.

**Impacto:** ruptura silenciosa o no activación de la skill, especialmente en Claude,
Gemini, Cursor, Windsurf u orquestadores propios que no compartan una resolución de
alias. También afecta handoffs entre agentes si un artefacto histórico conserva el
nombre camelCase.

**Recomendación:** definir un contrato de migración explícito. Según lo que soporte
cada runtime, usar alias declarativos, stubs de redirección mínimos o una tabla
canónica `nombre anterior → nombre actual` leída por el instalador/orquestador. Marcar
los nombres antiguos como deprecados antes de retirarlos. No duplicar el contenido de
las skills.

### P1 — La absorción de `design-md` preservó archivos, pero eliminó su identidad

**Evidencia:** en `449f64e` se borraron `design-md/SKILL.md` y once recursos. En el
padre del commit, los once recursos ya existían en `designUxUi` con los mismos hashes
Git; por tanto, la teoría, plantillas y scripts no se perdieron. El commit sólo amplió
la descripción de `designUxUi`, pero no dejó alias o redirección para `design-md`.

**Evaluación:** transferencia E correcta en lo físico y C riesgosa en el contrato de
invocación. La consolidación evita duplicados, pero cualquier consumidor que solicite
`design-md` deja de encontrar una skill con ese nombre.

**Recomendación:** incluir `design-md` en la misma estrategia de compatibilidad del
hallazgo anterior. No restaurar el paquete completo ni sus copias de recursos.

### P1 — Dos entrypoints documentan un ejecutable que no puede resolverse

**Evidencia reproducible:**

- `bpmnExtractor/SKILL.md`, sección **Modo BPMN-IR**, usa
  `python .\bpmnExtractor\scripts\...`.
- `requirementsExtractor/SKILL.md`, sección **Salida predeterminada**, usa
  `python .\requirementsExtractor\scripts\...`.
- En el entorno auditado, tanto `python` como `py -3` fallaron por comando no
  encontrado. Las pruebas sí pasaron al usar el intérprete Python provisto por el
  entorno de trabajo.
- `designUxUi/references/preview-and-runtime.md` ya contiene el patrón más portable:
  resolver `python3`, `python`, `py -3` o el runtime provisto.

**Impacto:** un agente puede omitir la validación, quedar bloqueado o afirmar que el
validador está roto cuando sólo falta resolución del runtime. Las barras invertidas y
el bloque `powershell` agregan una dependencia innecesaria de Windows, aunque los
scripts Python son portables.

**Recomendación:** llevar la regla de resolución de intérprete a un bloque común y
mostrar rutas con `/` o variantes Windows/POSIX. La condición debe ser explícita:
resolver intérprete → ejecutar el validador → reportar comando y resultado → si no hay
runtime, declarar “no ejecutado” sin simular éxito.

### P1 — Se eliminó la taxonomía necesaria para clasificar escenarios de calidad

**Evidencia:** antes de `a039b86`, `qualityScenarioSpecifier/SKILL.md` incluía el
modelo de calidad ISO/IEC 25010 y sus características/subcaracterísticas. La versión
actual sólo indica usar el perfil ISO/IEC 25010:2011 que figure en el material
(`qualityScenarioSpecifier/SKILL.md`, sección **Modelo de calidad**). Ni
`references/scenario-profiles.md` ni `references/tactics-and-validation.md` contienen
el catálogo de clasificación.

**Impacto:** si la entrada trae un RNF sin clasificación y el material del curso no
está disponible en el contexto, la acción “seleccionar atributo/subcaracterística”
depende del conocimiento previo del modelo. Un modelo de frontera probablemente la
complete; uno menor puede confundir calidad de producto/calidad en uso, elegir una
subcaracterística incorrecta o inventar una edición de la norma.

**Recomendación:** crear una referencia compacta y versionada con el perfil de cátedra
y su árbol mínimo de categorías, más una regla de selección y casos ambiguos. El
`SKILL.md` debe indicar exactamente cuándo leerla. No restaurar el catálogo exhaustivo,
los cinco casos completos ni las listas largas de tácticas.

## 3. Hallazgos transversales

### 3.1. Lo que la refactorización mejoró

En las 19 skills aparecen con mucha más regularidad los componentes operativos que
importan: modo, entrada, autoridad, límites de no invención, procedimiento, salida y
criterio de cierre. Esto reduce decisiones implícitas aun cuando los archivos son más
cortos.

También se corrigieron prescripciones riesgosas de las versiones anteriores:

- CRUD dejó de exigir C/R/U/D uniforme y de generar CU “remediadores” para balancear
  una matriz.
- EPC dejó de interpretarse como Entrada–Proceso–Consulta de interfaz y pasó a ser el
  Ejercicio Práctico Complementario de la cátedra.
- Microservicios dejó de ser el resultado por defecto; ahora compara contra monolito
  modular.
- ORM, API, testing y persistencia dejaron de imponer Java, C#, T-SQL, Redis,
  Testcontainers o porcentajes fijos.
- Las realizaciones separan análisis y diseño, y los patrones GoF/GRASP dejaron de ser
  una cuota que deba aparecer en todo diagrama.
- Los diagramas y modelos dejaron de producir dos sintaxis equivalentes por rutina.

Estas eliminaciones deben permanecer.

### 3.2. Progressive disclosure correcto, con dos excepciones

Trece entrypoints reescritos enlazan 43 recursos locales y todos existen. Los nuevos
archivos de dominio, DCD, GoF, GRASP, microservicios, calidad y persistencia indican
cuándo leerlos. BPMN y requisitos suman además validadores con pruebas.

Las excepciones son:

1. `mermaid-diagram-gen` conserva 30 manuales, pero el índice del entrypoint sólo
   nombra siete. Para las otras 23 familias dice “elegí por nombre en `references/`”.
   Eso es suficiente para un agente capaz de enumerar y discriminar archivos, pero
   demasiado implícito para uno menor y para hosts que sólo exponen recursos enlazados.
2. `designUxUi/references/course-source-map.md` explica que debe leerse para auditoría
   académica o para resolver reglas discutibles, pero ningún entrypoint lo referencia.
   No es necesario para implementar UI ordinaria, por lo que es P3; aun así, su ruta
   de descubrimiento está incompleta.

### 3.3. La reducción de ejemplos fue mayormente correcta

Se eliminaron casos integrales de hospitales, pedidos, Liga de la Justicia, BonVino,
IVR, código C#/Java y scripts T-SQL. Esos ejemplos consumían gran parte del contexto y
podían contaminar el dominio o el stack del usuario. Las plantillas que sí fijan un
contrato de salida se conservaron o se hicieron más pequeñas.

La regla recomendable no es “eliminar ejemplos”, sino conservar uno sólo cuando
enseña una decisión que una regla y una plantilla no vuelven inequívoca. El ejemplo
breve de requisitos con evidencia y `TBD` cumple ese criterio.

### 3.4. Falta una estructura OpenAPI mínima para modelos menores

`api-design` conserva semántica HTTP, idempotencia, compatibilidad, Problem Details,
validación y límites. Sin embargo, el ejemplo/estructura OpenAPI anterior se eliminó y
no quedó una plantilla o referencia local equivalente. Un modelo menor puede producir
un contrato conceptualmente correcto pero estructuralmente incompleto.

Esto es B, no D: restaurar el ejemplo Java o una especificación extensa sería
contraproducente. Conviene una referencia breve con campos mínimos por operación,
esquemas, seguridad declarativa, respuestas y un comando de validación condicionado a
la herramienta disponible.

### 3.5. La documentación promete Gherkin donde la skill ya no lo enruta

`use-case-extractor` retiró contratos de datos y criterios BDD/Gherkin, y ahora limita
su salida al modelo o a la descripción institucional del CU. Esa separación es
razonable. Sin embargo, `README.md` todavía afirma “Gherkin solo cuando se pide”, sin
que el entrypoint defina un modo, salida o handoff para hacerlo.

Un agente puede inventar Gherkin dentro del CU, omitirlo pese al catálogo o derivarlo a
la skill equivocada. Debe elegirse un dueño explícito —probablemente criterios
trazables en requisitos/CU y pruebas ejecutables en `backend-testing`— o eliminar la
promesa del catálogo.

### 3.6. Compatibilidad multiagente

El núcleo de las 19 skills no depende de herramientas exclusivas de Codex. La única
metadata OpenAI inspeccionada, `designUxUi/agents/openai.yaml`, está aislada del
entrypoint y no cambia el procedimiento para otros agentes. Los contratos basados en
Markdown, rutas relativas, tablas y scripts Python son reutilizables.

Los problemas reales de portabilidad son más concretos:

- nombres invocables modificados sin alias;
- comandos de runtime escritos para una forma de Windows;
- expectativa implícita de que el host pueda enumerar archivos no enlazados;
- referencias a otras skills sin describir qué hacer cuando el runtime no soporta
  invocación encadenada.

Para el último punto, `epc-flow-gen` debería permitir dos estrategias equivalentes:
invocar la skill especialista si el host lo soporta, o leer/aplicar su `SKILL.md` y
conservar el handoff si no existe despacho nativo.

## 4. Auditoría por skill

El impacto “modelo menor” se refiere a información que no debería depender de una
inferencia sofisticada. Todas las reescrituras de `a039b86` heredan además el riesgo
transversal de cambio de nombre detallado en P1.

### `api-design`

**Estado:** Revisar — B.

**Antes → después:** guía extensa REST/OpenAPI, dos respuestas Problem Details y un
handler Spring → contrato neutral con modos, semántica HTTP, compatibilidad,
idempotencia, validación y salida.

**Evaluación:** quitar Java/Spring, valores fijos, RMM como meta y ejemplos largos fue
correcto. No se perdió una restricción central. Sí quedó demasiado implícita la
estructura mínima de OpenAPI.

**Impacto:** frontera: bajo; modelo menor: medio por posible contrato incompleto;
multiagente: bajo.

**Recomendación:** mantener el entrypoint y añadir una referencia OpenAPI compacta;
no restaurar código de framework.

### `backend-testing`

**Estado:** Correcta — A.

**Antes → después:** tratado de pirámide, FIRST, dobles y ejemplos C#/Java/Python →
selección por riesgo, oráculo, nivel, dependencias, entorno y verificación real.

**Evaluación:** se preservaron AAA/Given–When–Then y la taxonomía de dobles en forma
operativa. El stack se toma del proyecto. Los ejemplos eliminados no eran necesarios
y podían inducir dependencias ajenas.

**Impacto:** frontera y modelo menor: bajo; multiagente: bajo.

**Recomendación:** mantener. No restaurar porcentajes, presupuestos de tiempo ni suites
multilenguaje.

### `bpmn-extractor`

**Estado:** Correcta — A, con corrección transversal del comando.

**Antes → después:** manual BPMN, ficha, IR, “change engine” y caso integral en un solo
archivo → tres modos, límites explícitos, ficha/IR/templates, taxonomía condicional y
transformador verificable.

**Evaluación:** la teoría necesaria fue trasladada a
`references/bpmn_taxonomy_and_editing.md`; el ejemplo, schema, ficha y XML siguen
accesibles. La versión nueva aclara que Mermaid no es BPMN interoperable y que el XML
no es ejecutable, corrigiendo promesas anteriores.

**Validación:** 16/16 pruebas pasan; ejemplo JSON y XML se parsean.

**Impacto:** modelo menor: bajo por contenido, medio por resolución de `python`;
multiagente: medio sólo por el comando.

**Recomendación:** mantener la arquitectura; hacer portable la ejecución.

### `crud-validator`

**Estado:** Correcta — A.

**Antes → después:** matriz obligatoriamente “balanceada”, taxonomía dramática,
remediación automática y CU generado → diagnóstico con evidencia, `N/A`, `EXT`, `?`
y límites explícitos.

**Evaluación:** la eliminación evita falsos positivos y requisitos inventados. La
plantilla y la referencia de calidad de enunciados preservan la salida verificable.

**Impacto:** menor riesgo para todos los modelos que antes; alta mejora de
determinismo.

**Recomendación:** mantener eliminado el motor de remediación automática y los scores
sin rúbrica.

### `design-ux-ui`

**Estado:** Correcta — A, con deuda P3 de descubrimiento.

**Antes → después:** hub que tendía a producir tokens, widget, localhost y DESIGN.md →
selección proporcional entre especificación, dirección visual, prototipo,
implementación y auditoría.

**Evaluación:** los recursos absorbidos de `design-md` siguen presentes y ocho
referencias tienen condiciones de lectura claras. Se eliminaron vetos estéticos
universales y defaults de framework. `course-source-map.md` quedó sin enlace.

**Impacto:** frontera: bajo; modelo menor: bajo en tareas ordinarias y medio sólo en
re-auditoría académica; multiagente: bajo. `agents/openai.yaml` es metadata opcional,
no una dependencia del núcleo.

**Recomendación:** mantener. Añadir una ruta condicional al source map y resolver el
alias `design-md`; no duplicar la antigua skill.

### `domain-design`

**Estado:** Correcta — A.

**Antes → después:** DDD, Clean Architecture, DCD, C# y caso completo mezclados →
modos separados `course-dcd`, `rich-domain` e `implementation`, con dos referencias.

**Evaluación:** la división hace explícito cuándo aplicar DDD y conserva trazabilidad,
responsabilidades, firmas y cierre. Los ejemplos de implementación eran prescriptivos.

**Impacto:** bajo para frontera, modelos menores y agentes distintos.

**Recomendación:** mantener la externalización y no restaurar arquitectura por defecto.

### `domain-model-gen`

**Estado:** Correcta — A.

**Antes → después:** catálogo largo de patrones, doble renderer y caso integral →
procedimiento conceptual, plantilla de salida y catálogo ASI compacto de 24 patrones.

**Evaluación:** se preservan condiciones, multiplicidades, evidencia, `TBD` y la
separación análisis/diseño. El nuevo catálogo es más amplio y menos dependiente de un
ejemplo particular.

**Impacto:** bajo. El enlace al catálogo indica cuándo leerlo.

**Recomendación:** mantener; no volver a duplicar Mermaid y PlantUML por rutina.

### `epc-flow-gen`

**Estado:** Correcta — A; reemplazo conceptual justificado.

**Antes → después:** EPC interpretado como Entrada–Proceso–Consulta y generador de UI
→ orquestador de Ejercicios Prácticos Complementarios ASI/DSI.

**Evaluación:** gran parte del texto eliminado no era contexto perdido sino una
responsabilidad equivocada. La versión actual explicita fuentes, matriz de cobertura,
ruteo por producto, no invención y cierre.

**Impacto:** mejora sustancial en todos los modelos. Riesgo menor si el host no soporta
invocar skills por nombre.

**Recomendación:** mantener. Añadir un fallback de handoff manual para hosts sin
orquestación nativa.

### `gof-adviser`

**Estado:** Correcta — A.

**Antes → después:** guía completa GoF/SOLID con cuatro implementaciones C# → método de
decisión y catálogo compacto en `pattern-selection.md`.

**Evaluación:** se preservan intención, participantes, alternativas y consecuencias.
La salida “ningún patrón” reduce sobrediseño. El código eliminado no era portable.

**Impacto:** bajo; la referencia ofrece señales y desambiguaciones suficientes para
modelos menores.

**Recomendación:** mantener.

### `grasp-sequence-realizer`

**Estado:** Correcta — A.

**Antes → después:** nueve GRASP, catálogo GoF, doble sintaxis y varios casos completos
→ flujo común y referencias separadas para realización de análisis y diseño.

**Evaluación:** conserva los cinco GRASP curriculares predeterminados, visibilidad,
trazabilidad y reglas de notación. Evita mezclar BCE con diseño físico.

**Impacto:** bajo. La separación por modo reduce decisiones implícitas.

**Recomendación:** mantener; cargar patrones adicionales sólo ante una fuerza concreta.

### `mermaid-diagram-gen`

**Estado:** Riesgosa — C en descubrimiento, correcta en semántica.

**Antes → después:** catálogo enlazado de 30 familias y reglas extensas → siete rutas
explícitas, una instrucción genérica para las otras 23, validación por capas y modo de
estados.

**Evaluación:** los 30 manuales trasladados por `0739617` conservan hash/historia y la
separación representación/contenido es una mejora. Lo riesgoso es eliminar el índice
completo sin reemplazarlo por otro descubrible.

**Impacto:** frontera: bajo; modelo menor y hosts que no enumeran directorios: medio;
multiagente: medio.

**Recomendación:** restaurar sólo una tabla compacta de las 30 familias o un
`references/index.md` enlazado desde el entrypoint.

### `microservice-decomposer`

**Estado:** Correcta — A.

**Antes → después:** DDD, Saga, Outbox, resiliencia, C4 y caso de superhéroes en el
entrypoint → decisión monolito/microservicios y dos referencias condicionales.

**Evaluación:** las reglas importantes se preservan; las tecnologías dejaron de ser
obligatorias. La referencia distribuida cubre fallos, idempotencia y validación.

**Impacto:** bajo y con menor riesgo de sobrearquitectura.

**Recomendación:** mantener.

### `orm-master`

**Estado:** Correcta — A.

**Antes → después:** ciclo ORM general, receta N+1 y ejemplo JPA/Spring → diagnóstico
por ORM/base/caso de uso con evidencia SQL y verificación antes/después.

**Evaluación:** eliminar recetas universales fue correcto. Persisten carga,
transacciones, concurrencia, cascadas, índices y condiciones de implementación.

**Impacto:** bajo; mejor portabilidad entre stacks y agentes.

**Recomendación:** mantener.

### `quality-scenario-specifier`

**Estado:** Riesgosa — C.

**Antes → después:** catálogo ISO exhaustivo, escenario de seis partes, tácticas y
cinco casos → perfil de tres campos por defecto, seis partes/tácticas condicionales y
dos referencias.

**Evaluación:** elegir el perfil por consigna y no inventar umbrales son mejoras. La
eliminación del árbol de clasificación sin una referencia equivalente dejó una
decisión crítica a la memoria del modelo.

**Impacto:** frontera: bajo/medio; modelo menor: alto en clasificación; multiagente:
medio por diferencias de conocimiento previo.

**Recomendación:** restaurar parcialmente como referencia compacta y versionada.

### `relational-object-map`

**Estado:** Correcta — A.

**Antes → después:** teoría O/R, DDL T-SQL, `BDHelper` y DAO C# → modos de mapeo,
schema, DDL y handoff con dos referencias.

**Evaluación:** se preservan identidad, tipos, asociaciones, herencia, integridad,
índices, seguridad y validación. El helper global eliminado era un riesgo técnico y de
portabilidad.

**Impacto:** bajo y con mejora fuerte multi-stack.

**Recomendación:** mantener; no restaurar código ni dialecto por defecto.

### `requirements-extractor`

**Estado:** Correcta — A, con corrección transversal del comando.

**Antes → después:** pipeline compacto con taxonomías y un ejemplo largo → modos
explícitos, evidencia, registro/ERS/historias/JSON, referencias acotadas y validador
semántico.

**Evaluación:** la reducción fue moderada y agregó más determinismo. El ejemplo se
redujo a un caso que enseña evidencia y `TBD`, sin contaminar el dominio.

**Validación:** 11/11 pruebas del validador pasan; el schema JSON se parsea.

**Impacto:** bajo por contenido; medio por el comando `python` no resoluble.

**Recomendación:** mantener y documentar resolución portable del runtime.

### `system-classifier`

**Estado:** Correcta — A.

**Antes → después:** diagnóstico TGS, clasificación, cinco dimensiones, PUD y caso
completo en cadena → cuatro modos independientes, evidencia, referencia y plantilla.

**Evaluación:** conserva los tres ejes de prefactibilidad de cátedra y evita inventar
legal/temporal, cronogramas, porcentajes o cálculos. La taxonomía SI y PUD siguen
disponibles bajo demanda.

**Impacto:** bajo y con mejor control para modelos menores.

**Recomendación:** mantener.

### `uml-consistency`

**Estado:** Correcta — A.

**Antes → después:** cinco reglas rígidas, JSON/reportes, auto-parches y tres casos →
baseline, matriz de cobertura, seis reglas condicionadas por precisión, certeza y
contrato de salida.

**Evaluación:** la versión actual maneja formatos no verificables, cobertura parcial,
señales/replies, aliases de tipos y fuente autoritativa. Esto reduce falsos positivos
y mutaciones indebidas.

**Impacto:** bajo; mejora notable para agentes con distintas capacidades de parsing.

**Recomendación:** mantener.

### `use-case-extractor`

**Estado:** Revisar — B.

**Antes → después:** modelo, descripción, realización BCE, contratos de datos y BDD en
un único entrypoint → sólo Modelo o Descripción; realizaciones delegadas a
`grasp-sequence-realizer`.

**Evaluación:** retirar la realización y la doble responsabilidad fue correcto. La
plantilla actual conserva actores, relaciones, flujos, alternativas, evidencia y
postcondiciones. El problema es que el catálogo raíz aún promete Gherkin sin definir
su propietario o handoff.

**Impacto:** frontera: bajo; modelo menor/multiagente: medio por documentación
contradictoria.

**Recomendación:** decidir y documentar el dueño de criterios BDD; no restaurar la
antigua realización dentro de esta skill.

### Identidad histórica `design-md`

**Estado:** Riesgosa — C/E.

**Antes → después:** skill autónoma de DESIGN.md → capacidades absorbidas por
`design-ux-ui`, con recursos ya duplicados antes del borrado.

**Evaluación:** no hubo pérdida física. Sí se eliminó un trigger público sin alias.

**Impacto:** frontera: bajo si conoce la historia; runtime exacto/modelo menor: alto.

**Recomendación:** compatibilidad de nombre, no restauración del contenido duplicado.

## 5. Información que debería restaurarse o reformularse

Ordenada por prioridad:

1. **P1 — Alias/migración de nombres:** tabla o mecanismo ejecutable para los 19
   nombres camelCase y `design-md`, con deprecación explícita.
2. **P1 — Taxonomía de calidad:** referencia compacta, versionada y ruteada desde
   `quality-scenario-specifier`.
3. **P1 — Resolución de Python:** condición portable y fallback verificable en BPMN y
   requisitos.
4. **P2 — Índice Mermaid:** las 30 familias, una línea por familia, en el entrypoint o
   en un índice enlazado.
5. **P2 — Contrato OpenAPI mínimo:** estructura/checklist condicional; no un caso de
   implementación completo.
6. **P2 — Propiedad de Gherkin:** alinear `README.md`, `use-case-extractor`,
   `requirements-extractor` y `backend-testing`.
7. **P3 — Source map UX/UI:** enlace condicional para auditoría académica.
8. **P3 — Fallback de orquestación:** indicar cómo aplicar una skill especialista
   cuando el host no soporta invocación encadenada.

## 6. Información que puede permanecer eliminada

- tratados teóricos completos en los entrypoints;
- repetición de definiciones disponibles en referencias condicionales;
- casos integrales con dominios ficticios usados como patrón universal;
- código Java, C#, T-SQL o configuración de frameworks cuando el stack no está dado;
- doble salida Mermaid/PlantUML y Markdown/JSON por rutina;
- porcentajes de pirámide, tiempos máximos, métricas o umbrales universales;
- CRUD completo obligatorio, scores sin rúbrica y generación automática de requisitos;
- microservicios, Saga, Outbox, DDD, Clean/Hexagonal o GoF como defaults;
- “change engines”, importación BPMN visual o conformidad UML/WCAG no demostrada;
- catálogos extensos de anti-patrones cuando una regla de decisión y una comprobación
  cubren el mismo riesgo;
- plantillas y scripts duplicados de la antigua `design-md`.

## 7. Compatibilidad multiagente y por capacidad

| Entorno | Evaluación | Riesgos principales |
|---|---|---|
| Codex / modelos de frontera | Alta después de corregir P1. Los entrypoints son claros y la carga progresiva funciona. | Puede enmascarar huecos infiriendo aliases, taxonomías y paths. |
| Claude | Alta a media según el mecanismo de instalación/despacho. | Nombre exacto, directorio distinto del `name`, comandos Windows y chaining de skills. |
| Gemini / Antigravity | Alta a media. El repositorio declara ese destino y conserva estructura `SKILL.md`. | Alias `design-md`, nombres migrados, recursos no enlazados y disponibilidad de Python. |
| Cursor / Windsurf / agentes propios | Media, porque suelen depender más de reglas de workspace o resolución manual. | No hay contrato universal de alias ni fallback explícito para “invocar otra skill”. |
| Modelos intermedios | Media/alta en las 15 skills A; media en las demás. | Índice Mermaid, OpenAPI mínimo, documentación Gherkin y runtime. |
| Modelos de menor capacidad | Media. Los modos y contratos ayudan, pero los cuatro P1 deben hacerse mecánicos. | Inferir equivalencias de nombres, recordar ISO 25010, enumerar recursos y adaptar comandos. |

La compatibilidad no debe medirse sólo por si el modelo “entiende” el texto. Debe
medirse por si puede descubrir la instrucción, elegir una ruta con datos observables,
ejecutarla en su host, validar y entregar el mismo contrato sin conocimiento tácito.

## 8. Principios recomendados para futuras optimizaciones

1. **Preservar el mínimo operacional:** objetivo, condición de activación/no
   activación, entradas, orden, decisiones, prohibiciones, fallbacks, validación,
   salida y término.
2. **Externalizar con ruta:** todo recurso crítico movido fuera del entrypoint debe
   responder `cuándo leer`, `para qué` y `qué decisión habilita`.
3. **No cambiar identidad silenciosamente:** un `name` es una API. Requiere alias,
   migración, deprecación y prueba de resolución.
4. **Usar ejemplos sólo para desambiguar:** si una regla y una plantilla bastan, el
   ejemplo sobra; si un modelo menor puede interpretar dos conductas distintas, un
   ejemplo mínimo aporta valor.
5. **Separar conocimiento de plataforma:** el objetivo y la validación son estables;
   el comando debe tener detección de runtime y variantes por host.
6. **No delegar taxonomías decisorias a la memoria:** si una clasificación cambia la
   salida, conservar un catálogo compacto y versionado.
7. **Validar transferencias automáticamente:** enlaces locales, frontmatter, nombres
   únicos, schemas, ejemplos, tests y recursos no ruteados.
8. **Probar con un agente menos capaz:** verificar que puede seguir la ruta sin
   inventar datos, listar mentalmente un estándar ni asumir capacidades del host.
9. **Distinguir brevedad de densidad:** una instrucción corta es buena sólo si conserva
   la condición y el criterio de decisión.
10. **Conservar la fuente autoritativa:** una skill downstream no debe recrear lo que
    otra produce; el handoff debe preservar IDs, estado, supuestos y pendientes.

## 9. Plan de corrección

### P0 — Puede producir comportamiento incorrecto inmediato

No se detectaron correcciones P0.

### P1 — Puede afectar significativamente compatibilidad o modelos menos capaces

1. Diseñar y documentar alias para 19 nombres migrados y `design-md`; agregar una
   prueba que resuelva ambos nombres hacia una sola implementación.
2. Agregar la taxonomía compacta de calidad y enlazarla condicionalmente.
3. Unificar resolución portable de Python y rutas para BPMN/requisitos; probar en
   Windows y POSIX o declarar plataformas soportadas.

### P2 — Mejora importante de robustez

1. Restaurar como índice compacto las 30 rutas Mermaid.
2. Añadir una referencia OpenAPI mínima y un criterio de validación por versión.
3. Alinear la promesa de Gherkin y su handoff entre catálogo y skills.
4. Definir fallback manual para orquestadores sin chaining nativo.

### P3 — Mejora opcional

1. Enlazar `designUxUi/references/course-source-map.md` sólo para auditoría académica.
2. Automatizar el inventario de recursos no ruteados y la validación de links.
3. Agregar una prueba de consistencia entre `README.md`, `GUIA.md`, carpetas y nombres
   de frontmatter.

## 10. Evidencia y verificaciones ejecutadas

| Verificación | Resultado |
|---|---|
| Historia y secuencia de refactorización | Revisados `449f64e`, `0739617`, `a039b86` y merge `35239db`. |
| Diff principal | 75 archivos; 5.780 inserciones y 13.593 eliminaciones. |
| Entry points reescritos | 19; 76.729 → 16.733 palabras. |
| Skills actuales | 22 `SKILL.md`; frontmatter presente y 22 nombres únicos. |
| Links locales desde los 19 entrypoints | 43 válidos, 0 rotos. |
| Recursos Mermaid | 30 presentes; 7 explícitamente ruteados en el entrypoint y 23 por descubrimiento implícito. |
| Transferencia `design-md` | 11 recursos ya duplicados con hashes idénticos en `designUxUi` antes del borrado. |
| BPMN | 16/16 pruebas pasan; JSON/XML versionados parsean. |
| Requisitos | 11/11 pruebas pasan; schema JSON parsea. |
| Comando documentado `python` | Falla en el host por ejecutable no encontrado. |
| Launcher alternativo `py -3` | También falla; el runtime provisto por el entorno ejecuta correctamente las 27 pruebas. |

## 11. Dictamen final

La refactorización debe conservarse como base. Restaurar todo lo borrado volvería a
introducir ruido, sesgo de stack, ejemplos contaminantes y decisiones automáticas que
la nueva versión corrigió. El trabajo pendiente es quirúrgico: preservar contratos de
invocación, hacer ejecutables los pasos de validación en distintos hosts y devolver
conocimiento decisorio sólo donde quedó implícito.

Después de aplicar los P1 y P2, el repositorio puede mantener casi toda la reducción de
tokens obtenida y, a la vez, mejorar determinismo, portabilidad y desempeño con modelos
intermedios o menores.
