# Heurísticas de Redacción y Calidad de Casos de Uso (Alistair Cockburn)

Esta referencia establece pautas metodológicas para modelar y redactar casos de uso institucionales rigurosos.

---

## 1. Granularidad: El "Nivel del Mar" (Sea Level)

- **Objetivo de Usuario (Sea Level / Nivel del Mar):** Representa una tarea completa que un actor humano realiza en una sola sesión de trabajo (típicamente de 2 a 20 minutos) y que deja los datos de negocio en un estado consistente y de valor (ej. *Registrar Pedido*, *Autorizar Crédito*).
- **Anti-patrón de Micro-Casos (Nivel Submarino / Clams):** Descomponer un CU en clics de interfaz o pantallas aisladas (❌ *Hacer clic en botón*, ❌ *Abrir ventana de búsqueda*, ❌ *Ingresar contraseña*).
- **Anti-patrón de Macro-Procesos (Nivel Resumen / Kite / Cloud):** Intentar cubrir todo el negocio en un solo caso de uso (❌ *Administrar la Empresa*, ❌ *Gestionar la Cadena de Suministro*).

---

## 2. Independencia de Interfaz y Tecnología

Los casos de uso describen la **intención de negocio** del actor y la **responsabilidad observable** del sistema, no la ergonomía física de la interfaz gráfica:

- ❌ **Incorrecto (Acoplado a UI):** *"El usuario hace clic en el botón azul de la barra lateral, se abre un modal emergente y selecciona la opción de un combo box..."*
- ✔️ **Correcto (Intención de Negocio):** *"El actor solicita registrar un nuevo pedido y selecciona el producto deseado del catálogo..."*

---

## 3. Semántica de Relaciones en el Modelo de Casos de Uso

| Relación UML | Semántica Estricta | Cuándo Utilizarla | Cuándo Evitarla |
|---|---|---|---|
| **Inclusión (`<<include>>`)** | Subflujo común obligatorio compartido por dos o más casos de uso. | Para evitar duplicar un fragmento idéntico de pasos (ej. *Validar Identidad*). | Para descomposición funcional paso a paso (anti-patrón de programación estructurada). |
| **Extensión (`<<extend>>`)** | Comportamiento condicional u opcional que amplía un caso de uso base. | Para flujos excepcionales complejos o variantes que solo ocurren bajo una condición explícita. | Cuando el desvío es una simple validación de datos que se resuelve con un flujo alternativo local. |
| **Generalización** | Especialización polimórfica de un actor o caso de uso abstracto. | Cuando múltiples variantes heredan el objetivo y precondiciones del caso base. | Cuando las variantes difieren sustancialmente en sus flujos y actores. |

> [!IMPORTANT]
> **Puntos de Extensión Obligatorios:** Toda relación `<<extend>>` debe documentar explícitamente en el caso de uso base su **Extension Point** (en qué paso exacto se produce la bifurcación) y su **Condición de Disparo**.
