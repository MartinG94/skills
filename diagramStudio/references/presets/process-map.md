# Preset: Mapa de Procesos Institucional (Institutional Process Map)

El Mapa de Procesos Institucional representa la arquitectura global de procesos de una organización estructurada en los 3 niveles canónicos:
1. **Procesos Estratégicos:** Definen el rumbo, la gobernanza, las políticas, la innovación y el cumplimiento institucional.
2. **Procesos Clave / Operativos (Core):** Transforman insumos de clientes/mercado en productos o servicios entregables de valor añadido (cadena de valor directa).
3. **Procesos de Apoyo / Soporte:** Brindan los recursos y servicios internos (TI, RRHH, Infraestructura, Legal, Compras internas) requeridos por los procesos clave y estratégicos.

---

## 1. Representación en Mermaid (`mode: "mermaid"`)

En Mermaid se modela mediante `flowchart TB` o `flowchart LR` utilizando subgraphs anidados con estilos y clases diferenciadas por nivel.

```mermaid
flowchart TB
    %% Clientes y Entorno (Entradas)
    subgraph INPUTS ["Entorno y Mercado"]
        direction TB
        REQ["Necesidades y Expectativas de Clientes / Stakeholders"]
    end

    %% Contenedor Principal del Sistema
    subgraph MAP ["MAPA DE PROCESOS INSTITUCIONAL"]
        direction TB

        %% Nivel 1: Estratégicos
        subgraph STRAT ["PROCESOS ESTRATÉGICOS"]
            direction LR
            PE1["Planificación Estratégica y Calidad"]
            PE2["Gobernanza y Gestión de Riesgos"]
            PE3["Innovación y Desarrollo de Negocio"]
        end

        %% Nivel 2: Clave / Operativos
        subgraph CORE ["PROCESOS CLAVE / OPERATIVOS (CADENA DE VALOR)"]
            direction LR
            PC1["Gestión Comercial y Ventas"]
            PC2["Planificación y Aprovisionamiento"]
            PC3["Operaciones / Fabricación / Servicio"]
            PC4["Logística y Distribución"]
            PC5["Atención al Cliente y Posventa"]
            PC1 --> PC2 --> PC3 --> PC4 --> PC5
        end

        %% Nivel 3: Soporte / Apoyo
        subgraph SUPP ["PROCESOS DE APOYO / SOPORTE"]
            direction LR
            PS1["Gestión de Personas y Talento"]
            PS2["Tecnologías de la Información (TI)"]
            PS3["Mantenimiento e Infraestructura"]
            PS4["Administración y Finanzas"]
            PS5["Gestión Legal y Cumplimiento"]
        end

        STRAT -. Directivas y Políticas .-> CORE
        SUPP -. Servicios y Recursos .-> CORE
    end

    %% Clientes y Entorno (Salidas)
    subgraph OUTPUTS ["Resultados de Valor"]
        direction TB
        SAT["Satisfacción de Clientes y Resultados de Impacto"]
    end

    REQ ==> CORE
    CORE ==> SAT

    %% Estilos institucionales
    classDef stratStyle fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b,font-weight:bold;
    classDef coreStyle fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20,font-weight:bold;
    classDef suppStyle fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#e65100,font-weight:bold;
    classDef envStyle fill:#f5f5f5,stroke:#9e9e9e,stroke-width:1px,stroke-dasharray: 4 4;

    class PE1,PE2,PE3 stratStyle;
    class PC1,PC2,PC3,PC4,PC5 coreStyle;
    class PS1,PS2,PS3,PS4,PS5 suppStyle;
    class REQ,SAT envStyle;
```

---

## 2. Representación en Draw.io (`mode: "drawio"`)

En formato nativo `.drawio`, se implementa con:
- 3 swimlanes horizontales o contenedores rectangulares agrupadores:
  - Franja Superior: Estratégicos (estilo azul `fillColor=#E1F5FE;strokeColor=#0288D1`).
  - Franja Central: Operativos/Cadena de Valor con conectores secuenciales (estilo verde `fillColor=#E8F5E9;strokeColor=#2E7D32`).
  - Franja Inferior: Soporte (estilo ámbar/naranja `fillColor=#FFF3E0;strokeColor=#EF6C00`).
- Dos bloques laterales o corchetes:
  - Izquierda: "Requisitos / Expectativas de Clientes y Partes Interesadas".
  - Derecha: "Satisfacción de Clientes y Cumplimiento de Objetivos".
- Conexiones de influencia:
  - Flechas ortogonales punteadas desde Estratégicos hacia Operativos (`dashed=1;strokeColor=#0288D1`).
  - Flechas ortogonales punteadas desde Soporte hacia Operativos (`dashed=1;strokeColor=#EF6C00`).
- Metadatos semánticos en las celdas: `customProperties: { "tier": "strategic|core|support", "processId": "PE-01" }`.
