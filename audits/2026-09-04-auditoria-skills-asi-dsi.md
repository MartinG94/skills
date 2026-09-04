# Registro de auditoría de skills de ASI y DSI

- **Fecha:** 2026-09-04
- **Repositorio:** `D:\Proyectos\skills`
- **Rama de trabajo:** `refactor/professionalize-skills`
- **Fuente académica primaria:** `D:\Proyectos\skills-vault`
- **Estado:** completada

## Propósito del registro

Este archivo conserva el prompt que originó la auditoría integral de las skills
relacionadas directa o indirectamente con Análisis de Sistemas y Diseño de Sistemas.
El texto se mantiene íntegro para permitir revisar el alcance, las restricciones y los
criterios de aceptación usados durante los cambios.

## Prompt original

````text
Quiero que realices una auditoría y mejora integral de las skills relacionadas con las materias **Análisis de Sistemas** y **Diseño de Sistemas**.

## Ubicaciones

Repositorio de skills:

```text
D:\Proyectos\skills
```

Material académico de referencia:

```text
D:\Proyectos\skills-vault
```

En `skills-vault` hay material real de ambas materias, incluyendo archivos `.zip`. Ese contenido debe ser considerado la **fuente de conocimiento principal** para validar y mejorar las skills.

---

# Objetivo

Identificar dentro de `D:\Proyectos\skills` todas las skills que estén directa o indirectamente relacionadas con:

* Análisis de Sistemas
* Diseño de Sistemas
* Ingeniería de requisitos
* Relevamiento
* Modelado de sistemas
* Casos de uso
* Historias de usuario
* Especificación funcional
* UML
* Análisis orientado a objetos
* Diseño orientado a objetos
* Arquitectura de software
* Patrones de diseño
* Modelado conceptual
* Diseño de componentes
* Responsabilidades y colaboraciones
* Diagramas utilizados en estas materias
* Cualquier otra temática cubierta por el material académico disponible

No te limites a buscar skills cuyo nombre coincida literalmente con estos conceptos. Analizá también su propósito, contenido y producto generado.

---

# Fuente de verdad

Antes de modificar una skill, inspeccioná el contenido correspondiente dentro de:

```text
D:\Proyectos\skills-vault
```

Los `.zip` deben ser abiertos y analizados.

No asumas conceptos académicos únicamente por conocimiento general si existe material de la materia que permita validarlos.

La mejora debe basarse prioritariamente en:

1. Material real de la materia.
2. Consistencia entre los diferentes documentos disponibles.
3. Buenas prácticas de creación de skills para agentes de IA.
4. Calidad del producto final generado por la skill.

Si detectás diferencias entre conocimiento general y el enfoque utilizado en la materia, priorizá el enfoque de los documentos académicos cuando corresponda.

---

# Proceso de trabajo

## 1. Descubrimiento

Recorré:

```text
D:\Proyectos\skills
```

e identificá todas las skills potencialmente relacionadas con Análisis de Sistemas o Diseño de Sistemas.

Para cada candidata determiná:

* nombre;
* propósito;
* materia o temática relacionada;
* entradas esperadas;
* proceso que ejecuta;
* producto entregado;
* problemas actuales;
* potencial de mejora.

No modifiques todavía las skills durante esta primera etapa.

---

## 2. Análisis del material académico

Recorré:

```text
D:\Proyectos\skills-vault
```

Identificá qué archivos corresponden a:

* Análisis de Sistemas;
* Diseño de Sistemas.

Inspeccioná también los `.zip` y su estructura interna.

Extraé únicamente el conocimiento que resulte útil para mejorar las skills existentes.

No generes grandes resúmenes académicos innecesarios.

El objetivo del material de referencia es **mejorar las skills**, no crear apuntes de estudio.

---

## 3. Auditoría individual

Para cada skill identificada, evaluá como mínimo estas dimensiones:

### A. Calidad del producto generado

Analizá si la skill conduce a un resultado:

* correcto;
* completo;
* profesional;
* accionable;
* reutilizable;
* consistente;
* verificable;
* alineado con la materia.

Priorizá siempre la calidad del producto final por encima de agregar instrucciones innecesarias.

---

### B. Precisión académica

Verificá que:

* utilice correctamente los conceptos;
* respete terminología de la materia;
* no mezcle etapas o artefactos incorrectamente;
* genere los diagramas/documentos esperados;
* diferencie correctamente análisis de diseño cuando corresponda;
* no invente elementos que deberían provenir del problema analizado.

---

### C. Eficiencia

Detectá:

* instrucciones redundantes;
* pasos que puedan consolidarse;
* verificaciones repetidas;
* procesos innecesariamente largos;
* contenido que el agente podría inferir de forma segura;
* operaciones que no aporten valor al producto final.

Simplificá el flujo sin perder precisión.

---

### D. Consumo de tokens

Optimizar especialmente:

* longitud de instrucciones;
* repetición de reglas;
* contexto cargado innecesariamente;
* pedidos de análisis exhaustivos que no impacten el resultado;
* generación de texto intermedio que luego no se utiliza;
* lectura indiscriminada de archivos;
* repetición de información entre etapas.

Aplicá el principio:

> Utilizar la menor cantidad de contexto e instrucciones posible que permita mantener o mejorar la calidad del resultado.

No sacrifiques calidad académica únicamente para reducir tokens.

---

### E. Claridad para el agente

La skill debe dejar claro:

* cuándo debe utilizarse;
* cuándo no debe utilizarse;
* qué información necesita;
* qué debe inferir;
* qué no debe inventar;
* qué pasos son obligatorios;
* cuáles son condicionales;
* qué producto debe entregar.

Evitá instrucciones ambiguas.

---

### F. Robustez

La skill debe manejar razonablemente:

* información incompleta;
* requisitos ambiguos;
* documentos parcialmente inconsistentes;
* ausencia de algún artefacto;
* sistemas pequeños o grandes;
* diferentes niveles de detalle en el input.

No agregues manejo de excepciones extremadamente improbable si aumenta mucho el tamaño de la skill.

---

### G. Modularidad

Evaluá si la skill intenta hacer demasiadas cosas.

Cuando corresponda:

* separá responsabilidades conceptualmente;
* reutilizá otras skills existentes;
* evitá duplicar instrucciones que ya pertenezcan claramente a otra skill.

Pero no fragmentes innecesariamente una skill si eso empeora la experiencia de uso.

---

### H. Determinismo y consistencia

Siempre que sea posible, una misma entrada debería conducir a productos estructuralmente similares.

Definí:

* estructura de salida;
* secciones obligatorias;
* criterios de completitud;
* reglas para elementos opcionales.

---

### I. Relación costo / valor

Cada instrucción debe justificar su existencia.

Considerá especialmente:

```text
valor aportado al resultado / tokens + complejidad introducida
```

Eliminá instrucciones cuyo aporte marginal sea muy bajo.

---

# 4. Mejora

Después de completar la auditoría de una skill, modificála directamente cuando la mejora esté justificada.

Podés:

* reescribir instrucciones;
* reorganizar el workflow;
* eliminar redundancias;
* agregar validaciones;
* mejorar criterios de entrada y salida;
* incorporar conceptos faltantes;
* corregir conceptos académicos;
* mejorar templates;
* mejorar ejemplos;
* agregar o eliminar pasos;
* mejorar criterios de calidad;
* reducir consumo de contexto;
* hacer que la skill entregue un producto más útil.

No hagas cambios cosméticos sin impacto real.

---

# Principio fundamental

No optimices las skills únicamente para que sean más cortas.

Busco optimizar simultáneamente:

```text
Calidad del producto
+ Precisión
+ Utilidad práctica
+ Eficiencia
+ Robustez
+ Consistencia
+ Mantenibilidad
- Tokens innecesarios
- Redundancia
- Complejidad accidental
```

La mejor skill no es necesariamente la más pequeña, sino la que obtiene **el mejor resultado con la menor complejidad y contexto razonables**.

---

# Producto esperado de las skills

Prestá especial atención al artefacto que produce cada skill.

Por ejemplo, dependiendo de su responsabilidad, una skill relacionada con estas materias podría producir:

* especificación de requisitos;
* listado estructurado de requisitos funcionales y no funcionales;
* modelo de dominio;
* casos de uso;
* especificaciones de casos de uso;
* diagramas UML;
* diagramas de clases;
* diagramas de secuencia;
* diagramas de estados;
* análisis de responsabilidades;
* arquitectura;
* diseño de componentes;
* documentación de decisiones;
* trazabilidad entre requisitos, análisis y diseño.

No fuerces estos productos en todas las skills.

Cada skill debe producir únicamente los artefactos correspondientes a su propósito.

---

# Uso de ejemplos

Si una skill contiene ejemplos:

* mantenelos breves;
* elegí ejemplos que enseñen estructura o comportamiento;
* evitá ejemplos largos que consuman contexto;
* no dupliques mediante ejemplos reglas que ya quedaron perfectamente claras;
* preferí un ejemplo representativo sobre varios ejemplos similares.

---

# Uso del material del vault

No copies grandes fragmentos de los documentos académicos dentro de las skills.

Transformá ese conocimiento en:

* reglas;
* criterios;
* heurísticas;
* estructuras;
* workflows;
* validaciones.

La skill debe contener el **conocimiento operativo necesario**, no convertirse en una copia de los apuntes.

---

# Relaciones entre skills

Durante la auditoría también detectá:

* skills duplicadas;
* skills parcialmente solapadas;
* contradicciones;
* oportunidades de reutilización;
* dependencias útiles;
* responsabilidades mal distribuidas.

Si encontrás una oportunidad clara de consolidación o separación, aplicala sólo cuando mejore objetivamente el sistema de skills.

No elimines una skill sin verificar primero que su funcionalidad quede cubierta.

---

# Restricciones

No modificar skills que no tengan relación razonable con Análisis de Sistemas o Diseño de Sistemas.

No agregar teoría académica que no tenga impacto operativo.

No inflar las skills con explicaciones para humanos si la información está destinada principalmente al agente.

No agregar pasos ceremoniales.

No introducir dependencias entre skills sin una ventaja clara.

No cambiar el objetivo funcional de una skill salvo que esté conceptualmente incorrecto.

No inventar contenido que no pueda justificarse con:

* material académico;
* contexto de la skill;
* buenas prácticas ampliamente aceptadas.

---

# Validación posterior

Después de modificar cada skill, realizá una segunda revisión preguntándote:

1. ¿El producto generado sería mejor que antes?
2. ¿Es académicamente más preciso?
3. ¿La skill tiene instrucciones innecesarias?
4. ¿Puede producir el mismo resultado usando menos contexto?
5. ¿Hay pasos redundantes?
6. ¿El agente sabe claramente cuándo terminar?
7. ¿La estructura de salida está suficientemente definida?
8. ¿La skill inventaría información ante datos faltantes?
9. ¿Hay reglas repetidas que puedan consolidarse?
10. ¿Se incorporó correctamente el conocimiento relevante del vault?
11. ¿La skill sigue teniendo una responsabilidad clara?
12. ¿La modificación realmente aporta valor?

Si una modificación no supera esta revisión, reconsiderala.

---

# Informe final

Al finalizar, generá un informe breve con:

## Skills analizadas

Listado de las skills relacionadas detectadas.

## Skills modificadas

Para cada una indicá:

```text
Skill:
Materia/área:
Problema principal:
Cambios realizados:
Mejora esperada del producto:
Mejora de eficiencia/tokens:
```

## Skills no modificadas

Indicá brevemente aquellas que fueron analizadas pero no requerían cambios importantes.

## Hallazgos transversales

Sólo si existen:

* duplicaciones;
* contradicciones;
* oportunidades de modularización;
* falta de alguna skill importante;
* problemas comunes de diseño.

---

# Criterio de éxito

Considerá finalizado el trabajo únicamente cuando las skills relevantes hayan quedado:

* respaldadas por el material académico real;
* orientadas a producir artefactos de alta calidad;
* más claras;
* más precisas;
* más eficientes;
* menos redundantes;
* más consistentes;
* más fáciles de mantener;
* optimizadas en consumo de tokens sin degradar resultados.

Priorizá **mejorar el sistema existente** sobre reescribir todo desde cero.
````

## Resultado de la ejecución

- Se evaluaron las 22 skills del repositorio.
- Se modificaron 19 skills relacionadas directa o indirectamente con ASI/DSI.
- `notebooklm`, `notebooklmSourceNaming` y `pnlOratoria` quedaron fuera de alcance y
  sin cambios.
- Se inspeccionaron los dos RAR del vault, sus tres ZIP internos, 38 PDF y dos
  plantillas DOCX; siete páginas representativas tuvieron además control visual.
- Los entrypoints de las 19 skills pasaron de 76.729 a 16.733 palabras sin mover teoría
  indiscriminada al contexto principal.
- Validación final: 19/19 paquetes válidos y 27/27 pruebas BPMN/requisitos aprobadas.
- Los artefactos temporales usados para inspeccionar el vault fueron eliminados.

Para el detalle operativo de rutas y responsabilidades resultantes, consultar
[la guía del repositorio](../GUIA.md).
