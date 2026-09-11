# cvOptimizer

Estudio integral para la ingeniería, modernización y optimización de Currículums Vitae (CV) en LaTeX orientados a superar filtros ATS (Applicant Tracking Systems), estructurados bajo la fórmula Google X-Y-Z y enriquecidos mediante una base de datos persistente e incremental (`profile_data.json`).

---

## 1. Propósito General

`cvOptimizer` automatiza el ciclo completo de preparación curricular técnica y ejecutiva:
1. **Memoria Viva Incremental:** Mantiene un único punto de verdad (`profile_data.json`) en la raíz del espacio de trabajo que acumula todo el historial laboral, proyectos, métricas, habilidades y certificaciones del usuario. Este archivo se enriquece de forma acumulativa e iterativa con cada entrevista y postulación.
2. **Alineación con la Empresa y Puesto:** Investiga la misión, visión y necesidades de la empresa convocante, ejecutando un análisis de brecha (Gap Analysis) para identificar fortalezas inmediatas y desenterrar habilidades omitidas sin inventar información.
3. **Fórmula Google X-Y-Z & Estilo Nominalizado (Humanizer):** Estructura cada logro demostrando impacto cuantificable mediante la fórmula Google X-Y-Z. En español, adopta el estilo sustantivado de acción (*"Relevamiento, análisis y formalización...", "Coordinación...", "Diseño y optimización..."*) para máxima elegancia y neutralidad ejecutiva, erradicando la monotonía de verbos en pretérito y clichés sintéticos de IA.
4. **Maquetación Modular LaTeX & ATS:** Estructura el código en módulos limpios (`main.tex`, `config.sty`, `sections/`), asegurando una topología lineal de 1 sola columna compatible con parsers (Workday, Greenhouse, Taleo, Lever, SAP SuccessFactors) y una paginación balanceada (1 a 2 páginas holgadas sin cortes accidentales ni sensación de saturación).
5. **Compilación Desatendida & Previsualización:** Compila localmente con `tectonic` o `pdflatex`, guardando el PDF final a la misma altura que la carpeta del proyecto (`<Apellido Nombre>CV_<Puesto>.pdf`) y generando una previsualización gráfica en PNG (`preview.png`) mediante `pymupdf`.
6. **Paquete de Postulación Multicanal:** Genera bloques de texto formateados y listos para copiar con un solo clic (correo formal para RRHH, mensaje de LinkedIn para el reclutador y elevator pitch de 3 líneas).

---

## 2. Arquitectura Interna de la Skill

```text
cvOptimizer/
├── SKILL.md                          # Contrato operacional consumido por el agente LLM
├── README.md                         # Documentación técnica y guía de uso para desarrolladores
├── scripts/
│   ├── build_cv.py                   # Compilación LaTeX, exportación del PDF y render PNG con PyMuPDF
│   └── update_profile.py             # Fusión incremental y deduplicada en profile_data.json
├── templates/
│   ├── profile_data_schema.json      # Esquema JSON Schema formal del perfil profesional
│   ├── profile_data_template.json    # Plantilla de perfil inicial en blanco
│   ├── awesome-cv/                   # Plantilla predeterminada modular (Executive Tech)
│   │   ├── config.sty                # Estilos, márgenes A4, paleta y switch de foto
│   │   ├── main.tex                  # Orquestador raíz del documento
│   │   └── sections/                 # Componentes desacoplados
│   │       ├── header.tex            # Encabezado, redes y foto
│   │       ├── summary.tex           # Perfil profesional
│   │       ├── experience.tex        # Experiencias con fórmula Google X-Y-Z
│   │       ├── education.tex         # Formación académica, títulos y subsección de capacitaciones
│   │       ├── skills.tex            # Habilidades duras, blandas y herramientas
│   │       ├── certifications.tex    # Módulo de certificaciones (utilizado de forma independiente o integrado en education)
│   │       ├── activities.tex        # Liderazgo social e institucional
│   │       └── projects.tex          # Módulo opcional de proyectos técnicos
│   ├── jake-resume/                  # Plantilla alternativa FAANG Minimalista (1 columna pura)
│   │   └── main.tex
│   └── moderncv-swiss/               # Plantilla alternativa Europea / Minimalista Suizo
│       └── main.tex
└── references/
    ├── ats-guidelines.md             # Normas técnicas para superar parsers ATS sin pérdidas
    ├── google-xyz-formula.md         # Catálogo de redacción y banco de verbos de acción
    ├── humanizer-cv-rules.md         # Pautas anti-IA para CVs y resúmenes profesionales
    └── outreach-templates.md         # Modelos de correos, mensajes LinkedIn y elevator pitch
```

---

## 3. Prerequisitos de Entorno y Protocolo de Auto-Instalación

- **Python:** Python 3.8 o superior.
- **PyMuPDF (`pymupdf`):** Utilizado para renderizar la primera página del PDF en `preview.png`.
  - *Protocolo de auto-instalación:* El script `build_cv.py` detecta si la librería está presente; si no lo está, la instala automáticamente ejecutando `pip install pymupdf --quiet`.
- **Compilador TeX:**
  - **Tectonic (Recomendado):** Compilador TeX moderno y autónomo que descarga paquetes al vuelo.
    - *Instalación:* `winget install Tectonic.Tectonic` (en Windows) o `cargo install tectonic`.
  - **pdfLaTeX:** Disponible a través de distribuciones tradicionales como MiKTeX o TeX Live (`pdflatex`).

---

## 4. Ejemplos de Invocación y Uso

### 4.1 Compilación y Renderizado desde Terminal
```bash
python C:\Users\Diego\.gemini\config\skills\cvOptimizer\scripts\build_cv.py \
  --project-dir "g:\My Drive\CV\latex" \
  --candidate-name "Diego Sanchez" \
  --target-role "Analista_IT" \
  --company "Pertrak"
```
**Salida esperada:**
```text
[INFO] Compilando con tectonic (C:\Users\Diego\.local\bin\tectonic.exe)...
[EXITO] PDF exportado a: g:\My Drive\CV\Diego_Sanchez_CV_Analista_IT_Pertrak.pdf
[EXITO] Previsualización renderizada en: g:\My Drive\CV\latex\preview.png
```

### 4.2 Actualización Incremental de `profile_data.json`
```bash
python C:\Users\Diego\.gemini\config\skills\cvOptimizer\scripts\update_profile.py \
  --profile "g:\My Drive\CV\profile_data.json" \
  --add-skill-hard "Docker" "Kubernetes" \
  --target-role "DevOps Engineer"
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- **Perfil base:** `profile_data.json` existente o archivo de CV previo (`.pdf`, `.docx`, `.md`).
- **Objetivo laboral:** Puesto o convocatoria (Job Description) y nombre de la empresa/institución.
- **Preferencias del usuario:** Inclusión de foto (`\showphototrue`/`\showphotofalse`), idioma (Español o Inglés) y estilo de plantilla.

### Salidas (Outputs)
1. **Archivo de Datos Actualizado:** `profile_data.json` en la raíz del espacio de trabajo con las nuevas habilidades y experiencias registradas.
2. **Carpeta de Proyecto LaTeX:** Subcarpeta `cv_<Rol>/` o `cv_<Rol>_<Empresa>/` con el código fuente desacoplado.
3. **Documento PDF Final:** Guardado a la misma altura que la carpeta del proyecto con el nombre canónico:
   `<Apellido Nombre>CV_<Puesto>.pdf` (o `<Apellido Nombre>CV_<Puesto>_<Empresa>.pdf`).
4. **Vista Previa Gráfica:** `preview.png` en alta resolución (200-300 DPI).
5. **Paquete de Postulación en Chat:** Cuadros de texto copiables con correo para RRHH, mensaje de LinkedIn y elevator pitch.
