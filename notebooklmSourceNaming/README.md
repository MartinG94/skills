# notebooklmSourceNaming

Skill de taxonomía y estandarización de nomenclatura para clasificar y renombrar archivos académicos antes de su carga en Google NotebookLM.

---

## 1. Propósito General

`notebooklmSourceNaming` estandariza los nombres de archivos de estudio y fuentes bibliográficas utilizando una taxonomía estricta de prefijos (`PLN_`, `LIB_`, `NOR_`, `SLI_`, `APU_`, `GUI_`, `VID_`, `CAS_`, `TP_`, `NOT_`). Garantiza que el panel de fuentes de NotebookLM y las citas al pie sean inmediatamente identificables por tipo y jerarquía temática.

### Capacidades Principales:
- **Taxonomía Estandarizada:** Asigna prefijos unificados por tipo de material académico.
- **Formato Determinista:** Elimina caracteres especiales y espacios, aplicando sintaxis `[PREFIJO]_[Materia/Tema]_[Detalle]_[Año].[ext]`.
- **Organización de Lotes:** Procesa directorios de archivos y genera comandos de renombrado seguros.

---

## 2. Arquitectura Interna

```
notebooklmSourceNaming/
├── SKILL.md                                # Contrato operacional del agente
└── README.md                               # Documentación técnica de la skill
```

---

## 3. Prerequisitos de Entorno

- No requiere software externo.

---

## 4. Ejemplos de Invocación y Uso

### Renombrado de Diapositivas de Clase
```
Entrada: "presentacion_u2_clase3_procesos.pdf"
Salida:  "SLI_U2_C03_Gestion_Procesos.pdf"
```

### Renombrado de Libro de Cátedra
```
Entrada: "Gestion de Procesos Bravo Carrasco 6ta ed.pdf"
Salida:  "LIB_BravoCarrasco_Gestion_Procesos_6taEd.pdf"
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Archivos o listados de documentos académicos sin clasificar.
- Metadatos de asignatura, unidad didáctica o autor.

### Salidas (Outputs)
- Lista de nombres de archivo normalizados bajo la taxonomía estándar.
- Scripts de PowerShell / Bash para renombrado masivo seguro.
