# notebooklm

Skill de integración con el servidor MCP de NotebookLM para autenticación, gestión de cuadernos, consultas fundamentadas (*grounded Q&A*) con citas y carga de fuentes.

---

## 1. Propósito General

`notebooklm` permite interactuar con Google NotebookLM mediante automatización de navegador en un perfil local aislado. Facilita formular preguntas fundamentadas con citas verificables, registrar cuadernos compartidos en la biblioteca local y añadir fuentes de texto o URLs.

### Capacidades Principales:
- **Diagnóstico y Autenticación:** Verifica el estado de sesión local (`get_health`) e inicia flujos de autenticación segura en Chrome (`setup_auth`).
- **Biblioteca de Cuadernos:** Registra, selecciona y lista cuadernos compartidos por URL y metadatos.
- **Consultas con Citas Fundamentadas:** Ejecuta preguntas a fuentes (`ask_question`) preservando referencias textuales y orígenes sin inventar citas.
- **Carga de Fuentes:** Incorpora fuentes web y documentos textuales a cuadernos existentes con confirmación previa.

---

## 2. Arquitectura Interna

```
notebooklm/
├── SKILL.md                                # Contrato operacional del agente
└── README.md                               # Documentación técnica de la skill
```

---

## 3. Prerequisitos de Entorno

- Servidor MCP `notebooklm-mcp` configurado en `mcp_config.json`.
- Google Chrome instalado con perfil persistente en `%LOCALAPPDATA%\notebooklm-mcp\Data\chrome_profile`.

---

## 4. Ejemplos de Invocación y Uso

### Consulta a Cuaderno de Estudio
```markdown
Acción: ask_question
Parámetros: question="¿Cuáles son los principios de la Lógica Dominante del Servicio según Vargo y Lusch?", source_format="footnotes"
Resultado: Respuesta fundamentada con notas al pie y lista de fuentes citadas.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- URLs compartidas de cuadernos de Google NotebookLM.
- Preguntas sobre los documentos indexados en el cuaderno.
- URLs o textos fuente para anexar al cuaderno.

### Salidas (Outputs)
- Respuestas fundamentadas en los documentos con referencias exactas y citas.
- Identificadores de sesión (`session_id`) para seguimiento conversacional.
