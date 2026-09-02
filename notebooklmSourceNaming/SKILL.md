---
name: notebooklmSourceNaming
description: >-
  Aplica la convención de nomenclatura y taxonomía estandarizada para clasificar y renombrar archivos
  académicos y fuentes antes de cargarlos en Google NotebookLM. Úsalo cada vez que el usuario pida renombrar,
  organizar o preparar archivos o fuentes para NotebookLM.
---

# Estandarización y Nomenclatura de Fuentes para NotebookLM

Esta skill define la taxonomía de prefijos y reglas de nombrado para organizar documentos de estudio y fuentes antes de ser subidos a NotebookLM, garantizando claridad en las citas automáticas y en el panel de fuentes.

## 1. Prefijos y Taxonomía

Cada archivo debe iniciar con un prefijo de 3 a 4 letras en mayúsculas seguido de un guion bajo (`_`):

- **`PLN_` (Planificación)**: Programas de estudio, cronogramas de clases, syllabus y condiciones de cursada/aprobación.
  * *Ejemplo*: `PLN_Programa_Diseno_Sistemas_2026.pdf`
- **`LIB_` (Libros de Referencia)**: Bibliografía completa y libros de texto de referencia (ej. Bravo Carrasco, Chang, Nudel).
  * *Ejemplo*: `LIB_BravoCarrasco_Gestion_Procesos.pdf`, `LIB_Chang_Sistemas_Informacion.pdf`
- **`NOR_` (Normas y Estándares)**: Normas oficiales, estándares internacionales y especificaciones técnicas (ej. BPMN 2.0, ISO 9001, ISO 27001).
  * *Ejemplo*: `NOR_BPMN_2_0_OMG_Spec.pdf`, `NOR_ISO_9001_2015_Requisitos.pdf`
- **`SLI_` (Diapositivas de Clase)**: Presentaciones y slides de cátedra, categorizadas por número de unidad y número de clase.
  * *Estructura*: `SLI_U[Unidad]_C[Clase]_[Tema].[ext]`
  * *Ejemplo*: `SLI_U1_C01_Introduccion_Sistemas.pdf`, `SLI_U3_C05_Modelado_BPMN.pdf`
- **`APU_` (Apuntes Teóricos)**: Apuntes teóricos, notas de cátedra, resúmenes y síntesis conceptuales.
  * *Ejemplo*: `APU_Teoria_General_Sistemas.pdf`
- **`GUI_` (Guías y Metodologías)**: Guías metodológicas, guías de relevamiento, enunciados de ejercicios prácticos y cuestionarios.
  * *Ejemplo*: `GUI_Relevamiento_Procesos_Negocio.pdf`, `GUI_TP_Modelado_Deducciones.pdf`
- **`VID_` (Videos y Multimedia)**: Grabaciones de clases sincrónicas, videos explicativos, audios o transcripciones multimedia.
  * *Ejemplo*: `VID_Clase_Grabada_2026_08_15_BPMN.mp4`
- **`TPI_` (Trabajo Práctico Integrador)**: Documentación del Trabajo Práctico Integrador (Caso BioTrace Logística, investigación de dominio, matrices de trazabilidad, diagramas, informes).
  * *Ejemplo*: `TPI_BioTrace_Logistica_Enunciado_Caso.pdf`, `TPI_Matriz_Trazabilidad_Requerimientos.xlsx`

## 2. Reglas de Estilizado y Convención

1. **Estructura General**: `[PREFIJO]_[DescriptorClaro].[extension]`
2. **Formato del Descriptor**:
   - Usar `CamelCase` o palabras separadas por guion bajo (`_`).
   - Evitar caracteres especiales, símbolos o tildes en los nombres de archivo para máxima compatibilidad con sistemas de archivos y herramientas.
   - Mantener nombres concisos pero informativos (máx. 40-50 caracteres de descriptor).
3. **Diapositivas con Unidad y Clase**:
   - Respetar siempre `U[X]_C[Y]` con números de 2 dígitos cuando corresponda (`U1_C01`, `U2_C10`).

## 3. Procedimiento para Renombrado

Cuando el usuario solicite renombrar archivos:
1. **Analizar los archivos**: Examinar el contenido y/o nombre original para inferir su categoría.
2. **Asignar prefijo**: Seleccionar el prefijo más adecuado de la taxonomía.
3. **Proponer / Confirmar**: Presentar una tabla comparativa con `Nombre Original` -> `Nuevo Nombre`.
4. **Ejecutar**: Una vez confirmado por el usuario, realizar el renombramiento de forma segura.
