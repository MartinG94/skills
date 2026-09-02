# Implementación y preview local

Lee esta referencia antes de ejecutar toolchains, instalar dependencias o levantar localhost.

## 1. Descubrir el runtime

En una aplicación existente, identifica antes de ejecutar:

- instrucciones del repositorio y límites del workspace;
- framework y versión;
- `package.json` u otro manifiesto, scripts y configuración;
- lockfile y package manager efectivo;
- runtime disponible;
- variables de entorno requeridas sin imprimir secretos;
- puertos, base paths, proxy y rutas relevantes;
- servidor que ya pueda estar activo.

No cambies de gestor, regeneres lockfiles ni actualices dependencias como efecto lateral de un trabajo visual.

## 2. Elegir cómo ejecutar

Prioridad:

1. script documentado por el repositorio;
2. script `dev`, `start` o `preview` ya definido y compatible con el objetivo;
3. comando oficial del framework instalado;
4. helper estático de esta skill para HTML/CSS/JS sin servidor propio.

Instala dependencias solo si son necesarias para el entregable, faltan realmente y el entorno lo autoriza. Usa el lockfile presente y evita ejecutar material descargado o scripts de paquetes no confiables sin evaluar el riesgo.

## 3. Preview estático portable

Para un directorio estático con `index.html`, resuelve primero un intérprete Python 3 disponible (`python3`, `python`, `py -3` o el runtime provisto por el entorno) y úsalo así:

```text
python <ruta-de-la-skill>/scripts/serve_preview.py --root <directorio-del-frontend> --port 0
```

Agrega `--spa` únicamente si una app estática necesita fallback de rutas del navegador. El helper:

- usa solo la biblioteca estándar;
- enlaza por defecto a `127.0.0.1`;
- elige un puerto libre cuando recibe `--port 0`;
- imprime `PREVIEW_URL=...`;
- bloquea dotfiles, symlinks y listados de directorio;
- valida el header `Host` y no ofrece una opción de bind externo.

Pasa como `--root` una carpeta publicable que contenga solo el frontend construido. No sirvas la raíz del repositorio, una carpeta con `.env`, credenciales, fuentes privadas o archivos ajenos al preview.

## 4. Ciclo de vida del servidor

- Inicia el proceso en una sesión que pueda permanecer viva y conservar logs.
- Espera una señal de readiness o la URL anunciada sin bloquear indefinidamente.
- Si el puerto está ocupado, usa uno libre; no termines procesos ajenos.
- Comprueba por HTTP la ruta inicial y las rutas críticas.
- Abre la URL con la herramienta de navegador disponible y confirma que el documento renderiza.
- Revisa consola, errores de runtime, recursos fallidos y rutas 404.
- Mantén el proceso activo para que el usuario interactúe, salvo que pida detenerlo o el entorno no lo permita.
- Registra el comando, URL, sesión/proceso y forma de detenerlo. No afirmes que sigue activo si terminó.

## 5. Fallas y límites

Cuando el servidor no inicia:

1. captura el primer error accionable;
2. distingue código del cambio, configuración, dependencia faltante, permisos, puerto y falla previa;
3. aplica una corrección local y proporcional si está dentro del alcance;
4. limita reintentos y reporta el bloqueo con comando y salida relevante.

No eludas políticas de sandbox, red o aprobación para conseguir un preview. Si no puede mantenerse un proceso, entrega un comando reproducible y explica qué parte sí se verificó.
