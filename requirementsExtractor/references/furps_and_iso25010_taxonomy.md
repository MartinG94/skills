# Taxonomía de Requerimientos: Matriz FURPS+ e ISO/IEC 25010:2023

Esta guía establece el mapeo formal, subcaracterísticas y métricas cuantificables para la categorización de Requerimientos No Funcionales (RNF) y Atributos de Calidad derivados de entrevistas no estructuradas.

---

## 1. Matriz de Alineación FURPS+ vs. ISO/IEC 25010

| Categoría FURPS+ | Dimensión ISO/IEC 25010:2023 | Subcaracterísticas Clave | Métricas Típicas de Medición (Planguage / SMART) |
| :--- | :--- | :--- | :--- |
| **F**unctionality | **Adecuación Funcional** *(Functional Suitability)* & **Seguridad** *(Security)* | • Completitud funcional<br>• Corrección funcional<br>• Pertinencia funcional<br>• Confidencialidad e integridad | • % de cobertura de casos de uso requeridos<br>• Tasa de error en cálculos (% error < 0.001%)<br>• Cifrado en reposo (AES-256) y tránsito (TLS 1.3)<br>• Autenticación multifactor (MFA) obligatoria |
| **U**sability | **Usabilidad** *(Usability)* & **Calidad en Uso** *(Quality in Use)* | • Reconocimiento de idoneidad<br>• Aprendibilidad (*Learnability*)<br>• Operabilidad<br>• Protección contra errores de usuario<br>• Estética de UI y Accesibilidad (WCAG) | • Tiempo para completar tarea (*Time on Task*) en min/seg<br>• Tasa de éxito en primer intento (> 90%)<br>• Puntuación SUS (*System Usability Scale*) > 80 pts<br>• Máximo de clics para acción primaria (<= 3 clics)<br>• Cumplimiento WCAG 2.1 AA |
| **R**eliability | **Fiabilidad** *(Reliability)* | • Madurez<br>• Disponibilidad (*Availability*)<br>• Tolerancia a fallos (*Fault Tolerance*)<br>• Capacidad de recuperación (*Recoverability*) | • Uptime en horario hábil/24x7 (ej. 99.95%)<br>• MTBF (*Mean Time Between Failures*) > 720 hrs<br>• MTTR (*Mean Time to Recovery*) < 15 min<br>• RPO (*Recovery Point Objective*) < 5 min<br>• RTO (*Recovery Time Objective*) < 30 min |
| **P**erformance | **Eficiencia de Desempeño** *(Performance Efficiency)* | • Comportamiento temporal (*Response Time / Latency*)<br>• Utilización de recursos (CPU, RAM, Red, Disco)<br>• Capacidad (*Throughput / Concurrency*) | • Latencia percentil 95 (P95) < 500 ms en consultas<br>• Latencia P99 < 1500 ms en transacciones pesadas<br>• Throughput >= 250 peticiones/segundo (TPS)<br>• Uso máximo de memoria en servidor <= 70% |
| **S**upportability | **Mantenibilidad** *(Maintainability)* & **Portabilidad** *(Portability)* | • Modularidad y Reusabilidad<br>• Analizabilidad y Diagnóstico<br>• Modificabilidad (*Maintainability*)<br>• Comprobabilidad (*Testability*)<br>• Adaptabilidad e Instalabilidad | • Cobertura de pruebas automatizadas >= 80%<br>• Complejidad ciclomática promedio < 10 por método<br>• Tiempo promedio de despliegue automatizado < 10 min<br>• Tasa de desacoplamiento arquitectónico (SOLID/DDD) |
| **+** (Plus): **Design** | **Restricciones de Diseño** | • Patrones arquitectónicos obligatorios<br>• Estructura de capas o microservicios<br>• Convenciones de diseño de dominio (DDD) | • Cumplimiento de Arquitectura Hexagonal / Limpia<br>• Separación estricta de responsabilidades |
| **+** (Plus): **Implementation** | **Restricciones de Implementación** | • Lenguajes de programación y versiones<br>• Frameworks, librerías y bases de datos permitidas<br>• Estándares de codificación corporativos | • Compatibilidad con Java 21 LTS / .NET 8 / Node 20 LTS<br>• Base de datos relacional PostgreSQL >= 15 |
| **+** (Plus): **Interface** | **Compatibilidad / Interoperabilidad** | • Coexistencia con sistemas legacy<br>• Intercambio de datos con APIs de terceros<br>• Protocolos de comunicación y contratos | • Integración REST OpenAPI 3.0 / gRPC / Webhooks<br>• Autenticación OAuth2 / OIDC con Azure AD / Keycloak |
| **+** (Plus): **Physical / Operation** | **Restricciones Físicas y Operativas** | • Hardware de despliegue y periféricos<br>• Condiciones ambientales o geográficas<br>• Topología de red y servidores físicos | • Funcionamiento en lectores de código de barras Honeywell / Zebra con Android 11+<br>• Conectividad intermitente / soporte Offline-first |

---

## 2. Desglose Detallado por Dimensión

### 2.1. Funcionalidad y Seguridad (FURPS+ F / ISO 25010)
Los requisitos funcionales expresan *qué* hace el sistema. Los atributos no funcionales asociados a la funcionalidad cubren la seguridad técnica y la corrección:
- **Seguridad y Control de Acceso**:
  - Control de acceso basado en roles (RBAC) o atributos (ABAC).
  - Trazabilidad y no repudio: Registro inmutable de auditoría para cada transacción financiera o cambio de estado sensible (usuario, IP, timestamp UTC, estado anterior, estado nuevo).
  - Encriptación: Algoritmos aprobados por NIST (AES-GCM-256 para datos en reposo, TLS 1.3 con PFS para datos en tránsito).

### 2.2. Usabilidad (FURPS+ U / ISO 25010 Usabilidad)
- **Aprendizaje (*Learnability*)**:
  - Tiempo máximo de inducción para que un operario novel ejecute el 100% de las tareas críticas sin supervisión (ej. <= 2 horas de capacitación).
- **Eficiencia Operativa**:
  - Reducción del conteo de pasos/clicks y soporte estricto de atajos de teclado (*keyboard-first navigation*) para puestos de captura intensiva de datos.
- **Prevención y Recuperación de Errores**:
  - Validación de campos en tiempo real (inline validation).
  - Acciones destructivas reversibles o con doble confirmación explícita (mecanismo *Undo / Redo* o confirmación con tipeo de nombre).
- **Accesibilidad**:
  - Estándar WCAG 2.1 Nivel AA: contraste mínimo de color 4.5:1 para texto estándar, soporte para lectores de pantalla, navegación por tabulación secuencial lógica.

### 2.3. Confiabilidad y Disponibilidad (FURPS+ R / ISO 25010 Fiabilidad)
- **Disponibilidad por Niveles de Servicio (SLA)**:
  - 99.0% ("dos nueves"): ~3.65 días de inactividad/año (Sistemas internos no críticos).
  - 99.9% ("tres nueves"): ~8.76 horas de inactividad/año (Sistemas operativos estándar).
  - 99.99% ("cuatro nueves"): ~52.6 minutos de inactividad/año (Sistemas misionales/core).
- **Recuperabilidad ante Desastres (DRP)**:
  - **RPO (*Recovery Point Objective*)**: Cantidad máxima de datos tolerada a perder (ej. < 5 minutos de transacciones).
  - **RTO (*Recovery Time Objective*)**: Tiempo máximo de recuperación de servicio (ej. < 30 minutos tras caída).
- **Tolerancia a Fallos**:
  - Resiliencia ante desconexiones de pasarelas o servicios externos (Circuit Breaker, Exponential Backoff, Dead Letter Queues).

### 2.4. Desempeño y Escalabilidad (FURPS+ P / ISO 25010 Eficiencia de Desempeño)
- **Tiempos de Respuesta (*Response Time*)**:
  - Búsquedas simples y autocompletado: `< 200 ms`.
  - Carga de pantallas transaccionales: `< 1.0 s` al percentil 95 (P95).
  - Procesamiento por lotes / reportes pesados: Notificación asíncrona mediante Webhook / SSE / Email si la ejecución supera los `5.0 s`.
- **Carga y Concurrencia**:
  - Capacidad nominal: Usuarios concurrentes activos simultáneos en régimen normal (ej. 500 sesiones activas concurrentes con consumo <= 40% CPU).
  - Carga pico (*Peak Load*): Factor multiplicador soportado (ej. 3x de tráfico normal con latencia P95 < 2.0 s).

### 2.5. Soportabilidad y Mantenibilidad (FURPS+ S / ISO 25010 Mantenibilidad)
- **Mantenibilidad de Código**:
  - Arquitectura modular desacoplada con inversión de dependencias.
  - Documentación de contratos de API viva (OpenAPI 3.0 / AsyncAPI).
- **Observabilidad y Diagnóstico**:
  - Logs estructurados en formato JSON (severidad, correlation ID / trace ID distribuido, timestamp UTC ISO-8601).
  - Métricas de telemetría y endpoints de salud (`/health/live`, `/health/ready`).

### 2.6. Restricciones (+ Plus Constraints)
- **Restricciones Legales y Regulatorias**: GDPR, Ley de Protección de Datos Personales, PCI-DSS para datos de tarjetas de crédito, retención fiscal obligatoria de comprobantes durante 10 años.
- **Restricciones Tecnológicas Institucionales**: Uso de la nube corporativa o servidores On-Premises existentes; compatibilidad con navegadores Evergreen (Chrome, Firefox, Edge, Safari últimas 2 versiones).
