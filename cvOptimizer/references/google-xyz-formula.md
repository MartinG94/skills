# Estándar de Redacción de Logros: Fórmula Google X-Y-Z

Popularizada por **Laszlo Bock** (ex-SVP de People Operations en Google), la fórmula Google X-Y-Z es el estándar de oro en la industria tecnológica para demostrar impacto concreto y medible en lugar de simples descripciones pasivas de tareas:

$$\text{“Logró [X], medido por [Y], mediante [Z]” \quad \longrightarrow \quad \text{En ES preferente: “[Sustantivo de acción + Alcance X], [Métrica Y], mediante [Z]”}}$$
$$\text{“Accomplished [X], as measured by [Y], by doing [Z]”}$$

---

## 1. Desglose Anatómico de la Fórmula

| Componente | Definición | Pregunta Guía | Ejemplo Concreto |
|---|---|---|---|
| **[X] Logro / Resultado** | El impacto directo de negocio, técnico o institucional obtenido. | ¿Qué mejoró, se construyó o se resolvió? | *Aceleró el procesamiento de consultas de datos y reportes institucionales* |
| **[Y] Métrica Cuantitativa** | La evidencia numérica del cambio respecto a una línea base. | ¿Cómo se cuantificó el éxito? (%, tiempo, dinero, volumen) | *reduciendo los tiempos de respuesta en un 35% y manteniendo el 100% de cumplimiento en plazos* |
| **[Z] Acción y Herramientas** | La intervención técnica, metodológica o de liderazgo ejecutada. | ¿Qué hiciste exactamente y con qué herramientas? | *mediante la reescritura y optimización de procedimientos almacenados en Oracle SQL e integración de APIs REST.* |

---

## 2. Comparativa: Redacción Pasiva vs. Fórmula Google X-Y-Z

| Rol | Redacción Pasiva Débil (Tarea) | Redacción Google X-Y-Z de Alto Impacto |
|---|---|---|
| **Desarrollo Full Stack** | *Hacía mantenimiento y desarrollo de módulos en la intranet con Oracle SQL y .NET.* | *Desarrolló módulos de reportería para Acción Social en VB/.NET y HTML/JS, optimizando procedimientos en Oracle SQL para reducir tiempos de procesamiento en un 35% y asegurar el 100% de disponibilidad transaccional para más de 5,000 usuarios.* |
| **Gestión de Proyectos** | *Encargado de organizar eventos y coordinar reuniones con miembros de la asociación.* | *Lideró la planificación y control operativo de 8 proyectos institucionales y solidarios en AVEIT, coordinando a 30+ voluntarios mediante tableros Trello y diagramas de Gantt, mitigando desvíos de cronograma en un 20%.* |
| **Soporte IT e Infraestructura** | *Brindaba soporte a computadoras y redes en la oficina.* | *Gestionó el soporte operativo L1/L2 e infraestructura de conectividad TCP/IP, resolviendo el 95% de incidentes técnicos en menos de 2 horas y asegurando la continuidad operativa del personal directivo.* |

---

## 3. Banco de Sustantivos y Verbos de Acción
 
 En español se prioriza el **estilo sustantivado de acción** para otorgar neutralidad, concisión y formalidad ejecutiva. En inglés se mantiene la convención de verbos en pasado simple activo (*Past Simple*).
 
 ### Comparativa de Redacción (Verbal vs. Nominal en Español):
 | Área Funcional | Verbo en Pretérito (Estilo Anterior) | Sustantivo de Acción (Estilo Preferente) |
 |---|---|---|
 | **Requerimientos y Procesos** | *Relevó, analizó y formalizó...* | **Relevamiento, análisis y formalización de...** |
 | **Ingeniería y Arquitectura** | *Diseñó, arquitecturó y modeló...* | **Diseño de arquitectura, modelado y especificación de...** |
 | **Desarrollo y Software** | *Desarrolló, implementó y desplegó...* | **Desarrollo, implementación y despliegue de...** |
 | **Optimización y Datos** | *Optimizó, redujo y aceleró...* | **Optimización de consultas y reducción de tiempos de...** |
 | **Coordinación y Proyectos** | *Coordinó, planificó y controló...* | **Coordinación, planificación y control de...** |
 | **Liderazgo y Gobernanza** | *Dirigió, administró y lideró...* | **Dirección administrativa, liderazgo y gestión de...** |
 | **Calidad y Soporte** | *Supervisó, testeó y verificó...* | **Supervisión técnica, control de calidad y testeo de...** |
 
 ### Banco de Términos por Idioma:
 - **Español (Sustantivos de Acción):** *Relevamiento, Análisis, Diseño, Arquitectura, Desarrollo, Implementación, Automatización, Optimización, Reducción, Coordinación, Dirección, Planificación, Gestión, Integración, Supervisión.*
 - **English (Action Verbs):** *Led, Coordinated, Engineered, Architected, Designed, Developed, Automated, Optimized, Reduced, Accelerated, Integrated, Deployed, Standardized.*

---

## 4. Regla de Oro Anti-Alucinación

Cuando falte un dato cuantitativo durante el análisis del perfil:
1. **Preguntar al usuario:** Presentar la propuesta del logro y consultar si recuerda el orden de magnitud (ej. *¿Aproximadamente cuántos usuarios usaban el sistema o cuánto tiempo se ahorraba?*).
2. **Uso de Marcador Temporal:** Si el usuario no dispone de la cifra en el momento de la entrevista, insertar en el código LaTeX la macro:
   `\metric{[X%]}` o `\metric{[X usuarios]}`
   para que resalte en rojo tenue en la previsualización y el usuario la complete antes del envío final. **Nunca inventar porcentajes ni métricas ficticias.**
