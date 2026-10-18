# impeccable

Skill de auditoría visual anti-slop y refinamiento estético de alta precisión para interfaces de usuario web y landing pages.

Inspirada en el enfoque artesanal y las herramientas de diseño de `pbakaus/impeccable`, esta skill detecta los vicios visuales genéricos producidos por la IA y aplica reglas ópticas y matemáticas rigurosas para lograr acabados de nivel profesional.

---

## 1. Propósito General

`impeccable` actúa como el ojo crítico de diseño para frontend y diseño UI, garantizando que el código no caiga en clichés visuales de LLMs ni en imprecisiones geométricas:
- **Detección Anti-Slop (`detect`):** Identifica degradados violetas genéricos, sombras difusas y sucias, colisiones de radios en esquinas anidadas, números inestables sin `tabular-nums` y abuso de cajas decorativas.
- **Micro-Refinamiento (`polish`):** Ajusta al píxel bordes sutiles de 1px con luminancia, radios concéntricos exactos ($R_{outer} = R_{inner} + Padding$), balance de texto y compensación óptica de iconos.
- **Poda de Ruido (`distill`):** Elimina contenedores decorativos y wrappers superfluos para devolver jerarquía y claridad al contenido.
- **Coreografía de Movimiento (`animate`):** Añade microinteracciones y transiciones con física natural, garantizando accesibilidad plena y respeto a preferencias de movimiento reducido.

---

## 2. Arquitectura Interna

```
impeccable/
├── SKILL.md                                # Contrato operativo del agente (YAML frontmatter + directivas)
├── README.md                               # Documentación técnica para desarrolladores
└── references/                             # Catálogo y normativas de precisión
    └── impeccable-design-rules.md          # Catálogo exhaustivo de anti-patrones y reglas matemáticas
```

---

## 3. Prerequisitos de Entorno

- **Requisitos de Sistema:** Ninguno obligatorio; funciona sobre código CSS, SCSS, Tailwind CSS, React / Next.js, Vue, Svelte o HTML puro.
- **Compatibilidad de Navegadores:** Se recomiendan navegadores modernos con soporte para `text-wrap: balance`, variables CSS y `@media (prefers-reduced-motion)`.

---

## 4. Ejemplos de Invocación y Uso

### Modo `detect`: Auditar un Componente Existente
```markdown
/impeccable detect src/components/DashboardCard.tsx
```
*Equivalente en lenguaje natural:* "Audita visualmente esta tarjeta y dime qué anti-patrones de diseño o fallos de jerarquía y espaciado tiene."

### Modo `polish`: Refinar Micro-Detalles
```markdown
/impeccable polish src/components/PricingTable.tsx
```
*Equivalente en lenguaje natural:* "Pule los radios de esquina, agrega tabular-nums a los precios y aplica bordes de luminancia sutiles a esta tabla."

### Modo `distill`: Reducir Cajas y Ruido
```markdown
/impeccable distill src/components/SettingsPanel.tsx
```
*Equivalente en lenguaje natural:* "Limpia el exceso de bordes y tarjetas anidadas en este panel de configuración."

### Modo `animate`: Transición Suave y Natural
```markdown
/impeccable animate src/components/DropdownMenu.tsx
```
*Equivalente en lenguaje natural:* "Agrega una animación de entrada suave con curva natural y soporte para prefers-reduced-motion a este menú desplegable."

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Archivos de componentes frontend (`.tsx`, `.jsx`, `.vue`, `.svelte`, `.html`).
- Hojas de estilo (`.css`, `.scss`, clases de Tailwind).
- Capturas o fragmentos de código de interfaz con solicitud de auditoría o pulido.

### Salidas (Outputs)
- **Informe de Auditoría (`IMPECCABLE_AUDIT.md`):** Lista priorizada de hallazgos (Crítico, Advertencia, Sugerencia) con causas y propuestas de solución.
- **Código Refinado:** Modificaciones quirúrgicas en el archivo objetivo aplicando correcciones ópticas, matemáticas y tipográficas.
