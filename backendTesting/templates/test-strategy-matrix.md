# Matriz de Estrategia de Pruebas Backend

**Proyecto / Sistema:** {{NOMBRE_SISTEMA}}  
**Stack Detectado:** {{LENGUAJE_FRAMEWORK_LIBRERIAS}}  
**Comando de Ejecución de Pruebas:** `{{COMANDO_TESTS}}` (ej. `pytest -v`, `dotnet test`, `mvn test`, `npm test`)  
**Fecha:** {{FECHA}}  

---

## 1. Matriz de Riesgo y Cobertura

| ID | Comportamiento / Escenario de Riesgo | Nivel de Prueba | Dependencias Reales vs. Dobles | Oráculo Observable (Assert) | Prioridad |
|---|---|---|---|---|:---:|
| `TC-01` | {{Descripción del flujo o regla crítica}} | Unitaria | Objetos de dominio puros (sin dobles) | Retorno esperado / Excepción de dominio | Alta |
| `TC-02` | {{Orquestación de caso de uso con efecto secundario}} | Componente | Mock en gateway externo; Entidades reales | Verificación de mensaje enviado con payload esperado | Alta |
| `TC-03` | {{Persistencia y consultas SQL complejas}} | Integración | Base de datos de prueba en memoria o contenedor efímero | Verificación de estado persistido y recuperación limpia | Media |
| `TC-04` | {{Contrato público HTTP de endpoint}} | Contrato | Servidor local en puerto efímero; cliente HTTP real | Código HTTP 201 + Header Location + Schema JSON | Media |
| `TC-05` | {{Flujo extremo a extremo de negocio}} | End-to-End | Todos los servicios en entorno de prueba | Estado final observable y auditoría generada | Baja |

---

## 2. Definición del Entorno y Dobles de Prueba

- **Base de Datos / Persistencia:** {{Indicar si usa SQLite/H2 en memoria, Testcontainers o BD de pruebas compartida con rollback}}.
- **Servicios Externos / APIs de Terceros:** {{Indicar si usa WireMock, Fake en memoria o Mockito/autospec}}.
- **Manejo de Tiempo y Concurrencia:** {{Indicar abstracción del reloj inyectado o TimeProvider para evitar dependencias de datetime.now()}}.

---

## 3. Riesgos Excluidos o Deuda Técnica Asumida

- **Riesgo Excluido 1:** {{Justificación técnica de por qué no se prueba en este nivel o se delega a QA/Infraestructura}}.
- **Riesgo Excluido 2:** {{Ej. No se prueba caída física del datacenter por exceder alcance de pruebas automatizadas}}.
