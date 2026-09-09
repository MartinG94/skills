# Reglas de Calidad para Enunciados de Requisitos (IEEE 29148 / ISO 25010)

Esta referencia establece pautas para auditar la calidad sintáctica y semántica de requerimientos funcionales y criterios de aceptación.

---

## 1. Lista Negra de Términos Ambiguos (Weak Words)

El uso de los siguientes términos en requisitos o casos de uso constituye un defecto de calidad que debe señalarse en la auditoría:

| Categoría | Términos Prohibidos | Causa del Rechazo | Reemplazo Cuantitativo Recomendado |
|---|---|---|---|
| **Rendimiento Subjetivo** | *rápido, veloz, inmediato, instantáneo, en tiempo real, óptimo, ágil* | No establece un umbral objetivo verificable. | Especificar percentil de latencia: $\le 500\text{ ms (P95)}$ bajo carga nominal. |
| **Usabilidad Indeterminada** | *fácil, intuitivo, amigable, sencillo, simple, cómodo, ergonómico* | Depende de la apreciación personal del usuario. | Tiempo de inducción $\le 15\text{ min}$ o tasa de éxito en primer intento $\ge 90\%$. |
| **Robustez Vacía** | *robusto, potente, eficiente, escalable, flexible, seguro, adecuado* | Adjetivos vacíos sin métrica de ingeniería. | Rango de concurrencia: $\ge 200\text{ peticiones/seg}$; MTBF $\ge 720\text{ h}$. |
| **Cláusulas de Escape** | *etc., y/o, entre otros, incluyendo pero no limitado a, cuando sea necesario* | Oculta requisitos incompletos y abre el alcance indefinidamente. | Listar exhaustivamente los elementos o abrir un ítem `TBD` / pregunta de negocio. |

---

## 2. Estructura Sintáctica Canónica: Voz Activa

Todo requisito funcional debe redactarse en voz activa respetando la fórmula:

$$\text{[Sujeto / Actor / Rol]} + \text{\textbf{DEBE}} + \text{[Verbo de Acción Transitivo]} + \text{[Objeto Directo]} + \text{[Condición / Parámetro de Negocio]}$$

### Ejemplo de Normalización
- ❌ **Incorrecto:** *"Los pedidos deben ser cancelados rápidamente si el cliente no tiene saldo."*
- ✔️ **Correcto:** *"El Sistema de Facturación DEBE rechazar el pedido si el saldo disponible del cliente es inferior al importe total cotizado."*

---

## 3. Rigor Modal Normativo (RFC 2119 / ISO 29148)

- **DEBE (SHALL / MUST):** Requisito contractual de cumplimiento obligatorio estricto.
- **DEBERÍA (SHOULD):** Característica deseable de alta prioridad, cuya postergación exige justificación.
- **PUEDE (MAY):** Característica opcional o alternativa permitida sin impacto bloqueante.
