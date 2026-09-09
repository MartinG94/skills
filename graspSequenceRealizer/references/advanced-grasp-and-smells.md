# Patrones GRASP Avanzados, Matriz GoF y Anti-Patrones de Secuencia

Esta referencia profundiza en el diseño de realizaciones de objetos y colaboración estricta.

---

## 1. Los 4 Patrones GRASP Avanzados de Diseño

Complementan a los 5 básicos (*Experto, Creador, Controlador, Alta Cohesión, Bajo Acoplamiento*):

| Patrón GRASP Avanzado | Problema que Resuelve | Solución de Asignación | Señal de Alarma / Abuso |
|---|---|---|---|
| **Polimorfismo (Polymorphism)** | Variaciones de comportamiento basadas en el tipo de entidad mediante condicionales `if/switch`. | Asignar la responsabilidad de la operación variable a una interfaz común polimórfica implementada por subclases. | Crear jerarquías de polimorfismo para variaciones menores que se resuelven con un parámetro. |
| **Fabricación Pura (Pure Fabrication)** | Una responsabilidad técnica no encaja de forma natural en ninguna entidad de dominio sin degradar su cohesión. | Crear una clase artificial de servicio o infraestructura que no representa un concepto del negocio (ej. `Repositorio`, `DAO`, `Logger`, `Fabrica`). | Degradar el dominio a un modelo anémico llenando el sistema de servicios de fabricación pura. |
| **Indirección (Indirection)** | Acoplamiento directo indeseable entre dos o más componentes de capas distintas. | Asignar la responsabilidad a un objeto intermediario (ej. adaptador, mediador o controlador) para canalizar la interacción. | Introducir capas de paso (*pass-through*) que solo reenvían llamadas sin aportar valor. |
| **Variaciones Protegidas (Protected Variations)** | Inestabilidad o cambios frecuentes en un subsistema impactan y rompen a otros componentes. | Diseñar una interfaz estable y encapsulada alrededor del punto previsible de variación o inestabilidad. | Proteger puntos de variación hipotéticos que nunca cambiarán (*YAGNI*). |

---

## 2. Matriz de Sinergia Conceptual: GRASP $\leftrightarrow$ GoF

| Patrón GoF | Principios GRASP Subyacentes que lo Justifican |
|---|---|
| **Strategy** | **Polimorfismo** + **Variaciones Protegidas** + **Bajo Acoplamiento** |
| **State** | **Polimorfismo** + **Experto en Información** + **Variaciones Protegidas** |
| **Adapter** | **Fabricación Pura** + **Indirección** + **Bajo Acoplamiento** |
| **Observer** | **Bajo Acoplamiento** + **Indirección** + **Variaciones Protegidas** |
| **Factory Method** | **Creador** + **Fabricación Pura** + **Polimorfismo** |

---

## 3. Catálogo de Anti-Patrones en Diagramas de Secuencia

1. **El Gestor Dios (God Gestor):**
   - *Fallo:* El controlador extrae todos los datos de las entidades mediante sucesivos `getters` y realiza él mismo los cálculos y validaciones.
   - *Solución:* Aplicar **Experto en Información** delegando el cálculo a la entidad que posee los datos (*Tell Don't Ask*).
2. **Trenes de Mensajes (Violación de la Ley de Demeter):**
   - *Fallo:* Encadenamiento profundo `gestor -> pedido.getCliente().getDireccion().getCiudad()`.
   - *Solución:* El gestor debe consultar únicamente a su colaborador directo: `pedido.obtenerCiudadDestino()`.
3. **Bypass de Capas:**
   - *Fallo:* La interfaz gráfica o controlador de API invoca directamente a entidades de dominio internas o pasarelas de terceros sin pasar por la capa de aplicación/gestor.
4. **Mutación Prematura de Estado:**
   - *Fallo:* La secuencia persiste o modifica el estado de entidades de dominio antes de que el actor confirme la transacción o antes de validar todas las reglas de negocio.
