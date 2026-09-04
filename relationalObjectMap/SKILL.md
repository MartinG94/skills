---
name: relational-object-map
description: >-
  Traduce un DCD o modelo de objetos a decisiones de mapeo relacional trazables. Genera
  esquema o DDL sólo si se solicita y existe un motor objetivo; no implementa acceso a
  datos ni presupone políticas de borrado, índices o herencia.
---

# Mapeo objeto–relacional

El producto predeterminado es un modelo relacional lógico y un registro de decisiones,
no un script ejecutable ni una capa de persistencia completa.

## Elegir el modo

- `mapping` — predeterminado: clases, identidad, atributos, asociaciones, herencia y
  restricciones. Lee [references/mapping-decisions.md](references/mapping-decisions.md).
- `schema` — añade DER/tablas y restricciones lógicas usando la misma referencia.
- `ddl` — sólo por pedido explícito y con motor/versión objetivo. Lee
  [references/ddl-and-implementation.md](references/ddl-and-implementation.md).
- `implementation-handoff` — describe decisiones que consumirá la solución ORM/DAO;
  no genera código salvo que el usuario lo pida expresamente.

Si el usuario dice “mapear” sin pedir código ni SQL, usa `mapping`.

## Entradas

Busca:

- DCD/modelo de objetos y alcance de clases persistentes;
- identidad y claves de negocio conocidas;
- multiplicidades, opcionalidad y propiedad del vínculo;
- invariantes, unicidad y reglas de eliminación/retención;
- consultas y volúmenes relevantes para índices;
- motor, versión y convenciones si se solicita DDL;
- estrategia de persistencia existente si se solicita implementación.

No inventes claves, longitudes, nulabilidad, cascadas, índices, zona horaria, precisión,
soft delete ni tipos específicos del motor. Usa `TBD` y explica el impacto de decidirlos.

## Flujo

1. Delimita qué objetos necesitan persistencia y cuáles se derivan o son de transporte.
2. Registra identidad, valor y ciclo de vida de cada clase.
3. Mapea atributos simples y descompón tipos compuestos sólo con semántica conocida.
4. Resuelve asociaciones según cardinalidad, opcionalidad y ownership de datos.
5. Compara estrategias de herencia; no elijas una por costumbre académica.
6. Traduce invariantes conocidas a claves/restricciones cuando el motor pueda aplicarlas.
7. Revisa normalización y duplicación deliberada.
8. Diseña índices sólo desde claves/restricciones o consultas demostradas.
9. Valida trazabilidad DCD → elemento relacional y registra pérdidas semánticas.

## Límites semánticos

- Agregación/composición UML no determina por sí sola nulabilidad ni acción de borrado.
- Un número de teléfono, documento o código suele ser texto si no participa en aritmética;
  decide por semántica, no por apariencia numérica.
- Una relación muchos-a-muchos puede ser tabla puente o entidad asociativa si tiene
  atributos, identidad o comportamiento propios.
- Herencia no tiene estrategia universal: TPH, TPT y TPC intercambian nulabilidad,
  joins, duplicación, restricciones y facilidad de consulta.
- Soft delete es una política de negocio/retención con efectos sobre unicidad y consultas,
  no una columna obligatoria.
- Una clave foránea no exige siempre un índice adicional; justifícalo por restricciones,
  joins, filtros y patrón de escritura.

## Producto predeterminado

1. `Alcance, hechos y TBD`.
2. `Matriz de mapeo` — elemento OO → elemento relacional → decisión/evidencia.
3. `Modelo relacional` — tablas, claves y relaciones a nivel lógico.
4. `Decisiones abiertas` — alternativas y consecuencias.
5. `Validación` — identidad, cardinalidad, integridad, normalización y trazabilidad.

Si aporta claridad, usa Mermaid ER como renderer predeterminado; utiliza otra notación
sólo si se solicita y no dupliques diagramas. DDL, migraciones y código son anexos
opcionales y nunca sustituyen el registro de decisiones.

## Seguridad y alcance

- No incluyas teardown, recreación destructiva ni limpieza de datos por defecto.
- No incrustes cadenas de conexión, credenciales, certificados ni nombres de servidor.
- No inventes una abstracción global de conexión/transacción.
- No ejecutes el DDL ni modifiques una base de datos sin autorización separada.
- Para un esquema existente, prefiere una migración incremental y revisable.

## Criterios de cierre

- Cada tabla/columna se remonta a un elemento, regla o decisión explícita.
- Claves, opcionalidad y cardinalidad están confirmadas o marcadas `TBD`.
- La estrategia de herencia se comparó con alternativas pertinentes.
- Índices y políticas de eliminación tienen una razón verificable.
- El producto no contiene configuración o tecnología fuera del alcance pedido.
