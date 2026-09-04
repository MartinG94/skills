---
name: use-case-extractor
description: Descubre, estructura y describe casos de uso de sistema trazables desde requisitos o procesos. Úsala para el modelo y las descripciones institucionales de CU; no para realizar secuencias BCE, asignar responsabilidades de diseño ni introducir interfaz, persistencia o tecnología no documentadas.
---

# Use Case Extractor

Produce un modelo de casos de uso que exprese el comportamiento externo del sistema en lenguaje del usuario. No reemplaza el modelo de negocio, el modelo de dominio, el diseño de interfaz ni los casos de prueba.

## Selección de modo

- **Modelo** (predeterminado ante una narrativa o catálogo de requisitos): identificar actores, CU y objetivos; estructurar relaciones; generar inventario y diagrama.
- **Descripción** (predeterminado si se proporciona uno o más CU seleccionados): especificar flujos y condiciones de esos CU.

Entrega únicamente el modo solicitado. Si el usuario pide “extraer casos de uso” sin más, usa **Modelo** y no describas todos los CU automáticamente. Cuando pida una realización, clases BCE o una secuencia de responsabilidades, completa primero la descripción del CU necesaria y deriva ese producto a `grasp-sequence-realizer`, propietaria de las realizaciones de análisis y diseño.

## Evidencia y límites

- Asigna IDs de fuente (`SRC-01`) y cita página, sección, párrafo o marca de tiempo para cada actor, CU, regla y flujo.
- Enlaza RF/RNF/RN existentes por sus IDs; no renumeres artefactos ajenos.
- Marca una conclusión como `explícita` o `derivada`. Una derivación debe explicar su base y quedar pendiente de validación.
- Usa `TBD` y una pregunta cuando falten actor, disparador, datos, condición o resultado.
- No inventes actores, permisos, pantallas, botones, campos, bases de datos, transacciones técnicas, eventos, APIs, mensajes ni excepciones.
- Mantén separadas las alternativas contradictorias hasta obtener una decisión.

## Modo Modelo

1. Define el límite del producto y lo que queda fuera.
2. Identifica actores como **roles externos**, no personas concretas ni componentes internos. Categoriza solo con evidencia: persona, hardware o software; principal o secundario respecto de cada CU.
3. Identifica CU que entreguen un resultado de valor a un actor. Nómbralos con verbo en infinitivo y objeto.
4. Registra objetivo, RF de origen y evidencia.
5. Clasifica `esencial` o `soporte`, y `concreto` o `abstracto`, solo cuando pueda justificarse.
6. Estructura relaciones con estas semánticas:
   - `include`: comportamiento obligatorio reutilizado por el CU base;
   - `extend`: comportamiento opcional o condicionado que amplía un CU completo;
   - generalización: actor o CU especializado hereda comportamiento del general.
7. Genera un diagrama con actores, límite del sistema y relaciones UML. Usa una herramienta UML cuando se requiera fidelidad notacional; si solo hay Mermaid, rotúlalo como aproximación y declara sus pérdidas. Usa paquetes únicamente si mejoran un modelo grande o la fuente ya define agrupaciones.

Salida predeterminada:

```markdown
# Modelo de casos de uso — <sistema o TBD>
## Alcance y fuentes
## Actores
| ID | Rol | Categoría | Evidencia | Pendientes |
| --- | --- | --- | --- | --- |
## Casos de uso
| ID | Nombre | Objetivo | Actor principal / secundarios | Tipo | Trazas | Evidencia | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
## Relaciones
| Origen | Relación | Destino | Condición / justificación | Evidencia |
| --- | --- | --- | --- | --- |
## Diagrama UML
## Preguntas y control de cobertura
```

No agregues asociaciones actor–CU sin evidencia de participación.

## Modo Descripción

Describe cada CU seleccionado con la siguiente ficha institucional:

```markdown
### <ID> — <Nombre>
- Actor principal: <rol o TBD>
- Actores secundarios: <roles, ninguno identificado o TBD>
- Tipo: concreto/abstracto; esencial/soporte; <TBD donde corresponda>
- Objetivo: <resultado de valor>
- Precondiciones: <solo condiciones que deben ser verdaderas antes del inicio>
- Disparador: <hecho que inicia el CU o TBD>
- Trazabilidad: <RF/RNF/RN y evidencias>

#### Curso normal
| Paso | Responsable | Acción observable | Evidencia / origen | Estado |
| --- | --- | --- | --- | --- |

#### Cursos alternativos y de error
| ID | Desde paso / condición | Flujo | Reincorporación o término | Evidencia / origen | Estado |
| --- | --- | --- | --- | --- | --- |

#### Postcondiciones
- Éxito: ...
- Fracaso o cancelación: ...

#### Observaciones y TBD
```

Reglas:

- Identifica al responsable de cada paso numerado. Conserva el orden observado; son válidos pasos consecutivos del sistema o de actores secundarios.
- Describe qué ocurre y qué información interviene, sin navegación de pantalla ni mecanismo interno.
- Cita evidencia u origen derivado en disparador, precondiciones, pasos, alternativas y postcondiciones; no basta la traza general del CU cuando la fuente cambia por flujo.
- Una precondición no es el primer paso; una postcondición expresa el estado observable al terminar.
- Separa flujo normal, alternativas y errores; no fabriques cobertura exhaustiva.
- Un prototipo o documentación complementaria es opcional y se referencia, no se genera por defecto.

## Criterio de término

- Cada actor, CU, relación y paso tiene evidencia o está marcado como derivado/TBD.
- El conjunto cubre los RF en alcance o declara cuáles siguen sin CU.
- `include`, `extend` y generalización respetan su semántica.
- Las descripciones separan condiciones, cursos y resultados.
- No aparecen decisiones de UI, persistencia o arquitectura no presentes en las fuentes.
- Se entregó un solo nivel de producto, salvo que el usuario pidiera más.
