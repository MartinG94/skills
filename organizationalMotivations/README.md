# organizationalMotivations

Habilidad de agente para la construcción, auditoría y validación de la **Matriz de Motivaciones de la Organización e Impulsores de Mejora**, correspondiente a la **Etapa 1 (Situación Actual)** de la metodología de **Gestión y Mejora de Procesos (GMP)**.

Implementa los requisitos académicos oficiales definidos en la `PlanillaMATRICES-TPI 2026` (Hoja *'Etapa 1 Situación actual'*, Matriz 3) y el **Mapa de Tendencias SDLI** (Sociedad de la Innovación) bajo el marco de **Lógica Dominante del Servicio (SDL)** de Vargo & Lusch.

---

## 1. Propósito y Valor Metodológico

En la Etapa 1 de GMP, antes de seleccionar qué proceso de negocio debe ser intervenido y mejorado, es indispensable comprender el contexto estratégico de la organización frente a las disrupciones globales del entorno y las demandas cambiantes del cliente.

Esta skill atómica permite:
1. **Analizar el Entorno Global y Sectorial:** Evalúa sistemáticamente las macrotendencias del sector a través de los **10 macro-sectores del Mapa de Tendencias SDLI** y las **3 dimensiones analíticas** (Sociedad-Cultura, Tecnología-Ciencia, Economía-Mercado).
2. **Aplicar la Lógica Dominante del Servicio (SDL):** Supera la visión tradicional de producto cerrado y bienes tangibles, interpretando las operaciones como plataformas colaborativas donde el valor se **co-crea activamente en el uso** (*Value-in-Use*).
3. **Mapear Necesidades del Cliente:** Identifica las expectativas emergentes de inmediatez, autogestión (DIY), omnicanalidad y sustentabilidad, contrastándolas con las fricciones del modelo operativo actual.
4. **Formular Impulsores de Rediseño (Drivers):** Proporciona la justificación causal y estratégica de por qué la organización debe transformar sus procesos, alimentando directamente el **Factor 2 ("Tendencias del Entorno y Mercado / SDL")** de la matriz de selección crítica (`seleccion_proceso.md`) y el cuadrante de **Oportunidades** del análisis FODA (`foda.md`).

---

## 2. Contrato de Entrada y Salida

### Entrada (Inputs)
- Descripción general de la organización, rubro, actividad principal, misión y visión.
- Objetivos estratégicos de la dirección (preferentemente formulados bajo criterios SMART).
- Evidencia o contexto de la industria y canales de atención actuales hacia el cliente.

### Salida Determinista (Output)
La skill genera y persiste obligatoriamente el entregable en el archivo canónico:
```text
motivaciones.md
```
Ubicado en la raíz del proyecto o en el directorio de trabajo del usuario.

---

## 3. Arquitectura de la Skill

```text
organizationalMotivations/
├── SKILL.md                          # Contrato operativo del agente (progressive disclosure)
├── README.md                         # Documentación para desarrolladores y usuarios
├── references/
│   └── sdli_trends_guide.md          # Taxonomía completa de los 10 macro-sectores y 3 dimensiones SDLI
├── templates/
│   └── motivations_template.md       # Plantilla Markdown estándar para motivaciones.md
├── examples/
│   └── motivaciones_ejemplo.md       # Caso canónico de cátedra validado (Universidad Privada)
├── scripts/
│   └── validate_motivations.py       # Validador determinista CLI en Python
└── tests/
    └── test_validate_motivations.py  # Suite de pruebas unitarias automatizadas
```

---

## 4. Los 10 Macro-Sectores del Mapa de Tendencias SDLI

| # | Macro-Sector | Sub-Tendencias Clave |
|---|---|---|
| 1 | **Conciencia Medio Ambiental** | Eco presión, Empresas limpias, Cadenas sostenibles, Movilidad consciente |
| 2 | **Post Capitalismo** | Desposesión (acceso > propiedad), Nuevos modelos socioeconómicos, Redes del futuro |
| 3 | **Digitalización** | Transformación digital, Nuevas profesiones digitales, Soluciones abiertas/APIs, Automatización |
| 4 | **Vida Datificada** | Todo predictivo, Trazabilidad de datos/IoT, Transhumanismo/Wearables, Bajo control |
| 5 | **Cultura de la Inmediatez** | Comercio ininterrumpido (24/7), Vida retransmitida (tracking en vivo), Última milla |
| 6 | **Nuevas Narrativas Digitales** | Realidades mezcladas (AR/VR/Digital Twins), Relaciones virtuales, Confianza digital, UX |
| 7 | **DIY (Do It Yourself)** | Autoliderazgo/Autogestión, Hiperpersonalización, Trabajo flexible |
| 8 | **Bienestar Integral** | Comunidad emocional, Seguridad sanitaria/Bioseguridad, Valores KM0, Balance de vida |
| 9 | **Inclusión** | Edad relativa (Silver Economy), Represéntame, Identidades líquidas, Democratización |
| 10 | **Slow Life** | Desconexión digital consciente, Menos es más (simplificación operativa), Intimidad renovada |

---

## 5. Validación Determinista (CLI)

Para auditar la conformidad metodológica de cualquier archivo `motivaciones.md`:

```bash
# Validación estándar por consola
python "skills/organizationalMotivations/scripts/validate_motivations.py" "ruta/hacia/motivaciones.md"

# Validación estructurada en JSON (para orquestadores o CI)
python "skills/organizationalMotivations/scripts/validate_motivations.py" "ruta/hacia/motivaciones.md" --json
```

### Reglas Validadas por el Script
1. Presencia obligatoria de las 5 secciones estándar.
2. Identificación institucional con objetivos SMART.
3. Evaluación de al menos 3 macro-sectores del mapa SDLI con códigos `TND-XX`.
4. Cobertura explícita de las 3 dimensiones analíticas (Sociedad, Tecnología, Economía).
5. Inclusión explícita del marco de Lógica Dominante del Servicio (SDL) y co-creación de valor.
6. Matriz de necesidades emergentes del cliente con códigos `CLI-XX`.
7. Impulsores de rediseño identificados con códigos `DRV-XX` y justificación causal.

---

## 6. Ejecución de Pruebas Unitarias

```bash
python "skills/organizationalMotivations/tests/test_validate_motivations.py"
```
Todas las pruebas unitarias deben reportar `OK`.
