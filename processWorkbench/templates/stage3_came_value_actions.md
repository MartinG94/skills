# Plantilla de Etapa 3: Matriz CAME, Acciones de Valor y Filtro de Restricciones

## 1. Matriz de Cruces Estratégicos CAME

| Tipo de Estrategia CAME | Cruce de Factores | Enunciado Estratégico de Intervención | Acción de Mejora Concreta Derivada |
|---|---|---|---|
| **DO (Corregir Debilidad con Oportunidad)** | `D3` (Silos TI) + `O2` (APIs SaaS) | Integrar la flota vehicular con el ERP central usando conectores cloud estándar | Implementar conector API REST entre sistema de seguimiento y ERP comercial |
| **DO (Corregir Debilidad con Oportunidad)** | `D2` (Papel 48h) + `O1` (Demanda digital) | Erradicar el remito papel mediante firma electrónica en dispositivo de entrega | Desplegar app móvil para choferes con captura de remito digital firmado |
| **FO (Mantener Fortaleza con Oportunidad)** | `F1` (Flota moderna) + `O3` (Servicio premium) | Apalancar la capacidad frigorífica moderna para captar contratos de alta exigencia | Lanzar línea de servicio pharma con garantía de temperatura en tiempo real |
| **FA (Afrontar Amenaza con Fortaleza)** | `F2` (Personal experto) + `A2` (Normativa sanitaria) | Certificar las competencias del personal en nuevos estándares de trazabilidad | Plan de capacitación y certificación en buenas prácticas de distribución |
| **DA (Minimizar Debilidad y eludir Amenaza)**| `D1` (Falla SoD) + `A1` (Competidores digitales) | Blindar el control interno antes de escalar la operativa frente a nuevos rivales | Reestructurar roles en almacén separando recepción física de confirmación contable |

---

## 2. Inventario de Acciones de Valor (Matriz EERR: Eliminar - Reducir - Incrementar - Crear)

| ID Acción | Acción de Valor Propuesta | Clasificación EERR | Cruce CAME Origen | Proceso Primario y Procesos Afectados |
|---|---|---|---|---|
| `AV-01` | Desplegar app móvil de entrega con firma digital y geolocalización | **Crear** | `DO (D2 + O1)` | Primario: Entrega. Afectados: Facturación, Atención al Cliente |
| `AV-02` | Eliminar remito triplicado en papel y doble transcripción | **Eliminar** | `DO (D2 + O1)` | Primario: Despacho. Afectados: Archivo, Administración |
| `AV-03` | Reducir el tiempo de espera por autorización de supervisor de 45m a 0m | **Reducir** | `DO (D4 + O2)` | Primario: Recepción. Afectados: Supervisión de Almacén |
| `AV-04` | Incrementar la frecuencia de visibilidad de inventario a tiempo real | **Incrementar** | `DO (D3 + O2)` | Primario: Gestión de Stock. Afectados: Ventas, Compras |

---

## 3. Matriz del Filtro de Restricciones Operativas (Viabilidad)

Toda Acción de Valor debe pasar los 4 filtros de viabilidad antes de ser incorporada al plan de implantación de Etapa 4:

| ID Acción | 1. Restricción de Plazos (¿Implementable en < 3-6 meses?) | 2. Restricción Presupuestaria (¿Costo dentro del límite operativo?) | 3. Restricción de Dependencia TI (¿Factible con arquitectura disponible?) | 4. Restricción de Resistencia al Cambio (¿Asimilable por el personal?) | Dictamen de Viabilidad | Ajuste o Mitigación Requerida si aplica |
|---|---|---|---|---|---|---|
| `AV-01` | Sí (Plazo estimado: 8 semanas con app SaaS lista) | Sí (Suscripción mensual por chofer, sin gasto de capital mayor) | Sí (Requiere API abierta del ERP existente) | Media (Requiere capacitar a choferes mayores de 50 años) | **APROBADA** | Incluir 2 talleres prácticos presenciales de uso de la app |
| `AV-02` | Sí (Inmediata tras salida de AV-01) | Sí (Ahorro directo de papel e impresoras) | Sí (Comprobante PDF firmado en S3/almacenamiento cloud) | Baja (Elimina trabajo tedioso al personal) | **APROBADA** | Mantener contingencia de remito papel por 30 días de piloto |
| `AV-03` | Sí (Configuración de workflows en ERP en 3 semanas) | Sí (Cero costo de licenciamiento adicional) | Sí (Módulo estándar de reglas de autorización) | Baja (Supervisor aprueba desde smartphone) | **APROBADA** | Definir matriz de delegación de firmas por montos |
| `AV-04` | Media (12 semanas para pruebas de integración) | Sí (Desarrollo interno de microservicio conector) | Media (Requiere soporte técnico del proveedor de ERP) | Baja (Operarios solo escanean productos) | **APROBADA** | Coordinar ventana de integración con el proveedor de TI |
