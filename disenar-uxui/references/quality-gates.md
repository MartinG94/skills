# Gates de calidad y evidencia

Lee esta referencia antes de validar y entregar. Deriva los escenarios del brief y ejecuta solo checks pertinentes, pero no omitas un gate aplicable por falta de tiempo sin decirlo.

## Gate 1: alcance y contenido

- La tarea principal y los criterios de aceptación están reflejados en la UI.
- El contenido es concreto, coherente y está en el idioma solicitado.
- Los datos simulados se distinguen de datos reales.
- No hay acciones prometidas sin comportamiento ni navegación falsa.
- No se modificó funcionalidad o trabajo ajeno fuera del alcance.
- No hay consentimiento engañoso, urgencia falsa, tracking no pedido ni un camino de cancelación deliberadamente más difícil.

## Gate 2: funcionamiento

Recorre el camino principal y las alternativas relevantes:

- navegación y enlaces;
- acciones primarias y secundarias;
- formularios, validación, envío y conservación de datos;
- valores vacíos, formatos inválidos, límites de rango y dependencias entre campos;
- corrección error por error: el valor válido se conserva, desaparecen mensajes obsoletos y cada enlace de recuperación enfoca un objetivo existente;
- carga, vacío, error, éxito, permisos y reintento cuando existan;
- modales, menús, tabs, filtros o drawers realmente implementados;
- persistencia o integración con datos según el contrato real.

Registra qué escenario se ejecutó y su resultado. Una revisión del código no sustituye la interacción.

## Gate 3: visual y responsive

- Inspecciona al menos un viewport estrecho, uno intermedio y uno amplio, además de redimensionar a través de los puntos donde cambie el layout; no valides solo los extremos.
- Varía también la altura cuando existan regiones `sticky`/`fixed`, overlays o teclado virtual, y comprueba que ninguna acción quede atrapada fuera del viewport.
- Comprueba jerarquía, alineación, ritmo, densidad, foco visual y consistencia.
- Busca recortes, superposición, scroll horizontal, contenido fuera de pantalla, saltos de layout, líneas huérfanas y assets borrosos.
- Prueba contenido largo, zoom y aumento de texto cuando sean relevantes.
- Si el layout oculta o abrevia etiquetas, confirma que el nombre y el contexto sigan presentes para tecnologías de asistencia.
- Captura o inspecciona visualmente los estados críticos, no solo la pantalla inicial.
- Corrige y vuelve a revisar las superficies afectadas.

## Gate 4: accesibilidad manual

- Recorre con teclado en orden lógico y con foco siempre visible.
- Activa cada control con las teclas definidas por su semántica o patrón.
- Comprueba nombres accesibles, labels, encabezados, landmarks, alt y mensajes dinámicos.
- En controles repetidos, verifica que cada nombre accesible identifique también el objeto; después de filtros o rerenders, confirma que el foco no se pierda.
- Verifica apertura/cierre y restauración de foco en overlays.
- Calcula contraste de texto —incluido placeholder—, límites de componentes y foco sobre los fondos reales.
- Verifica que el estado no dependa solo de color y que reduced motion no elimine información.
- Prueba reflow/zoom y targets pertinentes.

Si existe un scanner configurado, ejecútalo como complemento. No declares conformidad WCAG completa sin alcance y pruebas suficientes.

## Gate 5: ingeniería

- Ejecuta build, typecheck, lint y tests existentes que cubran el cambio.
- Revisa consola del navegador, errores no capturados, warnings relevantes, requests fallidos y 404.
- Comprueba rutas directas y refresh cuando haya routing.
- Evita secretos, tracking no pedido, contenido dinámico inseguro y dependencias innecesarias.
- Revisa el diff o la lista de archivos para detectar cambios accidentales.

Separa fallas causadas por el cambio de fallas previas o fuera de alcance.

## Gate 6: preview y handoff

Antes de entregar:

- la URL exacta responde y fue abierta;
- el servidor sigue activo o la limitación está documentada;
- el usuario puede reproducirlo con el comando informado;
- se enumeran archivos, escenarios, checks y resultados;
- se declaran supuestos, datos simulados, límites y riesgos restantes.

Usa lenguaje preciso: “pasó los escenarios X e Y” es evidencia; “garantizado”, “100 % accesible” o “pixel perfect” requieren una base que rara vez existe.
