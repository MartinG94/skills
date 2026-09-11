# Guía de Clasificación y Arquitectura del Mapa de Procesos (GMP Etapa 1)

Esta guía documenta los fundamentos teóricos, metodológicos y de diseño del **Mapa de Procesos Institucional** en la cátedra de **Gestión y Mejora de Procesos (GMP)**, basados en la diapositiva oficial `SLI_U1_C03_Mapa_de_Procesos.pdf` y la hoja *'Etapa 1 Situación actual'* (Matriz 2) de `PlanillaMATRICES-TPI 2026 con ejemplo.xlsx`.

---

## 1. Definición y Objetivo del Mapa de Procesos

Un **Mapa de Procesos** es la representación gráfica y estructural que muestra los procesos de una organización y sus interrelaciones sistémicas. Permite:
1. **Identificar los procesos del negocio:** Reconocer qué actividades transformadoras componen el quehacer organizacional.
2. **Visualizar las relaciones sistémicas:** Mapear cómo interactúan los flujos de información, control y recursos entre procesos.
3. **Comprender el flujo de valor de punta a punta:** Seguir el recorrido desde las necesidades y requisitos del cliente (a la izquierda) hasta su satisfacción y valor entregado (a la derecha).
4. **Alinear procesos con la estrategia:** Traducir los objetivos institucionales en operaciones tangibles y controlables.
5. **Identificar y priorizar el proceso crítico:** Servir de base analítica para la matriz multicriterio de selección (`processCriticalSelector`).

---

## 2. Los 3 Niveles Canónicos de Procesos

La cátedra de GMP estructura el mapa en tres niveles horizontales jerárquicos:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PROCESOS ESTRATÉGICOS                              │
│       (Definen la dirección, objetivos, políticas y control del sistema)    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PROCESOS OPERATIVOS / CLAVE                           │
│  [Requisitos Clientes] ──► (Crean valor directo para el cliente) ──► [Satisfacción] │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ▲
                                      │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PROCESOS DE SOPORTE                               │
│              (Proveen los recursos necesarios: RRHH, Finanzas, TI)          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Procesos Estratégicos (Dirección y Gobierno)
- **Definición:** Procesos que definen la dirección de la organización, establecen objetivos y políticas, asignan recursos a largo plazo y ejercen el control del sistema de gestión.
- **Características:** Foco en el largo plazo, visión holística del entorno, alineación institucional.
- **Ejemplos Canónicos:**
  - Planificación estratégica institucional y control de gestión.
  - Gestión de la innovación y transformación digital.
  - Gestión de alianzas estratégicas y vinculación institucional.
  - Aseguramiento de la calidad, acreditaciones y certificaciones.
  - Gestión de sostenibilidad y responsabilidad socioambiental.

### 2.2 Procesos Operativos, Clave o Misionales (Cadena de Valor Primaria)
- **Definición:** Procesos que intervienen directamente en la generación del producto o prestación del servicio.
- **Características:**
  - Crean valor directo y percibible para el cliente o usuario.
  - Constituyen el núcleo (*core business*) o razón de ser de la organización.
  - Están directamente vinculados con el mercado y los clientes (desde la captura de demanda hasta la entrega).
- **Ejemplos Canónicos:**
  - *Educación:* Admisión y enrolamiento, Gestión de la enseñanza-aprendizaje, Prácticas profesionales y graduación.
  - *Salud / Farmacia:* Admisión de pacientes, Diagnóstico y tratamiento, Dispensación y seguimiento farmacoterapéutico.
  - *Manufactura:* Adquisición de materias primas, Fabricación/Producción, Logística de distribución y ventas.

### 2.3 Procesos de Soporte o Apoyo (Habilitadores de Recursos)
- **Definición:** Procesos que apoyan y sostienen el funcionamiento de los procesos operativos y estratégicos.
- **Características:** No generan valor directo para el cliente externo, pero su ejecución eficiente es imprescindible para la continuidad operacional.
- **Ejemplos Canónicos:**
  - Gestión de talento humano (reclutamiento, nómina, capacitación, clima).
  - Gestión económica, financiera y presupuestaria.
  - Gestión de infraestructura, mantenimiento y servicios generales.
  - Gestión de tecnologías de la información (TI), ciberseguridad y soporte técnico.
  - Asesoría jurídica, compras y abastecimiento corporativo.

---

## 3. Estructura de Cada Proceso en el Inventario

Cada proceso identificado dentro del mapa debe documentar obligatoriamente:
1. **Identificador Unívoco:** `PE-01` (Estratégicos), `PO-01` (Operativos/Misionales), `PS-01` (Soporte).
2. **Nombre Canónico del Proceso:** Enunciado en sustantivo de acción (`Gestión de...`, `Desarrollo de...`, `Administración de...`).
3. **Objetivo del Proceso:** Redactado con verbo en infinitivo, estableciendo la finalidad, qué recursos transforma y qué valor genera, alineado a la misión o visión organizacional.
4. **Dueño o Responsable Funcional sugerido:** Rol o área responsable del proceso.
5. **Entradas y Proveedores clave:** Qué requiere el proceso para iniciar.
6. **Salidas y Clientes/Destinatarios:** Qué entrega el proceso y a quién.

---

## 4. Estándar de Representación Gráfica (Mermaid & Draw.io)

El diagrama del mapa de procesos debe mantener las siguientes pautas visuales:
- **Flujo Horizontal:** `flowchart LR` o `flowchart TB` con subgrafos horizontales.
- **Subgrafos:** Tres subgrafos claramente delimitados: `subgraph Estrategicos["1. Procesos Estratégicos"]`, `subgraph Operativos["2. Procesos Operativos (Misionales)"]` y `subgraph Soporte["3. Procesos de Soporte"]`.
- **Nodos Externos:** Nodo a la izquierda `Clientes_Entrada["Clientes / Mercado<br/>(Requisitos y Expectativas)"]` y nodo a la derecha `Clientes_Salida["Clientes / Mercado<br/>(Satisfacción y Valor Co-creado)"]`.
- **Conectores:** Flechas de control desde Estratégicos hacia Operativos; flechas de recursos desde Soporte hacia Operativos; y flecha de flujo principal desde Requisitos hacia Operativos y de Operativos hacia Satisfacción.
