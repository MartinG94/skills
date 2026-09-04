# backendTesting: Estrategia de Pruebas Automatizadas y Artesanía de Testing en Backend

Esta skill capacita al agente de inteligencia artificial para auditar, diseñar e implementar suites de pruebas automatizadas sostenibles, robustas y de alta velocidad para aplicaciones backend orientadas a objetos.

Se fundamenta en la **Pirámide de Pruebas de Mike Cohn**, la **taxonomía formal de Dobles de Prueba de Gerard Meszaros** (*xUnit Test Patterns*) y las directivas de **Diseño para la Testabilidad** en arquitecturas limpias (Hexagonal, Onion, DDD).

---

## Estructura de la Skill

```text
backendTesting/
├── SKILL.md            # Metodología exhaustiva, patrones AAA/FIRST, taxonomía de Test Doubles, anti-patrones y casos de estudio
└── README.md           # Manual de referencia rápida, directivas de arquitectura y guía de ejecución políglota
```

---

## Pilares Metodológicos

### 1. La Pirámide de Pruebas en Backend
- **Pruebas Unitarias de Dominio & Casos de Uso (60-75%)**: En memoria pura, ultra rápidas (< 10 ms), sin dependencias de I/O, base de datos ni red.
- **Pruebas de Integración de Adaptadores (20-30%)**: Verificación de mapeos ORM, consultas SQL reales y clientes HTTP mediante contenedores efímeros (*Testcontainers*, bases de prueba o *WireMock*).
- **Pruebas End-to-End & Contrato (5-10%)**: Flujos transversales y contratos de integración externos.

### 2. Taxonomía Rigurosa de Test Doubles (Gerard Meszaros)
| Doble | Propósito | Regla de Oro |
| :--- | :--- | :--- |
| **Dummy** | Relleno inerte de parámetros no utilizados. | No asertar sobre él. |
| **Stub** | Provee respuestas enlatadas preconfiguradas. | Usar para simular consultas a puertos secundarios. |
| **Spy** | Envuelve un objeto real o captura llamadas para auditoría. | Usar cuando se necesite inspeccionar payloads de salida. |
| **Mock** | Verifica interacciones y llamadas estrictas (efectos secundarios). | Usar solo para servicios de red/notificaciones (e.g. pasarela de pago, email). |
| **Fake** | Implementación funcional ligera en memoria (e.g. `InMemoryRepo`). | Preferir sobre cadenas complejas de mocks. |

> ⚠️ **Regla de Oro**: Jamás mockear Entidades de Dominio, Value Objects ni DTOs. Usar siempre instancias reales del dominio.

### 3. Anatomía de Pruebas Limpias: El Patrón AAA
Toda prueba unitaria debe estructurarse explícitamente en:
1. **Arrange (Preparar / Given)**: Instanciar objetos reales del dominio, inicializar datos y configurar dobles de puertos secundarios.
2. **Act (Ejecutar / When)**: Invocar el método único bajo prueba.
3. **Assert (Verificar / Then)**: Validar el valor devuelto, los invariantes del estado resultante y/o la interacción del puerto.

### 4. Estándar de Nomenclatura
`NombreMetodo_EscenarioOCondicion_ResultadoEsperado`

---

## Soporte Políglota y Comandos de Ejecución

La skill incluye casos de estudio completos para los 3 ecosistemas principales de backend:

| Ecosistema | Versión Mínima | Framework de Pruebas | Librerías de Dobles & Aserciones | Comando de Ejecución CLI |
| :--- | :--- | :--- | :--- | :--- |
| **C# / .NET** | .NET 8 / 9 | **xUnit** | `FluentAssertions`, `Moq` / `NSubstitute` | `dotnet test --logger "console;verbosity=detailed"` |
| **Java** | Java 17 / 21 | **JUnit 5** (Jupiter) | `Mockito`, `AssertJ` | `mvn test` o `./gradlew test` |
| **Python** | Python >3.10 | **pytest** | `unittest.mock` (`create_autospec`), `pytest-mock` | `pytest -v --tb=short` |

---

## Cómo Solicitar Asistencia al Agente con esta Skill

Con la skill activa, puedes solicitar asistencia al agente con prompts como:
- *"Audita este caso de uso y diseña sus pruebas unitarias en Python (>3.10) usando pytest y typing.Protocol sin sobre-mockear el dominio."*
- *"Refactoriza estas pruebas en C#/xUnit que usan Thread.sleep() y mocks de entidades a una suite determinista con el patrón AAA."*
- *"Diseña un Fake en memoria para el repositorio de clientes y crea las pruebas de orquestación en Java con JUnit 5 y AssertJ."*
- *"Identifica por qué este test es frágil frente a refactorizaciones y elimina las aserciones sobre métodos privados."*
