# Perfil de dominio rico

Lee esta referencia sólo si el usuario pide DDD táctico/modelo rico o las invariantes
y límites de consistencia proporcionados justifican ese enfoque.

## Decidir los elementos

- `Entity`: su continuidad depende de identidad estable a lo largo del tiempo.
- `Value Object`: se define por sus valores, tiene igualdad por valor y puede proteger
  una regla útil. La inmutabilidad suele ser conveniente, pero respeta el lenguaje y
  las restricciones del proyecto.
- `Aggregate`: conjunto que necesita un límite explícito de consistencia inmediata y
  una raíz que controle cambios internos.
- `Domain Service`: operación de dominio que no encaja de forma natural en una entidad
  u objeto de valor; no es un contenedor genérico de lógica.
- `Application Service/Interactor`: coordina un caso de uso y sus fronteras; no debe
  absorber invariantes del dominio.
- `Repository`: abstracción de acceso a una colección de agregados cuando el caso de
  uso realmente necesita persistencia; no uno por clase por convención.

Para cada propuesta, registra la evidencia: identidad, regla, transacción o variación
que la hace necesaria. Si no existe, conserva un diseño OO más simple.

## Límites importantes

- Referenciar otro agregado por identidad no se representa automáticamente con rombo
  de agregación UML; elige la relación UML por su semántica propia.
- No hagas que una transacción abarque varios agregados sólo para simplificar el código.
- No agregues eventos de dominio si ningún consumidor, regla temporal o desacoplamiento
  real los requiere.
- Puertos y adaptadores son una decisión arquitectónica, no componentes obligatorios
  de todo DCD.
- DTO y tipos de transporte no pertenecen al núcleo salvo que el alcance del diagrama
  los incluya explícitamente.

## Código opcional

Si se pide implementación:

1. usa el lenguaje, versión y convenciones detectados;
2. materializa sólo el fragmento cubierto por el diseño;
3. diferencia validación de forma, reglas de negocio y fallos de infraestructura;
4. no inventes dependencias ni configuración;
5. compila o ejecuta las comprobaciones disponibles antes de afirmar que funciona.
