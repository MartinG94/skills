# Checklist de Brechas de TI y Silos Informáticos (Eje 4 - GUI_U2)

| Dimensión Tecnológica | Pregunta de Evaluación | Estado Observado | Severidad de Brecha | Evidencia en el Caso | Estrategia de Solución TI |
|---|---|---|---|---|---|
| **Fragmentación de Sistemas (Silos)** | ¿Existen aplicaciones aisladas por sector que no dialogan entre sí (ej. Ventas, Depósito, Finanzas)? | Crítico | Alta | Ventas usa un CRM web independiente del ERP contable | Integración mediante API REST / Webhooks con sincronización en tiempo real |
| **Recaptura Manual de Datos** | ¿El personal transcribe información de una pantalla a otra o de un Excel al sistema central? | Crítico | Alta | Administrativo pasa pedidos de correo electrónico a ERP celda por celda | Automatización de ingesta (EDI, parser de órdenes o portal web B2B) |
| **Integridad y Única Fuente de la Verdad** | ¿El stock o saldo de cliente difiere según el sistema consultado? | Deficiente | Alta | Stock en CRM desfasado 24 horas respecto al stock físico del depósito | Modelo de inventario unificado en base de datos central con reservas atómicas |
| **Controles de Acceso y Trazabilidad** | ¿Se comparten usuarios genéricos (ej. `admin`, `caja1`) o faltan logs de auditoría de modificaciones? | Deficiente | Crítica | Todo el turno noche ingresa con la cuenta compartida `operador` | Autenticación individual por usuario con MFA y registro inmutable de transacciones |
