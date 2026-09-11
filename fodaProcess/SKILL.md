---
name: fodaProcess
description: >-
  Construye la Matriz FODA del proceso operativo (Etapa 2 de GMP) con estricta delimitación de cuadrantes
  (Fortalezas y Debilidades internas/controlables; Oportunidades y Amenazas externas/entorno) y 4 a 6
  factores por cuadrante. Aplica los 3 Ejes analíticos de cátedra (Estrategia, Stakeholders y Resultados/Evidencia).
  Garantiza la trazabilidad directa de las Debilidades a la evidencia forense y de auditoría (processAuditor),
  preparando los insumos para los cruces estratégicos CAME (cameStrategizer). Genera y guarda deterministamente
  el entregable en 'foda.md'.
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.1.0","category":"process-atomic","platforms":["windows","macos","linux"]}
---

# Matriz FODA del Proceso Operativo (GMP Etapa 2)

Skill atómica especializada en el diagnóstico estratégico situacional del proceso de negocio bajo el marco de **Gestión y Mejora de Procesos (GMP - Ciclo PDCA)** (UTN FRC - Ingeniería en Sistemas de Información). Estructura los 4 cuadrantes canónicos (Fortalezas, Debilidades, Oportunidades y Amenazas) aplicando los **3 Ejes de Análisis de Cátedra** (`PlanillaMATRICES-TPI 2026` Matriz 3) y una rigurosa segregación de frontera de controlabilidad.

---

## Límites de Autoridad y Reglas Invariables

1. **Persistencia Determinista Obligatoria:**
   El entregable final debe guardarse siempre en el archivo Markdown [`foda.md`](file:///c:/Users/Diego/.gemini/config/skills/fodaProcess/templates/foda_process_template.md) en la raíz del espacio de trabajo o directorio activo del proyecto. No usar nombres alternativos (`foda_proceso.md`, `swot.md`, `matriz_foda.md`).

2. **Cardinalidad Canónica por Cuadrante (Regla 4-6):**
   Cada cuadrante debe contener obligatoriamente entre **4 y 6 factores** significativos ($4 \le N \le 6$), conforme a la regla de diseño de cátedra (`SLI_U3_C03_Analisis_FODA.pdf`, diapositiva 6). Menos de 4 factores denota superficialidad analítica; más de 6 diluye el foco estratégico e imposibilita cruces CAME viables.

3. **Regla de Oro de Frontera Interna vs. Externa (Principio de Controlabilidad):**
   - **Ámbito Interno (Fortalezas y Debilidades):** Elementos que se originan **dentro** de la organización y sobre los cuales los dueños del proceso tienen capacidad directa de intervención, rediseño o gobierno (procesos, tecnología propia, competencias del personal, políticas internas, control documental).
   - **Ámbito Externo (Oportunidades y Amenazas):** Fenómenos originados **fuera** de los límites de la organización que el proceso no puede controlar directamente pero a los cuales debe responder o adaptarse (macroeconomía, competencia, regulaciones estatales, avances tecnológicos globales, comportamiento del consumidor).

4. **Trazabilidad Forense Obligatoria de las Debilidades:**
   Toda debilidad ($D_i$) debe contar con un enlace explícito a una fuente primaria de evidencia:
   - Hallazgos de auditoría de control interno COSO / RCM de [`processAuditor`](file:///c:/Users/Diego/.gemini/config/skills/processAuditor/SKILL.md).
   - Incompatibilidades de segregación de funciones (SoD).
   - Deficiencias en formularios, copias o ruta documental en papel.
   - Silos informáticos, recapturas manuales o interfaces fallidas.
   - Observaciones de campo en relevamiento o citas de entrevistas (`SRC-...`).
   Queda estrictamente prohibido inventar o asumir debilidades abstractas sin sustento probatorio.

5. **Los Tres Ejes de Análisis de Cátedra (`PlanillaMATRICES` Matriz 3):**
   Cada factor en las tablas detalladas debe articularse considerando:
   - **Eje 1: Propósito, Visión y Estrategia:** Cómo incide el factor en los objetivos de negocio y la visión institucional.
   - **Eje 2: Grupos de Interés (Stakeholders):** Quiénes se benefician o sufren el impacto (trazable a [`stakeholderMatrix`](file:///c:/Users/Diego/.gemini/config/skills/stakeholderMatrix/SKILL.md)).
   - **Eje 3: Resultados Actuales y Evidencia Forense:** Qué métricas del proceso AS-IS demuestran la fortaleza o qué hallazgo de auditoría prueba la debilidad.

6. **Codificación Determinista de Factores:**
   Todo factor debe identificarse unívocamente mediante prefijo canónico y número correlativo:
   - Fortalezas: `F1`, `F2`, `F3`, `F4` (hasta `F6`).
   - Debilidades: `D1`, `D2`, `D3`, `D4` (hasta `D6`).
   - Oportunidades: `O1`, `O2`, `O3`, `O4` (hasta `O6`).
   - Amenazas: `A1`, `A2`, `A3`, `A4` (hasta `A6`).

---

## Estructura de los 4 Cuadrantes y Test de Frontera

Para evitar sesgos y clasificaciones erróneas, aplicar el siguiente **Test de Controlabilidad**:
> *“Si el dueño del proceso emite una orden directa o invierte recursos propios asignados al proceso, ¿puede cambiar este factor de forma inmediata o directa?”*
> - **SÍ:** Es un factor **Interno** (Fortaleza o Debilidad).
> - **NO:** Es un factor **Externo** (Oportunidad o Amenaza).

```
                      ÁMBITO INTERNO                 ÁMBITO EXTERNO
               (Controlable por el Proceso)    (No Controlable / Entorno)
              +------------------------------+------------------------------+
   IMPACTO    |                              |                              |
   POSITIVO   |       FORTALEZAS (F)         |      OPORTUNIDADES (O)       |
  (Favorece   | Capacidades, recursos clave, | Tendencias tech (SaaS, IoT), |
   al proceso)| estandarización, know-how.   | cambios normativos pro-sector|
              |                              |                              |
              +------------------------------+------------------------------+
   IMPACTO    |                              |                              |
   NEGATIVO   |       DEBILIDADES (D)        |         AMENAZAS (A)         |
  (Perjudica  | Silos TI, SoD roto, cuellos  | Nuevos competidores ágiles,  |
   al proceso)| de botella, papel repetitivo.| inflación, corte suministros.|
              |                              |                              |
              +------------------------------+------------------------------+
```

### 1. Fortalezas (F) — Interno / Positivo
- **Definición:** Competencias distintivas, activos, metodologías o tecnologías que el proceso ejecuta con alto desempeño y que otorgan ventaja competitiva o resiliencia operativa.
- **Criterios de inclusión:** Experiencia técnica demostrada, infraestructura propia mantenida, certificaciones de calidad (ISO 9001), alta tasa histórica de resolución (OTIF > 90%).

### 2. Debilidades (D) — Interno / Negativo
- **Definición:** Vulnerabilidades estructurales, fallas de diseño organizativo, sobrecarga operativa o ineficiencias técnicas inherentes al proceso actual (AS-IS).
- **Criterios de inclusión:** Ruptura de SoD, transcripciones manuales de planillas, demoras por firmas físicas redundantes, falta de trazabilidad en sistemas aislados, sobrecarga ergonómica.

### 3. Oportunidades (O) — Externo / Positivo
- **Definición:** Situaciones, innovaciones o cambios en el entorno competitivo, regulatorio o tecnológico que el proceso puede capitalizar para optimizar su desempeño o co-crear valor (Lógica Dominante del Servicio - SDL).
- **Criterios de inclusión:** Disponibilidad de plataformas SaaS o APIs abiertas de bajo costo, estándares de interoperabilidad sectorial, subsidios o desregulaciones aplicables, cambios favorables en hábitos de clientes.
- **Anti-patrón a evitar:** No confundir oportunidad con una acción interna proyectada (ej: *"Oportunidad: Comprar tablets para los choferes"* es INCORRECTO; la oportunidad real es *"Maduración y bajo coste de dispositivos móviles rugerizados y redes 4G/5G en ruta"*).

### 4. Amenazas (A) — Externo / Negativo
- **Definición:** Eventos, tendencias o dinámicas del contexto externo que escapan al control de la organización y que pueden degradar la eficacia, eficiencia o continuidad del proceso.
- **Criterios de inclusión:** Irrupción de competidores nativos digitales con entregas ultrarrápidas, endurecimiento de inspecciones fiscales o sanitarias con sanciones severas, aumento de precios de insumos críticos o combustibles, fallas recurrentes de infraestructura pública o telecomunicaciones.

---

## Flujo de Trabajo Paso a Paso (Progressive Disclosure)

1. **Paso 1: Relevamiento y Consumo de Evidencias:**
   - Leer el informe de auditoría forense ([`processAuditor`](file:///c:/Users/Diego/.gemini/config/skills/processAuditor/SKILL.md)), la matriz de interesados ([`stakeholderMatrix`](file:///c:/Users/Diego/.gemini/config/skills/stakeholderMatrix/SKILL.md)), minutas de entrevista o especificación del proceso AS-IS.
   - Extraer la lista de hallazgos fácticos: matriz RCM, conflictos SoD detectados, análisis de formularios papel y silos TI.
   - Consultar la guía de referencia metodológica en [`references/foda_methodology_guide.md`](file:///c:/Users/Diego/.gemini/config/skills/fodaProcess/references/foda_methodology_guide.md).

2. **Paso 2: Formulación de Debilidades ($D_1$ a $D_6$):**
   - Redactar cada debilidad con precisión técnica y desplegar los 3 ejes: Eje 1 (desalineación estratégica), Eje 2 (stakeholders afectados) y Eje 3 (referencia explícita a la evidencia: `SRC-XXX`, `RCM-YYY`, `Obs-ZZZ`).

3. **Paso 3: Identificación de Fortalezas ($F_1$ a $F_6$):**
   - Identificar capacidades, recursos o tramos del proceso que funcionan correctamente bajo control interno, desplegando los 3 ejes (contribución a la Visión, stakeholders beneficiados, métricas actuales).

4. **Paso 4: Mapeo de Entorno Operativo ($O_1$ a $O_6$ y $A_1$ a $A_6$):**
   - Mapear fuerzas tecnológicas, regulatorias, de mercado y competitivas que interactúan con el proceso.
   - Formular de 4 a 6 oportunidades y de 4 a 6 amenazas strictly externas, desplegando los 3 ejes de cátedra.

5. **Paso 5: Validación de Frontera y Filtro Anti-Patrón:**
   - Aplicar el Test de Controlabilidad factor por factor.
   - Verificar que ningún cuadrante tenga menos de 4 ni más de 6 factores.
   - Comprobar que no se hayan redactado proyectos internos como si fuesen oportunidades ni problemas de empleados propios como amenazas.

6. **Paso 6: Persistencia Determinista:**
   - Cargar los factores en la plantilla oficial [`templates/foda_process_template.md`](file:///c:/Users/Diego/.gemini/config/skills/fodaProcess/templates/foda_process_template.md).
   - Generar y escribir el archivo canónico `foda.md` en el directorio de trabajo.

7. **Paso 7: Ejecución del Validador Automatizado:**
   - Ejecutar el validador determinista: `python scripts/validate_foda.py foda.md` y verificar estado `EXITOSO`.

---

## Contrato de Salida

El archivo final `foda.md` debe respetar estrictamente:
- **Estructura jerárquica:**
  1. `Encuadre y Metadatos del Proceso` (Nombre, Organización, Alcance, Fuentes analizadas).
  2. `Resumen Ejecutivo del Diagnóstico FODA` (Balance situacional AS-IS).
  3. `Matriz Panorámica 2x2` (Visualización integral sintética).
  4. `Cuadrante 1: Fortalezas (F1-F6)` (Tabla con Código, Factor, Eje 1 Estrategia, Eje 2 Stakeholders, Eje 3 Métrica de Respaldo, Controlabilidad).
  5. `Cuadrante 2: Debilidades (D1-D6)` (Tabla con Código, Brecha Operativa, Eje 1 Estrategia, Eje 2 Stakeholders, Eje 3 Evidencia Forense de Auditoría, Eje Temático).
  6. `Cuadrante 3: Oportunidades (O1-O6)` (Tabla con Código, Oportunidad del Entorno, Eje 1 Estrategia, Eje 2 Stakeholders, Eje 3 Evidencia del Mercado, Impacto).
  7. `Cuadrante 4: Amenazas (A1-A6)` (Tabla con Código, Amenaza del Entorno, Eje 1 Estrategia, Eje 2 Stakeholders, Eje 3 Impacto Observable, Severidad).
  8. `Control de Calidad y Gobernanza de la Matriz` (Checklist de verificación de 4 cuadrantes, 4-6 factores, controlabilidad, 3 ejes y trazabilidad).
  9. `Puente Metodológico hacia CAME` (Preparación de insumos para `cameStrategizer`).
