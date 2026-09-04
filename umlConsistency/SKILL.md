---
name: uml-consistency
description: >-
  Audita trazabilidad y consistencia entre realizaciones o diagramas de secuencia, diagramas de
  clases, máquinas de estados y código. Detecta contradicciones de firmas, receptores, creación,
  navegabilidad y ciclo de vida con evidencia y nivel de confianza. Usar cuando existen dos o más
  artefactos para comparar; no usar para inventar artefactos faltantes ni para corregirlos sin permiso.
---

# Auditoría de consistencia entre modelos

Compará únicamente lo que los artefactos realmente expresan. Una omisión en un modelo parcial no es automáticamente una contradicción y un archivo ilegible no es evidencia de ausencia.

## Alcance y límites

Esta skill puede contrastar:

- realización de caso de uso o DSD ↔ DCD;
- DSD/DCD ↔ DTE, cuando el objeto tiene un ciclo de vida modelado;
- modelos de diseño ↔ código, cuando se proporciona la implementación;
- artefactos ↔ IDs de requisitos, casos de uso o reglas, si están presentes.

No presupongas que todo proyecto usa BCE, arquitectura por capas, patrón State, DDD o una única notación. En Análisis, Boundary/Control/Entity son estereotipos posibles de una realización; en Diseño, DSD y DCD contienen decisiones físicas y firmas más precisas.

La auditoría es `report-only` por defecto. Proponé correcciones, pero no edites modelos o código hasta que el usuario identifique la fuente autoritativa y autorice el cambio.

## Comprobar los formatos antes del contenido

Registrá para cada entrada: ruta/nombre, formato, versión si se conoce, alcance declarado y método de lectura.

- Markdown, texto, Mermaid, PlantUML, XMI y código legible: auditables hasta el detalle efectivamente representado.
- StarUML `.mdj`: solo afirmar parsing estructural si se pudo leer su JSON y resolver sus referencias.
- `.qea`/`.eap` y otros formatos binarios: requieren exportación XMI o una herramienta disponible. Sin ella, clasificá el contenido como `no verificable`.
- Imagen/PDF: permite revisión visual parcial; no garantiza firmas, estereotipos o relaciones ocultas.

Nunca prometas parseo o parches automáticos para formatos que no se abrieron con éxito.

## Establecer el baseline

Antes de diagnosticar, determiná:

1. etapa: análisis, diseño o implementación;
2. artefactos y casos de uso incluidos; un subconjunto implica cobertura parcial;
3. convención de firmas y tipos por lenguaje/notación;
4. arquitectura o reglas de curso explícitamente adoptadas;
5. fuente autoritativa en caso de conflicto.

Si no se definió una fuente autoritativa, reportá la discrepancia y ofrecé alternativas; no decidas qué lado reescribir.

## Matriz de cobertura

Construí una matriz antes de aplicar reglas:

| Relación | Artefacto origen | Artefacto destino | Cobertura | Precisión disponible |
|---|---|---|---|---|
| mensajes ↔ operaciones | DSD/CU | DCD | completa/parcial/desconocida | nombre/aridad/tipos/retorno |
| transiciones ↔ operaciones | DTE | DSD/DCD/código | completa/parcial/desconocida | evento/guarda/efecto |
| clases ↔ implementación | DCD | código | completa/parcial/desconocida | tipo/miembro/visibilidad |

No ejecutes una regla si falta el detalle que necesita. Marcala `no verificable`.

## Reglas de consistencia

### C1. Mensaje y elemento receptor

Clasificá primero el `messageSort` o la notación equivalente; no todo mensaje representa una llamada a operación:

- llamada síncrona o asíncrona: resolvé la clase receptora y buscá la operación propia o heredada;
- señal: contrastá `Signal`/`Reception` cuando el artefacto los represente;
- `create`/`delete`: contrastá el ciclo de vida y aplicá además C3;
- `reply`: contrastá su llamada antecedente y el retorno declarado, no una segunda operación receptora;
- mensaje encontrado/perdido o sort no legible: tratá la cobertura como parcial o `no verificable`.

Para las llamadas, compará nombre y aridad solo si ambos artefactos muestran listas completas. Compará tipos, orden, retorno y visibilidad únicamente si ambos lados los declaran. Normalizá convenciones del lenguaje (`Nullable<T>`/`T?`, colecciones, aliases) antes de marcar conflicto.

Una flecha de retorno omitida o tipos abreviados en un DSD pueden ser abstracción, no error. Diferenciá `contradicción` de `detalle insuficiente`.

### C2. Referencia al receptor

Un emisor puede conocer al receptor por asociación navegable, parámetro, inyección, creación local o retorno previo. Una asociación sin dirección explícita no prueba ni niega navegabilidad.

Solo marcá salto de capa o `Boundary → Entity` como violación si el baseline adoptó esa restricción. En otro contexto, reportalo como observación arquitectónica, no como error universal.

### C3. Creación y responsabilidad

Contrastá el mensaje `create`/constructor con el DCD y, si existe, el código. GRASP Creador es una guía: contención, registro, uso estrecho o datos de inicialización son indicios, no una condición bicondicional. Fábricas, inyección y composición root pueden justificar otra asignación.

### C4. Ciclo de vida

Aplicá esta regla solo si existe una DTE relevante o la consigna la exige:

- el evento/transición invocado existe desde el estado de origen;
- la guarda y el efecto no contradicen el DSD o las reglas;
- el estado inicial y los finales coinciden donde estén expresados;
- las transiciones terminales no reciben operaciones incompatibles.

No exijas patrón State: una enumeración, tabla de transición u otra implementación puede realizar correctamente la máquina.

### C5. Correspondencia con código

Compará únicamente el alcance del código suministrado. Tené en cuenta sobrecargas, genéricos, métodos de extensión, interfaces, herencia, asincronía y visibilidad efectiva. Una operación técnica puede existir en código sin aparecer en un DSD; solo es drift si el baseline exige esa cobertura.

### C6. Elementos sin trazabilidad

Marcá una clase, operación o atributo como posible huérfano solo cuando:

- el conjunto de CU/DSD declarado es completo para el alcance;
- el elemento no es infraestructura, framework, accessor u operación transversal justificada;
- tampoco aparece en reglas, DTE, interfaces o código relevante.

Con cobertura parcial, emití `no cubierto por los artefactos revisados`, no `huérfano`.

## Clasificación de resultados

Usá tres estados de certeza:

- `confirmado`: existe evidencia directa en ambos artefactos y se contradice;
- `posible`: hay un indicio, pero una convención o pieza ausente podría resolverlo;
- `no verificable`: el formato, la cobertura o el detalle no permite evaluar.

La severidad depende del baseline:

- `error`: impide satisfacer una regla obligatoria o compilar el diseño objetivo;
- `advertencia`: riesgo de incoherencia o decisión no documentada;
- `información`: cobertura, deuda documental o mejora no bloqueante.

No emitas porcentajes de calidad ni veredictos `APPROVED/REJECTED` sin una rúbrica provista.

## Procedimiento determinista

1. Inventariá entradas, legibilidad y cobertura.
2. Extraé símbolos con localizadores: clase, lifeline, operación, mensaje, estado, transición e ID trazable.
3. Normalizá nombres y tipos sin perder el literal original.
4. Ejecutá C1–C6 solo donde haya datos suficientes.
5. Deduplicá hallazgos por `(regla, origen, destino, símbolo)`.
6. Buscá evidencia que podría refutar cada hallazgo antes de confirmarlo.
7. Priorizá por impacto y confianza.
8. Proponé la corrección mínima sobre la fuente que el usuario declare autoritativa.
9. Si se autoriza una edición, reejecutá la misma matriz y mostrá el delta.

## Contrato de salida

```markdown
# Auditoría de consistencia

## Alcance y cobertura
| Artefacto | Formato/lectura | Alcance | Limitaciones |

## Resumen
| ID | Regla | Estado | Severidad | Origen ↔ destino | Símbolo |

## Hallazgos
### UML-001 — título
- Evidencia origen: `archivo/diagrama/localizador`
- Evidencia destino: `archivo/elemento/localizador`
- Contradicción o incertidumbre:
- Impacto:
- Confianza: alta/media/baja
- Corrección mínima propuesta:
- Fuente autoritativa: definida/TBD

## No verificable y preguntas abiertas
## Delta de revalidación (solo si hubo cambios)
```

JSON es opcional y solo debe producirse si el usuario necesita automatización. Incluí los mismos campos; no dupliques siempre la salida Markdown.

## Revisión final

- ¿Cada hallazgo tiene dos localizadores o explica qué evidencia falta?
- ¿Se respetó la distinción análisis/diseño/implementación?
- ¿La regla aplicada pertenece al baseline y no a una arquitectura inventada?
- ¿Se evitó exigir tipos, retornos, navegabilidad o cobertura que el diagrama no expresa?
- ¿Los posibles falsos positivos quedaron como `posible` o `no verificable`?
- ¿La propuesta preserva requisitos y decisiones trazables?
- ¿No se mutó ningún archivo sin fuente autoritativa y autorización?
