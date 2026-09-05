---
name: microservice-decomposer
description: >-
  Evalúa monolito modular frente a microservicios y, cuando se justifican, propone
  límites de servicios trazables al negocio y a atributos de calidad. Úsala para
  decisiones de arquitectura, no para fragmentar automáticamente un sistema.
---

# Evaluación y descomposición de servicios

La primera decisión es si conviene distribuir el sistema. `Monolito modular` es un
resultado válido, especialmente con equipo pequeño, dominio incierto, operaciones
fuertemente transaccionales o capacidades operativas insuficientes.

## Elegir el perfil

- `course-architecture` — predeterminado para DSI/PPAI. Produce las vistas pedidas por
  la cátedra. Lee [references/decomposition-and-views.md](references/decomposition-and-views.md).
- `professional-decomposition` — para una decisión o migración real. Usa la misma guía
  y añade contratos/datos sólo hasta el nivel requerido.
- `distributed-workflow` — sólo si existen transacciones o integraciones entre límites;
  lee [references/distributed-patterns.md](references/distributed-patterns.md).

No uses C4, Saga, broker, gateway, Kubernetes, service mesh, gRPC o persistencia
políglota salvo que el usuario los pida o una decisión/evidencia concreta los requiera.

## Entradas

Busca:

- objetivos de negocio, capacidades, subdominios y vocabulario;
- casos de uso y flujos que cruzan responsabilidades;
- requisitos de despliegue, escala, disponibilidad, consistencia y seguridad;
- equipos, ownership, cadencia de cambio y capacidades de operación;
- arquitectura/datos actuales y restricciones de migración;
- formato de vistas requerido.

No inventes volumen, latencia, equipos, regiones, tecnologías ni SLO. Declara `TBD` o
una pregunta cuando uno de esos datos cambie la decisión.

## Decisión de distribución

1. Establece una alternativa base de monolito modular.
2. Identifica las fuerzas que podrían justificar despliegue independiente: cadencias
   distintas, escalado focalizado, aislamiento, ownership o autonomía regulatoria.
3. Expone costes: red, consistencia, pruebas, despliegue, observabilidad, seguridad y
   coordinación de versiones.
4. Recomienda microservicios sólo si los beneficios esperados superan esos costes con
   evidencia suficiente. Si hay incertidumbre, elige límites más gruesos y una ruta de
   extracción reversible.

Microservicios no garantizan escalabilidad, disponibilidad, velocidad de equipo ni
aislamiento. Esas propiedades dependen del diseño y la operación.

## Descomposición cuando está justificada

1. Agrupa funcionalidades por capacidad de negocio y cohesión de cambio.
2. Usa subdominios y bounded contexts para razonar sobre modelos y lenguaje.
3. Propón servicios como hipótesis desplegables; no asumas una equivalencia obligatoria
   entre subdominio, bounded context y microservicio.
4. Comprueba responsabilidad, chattiness, transacciones, ownership de datos y capacidad
   del equipo. Fusiona límites débiles o conversadores.
5. Define contratos y consistencia sólo para interacciones necesarias.
6. Traza cada límite a casos de uso, RNF y decisiones.

`Database per service` significa que un servicio es dueño de sus datos y otros acceden
mediante su contrato. No exige un servidor físico distinto ni motor diferente.

## Producto predeterminado

1. `Contexto y evidencia` — alcance, restricciones, hechos y TBD.
2. `Decisión` — monolito modular o microservicios, alternativas y trade-offs.
3. `Límites propuestos` — capacidades, responsabilidades, datos propios y equipo si se
   conoce.
4. `Interacciones críticas` — síncronas/asíncronas sólo donde corresponda.
5. `Vistas y trazabilidad` — según perfil.
6. `Riesgos y validación` — hipótesis que requieren prueba o medición.

Usa Mermaid como renderer predeterminado y un único diagrama por vista. C4 es opcional;
para DSI prioriza las vistas solicitadas por la consigna. No produzcas manifiestos de
infraestructura ni código salvo pedido explícito.

## Criterios de cierre

- Se comparó explícitamente con un monolito modular.
- Cada límite tiene cohesión y una razón de despliegue independiente, o está marcado
  como hipótesis.
- Las transacciones y consultas que cruzan límites son visibles.
- No se confundieron relaciones organizacionales de Context Map con protocolos.
- Toda tecnología o patrón tiene una fuerza y un coste documentados.
