# Informe de Auditoría UX/UI y Accesibilidad

**Producto / Interfaz Auditada:** {{NOMBRE_INTERFAZ_O_PANTALLA}}  
**Alcance de la Auditoría:** {{DESCRIPCION_ALCANCE}}  
**Normas y Marcos de Evaluación:** Heurísticas de Nielsen (10 Usability Heuristics) y WCAG 2.2 Nivel AA  
**Fecha:** {{FECHA}}  

---

## 1. Resumen Ejecutivo de Hallazgos

| Nivel de Severidad | Cantidad | Descripción del Impacto |
|---|:---:|---|
| **Bloqueante (P0)** | 0 | Impide al usuario completar la tarea crítica o viola barreras de accesibilidad total. |
| **Mayor (P1)** | 0 | Causa frustración severa, lentitud o alta probabilidad de error sin bloqueo total. |
| **Menor / Oportunidad (P2)**| 0 | Detalle estético, inconsistencia menor de espaciado o microcopia mejorable. |

---

## 2. Matriz Detallada de Hallazgos

| ID | Ubicación / Componente | Criterio / Heurística Afectada | Evidencia Observable | Impacto en Usuario | Propuesta de Remediación Concreta |
|---|---|---|---|---|---|
| `AUD-01` | Formulario de Registro | Heurística H5: Prevención de errores | El botón de envío se activa con campos requeridos vacíos sin advertencia. | El usuario envía el formulario y pierde los datos ingresados al recargar. | Implementar validación en tiempo real en evento `blur` y deshabilitar envío hasta completar obligatorios. |
| `AUD-02` | Botón secundario en Modal | WCAG 1.4.3: Contraste Mínimo (AA) | Texto gris `#94a3b8` sobre fondo blanco `#ffffff` (ratio 2.8:1). | Ilegibilidad para usuarios con baja visión o bajo luz ambiental intensa. | Ajustar el color de texto a `#475569` para alcanzar ratio $\ge 4.5:1$. |
| `AUD-03` | Menú desplegable móvil | WCAG 2.5.8: Tamaño del Objetivo Táctil | Elementos de lista con altura de 28px y padding de 4px. | Errores de pulsación involuntaria en dispositivos móviles. | Incrementar la altura del objetivo interactivo a un mínimo de $44 \times 44\text{ px}$. |

---

## 3. Checklist de Cierre y Gates de Calidad

- [ ] ¿Todos los contrastes de texto normal cumplen con el ratio mínimo de 4.5:1 (o 3:1 para texto grande/interfaz)?
- [ ] ¿Todos los controles interactivos tienen estados visuales diferenciados para `:focus`, `:hover` y `:active`?
- [ ] ¿Los campos de formulario cuentan con elementos `<label>` vinculados mediante `for`/`id`?
- [ ] ¿Los mensajes de error explican qué falló y cómo solucionarlo sin culpar al usuario?
