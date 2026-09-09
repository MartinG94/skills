---
name: processWorkbench
description: >-
  Gobierna el razonamiento metodológico, estratégico y analítico en las Etapas 1, 2 y 3 de Gestión
  y Mejora de Procesos (GMP). En Etapa 1: encuadre de negocio, análisis de tendencias del sector bajo
  Lógica Dominante del Servicio (SDL), Cadena de Valor Virtual (Rayport & Sviokla: Recopilar, Organizar,
  Seleccionar, Sintetizar, Distribuir) y Selección Ponderada del Proceso Crítico mediante los 5 criterios de cátedra.
  En Etapa 2: Matriz de Stakeholders y Matriz FODA del proceso. En Etapa 3: Cruces estratégicos CAME,
  Acciones de Valor (Eliminar, Reducir, Incrementar, Crear) y Filtro de Restricciones Operativas con procesos afectados.
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.0.0","category":"strategy","platforms":["windows","macos","linux"]}
---

# Process Strategic & Analytical Workbench (GMP Etapas 1 a 3)

Herramienta rectora del análisis metodológico en proyectos de Gestión y Mejora de Procesos (GMP). Estructura el encuadre estratégico, la priorización matemática del proceso a intervenir, el diagnóstico de partes interesadas y FODA, y la formulación rigurosa de acciones de valor filtradas por viabilidad operativa.

---

## Límites de Autoridad y Reglas Invariables

1. **Trazabilidad Estricta de Acciones de Valor:** Ninguna Acción de Valor puede surgir de la nada; toda acción debe provenir de un cruce explícito de la Matriz CAME (`FO`, `FA`, `DO`, `DA`), el cual a su vez debe originarse en un elemento concreto del FODA.
2. **Filtro Obligatorio de Restricciones:** Ninguna Acción de Valor puede pasar a la Etapa 4 de diseño/implantación sin haber superado los 4 filtros de viabilidad operativa:
   - Plazos de implantación (horizonte temporal realista).
   - Presupuesto disponible (viabilidad económica).
   - Dependencia tecnológica (factibilidad según infraestructura y madurez TI).
   - Resistencia al cambio (gestión del factor humano).
3. **No invención de cifras:** Las ponderaciones y datos del caso deben basarse en la narrativa o caso práctico provisto; donde falte información, explicitá el supuesto o marcá `TBD`.

---

## Flujo Metodológico por Etapas

### Etapa 1: Encuadre Estratégico y Selección del Proceso Crítico
1. **Encuadre Organizacional:** Misión, visión, propuesta de valor y objetivos estratégicos.
2. **Tendencias del Sector (SDL):** Analizá las fuerzas del entorno considerando cómo la Lógica Dominante del Servicio (co-creación con clientes, servitización) impacta las operaciones.
3. **Cadena de Valor Virtual (Rayport & Sviokla):** Mapeá la transformación de datos brutos en valor a través de los 5 pasos: *Recopilar* ➔ *Organizar* ➔ *Seleccionar* ➔ *Sintetizar* ➔ *Distribuir*.
4. **Selección Ponderada (Los 5 Criterios de Cátedra):** Evaluá los procesos candidatos con escala 1 a 5:
   - $C_1$: Alineación con la Estrategia (peso sugerido 0.25).
   - $C_2$: Impacto en Tendencias del Sector / SDL (peso 0.20).
   - $C_3$: Magnitud de Problemas y Costos Operativos (peso 0.25).
   - $C_4$: Impacto Directo en la Experiencia del Cliente (peso 0.20).
   - $C_5$: Relevancia para el Producto / Servicio Central (peso 0.10).
   Calculá el puntaje ponderado $\sum w_i C_i$ y formalizá la justificación de la selección.
   *Plantilla:* [templates/stage1_framing_and_selection.md](templates/stage1_framing_and_selection.md).
   *Plantilla Virtual:* [templates/virtual_value_chain_matrix.md](templates/virtual_value_chain_matrix.md).

### Etapa 2: Stakeholders y Matriz FODA del Proceso Crítico
1. **Matriz de Stakeholders:** Identificá a los actores clave, sus resultados esperados, expectativas de calidad y los obstáculos u oposiciones observadas en el proceso actual.
2. **Matriz FODA del Proceso:**
   - **Fortalezas (F):** Capacidades internas, activos y competencias distintivas.
   - **Debilidades (D):** Alimentadas directamente por los hallazgos fácticos de `processAuditor` (fallas de control interno, ruta documental, silos TI, factores ergonómicos).
   - **Oportunidades (O) y Amenazas (A):** Factores del entorno, competidores, tecnología y normativa.
   *Plantilla:* [templates/stage2_stakeholders_foda.md](templates/stage2_stakeholders_foda.md).

### Etapa 3: Cruces CAME, Acciones de Valor y Filtro Operativo
1. **Matriz CAME:** Formulación de cruces sistemáticos:
   - **DO:** Corregir debilidades aprovechando oportunidades del entorno.
   - **FA:** Afrontar amenazas del mercado apoyándose en fortalezas internas.
   - **FO:** Mantener fortalezas potenciándolas con oportunidades de mercado.
   - **DA:** Mitigar debilidades para evitar ser vulnerables ante amenazas externas.
2. **Matriz EERR de Acciones de Valor:** Clasificá cada intervención en:
   - **Eliminar:** Pasos innecesarios, burocracia, dobles controles, documentos redundantes.
   - **Reducir:** Tiempos de espera (*lead times*), handoffs entre áreas, errores manuales.
   - **Incrementar:** Exactitud de inventario, nivel de servicio, frecuencia de información.
   - **Crear:** Nuevas capacidades, portales digitales de autoservicio, trazabilidad proactiva.
3. **Filtro de Restricciones Operativas:** Auditá cada acción contra Plazos, Presupuesto, Dependencia TI y Resistencia Organizacional.
4. **Mapeo de Procesos Afectados:** Explicitá qué procesos de soporte o adyacentes se ven modificados por la implantación de la acción.
   *Plantilla:* [templates/stage3_came_value_actions.md](templates/stage3_came_value_actions.md).

---

## Contrato de Salida

Entregá la resolución estructurada según la etapa solicitada o el paquete consolidado:
1. `Etapa 1`: Encuadre de negocio, análisis SDL, matriz de la Cadena de Valor Virtual y Matriz de Selección Ponderada de 5 Criterios con dictamen de proceso crítico.
2. `Etapa 2`: Matriz de Stakeholders completa y Matriz FODA con trazabilidad a evidencias de auditoría.
3. `Etapa 3`: Matriz de cruces estratégicos CAME, Inventario EERR de Acciones de Valor, Matriz del Filtro de Restricciones Operativas y tabla de procesos afectados.
