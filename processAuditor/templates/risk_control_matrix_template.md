# Matriz de Riesgos y Controles Operativos (Risk & Control Matrix - RCM)

| ID | Actividad / Paso del Proceso | Riesgo Operativo Identificado | Probabilidad / Frecuencia (1-5) | Impacto Operativo (1-5) | Severidad Inherente ($P \times I$) | Control Actual Existente | Tipo de Control (Preventivo / Detectivo / Correctivo) | Deficiencia / Brecha Observada | Control Propuesto / Recomendación |
|---|---|---|---|---|---|---|---|---|---|
| `RC-01` | Recepción de mercadería en almacén | Ingreso de productos no solicitados o en exceso | 4 (Alta) | 3 (Medio) | 12 (Alto) | Cotejo visual contra remito físico en papel | Detectivo | Sin validación contra orden de compra abierta en ERP | Bloqueo en sistema por orden de compra previa y escaneo de código de barras |
| `RC-02` | Emisión de orden de pago a proveedores | Pago por mercadería defectuosa o no recibida | 3 (Media) | 5 (Crítico) | 15 (Crítico) | Firma manual de Tesorería | Detectivo tardío | No se exige triple coincidencia (*three-way matching*) remito-orden-factura | Validación cruzada obligatoria en ERP previa a la programación de pago |
| `RC-03` | Modificación de lista de precios de venta | Aplicación de descuentos indebidos por parte del vendedor | 4 (Alta) | 4 (Alto) | 16 (Crítico) | Ninguno (campo editable libre en terminal) | Ninguno | Falta de control de acceso y límites por perfil | Esquema de autorización multinivel por perfil según rango de descuento |

---

## Escala de Severidad de Riesgo
- **Crítico (15 - 25):** Requiere mitigación inmediata; compromete activos, cumplimiento legal o continuidad del negocio.
- **Alto (10 - 14):** Pérdidas económicas o retrasos significativos; requiere control preventivo automatizado.
- **Medio (5 - 9):** Fricción operativa mitigable mediante controles detectivos periódicos.
- **Bajo (1 - 4):** Riesgo residual asumible con monitoreo básico.
