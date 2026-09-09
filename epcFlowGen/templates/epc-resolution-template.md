# Resolución de Ejercicio Práctico Complementario (EPC)

**Asignatura / Cátedra:** Análisis de Sistemas de Información (ASI) / Diseño de Sistemas de Información (DSI)  
**Denominación del EPC / Enunciado:** {{NOMBRE_O_TITULO_DEL_EPC}}  
**Versión / Fecha de Entrega:** {{FECHA}}  
**Equipo / Alumno:** {{AUTORES_ALUMNOS}}  

---

## 1. Ficha del Enunciado y Hechos Primarios
- **Dominio del Problema:** {{Resumen ejecutivo del negocio relevado}}.
- **Actores y Stakeholders Identificados:** {{Lista de roles y participantes}}.
- **Objetivos de Negocio Declarados:** {{Metas operativas del enunciado}}.

---

## 2. Matriz de Cobertura de la Consigna del EPC
| Ítem Consigna | Artefacto Solicitado | Evidencia en Enunciado | Skill Especialista Responsable | Estado de Resolución |
|---|---|---|---|:---:|
| 1 | Registro de Requisitos Funcionales | Párr. 2-4 (Relevamiento) | `requirements-extractor` | Resuelto |
| 2 | Modelo de Casos de Uso del Sistema | Párr. 5-7 (Alcance software) | `use-case-extractor` | Resuelto |
| 3 | Especificación Detallada de Caso de Uso | CU Crítico solicitado | `use-case-extractor` | Resuelto |
| 4 | Realización de Caso de Uso (RCU/DSD) | Flujo principal del CU | `grasp-sequence-realizer` | Resuelto |
| 5 | Diagrama de Clases de Diseño (DCD) | Clases y métodos del RCU | `domain-design` | Resuelto |
| 6 | Diagrama de Transición de Estados (DTE) | Ciclo de vida entidad clave | `mermaid-diagram-gen` | Resuelto |
| 7 | Mapeo Objeto-Relacional Lógico | Persistencia del DCD | `relational-object-map` | Resuelto |

---

## 3. Desarrollo Trazable de Artefactos

{{SECCIONES_POR_ARTEFACTO_CON_SUS_CORRESPONDIENTES_DIAGRAMAS_Y_TABLAS}}

---

## 4. Matriz de Supuestos y Decisiones Asumidas
| ID | Elemento Afectado | Duda / Ambigüedad en la Consigna | Supuesto Asumido | Justificación de Cátedra |
|---|---|---|---|---|
| `SUP-01` | RCU Paso 4 | No explicita cómo se calculan recargos | Se asume cálculo proporcional por mora | Estándar de la cátedra DSI |

---

## 5. Checklist de Consistencia Inter-Artefactos
- [ ] ¿Todo mensaje del DSD existe como método en el DCD del receptor?
- [ ] ¿Los estados mutados en la secuencia coinciden con el DTE de la entidad?
- [ ] ¿Todos los casos de uso derivan de requerimientos funcionales aprobados?
- [ ] ¿No se inventaron entidades ni tecnologías ajenas al alcance del enunciado?
