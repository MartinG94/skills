# Humanizer: Desintoxicación y Refinamiento de Salidas de IA

Skill modular diseñada para detectar, auditar y erradicar los marcadores estadísticos y estilísticos propios de los modelos de lenguaje (LLM). Dota a la prosa de voz humana genuina, variación de ritmo (*burstiness*), perplejidad y especificidad factual, adaptando el tono a contextos conversacionales, técnicos o académicos.

---

## Propósito y Filosofía

Evitar los patrones algorítmicos típicos es solo la mitad del trabajo. La redacción esterilizada, plana y desprovista de voz es tan delatadora como el texto sintético sin editar. 

`humanizer` transforma la salida artificial restaurando:
- **Cadencia rítmica viva (*burstiness*)**: Alternancia dinámica entre oraciones cortas (5–10 palabras), medianas (12–20 palabras) y compuestas (25–35 palabras).
- **Especificidad empírica**: Sustitución de generalidades abstractas por datos concretos, mecanismos causales y nombres precisos.
- **Voz y postura**: Eliminación de la complacencia de chatbot, los descargos defensivos y la neutralidad estéril.
- **Fidelidad semántica**: Preservación del 100% del significado original, rigor técnico y argumentos de fondo sin inventar información.

---

## Arquitectura de la Skill

```
humanizer/
├── SKILL.md                          # Contrato operativo e instrucciones canónicas para el agente
├── README.md                         # Documentación general orientada al usuario y desarrollador
├── scripts/                          # Herramientas analíticas en Python estándar (sin dependencias externas)
│   ├── ai_detector.py                # Detector de patrones de IA, cálculo de burstiness y reporte JSON
│   ├── text_analyzer.py              # Análisis métrico de longitud, oraciones y legibilidad Flesch
│   ├── check_upstream.py             # Verificador y sincronizador contra fuentes upstream en GitHub
│   └── test_humanizer.py             # Suite de pruebas unitarias y de regresión automatizada
├── references/                       # Pautas especializadas y guías de estilo canónicas
│   ├── signs-of-ai-writing.md        # Catálogo detallado de los 24 patrones típicos de IA
│   ├── intensity-matrix.md           # Criterios para seleccionar intensidad (light, medium, aggressive)
│   ├── technical-documentation.md    # Estándares para software, APIs, PRDs y READMEs
│   └── academic-scholarly.md         # Pautas de perplejidad, hedging y tono científico
└── examples/                         # Muestras y casos de estudio reales
    ├── before_after_catalog.md       # Catálogo comparativo antes vs. después por dominio
    └── sample_texts/                 # Textos de prueba para validación y benchmarking
```

---

## Modos de Operación

| Modo | Caso de Uso | Enfoque de Estilo | Referencia Clave |
|---|---|---|---|
| **1. General / Conversacional** | Chats, correos, posts, divulgación, artículos. | Admite primera persona, opiniones claras, incertidumbre genuina y variedad de tono. | [`references/intensity-matrix.md`](references/intensity-matrix.md) |
| **2. Documentación Técnica** | READMEs, contratos de API, especificaciones, notas de release. | Voz activa, modo imperativo, eliminación de adjetivos inflados (*seamless*, *robusto*), exactitud verificable. | [`references/technical-documentation.md`](references/technical-documentation.md) |
| **3. Académico / Científico** | Papers, abstracts, ensayos, revisiones bibliográficas. | Alta perplejidad y *burstiness*, eliminación de andamiaje abstracto, rigor disciplinar y *hedging* preciso. | [`references/academic-scholarly.md`](references/academic-scholarly.md) |
| **4. Diagnóstico / Auditoría** | Análisis métrico y cuantitativo previo. | Inspección sin reescritura obligatoria para evaluar varianza, TTR y densidad de clichés. | [`scripts/ai_detector.py`](scripts/ai_detector.py) |

---

## Niveles de Intensidad

- **`light` (Cosmético)**: Elimina clichés flagrantes (*delve*, *pivotal*, *testament*, *tapestry*), poda muletillas de chatbot y remueve emojis decorativos manteniendo la sintaxis original.
- **`medium` (Predeterminado)**: Reestructuración de oraciones monótonas, corte de conectores mecánicos (*moreover*, *furthermore*, *cabe destacar que*) y remoción de andamiaje abstracto.
- **`aggressive` (Reescritura de Autor)**: Reformulación profunda, reordenamiento de argumentos, inyección de personalidad, ritmo asimétrico y postura de autor explícita.

---

## Guía de Scripts y Prerrequisitos

Todos los scripts están desarrollados en **Python 3.8+ estándar** sin dependencias externas.

### 1. Detector de Señales de IA (`ai_detector.py`)
Escanea texto plano o Markdown ignorando bloques de código y tablas. Identifica los 24 patrones algorítmicos con límites de palabra (`\b`), calcula varianza de oraciones y computa un índice de artificialidad (0 a 100):

```bash
# Diagnóstico estándar en consola
python scripts/ai_detector.py borrador.md

# Salida estructurada JSON para pipelines o herramientas
python scripts/ai_detector.py borrador.md --json
```

### 2. Analizador de Métricas de Texto (`text_analyzer.py`)
Mide longitud de palabras, distribución de frases, índice de legibilidad Flesch bilingüe y genera comparativas cuantitativas antes/después:

```bash
# Comparación cuantitativa entre borrador original y versión pulida
python scripts/text_analyzer.py original.txt revisado.txt --compare
```

### 3. Suite de Regresión (`test_humanizer.py`)
Ejecuta la batería de pruebas para comprobar que los detectores no generen falsos positivos en citas, código o abreviaturas:

```bash
python scripts/test_humanizer.py
```

### 4. Sincronizador de Fuentes Upstream (`check_upstream.py`)
Monitorea las fuentes upstream (`skills-lock.json`), compara commits remotos en GitHub y sincroniza la caché local:

```bash
# Verificación remota contra repositorios oficiales
python scripts/check_upstream.py

# Verificación en modo local/desconectado
python scripts/check_upstream.py --offline

# Actualizar lockfile y descargar versiones upstream a caché local
python scripts/check_upstream.py --update-lock --sync-cache
```

---

## Los 24 Patrones de Detección

1. **Inflación de Trascendencia**: Proclamar que hechos mundanos son un "hito crucial" o "testimonio perdurable".
2. **Mención Forzada de Notoriedad**: Listar medios o redes solo para simular relevancia.
3. **Análisis Superficiales con Gerundios**: Cláusulas flotantes (*"fomentando...", "garantizando..."*) sin mecanismo explicativo.
4. **Lenguaje Promocional**: Adjetivos vacíos (*vibrante, rico tapiz, groundbreaking, nested*).
5. **Atribuciones Difusas**: Apelar a entidades abstractas (*"los expertos coinciden"*, *"estudios demuestran"*).
6. **Secciones de 'Desafíos' Predecibles**: El clásico *"A pesar de las dificultades... el panorama es brillante"*.
7. **Vocabulario Típico de IA**: *Delve, tapestry, pivotal, intricate, foster, ahondar, orquestar*.
8. **Evasión de Cópula**: Cambiar "es" o "tiene" por *"se erige como"*, *"sirve como"*, *"ostenta"*.
9. **Paralelismos Negativos**: Fórmulas retóricas vacías (*"No es solo X; es Y"*).
10. **Abuso de la Regla de Tres**: Agrupaciones forzadas de tres elementos o adjetivos.
11. **Ciclado de Sinónimos**: Rotar términos arbitrariamente por miedo algorítmico a repetir palabras clave.
12. **Falsos Rangos**: Comparaciones *"desde X hasta Y"* con variables inconmensurables.
13. **Saturación de Guiones Largos (—)**: Inserción mecánica de em dashes para simular énfasis.
14. **Abuso de Negritas**: Resaltar palabras clave en cada oración.
15. **Listas con Encabezados en Negrita y Dos Puntos**: Viñetas mecánicas en lugar de párrafos fluidos.
16. **Mayúsculas Iniciales en Títulos**: Title Case anglosajón forzado en español.
17. **Emojis Decorativos en Contextos Técnicos**: Iconos prescindibles (🚀, 💡, 🔍) en prosa seria.
18. **Comillas Curvas Fuera de Lugar**: Comillas tipográficas mezcladas con código o salidas de consola.
19. **Residuos de Chatbot**: Despedidas y saludos enlatados (*"¡Espero que esto te sea de utilidad!"*).
20. **Descargos Defensivos**: Aclaraciones superfluas sobre cortes de conocimiento o limitaciones del modelo.
21. **Adulación y Complacencia**: Elogiar la pregunta del usuario (*"¡Excelente pregunta! Absolutamente..."*).
22. **Frases de Relleno Infladas**: *"Con el objetivo de llevar a cabo"* en lugar de *"Para"*.
23. **Cautela Excesiva (*Over-Hedging*)**: Acumulación de condicionales temerosos.
24. **Conclusiones Genéricas Optimistas**: Cierres que prometen horizontes prometedores sin sustancia.

*Detalles, etiología y transformaciones en [`references/signs-of-ai-writing.md`](references/signs-of-ai-writing.md).*

---

## Compuertas de Calidad de Cierre

Toda salida procesada por `humanizer` debe validar cinco criterios antes de considerarse aprobada:

| Criterio | Validación |
|---|---|
| **Fidelidad Semántica** | Preservación total de conceptos, datos, citas y argumentos del autor original. |
| **Cadencia Viva** | Alternancia rítmica comprobable (ratio de varianza de longitud de oraciones > 0.35). |
| **Erradicación de Clichés** | Ausencia absoluta de vocabulario delator de LLM. |
| **Exactitud Fáctica** | No invención de parámetros, flags o datos ausentes en el contexto original. |
| **Registro Adecuado** | Tono ajustado a la audiencia objetivo sin rigidez ni exceso de coloquialismo. |
