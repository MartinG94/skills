# Plantilla Maestra de Reporte: Auditoría CRUD y Calidad de Requerimientos

```markdown
# Reporte de Auditoría CRUD, Consistencia y Calidad ERS
**Proyecto / Sistema:** [Nombre del Sistema]  
**Versión de Especificación:** [vX.Y]  
**Fecha de Evaluación:** [YYYY-MM-DD]  
**Auditor / Herramienta:** Agente de Validación CRUD & Linter ISO 29148  

---

## 1. Resumen Ejecutivo y Métricas Globales (Scorecard)

| Indicador Clave de Calidad | Valor Obtenido | Umbral de Aprobación | Estado |
| :--- | :---: | :---: | :---: |
| **Total de Entidades de Dominio** | [N] | - | - |
| **Total de Casos de Uso Evaluados** | [M] | - | - |
| **Entidades con Ciclo CRUD Balanceado** | [X] / [N] ([%]%) | 100% | [🟢 / 🔴] |
| **Entidades Fantasma (Ghost Entities)** | [G] | 0 | [🟢 / 🚨] |
| **Datos Agujero Negro (Black Holes)** | [B] | 0 | [🟢 / ⚠️] |
| **Entidades Huérfanas (Orphan Entities)**| [O] | 0 | [🟢 / ❌] |
| **Violaciones Linter ISO 29148 / IEEE 830** | [V] | 0 Críticas | [🟢 / ⚠️] |
| **Índice de Trazabilidad Bidireccional** | [%]% | 100% | [🟢 / 🔴] |

---

## 2. Matriz CRUD Bidimensional (Entidades x Casos de Uso)

| Entidad de Dominio \ Caso de Uso | [CU-01: Nombre] | [CU-02: Nombre] | [CU-03: Nombre] | [CU-Rem-XX] | Cobertura CRUD | Estado Diagnóstico |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **[Entidad 1]** | C | R | R, U | - | C, R, U | ✅ Balanceada |
| **[Entidad 2]** | - | R | R | C | C, R | ✅ Balanceada (Inmutable) |
| **[Entidad 3]** | R | R | U | - | R, U | 🚨 GHOST ENTITY (Sin C) |
| **[Entidad 4]** | C | - | - | - | C | ⚠️ BLACK HOLE (Sin R) |

---

## 3. Registro Detallado de Brechas Estructurales (Gap Log)

### 3.1. Entidades Fantasma Detectadas (Ghost Entities)
- **ID Brecha:** `GAP-GHOST-[XX]`
  - **Entidad Afectada:** `[NombreEntidad]`
  - **Casos de Uso Consumidores:** `[CU-XX] (R)`, `[CU-YY] (U)`
  - **Impacto:** Fallo en tiempo de ejecución por ausencia de datos de origen.
  - **Acción de Remediación:** Se generó `[CU-Rem-XX: Registrar Alta de NombreEntidad]`.

### 3.2. Datos Agujero Negro Detectados (Black Hole Data)
- **ID Brecha:** `GAP-BH-[XX]`
  - **Entidad Afectada:** `[NombreEntidad]`
  - **Casos de Uso Creadores:** `[CU-ZZ] (C)`
  - **Impacto:** Almacenamiento inútil sin generación de reportes ni valor para el negocio.
  - **Acción de Remediación:** Se generó `[CU-Rem-YY: Consultar / Auditar NombreEntidad]`.

---

## 4. Hallazgos del Linter de Calidad de Requerimientos

| ID Requerimiento | Regla Violada | Fragmento Original Defectuoso | Severidad | Propuesta Reescrita (ISO 29148) |
| :--- | :--- | :--- | :---: | :--- |
| **RF-[XX]** | `LINT-01` (Atomicidad) | *"[Texto original con conjunciones múltiples]"* | `CRÍTICA` | Dividir en `RF-[XX].1` y `RF-[XX].2` |
| **RNF-[YY]** | `LINT-02` (Vaguedad) | *"[Texto original con palabras vagas: rápido, fácil]"*| `ALTA` | Reemplazar por métrica cuantitativa SLA |

---

## 5. Especificaciones de Casos de Uso de Remediación

[Insertar aquí la especificación completa en plantilla estándar de cada CU-Rem generado]

---

## 6. Matriz de Trazabilidad Cruzada Consolidada

| RF Origen | Caso de Uso Principal | Reglas de Negocio Asociadas | Entidades Afectadas (CRUD) | Estado |
| :--- | :--- | :--- | :--- | :---: |
| **RF-01.1** | `CU-01` | `RN-01`, `RN-04` | `Cliente (C)`, `Tarjeta (C)` | ✅ Trazado |
| **RF-02.1** | `CU-02` | `RN-02` | `Pedido (C)`, `Producto (R, U)` | ✅ Trazado |
```
