# Ejemplo breve: extracción con evidencia y TBD

## Fuente

`SRC-01`, minuta de logística, párrafos 3–4:

> “Necesitamos consultar el estado de cada envío. La consulta tiene que ser rápida. Los clientes también deberían poder verla, pero todavía no definimos cómo se identificarán.”

## Registro resultante

```markdown
## Requisitos funcionales
| ID | Nivel / padre | Enunciado | Origen | Derivación / validación | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| RF-01 | global | Consultar el estado de un envío | explícito | confirmar alcance y actores | SRC-01 ¶3 | pendiente de validación |

## Requisitos no funcionales
| ID | Categoría | Enunciado / medida | Alcance | Origen | Derivación / validación | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RNF-01 | Producto / eficiencia | La consulta debe responder en un tiempo aceptable; escala: tiempo de respuesta; condiciones y objetivo: TBD | RF-01 | explícito | acordar condiciones y umbral | SRC-01 ¶3 | TBD |

## Supuestos y preguntas abiertas
| ID | Tipo | Afecta a | Enunciado / pregunta | Base / evidencia | Acción y estado |
| --- | --- | --- | --- | --- | --- |
| OPEN-01 | pregunta | RNF-01 | ¿Bajo qué carga y con qué tiempo máximo se aceptará la consulta? | SRC-01 ¶3 | acordar criterio medible; abierto |
| OPEN-02 | pregunta | RF-01 | ¿Los clientes están dentro del alcance y cómo se determina qué envíos pueden consultar? | SRC-01 ¶4 | confirmar actor, alcance y regla de acceso; abierto |

## Control de cobertura

- Fuente revisada: `SRC-01`, párrafos 3–4.
- Elementos derivados: ninguno.
- `TBD` bloqueante: condiciones y objetivo de `RNF-01`.
```

El ejemplo no elige autenticación, canal, tecnología ni umbral porque la fuente no los determina.
