# Catálogo Neutral de Discrepancias e Inconsistencias UML

Esta referencia cataloga las patologías de inconsistencia detectables entre realizaciones (DSD), modelos estáticos (DCD), ciclos de vida (DTE) y código.

---

## 1. Regla C1: Mensajes y Operaciones del Receptor
- **Método Inexistente:** El mensaje enviado a un objeto receptor en el DSD no existe en la interfaz/clase del DCD.
- **Discordancia de Aridad o Parámetros:** El DSD envía 2 parámetros pero el método en el DCD declara 1 o ninguno.
- **Incompatibilidad de Retorno:** El DSD espera un objeto retornado complejo (`p: Pedido`) pero el DCD tipa el retorno como `void` o `boolean`.
- **Violación de Visibilidad:** Un objeto externo invoca un método declarado como privado (`-`) o protegido (`#`) en el DCD.

---

## 2. Regla C2: Rutas de Navegabilidad y Referencias
- **Ausencia de Asociación:** Un objeto $A$ envía un mensaje a $B$ en el DSD, pero en el DCD no existe asociación, agregación, composición ni paso de $B$ como parámetro.
- **Navegabilidad Invertida:** La flecha de asociación en el DCD apunta de $B \to A$, pero en el DSD es $A$ quien invoca a $B$.
- **Violación de la Ley de Demeter:** Un objeto navega intermediarios privados sin ruta legítima de visibilidad.

---

## 3. Regla C3: Creación y Responsabilidad (GRASP Creador)
- **Creación Directa Ilegítima:** La UI o un Boundary instancia directamente una entidad de dominio persistente omitiendo al Agregado o Fábrica.
- **Inconsistencia de Constructor:** El mensaje de creación `create(...)` en el DSD no coincide con los constructores del DCD.

---

## 4. Regla C4: Ciclo de Vida y Transiciones de Estado
- **Transición Ilegal:** El DSD ejecuta una mutación que conduce la entidad a un estado inexistente o no permitido en el DTE desde el estado actual.
- **Mutación sobre Estado Terminal:** El DSD invoca un método modificador sobre una entidad que ya alcanzó su estado terminal en el DTE.
- **Falta de Evento Disparador:** El DTE declara una transición pero el DSD jamás invoca el método que produce dicho evento.

---

## 5. Regla C5 y C6: Elementos Huérfanos y Drift
- **Método Huérfano en DCD:** Un método de dominio específico no es invocado por ninguna realización de caso de uso del sistema.
- **Clase Huérfana:** Entidad presente en el DCD que carece de trazabilidad hacia requisitos o flujos de usuario.
