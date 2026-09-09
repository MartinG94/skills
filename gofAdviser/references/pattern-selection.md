# Selección operativa de patrones GoF

Usa esta referencia cuando debas comparar candidatos o justificar un patrón.

## Registro de decisión

Completa sólo los campos respaldados por el material:

| Campo | Contenido |
|---|---|
| Problema | comportamiento/responsabilidad y evidencia |
| Variable | qué se espera que cambie |
| Fuerzas | restricciones y objetivos en tensión |
| Alternativa simple | diseño sin patrón o refactor local |
| Candidatos | hasta tres patrones plausibles |
| Decisión | patrón o `ninguno` |
| Participantes | roles GoF → elementos del dominio |
| Consecuencias | beneficios, costes y riesgos concretos |
| Validación | cambio futuro, prueba o revisión estructural |

## Patrones priorizados en DSI

| Patrón | Intención y señal suficiente | Evitar cuando | Participantes mínimos |
|---|---|---|---|
| Strategy | Familia real de algoritmos intercambiables que cambia independientemente del cliente. | Hay una sola variante estable o el polimorfismo existente basta. | Context, Strategy, ConcreteStrategy. |
| State | El comportamiento y las operaciones válidas cambian sustancialmente con el estado. | Sólo se almacena/visualiza un estado o hay pocas transiciones triviales. | Context, State, ConcreteState. |
| Observer | Un cambio debe notificar a múltiples dependientes cuya lista puede variar. | Hay receptor único conocido, orden transaccional estricto o llamada directa más clara. | Subject/Publisher, Observer, ConcreteObserver. |
| Adapter | Un cliente debe usar una interfaz incompatible que no puede o no conviene modificar. | Se controla ambos lados y puede alinearse el contrato directamente. | Client, Target, Adapter, Adaptee. |
| Iterator | Se necesita recorrer una estructura sin exponer representación o con recorridos propios. | La colección/lenguaje ya ofrece la iteración requerida. | Iterator, ConcreteIterator, Aggregate. |

Al justificar uno, usa la forma académica: nombre, problema, aplicabilidad, solución
abstracta, participantes, colaboraciones y consecuencias. No copies una implementación
genérica como si fuera la solución del dominio.

## Catálogo compacto para ampliar la búsqueda

### Creacionales

- Abstract Factory — crea familias relacionadas sin fijar clases concretas.
- Builder — separa construcción por pasos de la representación final.
- Factory Method — difiere a subclases/implementaciones la clase concreta creada.
- Prototype — crea por clonación cuando configurar/copiar el prototipo es significativo.
- Singleton — restringe a una instancia y acceso global; alto riesgo de estado global,
  acoplamiento y pruebas difíciles, por lo que exige una necesidad explícita.

### Estructurales

- Adapter — convierte un contrato a otro esperado.
- Bridge — separa abstracción e implementación para que ambas varíen.
- Composite — trata uniformemente objetos individuales y composiciones jerárquicas.
- Decorator — agrega responsabilidades por envoltura dinámica.
- Facade — ofrece una interfaz simplificada a un subsistema.
- Flyweight — comparte estado intrínseco de muchos objetos pequeños.
- Proxy — controla acceso mediante un representante con el mismo contrato.

### De comportamiento

- Chain of Responsibility — pasa una solicitud por manejadores hasta que alguno actúe.
- Command — encapsula una petición para colas, historial o deshacer.
- Interpreter — representa y evalúa una gramática pequeña y estable.
- Iterator — recorre sin exponer representación.
- Mediator — centraliza interacciones complejas entre colegas.
- Memento — captura/restaura estado sin romper encapsulación.
- Observer — notifica dependientes ante cambios.
- State — varía comportamiento según estado interno.
- Strategy — intercambia algoritmos.
- Template Method — fija esqueleto y deja pasos a subclases.
- Visitor — agrega operaciones sobre una estructura estable de tipos.

## Desambiguaciones frecuentes

- Strategy vs State: Strategy representa una política elegible; State representa ciclo
  de vida y puede gobernar transiciones.
- Adapter vs Facade: Adapter cambia contrato; Facade simplifica un subsistema.
- Decorator vs Proxy: Decorator agrega responsabilidad; Proxy controla acceso.
- Factory Method vs Abstract Factory: uno difiere una creación; el otro coordina una
  familia de productos.
- Observer vs Mediator: Observer difunde cambios; Mediator organiza conversaciones.

Si dos opciones siguen empatadas, expresa qué evidencia falta en vez de seleccionar al
azar o recomendar ambas como una combinación obligatoria.


## Matriz de Síntomas / Code Smells $\to$ Patrones GoF Candidatos

| Síntoma Clínico en el Código | Principio Violado | Patrón(es) Candidato(s) a Evaluar |
|---|---|---|
| Múltiples sentencias `switch` o `if/else` ramificando por tipo de algoritmo | Open/Closed Principle (OCP) | **Strategy** |
| Condicionales complejos que cambian según el estado actual del objeto | Single Responsibility / OCP | **State** |
| Acoplamiento rígido a librerías de terceros o SDKs con interfaces incompatibles | Dependency Inversion (DIP) | **Adapter** |
| Clases dios orquestadoras que notifican manualmente a múltiples módulos | Low Coupling | **Observer** o **Mediator** |
| Constructores con excesivos parámetros opcionales (*Telescoping Constructor*) | Clean Construction | **Builder** |
| Clientes acoplados a una jerarquía compleja de subsistemas | Information Hiding | **Facade** |
| Estructuras recursivas parte-todo tratadas con comprobaciones manuales de tipo | High Cohesion | **Composite** |
| Proliferación de subclases para combinar responsabilidades dinámicas | Favor Composition | **Decorator** |
| Creación directa de objetos costosos o control de acceso/caching en red | Single Responsibility | **Proxy** o **Flyweight** |
| Instanciaciones rígidas con `new` dispersas por todo el código | Inversión de Control | **Factory Method** o **Abstract Factory** |

---

## Catálogo de Criterios para Patrones Estructurales y Creacionales Clave

- **Builder:** Usar cuando la construcción de un objeto complejo requiera pasos secuenciales y validaciones de invariantes antes de emitir la instancia terminada. Evitar para DTOs simples con 3 atributos.
- **Composite:** Usar cuando clientes deban tratar de manera idéntica a objetos individuales y a composiciones de objetos (árboles). Participantes: `Component`, `Leaf`, `Composite`.
- **Decorator:** Usar para agregar responsabilidades dinámicamente a objetos en tiempo de ejecución sin recurrir a herencia estática. Participantes: `Component`, `ConcreteComponent`, `Decorator`, `ConcreteDecorator`.
- **Facade:** Usar para brindar una interfaz simplificada y de alto nivel a un subsistema complejo. Participantes: `Facade`, clases internas del subsistema.
- **Command:** Usar para parametrizar objetos con solicitudes, diferir su ejecución en colas o soportar operaciones de deshacer (*undo/redo*). Participantes: `Command`, `ConcreteCommand`, `Invoker`, `Receiver`.
- **Template Method:** Usar cuando el esqueleto de un algoritmo invariante deba definirse en una clase base, permitiendo a las subclases redefinir pasos específicos sin alterar la estructura global.
