# Manual práctico: NotebookLM MCP en Antigravity

## Estado de esta instalación

El servidor queda configurado para ejecutarse con:

    C:\Program Files\nodejs\npx.cmd -y notebooklm-mcp@latest

Se usa npx.cmd porque en esta máquina PowerShell bloquea npx.ps1 por su política de ejecución.

NotebookLM MCP v2 es una integración comunitaria que automatiza Chrome; no es una API oficial de Google. Las respuestas son generadas por Gemini a partir de las fuentes del cuaderno y sus citas deben revisarse antes de usarlas como dato definitivo.

## Primer inicio de sesión

1. Reinicia Antigravity para que recargue C:\Users\Diego\.gemini\config\mcp_config.json y la Skill.
2. En el chat, escribe: Iniciá sesión en NotebookLM.
3. El agente debe llamar a setup_auth con show_browser: true.
4. Se abrirá una ventana de Chrome. Inicia sesión allí con la cuenta de Google que contiene los cuadernos y termina cualquier verificación de Google.
5. Vuelve al chat y pide: Verificá el estado de NotebookLM.

El resultado correcto es authenticated: true en get_health. La sesión se conserva como perfil local de Chrome en:

    C:\Users\Diego\AppData\Local\notebooklm-mcp\Data\chrome_profile

No compartas tu contraseña, cookies, códigos de doble factor ni tokens para pegarlos en un archivo. No hay que hardcodear credenciales: la sesión persistente del perfil de Chrome es el mecanismo previsto por este servidor.

### Por qué npx -y notebooklm-mcp auth no abre Chrome

Ese subcomando no es el flujo de autenticación de la versión v2. npx únicamente inicia el servidor MCP. La ventana de login aparece cuando un cliente MCP invoca setup_auth. Además, en PowerShell npx puede quedar bloqueado porque resuelve a npx.ps1; si necesitas ejecutar una orden de npx manualmente, usa:

    & 'C:\Program Files\nodejs\npx.cmd' -y notebooklm-mcp@latest config get

Este comando solo muestra la configuración; no inicia sesión. No uses auth como argumento.

## Uso diario

### 1. Registrar y listar cuadernos

El MCP no puede descubrir automáticamente todos los cuadernos de tu cuenta. Primero registra el enlace compartido de cada cuaderno:

    Agregá este cuaderno a la biblioteca: https://notebooklm.google.com/notebook/...; nombre: Final de Simulación; descripción: apuntes y ejercicios; temas: simulación, colas.

Luego pide:

    Listá mis cuadernos de NotebookLM.

El agente mostrará los cuadernos de la biblioteca local, con sus ID. Para elegir uno:

    Usá el cuaderno Final de Simulación como activo.

### 2. Consultar con referencias

    Preguntale al cuaderno activo cuáles son las hipótesis del modelo. Respondé con citas al pie.

El agente debe pedir a NotebookLM source_format: footnotes y conservar las referencias devueltas. Si necesitas procesarlas en código, pide formato JSON de fuentes.

### 3. Continuar una conversación

    Sobre la respuesta anterior, ¿cuál de esas hipótesis es la más restrictiva? Conservá el contexto.

El agente reutiliza el session_id de la consulta anterior. Para cambiar completamente de tema:

    Hacé esta pregunta en un contexto nuevo: ...

### 4. Agregar fuentes

Solo después de confirmarlo, puedes usar:

    Agregá esta web al cuaderno activo: https://ejemplo.com/articulo

O:

    Agregá esta nota de texto al cuaderno activo: "..."

La versión instalada admite URLs web y texto pegado. No admite subir PDFs, archivos locales, Drive, YouTube o videos mediante MCP. Después, el agente debe informar los recuentos antes/después que devuelve el servidor.

## Problemas frecuentes

| Problema | Acción recomendada |
| --- | --- |
| No se abre el navegador | Pedí al agente Iniciá sesión en NotebookLM; eso debe ejecutar setup_auth, no un comando auth de npx. |
| npx bloqueado por PowerShell | Ejecuta npx.cmd con la ruta completa mostrada arriba. No cambies la política de ejecución del sistema para esto. |
| Chrome no inicia o se cierra | Conserva el error; puede cambiarse el canal a Chromium incluido. No borres datos ni reautentiques sin revisar antes. |
| authenticated: false | Repite setup_auth y completa el login. Para cuentas distintas o sesión dañada, solicita una reautenticación explícita. |
| Lista de cuadernos vacía | Registra el enlace compartido de cada cuaderno con add_notebook; la lista es local. |
| No hay citas | Repite la consulta pidiendo source_format footnotes o json; no inventes referencias. |

## Archivos locales relevantes

- Configuración MCP: C:\Users\Diego\.gemini\config\mcp_config.json
- Instrucciones para agentes: C:\Users\Diego\.gemini\config\skills\notebooklm\SKILL.md
- Este manual: C:\Users\Diego\.gemini\config\skills\notebooklm\manual_notebooklm_mcp.md
- Perfil de sesión: C:\Users\Diego\AppData\Local\notebooklm-mcp\Data\chrome_profile

No copies ni sincronices el perfil de sesión a repositorios, Drive o servicios compartidos.
## Compatibilidad con el cambio de dominio de Google

Google ahora redirige la autenticación a notebook.google.com. La versión v2.0.0 instalada solo reconocía notebooklm.google.com y por eso setup_auth quedaba esperando aunque la sesión ya estuviera iniciada. Se aplicó un parche local de compatibilidad en el paquete instalado y Antigravity inicia esa copia con node.exe. No reemplaces esta configuración por npx hasta que una versión posterior del paquete reconozca notebook.google.com de forma nativa.
