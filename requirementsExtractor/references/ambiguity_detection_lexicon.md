# Léxico de Detección de Ambigüedad y Generador de Preguntas de Clarificación

Este documento define el catálogo de términos vagos, expresiones evasivas y trampas lingüísticas habituales en entrevistas con stakeholders, junto con el mecanismo de desambiguación formal basado en **Planguage (Tom Gilb)** y criterios **SMART**.

---

## 1. Catálogo de Patrones de Lenguaje Vago

### 1.1. Adjetivos Cualitativos Subjetivos (Sin Métrica)

| Término Detectado | Riesgo / Interpretación Ambigua | Categoría FURPS+ / ISO | Estrategia de Desambiguación |
| :--- | :--- | :--- | :--- |
| **"Amigable" / "Intuitivo" / "Fácil de usar"** | ¿Fácil para quién? ¿Qué nivel de capacitación previa se asume? ¿Cuántos errores se toleran? | Usabilidad (Learnability / Operability) | Medir tiempo de inducción (*Time on Task*), tasa de éxito sin asistencia en primer uso, o puntuación en System Usability Scale (SUS). |
| **"Rápido" / "Ágil" / "Veloz"** | ¿Rápido en milisegundos? ¿Bajo qué condiciones de carga y concurrencia? | Rendimiento (Response Time) | Definir latencia percentil 95 (P95) en ms bajo carga nominal y carga pico. |
| **"Robusto" / "Confiable" / "Seguro"** | ¿Tolerante a caídas de red? ¿Cifrado de datos? ¿Sin pérdida de sesiones? | Fiabilidad / Seguridad | Especificar SLA de disponibilidad (99.9%), RPO/RTO, y algoritmos de autenticación/cifrado. |
| **"Escalable" / "Potente"** | ¿Escalar vertical u horizontalmente? ¿Hasta cuántos usuarios o transacciones por segundo? | Rendimiento (Capacity) | Definir umbrales de concurrencia actual, concurrencia objetivo y throughput (TPS). |
| **"Liviano" / "Óptimo"** | ¿Bajo consumo de RAM en cliente? ¿Tamaño del bundle web en MB? | Rendimiento / Portabilidad | Establecer tamaño máximo de bundle (ej. < 500 KB gzip) y consumo de memoria (ej. < 150 MB RAM). |
| **"Moderno" / "Innovador"** | Término estético vacío; no define comportamiento ni contrato técnico. | Usabilidad (UI Aesthetics) | Alinear con Design System corporativo, directrices WCAG 2.1 AA o biblioteca de componentes acordada. |

### 1.2. Adverbios y Cuantificadores Imprecisos

| Término Detectado | Riesgo / Interpretación Ambigua | Estrategia de Desambiguación |
| :--- | :--- | :--- |
| **"En tiempo real"** | ¿Sincrónico estricto (< 10 ms)? ¿WebSockets / SSE (< 500 ms)? ¿Polling cada 5 segundos? | Especificar latencia máxima tolerable desde la emisión del evento hasta su visualización en pantalla. |
| **"Inmediatamente" / "Al instante" / "Al toque"** | Puede ocultar procesos asíncronos que requieren confirmación transaccional o validación externa. | Definir si la operación es bloqueante o si admite procesamiento asíncrono con notificación push/webhook. |
| **"Frecuentemente" / "A veces" / "Raramente"** | Imposibilita dimensionar colas, bases de datos o capacidad de infraestructura. | Solicitar volumen promedio y pico: transacciones por hora, día o mes. |
| **"Casi siempre" / "La mayoría de las veces"** | Oculta casos de borde (*edge cases*) y reglas de negocio no declaradas. | Preguntar explícitamente: *¿Qué ocurre en el porcentaje restante de los casos? ¿Cuál es el flujo de excepción?* |
| **"Muchos datos" / "Gran volumen"** | Imprecisión que impide elegir entre indexación básica, particionado o Big Data pipelines. | Cuantificar: número de filas/registros iniciales, tasa de crecimiento mensual (GB/mes) y políticas de retención. |

### 1.3. Expresiones Evasivas y Cláusulas de Escape

| Expresión Detectada | Riesgo de Implementación | Pregunta de Aclaración para el Stakeholder |
| :--- | :--- | :--- |
| **"Según corresponda" / "De acuerdo al caso"** | Oculta una tabla de decisión o una máquina de estados no documentada. | *"¿Cuáles son los criterios exactos o condiciones lógicas que determinan cada variante de acción?"* |
| **"Y/O" (Disyunción no inclusiva)** | Confusión entre bifurcación concurrente (ambas) o exclusiva (una u otra). | *"¿El sistema debe permitir ambas opciones simultáneamente o son mutuamente excluyentes?"* |
| **"Etcétera" / "Y demás" / "Y otros campos"** | Deja el alcance abierto a asunciones erróneas del desarrollador. | *"Por favor detalle la lista exhaustiva y cerrada de todos los elementos o campos requeridos."* |
| **"Adecuado" / "A criterio del usuario"** | Transfiere la responsabilidad del diseño de negocio al usuario final de forma arbitraria. | *"¿Quién tiene el rol/permiso de tomar esta decisión y qué límites o valores por defecto aplican?"* |
| **"Lo antes posible" / "Lo más pronto posible"** | Ausencia de SLA o ventana de procesamiento formal. | *"¿Cuál es el plazo límite en horas/minutos antes de que el retraso genere un impacto operativo o sanción?"* |

### 1.4. Voz Pasiva y Sujetos Omitidos

| Patrón Detectado | Ejemplo en Transcripción | Pregunta de Aclaración |
| :--- | :--- | :--- |
| **Voz Pasiva sin Actor** | *"Los pedidos deben ser aprobados antes del despacho."* | *"¿Qué rol o sistema específico realiza la aprobación y qué sucede si no hay respuesta en X tiempo?"* |
| **Acción sin Destinatario** | *"Se enviará una notificación con el detalle."* | *"¿A qué destinatarios específicos se envía, por qué canal (Email, SMS, Push, WhatsApp) y con qué plantilla de datos?"* |

---

## 2. Marco Planguage de Tom Gilb para Atributos de Calidad

Para cada Requerimiento No Funcional con lenguaje vago detectado, el extractor debe estructurar una especificación formal bajo el estándar Planguage:

```
TAG: [Identificador RNF-XXX]
AMBIGUOUS_SOURCE: "[Cita textual del stakeholder con la palabra vaga]"
SCALE: [Unidad de medida física o métrica estandarizada]
METER: [Método, herramienta o procedimiento de medición y verificación]
BASELINE: [Nivel actual del sistema legacy o proceso manual]
WORST_ACCEPTABLE: [Límite mínimo o máximo tolerable para no rechazar la entrega]
TARGET_PLAN: [Nivel objetivo que el sistema debe alcanzar en producción]
STRETCH_WISH: [Nivel deseable / aspiracional para futuras iteraciones]
```

---

## 3. Generador de Preguntas de Clarificación (Templates por Dominio)

Cuando se detecta una ambigüedad, el agente debe generar preguntas estructuradas con opciones múltiples sugeridas:

### Plantilla de Pregunta para Tiempos de Respuesta:
> **Pregunta para [Rol del Stakeholder]:**  
> *"En la entrevista mencionó que el proceso de [Nombre del Proceso] debe ser 'rápido'. Para garantizar el dimensionamiento de servidores y arquitectura:*  
> *a) ¿Cuál es el tiempo máximo de espera tolerable por el operador antes de que considere que el sistema falló? (ej. < 1 seg, < 3 seg, < 10 seg)*  
> *b) ¿Cuántos operadores estarán ejecutando esta consulta simultáneamente en el momento de mayor demanda?"*

### Plantilla de Pregunta para Reglas de Negocio Ocultas ("Según corresponda"):
> **Pregunta para [Rol del Stakeholder]:**  
> *"Se indicó que se aplicará un recargo 'según corresponda'.*  
> *a) ¿Cuáles son las variables exactas que determinan el recargo (ej. tipo de cliente, zona geográfica, medio de pago, monto total)?*  
> *b) ¿Existe una tabla de porcentajes fija o una fórmula de cálculo específica? ¿Dónde se encuentra documentada?"*
