# ponytail

Skill basada en `DietrichGebert/ponytail` que encarna la filosofía del *"Lazy Senior Developer"*: el mejor código es el que nunca se escribe, y la mayor victoria técnica es la reducción de líneas y complejidad innecesaria. Proporciona herramientas de implementación minimalista, revisión de código anti-bloat (`/ponytail-review`) y auditoría de complejidad arquitectónica (`/ponytail-audit`).

---

## 1. Propósito General

En entornos de desarrollo acelerados o asistidos por inteligencia artificial, existe una tendencia recurrente a generar código inflado, capas superfluas de indirección, dependencias excesivas y abstracciones especulativas (YAGNI). `ponytail` actúa como un regulador de simplicidad que fuerza al agente y al equipo a elegir la solución más elegante, compacta y directa posible, priorizando APIs nativas de la plataforma.

### Capacidades Principales:
- **Implementación Mínima Viable:** Soluciones directas concentradas en el menor número de archivos posible (mínimo *blast radius*).
- **Poda de Wrappers y Abstracciones Prematuras:** Desmantelamiento de clases o funciones intermedias que no agregan valor de negocio.
- **Sustitución de Dependencias por Primitivas Nativas:** Reemplazo automático de librerías externas obsoletas o redundantes por APIs de Node.js moderno, navegadores o Python estándar.
- **Revisión de Código `/ponytail-review`:** Inspección cuantitativa de Pull Requests y diffs para certificar un balance de líneas saludable y cero sobreingeniería.
- **Auditoría de Complejidad `/ponytail-audit`:** Mapeo de la superficie de mantenimiento, profundidad de llamadas y fragmentación de archivos en un repositorio.

---

## 2. Arquitectura Interna

```
ponytail/
├── SKILL.md                                # Contrato operacional del agente y modos de ejecución
├── README.md                               # Documentación técnica de la skill
└── references/                             # Guías de referencia y catálogos
    └── anti-overengineering-rules.md       # Catálogo de síntomas, tabla de reemplazos nativos y rúbricas
```

---

## 3. Prerequisitos de Entorno

- No requiere dependencias externas de ejecución. Opera sobre cualquier repositorio Git y cualquier stack tecnológico (TypeScript, JavaScript, Python, Rust, Go, etc.).
- Integración con comandos slash de terminal o entornos de chat interactivos mediante `/ponytail-review` y `/ponytail-audit`.

---

## 4. Ejemplos de Invocación y Uso

### Caso 1: Implementación Minimalista
```markdown
Modo: implement
Solicitud: Agregar un endpoint para generar IDs únicos de sesión y validar tokens HMAC.
Comportamiento Ponytail:
- Utiliza crypto.randomUUID() nativo en lugar de instalar el paquete 'uuid'.
- Utiliza crypto.createHmac nativo en lugar de una librería externa.
- Mantiene la lógica en el controlador de autenticación existente sin crear 3 capas de servicios y fachadas intermedias.
```

### Caso 2: Revisión Anti-Sobreingeniería de un PR
```markdown
Modo: /ponytail-review
Solicitud: Revisar diff de la rama feat/user-notifications.
Salida esperada:
- Identificación de una clase NotificationStrategyFactory redundante con un solo tipo de notificación.
- Propuesta de simplificación a una función plana notifyUser().
- Balance neto sugerido: -45 líneas de código y 1 archivo menos.
```

---

## 5. Especificación de Artefactos de Entrada y Salida

### Entradas (Inputs)
- Solicitudes de nuevas funciones o refactorizaciones de código.
- Diffs de Git (`rtk git diff`), archivos fuente o árboles de directorios para revisión.
- Listas de dependencias (`package.json`, `requirements.txt`, `Cargo.toml`).

### Salidas (Outputs)
- Código limpio, compacto y concentrado con mínima huella de mantenimiento.
- Reporte formal de revisión `/ponytail-review` con veredicto, balance de líneas y propuestas de sustitución nativa.
- Dictamen de auditoría `/ponytail-audit` con recomendaciones de consolidación de módulos.
