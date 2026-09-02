# Especificación de Requerimientos de Software (ERS / SRS)
## Proyecto: [Nombre del Proyecto]
**Fuente de Elicitación:** [Título de la Entrevista / Minuta / Taller]  
**Fecha de Análisis:** [YYYY-MM-DD]  
**Analista:** [Nombre o Agente `rawInterviewToRequirementsExtractor`]  
**Versión:** [1.0.0-draft]

---

## 1. Ficha del Ecosistema de Stakeholders

| ID | Nombre / Rol | Unidad Organizacional | Nivel de Influencia | Interés Principal |
| :---: | :--- | :--- | :---: | :--- |
| **STK-01** | [Nombre del Stakeholder] | [Área / Depto] | Alta / Media / Baja | [Foco u objetivo principal] |
| **STK-02** | [Nombre del Stakeholder] | [Área / Depto] | Alta / Media / Baja | [Foco u objetivo principal] |

---

## 2. Requerimientos Funcionales (RF)

| ID | Título y Descripción | Actor Principal | Entradas / Salidas | Reglas Asociadas | Prioridad | Cita Textual de Origen (Traceability) |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **RF-01** | **[Título del Requerimiento]**<br>[Descripción detallada del comportamiento del sistema] | [Actor] | • **In:** [Datos de entrada]<br>• **Out:** [Respuesta/Persistencia] | `RN-01`, `RN-02` | **Must Have** | *"[Cita textual exacta del stakeholder]"* — `[STK-01:P05]` |
| **RF-02** | **[Título del Requerimiento]**<br>[Descripción detallada del comportamiento del sistema] | [Actor] | • **In:** [Datos de entrada]<br>• **Out:** [Respuesta/Persistencia] | `RN-03` | **Should Have** | *"[Cita textual exacta del stakeholder]"* — `[STK-02:P12]` |

---

## 3. Requerimientos No Funcionales (RNF) — Taxonomía FURPS+ / ISO 25010

| ID | Dimensión (FURPS+ / ISO 25010) | Subcaracterística | Especificación Planguage (Tom Gilb) | Prioridad | Trazabilidad |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **RNF-01** | **Performance**<br>*(ISO 25010: Desempeño)* | Comportamiento temporal | • **Escala:** Tiempo de respuesta en ms al P95<br>• **Medidor:** JMeter bajo 200 usuarios concurrentes<br>• **Límite Inaceptable:** > 2.0 s<br>• **Objetivo Plan:** <= 500 ms | **Crítica** | *"[Cita sobre lentitud o rapidez]"* — `[STK-01:P08]` |
| **RNF-02** | **Usability**<br>*(ISO 25010: Usabilidad)* | Aprendibilidad & Operabilidad | • **Escala:** Minutos de entrenamiento requeridos<br>• **Medidor:** Prueba con 5 operarios nuevos<br>• **Límite Inaceptable:** > 4 horas<br>• **Objetivo Plan:** <= 45 minutos sin supervisión | **Alta** | *"[Cita sobre interfaz amigable]"* — `[STK-02:P15]` |

---

## 4. Reglas de Negocio Aisladas (RN)

| ID | Título | Tipo de Regla | Declaración / Lógica Formal | Nivel de Cumplimiento | Origen |
| :---: | :--- | :---: | :--- | :---: | :--- |
| **RN-01** | [Nombre de la Regla] | Restricción / Cálculo / Habilitación | [Declaración formal de la política de negocio sin detalles técnicos] | Estricta / Sobrescribible | `[STK-01:P03]` |
| **RN-02** | [Nombre de la Regla] | Restricción / Cálculo / Habilitación | [Fórmula o algoritmo de negocio] | Estricta | `[STK-02:P19]` |

---

## 5. Supuestos, Restricciones y Dependencias

### 5.1. Supuestos (SUP)
- **SUP-01:** [Declaración del supuesto].  
  *Impacto si es falso:* [Riesgo de retrabajo o falla].  
  *Acción de validación:* [Cómo confirmar con el cliente].

### 5.2. Restricciones Técnicas y Regulatorias (RES)
- **RES-01:** [Restricción arquitectónica, legal o de infraestructura].  
  *Justificación:* [Motivo no negociable].

### 5.3. Dependencias de Sistemas Externos (DEP)
- **DEP-01:** [Nombre de API / Servicio externo / Base legacy].  
  *Nivel de Criticidad:* [Alta / Media / Baja] — *Descripción del intercambio de datos.*

---

## 6. Matriz de Desambiguación y Cuestionario para Stakeholders

| ID | Fragmento de Entrevista con Ambigüedad | Término Detectado | Riesgo Técnico | Pregunta de Clarificación Generada con Opciones |
| :---: | :--- | :--- | :--- | :--- |
| **AMB-01** | *"[Texto textual donde se usó palabra vaga]"* | *"amigable"*, *"rápido"*, *"según corresponda"* | [Riesgo de mala interpretación o arquitectura insuficiente] | **Para [STK-XX]:** [Pregunta formulada con opciones a), b), c) para votación o respuesta rápida] |

---

## 7. Conflictos de Alcance y Puntos de Decisión Abiertos (CONF)

| ID | Stakeholders Enfrentados | Resumen del Conflicto | Opciones de Solución Planteadas | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **CONF-01** | [STK-01 (Área X)] vs. [STK-02 (Área Y)] | [Descripción de la contradicción detectada en el discurso] | **Opción A:** [...]<br>**Opción B:** [...]<br>**Recomendación Técnica:** [...] | Pendiente de Decisión |
