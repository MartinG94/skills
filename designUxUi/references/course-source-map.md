# Trazabilidad y calibración del curso UX/UI

Esta referencia documenta de dónde provienen los principios sintetizados en la skill. No es necesaria para implementar un frontend ordinario. Léela para justificar decisiones académicamente, volver a auditar la fidelidad al material o resolver una regla discutible.

## Corpus

La síntesis se realizó sobre 18 PDFs (288 páginas) del curso “[UX] Experiencia e Interfaces de Usuario (Elec.)”, incluyendo la presentación, las clases 1 a 13 y cuatro variantes 2026 sobre layouts, móvil, plataformas y discapacidad.

Los PDFs no se incluyen en la skill: son material fuente local y el paquete debe ser portable. Esta referencia conserva una síntesis transformativa y la ubicación de la evidencia, no una copia de las diapositivas.

## Principio de uso

- Conserva conceptos estables: diseño centrado en personas, contexto, arquitectura de información, jerarquía, feedback, consistencia, accesibilidad, adaptación por plataforma y evaluación.
- Convierte listas y leyes en preguntas de revisión; no transforma ejemplos de clase, cifras aisladas o convenciones de una plataforma en mandatos universales.
- Prefiere el estándar vigente y una prueba observable cuando una diapositiva, la skill original y una norma técnica difieren.
- No atribuye a los PDFs conceptos que provienen de la auditoría técnica o de estándares actuales.

## Mapa de fuentes

La numeración corresponde a la página física del PDF.

### Fundamentos, investigación y evaluación

| Fuente | Aportes incorporados | Calibración |
|---|---|---|
| `01_UXUI_Presentacion.pdf` | alcance del proceso, investigación, necesidades, prototipado, evaluación, accesibilidad e integración (pp. 9, 11) | pp. 12-17 son información institucional, no workflow |
| `02_UXUI_Clase-01.pdf` | UX/UI, utilidad, usabilidad, accesibilidad, deseabilidad y equilibrio entre tarea y percepción (pp. 2-8, 17-18) | la división UX/UI de pp. 9-16 es pedagógica y no define silos rígidos; no repetir cifras promocionales sin fuente |
| `03_UXUI_Clase-02.pdf` | ciclo iterativo, investigación cualitativa/cuantitativa, ética, triangulación, síntesis, IA, requisitos, trazabilidad y priorización (pp. 14-24) | pp. 2-13 contienen empresas y datos temporales |
| `04_UXUI_Clase-03.pdf` | personas basadas en patrones, investigación, clustering, validación y actualización (pp. 4-22) | cantidades, demografía y cita de “dos clics” son ejemplos, no cuotas; pp. 23-24 son herramientas/consigna |
| `05_UXUI_Clase-04.pdf` | flows, journeys, decisiones, alternativas, fricción y validación (pp. 2-13) | mobile-first y login social son opciones contextuales; p. 14 es práctica |
| `06_UXUI_Clase-05.pdf` | fidelidad de prototipo según riesgo, interacción e iteración (pp. 2-11) | la secuencia idea-wireframe-prototipo no es cascada; marcas de herramientas pueden caducar; pp. 12-13 son consigna/cierre |
| `07_UXUI_Clase-06.pdf` | efectividad, eficiencia, satisfacción, heurísticas de Nielsen, SUS, tareas, observación y priorización (pp. 3-15) | SUS requiere participantes y no sustituye pruebas cualitativas; p. 16 es práctica |
| `08_UXUI_Clase-07.pdf` | privacidad, transparencia, inclusión, seguridad y rechazo de dark patterns (pp. 2-13) | conservar patrones éticos, no reputaciones cambiantes de marcas; p. 13 es consigna |
| `09_UXUI_Clase-08.pdf` | simplicidad, consistencia, jerarquía, feedback, recuperación y accesibilidad (pp. 4-15) | F/Z, CTA y design systems de plataforma son heurísticas/versiones, no leyes |
| `10_UXUI_Clase-09.pdf` | botones, enlaces, navegación, formularios, errores, estados, imágenes e iconos (pp. 3-13) | placeholder no sustituye label; validar por color o siempre “en tiempo real” no es universal; p. 14 es consigna |

### Layouts, móvil, plataformas y discapacidad

| Fuente | Aportes incorporados | Calibración |
|---|---|---|
| `11_UXUI_Clase-10_Diseño-de-Layouts.pdf` | proximidad, alineación, repetición, contraste, grillas, espacio, jerarquía y formularios (pp. 3-12) | 12 columnas, simetría y patrones F/Z son repertorio, no requisitos |
| `2026_11_UXUI_Clase-10_Diseño-Layouts_G13.pdf` | balance, tercios, anatomía/tipos de grilla, proximidad, jerarquía, escala y responsive (pp. 2-5, 11-16) | descartar porcentajes sin respaldo, “puntos neurológicos” y “matemáticas perfectas”; 12/6/1 es ilustración |
| `12_UXUI_Clase-11.pdf` | prioridad móvil, navegación, gestos, alcance, conectividad, performance, feedback y accesibilidad (pp. 3-9) | mobile-first, hamburger, bottom nav, cards e infinite scroll son patrones contextuales; 44 px no es baseline web universal |
| `2026_12_UXUI_Diseno-de-Interfaces-para-Dispositivos-Moviles.pdf` | contexto móvil, web/nativo, formularios, capacidades, estados y prueba real (pp. 2-9) | no usar cinco segundos ni cifras aisladas como criterio universal; reconciliar unidades por plataforma |
| `13_UXUI_Clase-12_Interfaces-diferentes-plataformas.pdf` | identidad compartida y adaptación de navegación, densidad e interacción por plataforma (pp. 2-9) | consultar HIG/Material/Fluent vigentes; web, móvil y escritorio no son entradas excluyentes |
| `2026_13_UXUI_Clase-12_G09_Diseno-de-Interfaces-para-diferentes-plataformas.pdf` | contexto, patrones y continuidad entre plataformas (pp. 2-11) | sintetiza el material anterior; usar como complemento visual, no norma |
| `14_UXUI_Clase-13.pdf` | POUR, tipos de discapacidad, semántica, teclado, contraste, alternativas y checklist (pp. 3-17) | referencias a herramientas/atajos pueden caducar; scans automáticos no certifican |
| `2026_14_UXUI_Clase-13_G4_Interfaces-para-Discapacidades.pdf` | discapacidad permanente/temporal/situacional, necesidades cognitivas, motoras y visuales (pp. 2-12) | sans-serif, 16 px y line-height 1.5 no son fórmulas WCAG; evitar porcentajes de detección y “funciona para todos” |

Las variantes 2026 amplían visualmente las unidades, pero algunas muestran señales de generación y afirmaciones sin fuente. Por eso se usan para enriquecer preguntas y escenarios, no para crear requisitos normativos.

## Correcciones normativas aplicadas

La skill original contenía ratios de contraste calculados incorrectamente, un target táctil universal de 44/48 y un modal incompleto. La versión revisada usa estos mínimos como criterios verificables, no como promesas:

- WCAG 2.2 SC 1.4.3: contraste mínimo de texto 4.5:1, o 3:1 para texto grande definido por la norma.
- WCAG 2.2 SC 1.4.11: contraste no textual evaluado en los componentes y estados donde aplica.
- WCAG 2.2 SC 2.5.8 AA: target de 24 × 24 CSS px o una excepción aplicable, incluido el espaciado; áreas mayores siguen siendo una buena práctica contextual.
- WAI-ARIA APG Dialog Modal: fondo inerte, foco dentro del diálogo, nombre accesible, Escape y retorno de foco coherente.

Referencias normativas:

- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
