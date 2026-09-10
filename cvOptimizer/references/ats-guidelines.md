# Directrices Canónicas de Optimización ATS (Applicant Tracking Systems)

Los sistemas ATS (Workday, Greenhouse, Taleo, Lever, SAP SuccessFactors, BambooHR) procesan miles de currículums convirtiendo el archivo PDF en un flujo lineal de texto plano estructurado mediante técnicas de Optical Character Recognition (OCR) y parsing semántico de entidades (NER).

Para garantizar un índice de lectura del 100% y un ranking superior en el filtrado algorítmico, `cvOptimizer` aplica rigurosamente las siguientes directivas:

---

## 1. Topología y Maquetación

| Criterio | Práctica Permitida (100% ATS-Safe) | Práctica Prohibida (Riesgo Crítico de Fallo ATS) |
|---|---|---|
| **Disposición de Columnas** | **Lectura Lineal de 1 Columna.** El flujo de arriba hacia abajo asegura orden cronológico y semántico continuo. | **Columnas dobles en el cuerpo de experiencia.** Los parsers leen horizontalmente a través de las columnas, mezclando empresas, fechas y tareas en un párrafo incomprensible. |
| **Tablas y Minipages** | Permitidas únicamente en el encabezado de contacto o sin anidamiento profundo. | Tablas anidadas para alinear viñetas de experiencia o bloques de habilidades con bordes invisibles. |
| **Cuadros de Texto (Text Boxes)** | Prohibidos en LaTeX y Word. | Elementos flotantes que los parsers ignoran por completo al extraer texto en capas de fondo. |
| **Encabezados y Pies de Página** | Toda la información crítica debe residir en el cuerpo principal (`body`). | Colocar email, teléfono o enlaces en el `\fancyfoot` o `\fancyhead` (la mayoría de parsers los descartan para no duplicar datos). |
| **Longitud** | **1 Página A4 estricta** para perfiles junior/semi-senior/senior (<10 años); **2 Páginas** para perfiles ejecutivos C-Level o investigación académica con publicaciones. | Dejar desbordes de 3-5 líneas en una segunda página en blanco. |

---

## 2. Tipografía y Codificación

1. **Codificación UTF-8 Universal:** Todo carácter diacrítico (tildes, eñes, diéresis) debe compilarse limpiamente (`\usepackage[utf8]{inputenc}` y `\usepackage[T1]{fontenc}`) para que el texto sea seleccionable y copiable como texto plano.
2. **Tipografías Estándar Vectoriales:**
   - *Roboto* (neutral, moderna, de alta legibilidad en pantallas y parsers).
   - *Source Sans Pro* (geométrica, limpia).
   - *Computer Modern / Latin Modern* (clásica académica).
3. **Seleccionabilidad:** Si abres el PDF generado y no puedes seleccionar o buscar con `Ctrl+F` las palabras "Desarrollo" o "Ingeniería", el ATS lo descartará como imagen rasterizada vacía.

---

## 3. Nomenclatura Estándar de Secciones

Los algoritmos de indexación buscan cabeceras estándar reconocibles por sus clasificadores de NLP:

- **Español:**
  - `Experiencia Profesional` o `Experiencia Laboral`
  - `Educación` o `Educación y Formación`
  - `Habilidades` o `Habilidades Técnicas`
  - `Certificaciones` o `Cursos y Certificaciones`
  - `Proyectos` o `Proyectos Destacados`
  - `Idiomas`
- **Inglés:**
  - `Work Experience` o `Professional Experience`
  - `Education`
  - `Technical Skills` o `Skills & Competencies`
  - `Certifications & Training`
  - `Projects`
  - `Languages`

*Evitar títulos creativos o metafóricos como "Mi Travesía", "¿Qué me apasiona?" o "Caja de Herramientas", ya que los parsers no los mapean a categorías estándar.*

---

## 4. Estructura de Fechas y Entradas de Empleo

Formato estricto para cada entrada:
```text
[Nombre del Puesto] | [Nombre de la Empresa o Institución]
[Mes/Año Inicio] -- [Mes/Año Fin o "Actualidad" / "Present"] | [Ciudad, País]
```
Ejemplo óptimo:
`Analista Programador | UEPC`
`11/2023 -- Actualidad | Córdoba, Argentina`

---

## 5. Formato de Viñetas y Densidad de Palabras Clave

1. Cada viñeta debe comenzar con un **Verbo de Acción Directo** en pasado (o presente para el rol actual): *Desarrolló, Implementó, Automatizó, Coordinó, Diseñó, Optimizó*.
2. **Densidad de Palabras Clave (Keywords):** El ATS calcula la concordancia léxica contra la descripción del puesto (Job Description). Se deben incluir los términos tecnológicos exactos (*Oracle SQL*, *APIs REST*, *Docker*, *Gantt*, *EVM*) en su forma canónica de la industria.
