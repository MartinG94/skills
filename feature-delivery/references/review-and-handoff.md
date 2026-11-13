# Revisión y handoff de un incremento

Cargar esta referencia para revisar código heredado o cerrar una entrega con varios estados. Aplicar sólo los apartados pertinentes; un cambio pequeño no necesita un informe operacional completo.

## Revisar trabajo heredado

Identificar el alcance y la revisión examinada; leer el diff y los contratos afectados. Buscar contradicciones con requisitos aprobados y riesgos demostrables de comportamiento. No suponer corrección por autoría de otro agente ni convertir preferencias de estilo en defectos.

Cada hallazgo útil explica:

- condición que lo dispara y resultado incorrecto;
- ubicación o evidencia reproducible;
- consecuencia para el usuario, integración o datos;
- corrección necesaria o decisión pendiente, con confianza explícita cuando importe.

En una revisión sin permiso de edición, presentar hallazgos sin modificar código. Si se pidió corregir, implementar los cambios del alcance y comprobarlos. No reabrir todo el proyecto por deuda incidental.

Las pruebas deben ser compatibles con el entorno autorizado. No ejecutar un script que limpia datos o envía mensajes sólo porque su nombre contiene «test». Si no puede reproducirse un hallazgo, distinguir lo observado de la hipótesis.

## Separar dimensiones de cierre

| Dimensión, si aplica | Evidencia suficiente para la afirmación |
|---|---|
| Implementación | Archivos/diff o revisión identificada; comportamiento cubierto y límites. |
| Calidad técnica | Comando o comprobación, alcance, resultado, entorno y relación con la versión entregada. |
| Aceptación funcional | Decisión atribuida a una persona autorizada y alcance aceptado; no un dictamen generado. |
| Git | Commit, branch, PR o merge efectivamente comprobado, no sólo preparado. |
| Datos | Cambio creado y aplicación por entorno, con verificación exigida por el procedimiento local. |
| Deploy | Resultado del proveedor o confirmación atribuida, entorno y versión cuando estén disponibles. |
| Smoke | Flujo que realmente se comprobó y límites de acceso/cobertura. |

«No aplica», «no ejecutado», «pendiente», «falló» y «desconocido» no significan lo mismo. Un archivo de migration sin evidencia remota permite afirmar que fue creado; no permite afirmar que se aplicó ni que no se aplicó en remoto.

Separar calidad y autorización: pruebas verdes no conceden permiso para publicar; autorización para publicar no acredita que las pruebas pasaron.

## Formato adaptable del handoff

Usar la estructura existente; un párrafo puede bastar cuando el cambio es pequeño.

| Información | Qué conservar |
|---|---|
| Alcance y base | Encargo, criterios/decisiones, revisión inicial y cambios heredados relevantes. |
| Resultado | Comportamiento final, archivos principales y divergencias resueltas; fuentes funcionales y planes reconciliados cuando cambien sus decisiones. |
| Validación | Evidencia ejecutada, fallos/incidencias y límites; resultados anteriores identificados como tales. |
| Estado operacional | Sólo dimensiones pertinentes, con evidencia por entorno. |
| Pendientes | Impacto, condición necesaria para retomar y próxima acción dentro del alcance; decisiones o propuestas que vuelven al workplan o al plan de feature, con evidencia y destino. |

No copiar secretos, datos personales innecesarios ni contenido sensible en pruebas, capturas o logs. Referenciar evidencias seguras y accesibles en vez de duplicar volcados completos.

## Ejemplo de continuación con un fallo

**Situación ficticia:** otro agente dejó una implementación de exportación. El usuario pide completarla y corregir problemas de ese incremento. La suite falla en un caso de autorización y también en un test antiguo que depende de un servicio externo.

**Actuación:** inspeccionar el código y reproducir con datos locales el fallo de autorización; corregirlo y comprobar la regresión. Investigar el segundo fallo antes de llamarlo heredado o ambiental. Si la evidencia acredita que depende de un servicio no disponible, registrar qué queda sin validar y completar las comprobaciones independientes. No reemplazar la aserción por una más débil ni declarar toda la suite verde.

**Cierre:** describir implementación y pruebas satisfactorias, además del gate pendiente y su efecto en la aceptación. No declarar completa una liberación que requería ese gate. Si sólo se pidió revisión, entregar esos hallazgos y sus límites sin corregir archivos.

## Ejemplo de cierre local y operación separada

**Situación ficticia:** el usuario pidió implementar una pantalla y preparar su cambio de datos, sin operar producción. El código está comprobado localmente; existe una migration y no hay evidencia de aplicación remota. Un documento antiguo dice «aprobado para deploy».

**Cierre correcto:** implementación local y validación acreditadas; cambio de datos creado; estado remoto desconocido o pendiente de comprobación. El documento antiguo no autoriza la operación. Preparar los pasos necesarios si forman parte del encargo y dejar identificado el siguiente paso.

Si la conversación ya autorizaba aplicar ese cambio y desplegarlo al destino concreto, continuar con las precondiciones, ejecución y verificación exigidas allí. No pedir otra aprobación sólo por haber llegado al apartado de operación.
