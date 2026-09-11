# Guía Metodológica Oficial: Matriz FODA del Proceso Operativo (GMP Etapa 2)

> **Marco Académico:** Cátedra de Gestión y Mejora de Procesos (GMP / Ciclo PDCA) — Ingeniería en Sistemas de Información, Universidad Tecnológica Nacional (UTN FRC).  
> **Fuentes Primarias Oficiales:**  
> - Diapositivas de Cátedra: `SLI_U3_C03_Analisis_FODA.pdf` (Clase 3: Análisis estratégico: FODA).  
> - Planilla Maestra de Cátedra: `PlanillaMATRICES-TPI 2026 con ejemplo.xlsx` — Pestaña *'Etapa 2 Análisis del proceso'*, Matriz 3: *ANÁLISIS FODA DEL PROCESO*.

---

## 1. Fundamento Metodológico y Ecosistema de Mejora Continua

El análisis FODA a nivel de proceso de negocio no es un simple ejercicio de enumeración abstracta ni una repetición del FODA corporativo general. Como define la cátedra:

> *"Un proceso no es una isla, sino una pieza que debe empujar la misión de la empresa y satisfacer a sus actores clave. La Matriz FODA del Proceso está diseñada para conectar la estrategia con la realidad operativa, usando tres ejes de análisis."*

### Ubicación en el Ciclo PDCA y Etapas de GMP
1. **Etapa 1 (Planificar - Situación Actual):** Encuadre del negocio, mapa de procesos, tendencias SDL, virtual value chain y selección ponderada del proceso crítico.
2. **Etapa 2 (Planificar - Análisis del Proceso AS-IS):**
   - Matriz 1: Definición, clientes, límites y alcance del proceso.
   - Matriz 2: Grupos de Interés del Proceso (`stakeholderMatrix` con Resultados, Expectativas y Obstáculos).
   - Matriz 3: **Análisis FODA del Proceso (`fodaProcess`)**, conectando estrategia, stakeholders y resultados/auditoría.
   - Diagnóstico Forense y Auditoría Operativa (`processAuditor`: COSO, RCM, SoD, ruta documental, silos TI).
3. **Etapa 3 (Hacer - Propuesta de Mejora):**
   - Matriz CAME (`cameStrategizer`): Corregir debilidades, Afrontar amenazas, Mantener fortalezas y Explotar oportunidades.
   - Inventario de Acciones de Valor EERR (`valueActionsBuilder`): Eliminar, Reducir, Incrementar, Crear con Filtro de Restricciones Operativas.
4. **Etapa 4 (Verificar/Actuar - Mejora del Proceso):**
   - Objetivos SMART, Indicadores de Proceso y Resultado (`kpiDesigner`), y Plan de Implementación / Cronograma Gantt.

---

## 2. Los Tres Ejes de Análisis Obligatorios de la Cátedra (Matriz 3)

La cátedra de GMP estructura el análisis de cada cuadrante sobre **tres ejes transversales**:

```
+----------------------------------------------------------------------------------------------------+
|                                    MATRIZ FODA DEL PROCESO                                         |
+------------------------------------+------------------------------------+--------------------------+
| EJE 1: PROPÓSITO, VISIÓN           | EJE 2: GRUPOS DE INTERÉS           | EJE 3: RESULTADOS        |
|        Y ESTRATEGIA                |        (STAKEHOLDERS)              |        ACTUALES          |
+------------------------------------+------------------------------------+--------------------------+
| ¿Cómo impacta el factor en la      | ¿Quién se beneficia o se ve        | ¿Qué evidencia empírica, |
| misión, visión u objetivos         | perjudicado/afectado por este      | métricas actuales o      |
| estratégicos de la organización?   | factor dentro o fuera del proceso? | hallazgos de auditoría   |
|                                    | (Mapeo con stakeholderMatrix)      | sustentan el factor?     |
+------------------------------------+------------------------------------+--------------------------+
```

### Detalle por Cuadrante según la Guía Oficial:

### A. Fortalezas (Factores Internos Positivos — Puntos fuertes del proceso)
- **Definición:** Aspectos positivos bajo control directo del proceso. Fuentes de satisfacción del cliente o creación de valor (rapidez, tecnología actual, bajo costo, personal capacitado, certificaciones de calidad).
- **Eje 1 (Estrategia):** ¿En qué es excelente el proceso para ayudar a cumplir la misión, visión y objetivos estratégicos?
- **Eje 2 (Grupos de Interés):** Identificar quién se beneficia de esta fortaleza identificada (colaboradores con pertenencia, clientes con atención ágil).
- **Eje 3 (Resultados Actuales):** ¿Qué resultados o métricas positivas alcanza hoy el proceso relacionados a esas fortalezas? (ej. OTIF 92%, 80% de casos resueltos en primer contacto).

### B. Debilidades (Factores Internos Negativos — Puntos débiles del proceso)
- **Definición:** Puntos negativos que frenan el proceso. Brechas, deficiencias o problemas que afectan la calidad o la entrega, fuentes de insatisfacción o pérdida de valor para el cliente (falta de personal, cuellos de botella, equipo obsoleto, infraestructura inadecuada, silos TI).
- **Eje 1 (Estrategia):** ¿Qué falla en el proceso que lo desalinea de la visión u objetivos estratégicos (ej. falta de omnicanalidad, catálogo restringido)?
- **Eje 2 (Grupos de Interés):** Identificar a quiénes afecta esa debilidad identificada (clientes frustrados por repetir reclamos, operarios con sobrecarga burocrática).
- **Eje 3 (Resultados Actuales):** ¿Qué resultados no alcanza el proceso o qué evidencia de auditoría prueba la falla? (NPS pasivo, demora >48h, hallazgos RCM de `processAuditor`, conflictos SoD, doble carga manual).

### C. Oportunidades (Factores Externos Positivos — Factores del entorno explotables)
- **Definición:** Tendencias, innovaciones, cambios normativos o eventos del entorno que pueden mejorar el rendimiento o los resultados del proceso (nuevas tecnologías SaaS/IoT, subsidios estatales, cambios favorables en hábitos de clientes).
- **Eje 1 (Estrategia):** ¿Qué factores o tecnologías externas impulsan los ejes de innovación o crecimiento fijados en la visión?
- **Eje 2 (Grupos de Interés):** Qué alianzas o nuevas relaciones con actores del entorno permiten capturar o co-crear valor (Lógica Dominante del Servicio - SDL).
- **Eje 3 (Resultados Actuales):** Indicadores de mercado o disponibilidad concreta de soluciones en el sector que sustentan la oportunidad.

### D. Amenazas (Factores Externos Negativos — Riesgos e incertidumbres del entorno)
- **Definición:** Dinámicas externas que escapan al control directo del proceso y que pueden dañar el rendimiento, la continuidad o los márgenes (nuevos competidores nativos digitales, endurecimiento regulatorio/fiscal, inestabilidad macroeconómica, volatilidad de insumos).
- **Eje 1 (Estrategia):** Qué regulaciones o cambios de contexto amenazan el modelo operativo o ponen en jaque el cumplimiento normativo.
- **Eje 2 (Grupos de Interés):** Reacciones adversas o riesgos provenientes de actores externos (viralización de quejas de usuarios en redes sociales, sanciones de entes reguladores).
- **Eje 3 (Resultados Actuales):** Impacto observable de factores externos en la operación (incremento en volumen de reclamos por fallas externas, suba de costos operativos de combustible/transporte).

---

## 3. Principio de Delimitación Estricta de Frontera (Test de Controlabilidad)

La frontera entre lo **interno** (Fortalezas y Debilidades) y lo **externo** (Oportunidades y Amenazas) se rige por el **Principio de Controlabilidad**:

> **Test de Controlabilidad:**  
> *"Si el dueño del proceso emite una orden directa o invierte recursos propios asignados al proceso, ¿puede alterar o rediseñar este factor de forma inmediata y directa?"*
> - **SÍ:** Es un factor **Interno** (Fortaleza o Debilidad).
> - **NO:** Es un factor **Externo** (Oportunidad o Amenaza).

### Anti-Patrones de Frontera Frecuentes y su Corrección:
1. **Confundir Oportunidad con Proyecto o Acción Interna:**
   - *Error:* *"Oportunidad: Desarrollar una app móvil o comprar un sistema ERP"*.
   - *Razón del error:* Desarrollar o comprar es una decisión interna de gestión (futura acción CAME).
   - *Corrección:* *"Oportunidad: Maduración y disponibilidad en el mercado de plataformas SaaS logísticas con APIs abiertas y bajo costo de implementación"*.
2. **Confundir Amenaza con Ineficiencia del Personal Propio:**
   - *Error:* *"Amenaza: Los operarios cargan tarde las planillas de recepción"*.
   - *Razón del error:* El personal y los procedimientos internos son 100% controlables por la gerencia del proceso.
   - *Corrección (como Debilidad):* *"D2: Registro manual diferido de remitos que genera 24-48h de desactualización del inventario en el ERP (Evidencia: RCM-02)"*.
3. **Confundir Fortaleza con Tendencia Favorable del Mercado:**
   - *Error:* *"Fortaleza: Crecimiento de la demanda de nuestros productos en el mercado regional"*.
   - *Razón del error:* El comportamiento del mercado es externo.
   - *Corrección (como Oportunidad):* *"O3: Expansión de la demanda insatisfecha de servicios logísticos refrigerados en la región centro"*.

---

## 4. Regla Canónica de Cardinalidad (4 a 6 Factores por Cuadrante)

Conforme a la diapositiva 6 de la cátedra:
> *"Buena práctica de diseño: Limitar a 4-6 puntos clave por cuadrante ayuda a garantizar un análisis manejable y operativo."*

- **Límite Inferior ($N \ge 4$):** Menos de 4 factores por cuadrante evidencia un relevamiento superficial y falta de rigurosidad analítica.
- **Límite Superior ($N \le 6$):** Más de 6 factores por cuadrante diluye el foco estratégico, complejiza innecesariamente la matriz 2x2 y vuelve inmanejable la matriz de cruces CAME posterior ($6 \times 6 = 36$ combinaciones máximas teóricas).
- **Rango Válido Obligatorio:** $4 \le N \le 6$ factores en Fortalezas, Debilidades, Oportunidades y Amenazas.

---

## 5. Casos Oficiales de Referencia de la Cátedra

### Caso 1: Proceso "Atención de Reclamos de Servicios" (Municipalidad Serrana — `SLI_U3_C03_Analisis_FODA.pdf`)
- **Organización:** Secretaría de Atención al Ciudadano de una municipalidad serrana.
- **Proceso:** Atención de reclamos de servicios.
- **Objetivo:** Recibir y gestionar los reclamos efectuados por los ciudadanos del municipio.
- **Límites:** Desde que se recibe el reclamo por parte del ciudadano hasta su resolución y calificación final.
- **Factores Canónicos Identificados:**
  - **Fortalezas:**
    - `F1:` Personal con alta capacitación técnica y conocimiento de la normativa administrativa y los procedimientos internos.
    - `F2:` Existencia de registros históricos de reclamos que permiten identificar problemas recurrentes y zonas críticas para priorizar intervenciones.
  - **Debilidades (con Evidencia Operativa):**
    - `D1:` Escasa trazabilidad de los trámites debido al uso predominante de expedientes físicos y planillas manuales.
    - `D2:` Elevados tiempos en la resolución de reclamos debido a procesos de aprobación internos burocráticos y centralizados.
    - `D3:` Falta de integración entre los canales de atención (presencial, telefónico, digital) que genera duplicidad de gestiones para un mismo incidente.
    - `D4:` Carencia de indicadores de gestión automatizados para medir la productividad y eficiencia de las áreas resolutivas.
  - **Oportunidades:**
    - `O1:` Acceso a líneas de financiamiento o subsidios estatales destinados a proyectos de transformación digital en gobiernos locales.
    - `O2:` Alta tasa de uso de dispositivos móviles por parte de los ciudadanos, facilitando la autogestión y reporte geolocalizado.
    - `O3:` Existencia de un marco legal nacional que promueve la transparencia, el gobierno abierto y la rendición de cuentas.
  - **Amenazas:**
    - `A1:` Creciente exposición negativa en redes sociales que deteriora la imagen institucional de la gestión pública.
    - `A2:` Inestabilidad económica general que deriva en recortes presupuestarios para el mantenimiento operativo y equipamiento de cuadrillas.
    - `A3:` Posibles cambios en la legislación provincial que exijan tiempos de respuesta más cortos con sanciones administrativas por incumplimiento.

### Caso 2: Proceso "Gestión de la Trayectoria, Formación Integral y Graduación" (Universidad Privada — `PlanillaMATRICES-TPI 2026`)
- **Organización:** Universidad Privada regional.
- **Estructura bajo los 3 Ejes:**
  - **Fortalezas:**
    - `F1:` *Experiencia docente calificada.* (Eje 1: Solidez pedagógica alineada a la Visión; Eje 2: Sentido de pertenencia docente; Eje 3: 80% de resolución de casos).
    - `F2:` *Infraestructura adecuada para el aprendizaje.* (Eje 1: Soporte presencial; Eje 2: Estudiantes con instalaciones funcionales; Eje 3: Auditoría de aulas y talleres).
    - `F3:` *Programas de estudio actualizados.* (Eje 1: Pertinencia formativa; Eje 2: Mercado laboral y graduados; Eje 3: Alta tasa de inserción laboral).
    - `F4:` *Solidez de convenios de pasantías.* (Eje 1: Articulación académica-empresa; Eje 2: Empresas aliadas; Eje 3: Más de 50 empresas con convenios activos).
  - **Debilidades:**
    - `D1:` *Limitaciones en la oferta académica.* (Eje 1: Desalineado de la diversificación estratégica; Eje 2: Aspirantes buscan carreras cortas; Eje 3: Estancamiento de matrícula en programas tradicionales).
    - `D2:` *Insuficiente apoyo a necesidades específicas.* (Eje 1: Compromiso de inclusión no cumplido; Eje 2: Estudiantes con barreras; Eje 3: 15% de deserción por falta de tutorías tempranas).
    - `D3:` *Comunicación deficiente docentes-estudiantes.* (Eje 1: Visión de acompañamiento afectada; Eje 2: Estudiantes insatisfechos; Eje 3: Tiempos de respuesta >48h en consultas académicas).
    - `D4:` *Fragmentación de sistemas administrativos.* (Eje 1: Desarticulación digital; Eje 2: Personal administrativo saturado; Eje 3: RCM-03 doble carga de actas en Excel y SIU).
  - **Oportunidades:**
    - `O1:` *Tecnologías educativas innovadoras.* (Eje 1: Impulsa innovación de la Visión; Eje 2: Docentes y alumnos adoptan campus virtual; Eje 3: Ecosistema EdTech maduro).
    - `O2:` *Colaboraciones con instituciones internacionales.* (Eje 1: Internacionalización de la Visión; Eje 2: Alumnos en intercambio; Eje 3: Redes universitarias globales abiertas).
    - `O3:` *Demanda creciente de educación continua.* (Eje 1: Nuevas fuentes de ingresos; Eje 2: Profesionales en ejercicio; Eje 3: Incremento sostenido en consultas de diplomaturas).
    - `O4:` *Marco regulatorio para carreras a distancia.* (Eje 1: Expansión geográfica; Eje 2: Alumnos remotos; Eje 3: Nuevas resoluciones ministeriales favorables).
  - **Amenazas:**
    - `A1:` *Cambios en políticas educativas nacionales.* (Eje 1: Riesgo de acreditación; Eje 2: Gestión institucional bajo presión; Eje 3: Exigencia de rápida adecuación curricular).
    - `A2:` *Aumento de la competencia entre instituciones.* (Eje 1: Presión sobre cuotas; Eje 2: Familias comparan aranceles; Eje 3: Incremento del costo de adquisición de alumnos).
    - `A3:` *Reducción de fondos y subsidios públicos.* (Eje 1: Sostenibilidad financiera; Eje 2: Becarios afectados; Eje 3: Caída del 20% en financiamiento para investigación).
    - `A4:` *Desactualización rápida de tecnologías del mercado.* (Eje 1: Obsolescencia de programas; Eje 2: Empleadores demandan habilidades de día 1; Eje 3: Brecha en egresados TI).

---

## 6. Conexión Directa con el Cruce CAME (Etapa 3 de GMP)

La Matriz FODA del Proceso es el insumo fundamental para la formulación estratégica CAME:
- **Estrategias Ofensivas (FO - Max-Max) ➔ EXPLOTAR:** Usar Fortalezas internas para capitalizar Oportunidades externas.
- **Estrategias Defensivas (FA - Max-Min) ➔ MANTENER:** Usar Fortalezas internas para neutralizar o amortiguar Amenazas del entorno.
- **Estrategias de Reorientación (DO - Min-Max) ➔ CORREGIR:** Superar Debilidades internas aprovechando Oportunidades que ofrece el mercado o la tecnología.
- **Estrategias de Supervivencia (DA - Min-Min) ➔ AFRONTAR:** Mitigar Debilidades internas críticas para resistir las Amenazas externas y controlar daños potenciales.
