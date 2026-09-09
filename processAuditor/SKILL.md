---
name: processAuditor
description: >-
  Audita y diagnostica integralmente procesos operativos de negocio en la Etapa 2 de Gestión y Mejora
  de Procesos (GMP). Evalúa los 4 ejes de la guía oficial GUI_U2: 1) Control Interno (COSO, salvaguarda de activos,
  segregación de funciones SoD, autorizaciones y conciliaciones); 2) Formularios y Ruta Documental (diseño, copias,
  legibilidad y archivo); 3) Factores Humanos y Condiciones Laborales (ergonomía física/cognitiva, tiempos muertos y
  sobrecarga burocrática); 4) Soporte Informático y Silos TI (recapturas manuales, fragmentación y seguridad).
license: MIT
allowed-tools: [Bash, Read, Write]
metadata: {"author":"Agents365-ai / Antigravity","version":"1.0.0","category":"analysis","platforms":["windows","macos","linux"]}
---

# Process Diagnostic Auditor (GUI_U2 / COSO)

Audita procesos de negocio a partir de entrevistas, minutas de relevamiento o narrativas operativas, identificando debilidades estructurales que fundamentan con evidencia fáctica las debilidades del análisis FODA y los puntos de intervención del rediseño.

## Límites de Autoridad

- Cada hallazgo debe estar anclado a un localizador fáctico (`EV-xx`) de la transcripción o relato; no asumas fallas de control que no tengan respaldo en la fuente.
- Distinguí entre controles ausentes (vacío normativo) y controles defectuosos (controles existentes que fallan o son eludidos).
- No inventes tecnologías, montos de pérdida económica ni responsabilidades personales no documentadas.

---

## Los 4 Ejes de Auditoría (`GUI_U2`)

### Eje 1: Control Interno y Segregación de Funciones (COSO)
Evalúa los riesgos sobre activos, inventarios y fondos:
- **Custodia vs. Registro:** Quien custodia el activo no debe registrar sus movimientos en sistema.
- **Autorización vs. Ejecución:** Quien aprueba una transacción no debe ser el ejecutor directo.
- **Conciliación Independiente:** Conteos físicos, arqueos y conciliaciones bancarias deben ser ejecutados por personal ajeno a la custodia y al registro diario.
- *Plantillas:* [templates/risk_control_matrix_template.md](templates/risk_control_matrix_template.md) y [templates/segregation_of_duties_matrix.md](templates/segregation_of_duties_matrix.md).

### Eje 2: Formularios y Ruta Documental
Evalúa la eficiencia y formalidad del flujo de papeles y comprobantes:
- Identificación unívoca, numeración preimpresa o correlativa y codificación de versión.
- Justificación estricta de copias (Original, Duplicado, Triplicado) y su ruta física.
- Legibilidad, erradicación de manuscritos sobre impresos y eliminación de sellos/firmas redundantes.
- Archivo transitorio vs. archivo definitivo y protocolo de digitalización.
- *Plantilla:* [templates/document_routing_checklist.md](templates/document_routing_checklist.md).

### Eje 3: Factores Humanos y Condiciones Laborales
Evalúa el impacto ergonómico, ambiental y motivacional sobre los operarios:
- Ergonomía física (cargas pesadas, posturas forzadas) y cognitiva (memorización de códigos, pantallas confusas).
- Tiempos muertos por bloqueos administrativos o esperas de supervisores.
- Sobrecarga burocrática por doble registro (cuadernos personales + planillas).
- *Plantilla:* [templates/human_factors_checklist.md](templates/human_factors_checklist.md).

### Eje 4: Soporte Informático y Silos TI
Evalúa la madurez digital y conectividad del ecosistema informático:
- Identificación de aplicaciones aisladas (silos departamentales) que no sincronizan datos.
- Recapturas manuales de información entre sistemas (ej. copiar datos de emails/Excel a ERP).
- Discrepancias de datos y ausencia de una única fuente de verdad (*single source of truth*).
- Vulnerabilidades de acceso: usuarios compartidos, falta de logs de auditoría o permisos excesivos.
- *Plantilla:* [templates/it_silos_checklist.md](templates/it_silos_checklist.md).

---

## Flujo de Trabajo

1. **Extracción de Hechos Operativos:** Identificá afirmaciones del caso que evidencien fallas, demoras o fricciones.
2. **Clasificación en los 4 Ejes:** Asigná cada hecho a su eje temático correspondiente.
3. **Ponderación de Riesgo:** Calculá Severidad ($P \times I$) para la Matriz de Riesgos y Controles (RCM).
4. **Análisis de Incompatibilidades:** Mapeá roles contra funciones en la Matriz SoD.
5. **Emisión de Recomendaciones de Mitigación:** Proponé controles preventivos, automatizaciones de interfaz o reasignaciones organizacionales viables.

---

## Contrato de Salida

Entregá el reporte diagnóstico estructurado en:
1. `Resumen Ejecutivo del Diagnóstico`: Principales riesgos y áreas críticas.
2. `Matriz de Riesgos y Controles (RCM)`: Tabla detallada con severidad y control propuesto.
3. `Matriz de Segregación de Funciones (SoD)`: Incompatibilidades detectadas y separación recomendada.
4. `Diagnóstico de Ruta Documental y Formularios`: Evaluación de comprobantes y archivos.
5. `Evaluación Ergonómica y Factores Humanos`: Puntos de fricción, tiempos muertos y sobrecarga.
6. `Mapa de Brechas de Silos Informáticos`: Oportunidades de integración y automatización de datos.
7. `Entradas para FODA (Debilidades Fácticas)`: Lista de enunciados listos para ser consumidos por `processWorkbench`.
