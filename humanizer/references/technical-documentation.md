# Guía de Redacción y Humanización para Documentación Técnica

Basada en los estándares de calidad de ingeniería de Vercel Eve y buenas prácticas de documentación para desarrolladores.

---

## 1. Principio Fundamental: Verificación antes de Escribir

La documentación técnica para desarrolladores y agentes exige **máxima fidelidad fáctica**. 
Nunca inventar comportamiento, parámetros, flags o garantías de plataforma para hacer que un párrafo suene más fluido o completo.

### Jerarquía de Fuentes de Verdad
1. Código fuente actual, tipos públicos (`TypeScript`, `Go`, `Rust`, etc.) y suites de pruebas reales.
2. Ayuda de la CLI (`--help`) e implementación de comandos en el repositorio.
3. Páginas de documentación existentes y contratos OpenAPI/REST validados.
4. Notas de versión (*release notes*) y commits mergeados.
5. Issues y discusiones técnicas (para entender el dolor del usuario, no para inferir comportamiento).

> [!WARNING]
> Si una afirmación no puede verificarse empíricamente en el código o en la base de datos, **omítela o consúltala**. No dejes marcadores no resueltos en entregables finales.

---

## 2. Redactar Orientado a la Tarea (Task-Focused)

- **Liderar con el resultado**: Comenzar cada sección con la respuesta, el comando o el desenlace concreto. Evitar preámbulos y rodeos introductorios (*throat-clearing*).
- **Tratar al lector en segunda persona**: Dirigirse como "tú" / "vos" o mantener una voz instructiva directa.
- **Voz activa y verbos imperativos**: Emplear verbos en infinitivo o imperativo para pasos de ejecución (`Ejecuta el script`, `Configura la variable`, `Valida el token`).
- **Camino feliz primero**: Describir primero el flujo estándar sin errores; ubicar el manejo de excepciones, fallos de red y casos de borde en apartados posteriores o de resolución de problemas (*troubleshooting*).
- **Secciones autocontenidas**: No abusar de pronombres ambiguos ("este", "aquello", "dicho componente"). Repetir el nombre exacto del módulo o símbolo cuando sea necesario para permitir lectura modular.

---

## 3. Calidad de Prosa Técnica (Prose Quality)

### Edición Mínima Efectiva
- Respeta la intención, hechos y matices del autor original.
- Si una oración técnica ya es precisa y clara, no la reescribas solo por variar sinónimos.
- Mantén la terminología oficial del proyecto (nombres de funciones, tablas, comandos) de manera consistente.

### Errores Comunes a Erradicar en Documentación
1. **Elogios artificiales de marketing**: Suprimir calificativos vacíos como *seamless*, *robusto*, *revolucionario*, *potente*, *intuitivo*. Explicar la mecánica concreta: en vez de "un mecanismo robusto de recuperación", escribir "reintenta hasta tres veces con retroceso exponencial".
2. **Afirmaciones de facilidad**: Eliminar "simplemente", "fácilmente", "de manera trivial", "en tan solo un paso". Lo que para el autor es simple puede ser frustrante para un usuario lidiando con un error de dependencias.
3. **Preguntas retóricas**: Evitar estructurar párrafos con auto-preguntas infantiles (*"¿Por qué es esto importante? Bueno, porque..."*). Ir directo al punto.
4. **Revelaciones tras dos puntos**: Evitar la trampa retórica de preparar una revelación dramática con dos puntos cuando la frase funciona sola.
5. **Cierres redundantes**: No terminar guías técnicas con un párrafo que empiece con "En resumen" o "En conclusión" repitiendo lo dicho; finalizar en la última acción o paso siguiente.

---

## 4. Estructuración de Procedimientos y Resolución de Problemas

### Listas y Pasos Operativos
- Usa listas numeradas exclusivamente para secuencias con orden de ejecución estricto.
- Inicia cada paso con un único verbo de acción imperativo (*"Ejecuta `npm test`"*, *"Añade el secreto en `.env`"*).
- Si un paso requiere explicación, escribe oraciones completas terminadas en punto.

### Tablas de Troubleshooting (Síntoma Primero)
Cuando varios fallos comparten un flujo de trabajo, documenta con una tabla orientada a síntomas:

| Síntoma Observable | Verificación / Diagnóstico | Acción de Recuperación |
|---|---|---|
| Fallo visible o código de error | Comando o archivo de log verificado | Paso de mitigación soportado |

No afirmes una causa raíz a menos que exista evidencia empírica que la respalde. Si varios motivos producen el mismo síntoma, explica cómo distinguirlos antes de sugerir el arreglo.

---

## 5. Revisiones Técnicas (Review-Only Requests)

Si un usuario solicita auditar o revisar documentación existente sin reescribirla:
1. Reporta hallazgos concisos acompañados del enlace clickeable al archivo y línea (`[archivo.md](file:///c:/Git/.../doc.md#L12)`).
2. Explica el problema fáctico, la afirmación no comprobada o el patrón de estilo concreto.
3. No califiques con adjetivos despectivos ni afirmes categóricamente si el texto fue generado por una IA; concéntrate en la exactitud técnica, la claridad operativa y la concisión.

---

## 6. Checklist de Verificación para Cambios Técnicos

Antes de entregar documentación técnica humanizada, comprueba:
- [ ] ¿Cada comando, flag y ruta de archivo existe y fue validado en el repositorio?
- [ ] ¿Se eliminaron adjetivos publicitarios (*seamless*, *robusto*, *revolucionario*)?
- [ ] ¿Se eliminaron afirmaciones de facilidad (*fácilmente*, *simplemente*, *de forma trivial*)?
- [ ] ¿Los pasos operativos emplean verbos de acción claros en modo imperativo?
- [ ] ¿Se mantuvo la terminología exacta del proyecto sin alternar sinónimos caprichosos?
- [ ] ¿El texto suena conciso, sobrio y natural al leerse en voz alta?
