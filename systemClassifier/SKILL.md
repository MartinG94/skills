---
name: system-classifier
description: Analiza un sistema de información, clasifica sus capacidades como TPS/MIS/DSS/ESS/KMS/AI, evalúa prefactibilidad técnica-económica-operativa o ubica artefactos en PUD. Selecciona un modo según la pregunta y basa todo dictamen en evidencia; no crea arquitectura, cifras, cronogramas ni tecnología faltante.
---

# System Classifier

Responde una pregunta de encuadre concreta. No ejecutes diagnóstico, clasificación, prefactibilidad y PUD en cadena salvo que el usuario solicite expresamente un informe combinado.

## Modos

- **Diagnóstico de SI:** delimitar objetivo, entradas, proceso, salidas, retroalimentación y componentes.
- **Clasificación de SI:** clasificar capacidades como TPS, MIS, DSS, ESS, KMS o AI/sistema experto.
- **Prefactibilidad:** evaluar dimensiones técnica, económica y operativa.
- **Contexto PUD:** ubicar objetivos, artefactos, riesgos o trabajo pendiente en Inicio, Elaboración, Construcción o Transición.

Si la petición es ambigua, elige el modo que responde directamente al verbo del usuario y declara la elección. Usa [templates/prefeasibility_and_pud_report_template.md](templates/prefeasibility_and_pud_report_template.md) solo para informes formales; elimina las secciones de modos no solicitados.

## Reglas de evidencia

- Asigna IDs a fuentes y conserva página, sección, párrafo o marca de tiempo.
- Para cada conclusión cita evidencia y marca `explícita`, `derivada` o `NO DETERMINADO`.
- Una derivación incluye razonamiento breve y queda pendiente de validación.
- No inventes usuarios, módulos, niveles decisorios, hardware, stack, costos, beneficios, volúmenes, normativa, fechas, duraciones, iteraciones ni porcentajes.
- No transformes una recomendación en decisión aprobada.
- Conserva alternativas contradictorias y formula la decisión pendiente.

Lee solo la sección pertinente de [references/tgs_and_pud_handbook.md](references/tgs_and_pud_handbook.md) cuando necesites los criterios de clasificación o fase.

## Diagnóstico de sistema de información

Un sistema de información coordina información, personas y procedimientos para apoyar operaciones, control, gestión o decisiones; puede ser manual o computarizado y no equivale al software.

Identifica únicamente con evidencia:

- objetivo;
- entradas;
- transformación/proceso;
- salidas;
- retroalimentación/control;
- personas, procedimientos, datos, hardware y software conocidos;
- límite, entorno e interfaces relevantes.

No derives módulos o arquitectura desde estos componentes.

Salida: tabla `Elemento | Origen | Evidencia | Interpretación/derivación | Estado` y preguntas pendientes.

## Clasificación de SI

Clasifica capacidades, no necesariamente el producto completo:

- `TPS`: operaciones rutinarias, estructuradas y de volumen transaccional;
- `MIS`: información o reportes regulares para gestión y control;
- `DSS`: apoyo interactivo o ad hoc a decisiones semiestructuradas/no estructuradas;
- `ESS`: información agregada para dirección estratégica;
- `KMS`: creación, organización o difusión de conocimiento;
- `AI/experto`: inferencia o recomendación basada en conocimiento/modelos.

Una capacidad puede tener más de una etiqueta si cada una tiene evidencia. ERP, CRM o SCM pueden describir alcance de un producto empresarial, pero no sustituyen esta clasificación académica.

Salida predeterminada:

| Capacidad | Tipo(s) | Nivel/decisión si consta | Origen | Evidencia | Justificación / derivación | Estado |
| --- | --- | --- | --- | --- | --- | --- |

No asignes nivel operativo, táctico o estratégico por el nombre de la categoría solamente.

## Prefactibilidad

Evalúa por separado:

1. **Técnica:** recursos y capacidad técnica disponibles, infraestructura/equipamiento necesario, compatibilidad y brechas comprobadas.
2. **Económica:** costos, beneficios y disposición/capacidad de inversión conocidos; distingue tangibles e intangibles.
3. **Operativa:** aceptación, adecuación al trabajo, capacitación, resistencia e impacto en procedimientos.

Dictamen de cada dimensión y de la prefactibilidad consolidada: `FAVORABLE`, `CONDICIONADA`, `DESFAVORABLE` o `NO DETERMINADO`. El resultado global solo puede ser concluyente si las tres dimensiones tienen evidencia suficiente; en otro caso enumera los datos necesarios.

Calcula ROI, recupero, VAN o TIR únicamente si el usuario los pide y proporciona los flujos, horizonte, moneda y, cuando corresponda, tasa. Muestra fórmula y supuestos; nunca completes valores de ejemplo.

Restricciones legales, organizacionales o temporales se registran si la fuente las menciona, pero no se convierten automáticamente en nuevas dimensiones obligatorias.

## Contexto PUD

PUD es dirigido por casos de uso, centrado en arquitectura, iterativo e incremental. Usa sus fases como marco, no como cronograma predeterminado:

- **Inicio:** visión/producto, negocio, alcance y funciones principales, arquitectura inicial, riesgos, plan y presupuesto.
- **Elaboración:** especificación de CU significativos y consolidación de arquitectura/riesgos.
- **Construcción:** creación e integración del producto.
- **Transición:** instalación, evaluación de usuarios y ajustes para entrega.

Mapea evidencia existente y faltantes por fase o flujo. No declares avance de fase, hitos cumplidos, cantidad de iteraciones, fechas o distribución de esfuerzo sin criterios y datos del proyecto.

Salida: `Elemento | Fase/flujo | Origen | Evidencia | Derivación/estado | Falta para decidir`.

## Criterio de término

- El informe responde solo al modo pedido.
- Cada clasificación y dictamen tiene evidencia o `NO DETERMINADO`.
- SI, software y producto empresarial no se confunden.
- La prefactibilidad conserva sus tres dimensiones institucionales.
- Los cálculos reproducen únicamente datos suministrados.
- PUD no contiene cronograma, porcentajes ni gates inventados.
- Los vacíos terminan en preguntas accionables, no en supuestos ocultos.
