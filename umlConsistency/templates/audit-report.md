# Informe de Auditoría de Consistencia UML (DSD $\leftrightarrow$ DCD $\leftrightarrow$ DTE)

**Proyecto / Sistema Auditado:** {{NOMBRE_PROYECTO}}  
**Alcance:** {{ALCANCE_AUDITORIA}}  
**Fuente Autoritativa Establecida:** {{DCD_O_RCU_O_CODIGO}}  
**Fecha:** {{FECHA}}  

---

## 1. Matriz de Cobertura y Legibilidad de Artefactos

| Artefacto Inspeccionado | Formato / Origen | Nivel de Detalle | Estado de Verificación |
|---|---|---|:---:|
| Diagrama de Secuencia (DSD/RCU) | Mermaid / PlantUML | Completo con participantes | Verificado |
| Diagrama de Clases (DCD) | Mermaid / XMI / Imagen | Clases con atributos y operaciones | Verificado |
| Diagrama de Transición de Estados | Mermaid / MTE | Estados y eventos de ciclo de vida | Verificado |
| Código Fuente de Implementación | C# / Java / Python / TS | Controladores y Entidades | Opcional / No aportado |

---

## 2. Resumen Ejecutivo de Hallazgos

| ID | Regla (C1-C6) | Certeza | Severidad | Origen $\leftrightarrow$ Destino | Símbolo Involucrado |
|---|---|:---:|:---:|---|---|
| `DISC-01` | C1: Firma y Receptor | Confirmado | Error | `DSD: Paso 4` $\to$ `DCD: Pedido` | `confirmar(monto: Decimal)` |
| `DISC-02` | C2: Ruta Navegabilidad | Posible | Advertencia | `DSD: Paso 6` $\to$ `DCD: Cliente` | Falta asociación navegable |
| `DISC-03` | C4: Ciclo de Vida | Confirmado | Error | `DSD: Paso 8` $\to$ `DTE: Pedido` | Transición ilegal a `Cancelado` |

---

## 3. Desglose Detallado de Discrepancias

### Hallazgo `DISC-01`: Discordancia de Firma de Método (Regla C1)
- **Certeza y Severidad:** `Confirmado` / `Error Crítico`.
- **Evidencia en Origen (DSD):** En el paso 4, la lifeline `Gestor` envía el mensaje `confirmar(monto)` a la instancia `p: Pedido`.
- **Evidencia en Destino (DCD):** La clase `Pedido` declara únicamente la operación `+ confirmar(): void` sin parámetros.
- **Impacto de la Inconsistencia:** El contrato estático rechaza la invocación; error de compilación inmediato en el paso a código.
- **Propuesta de Remediación Mínima:** Ajustar la firma en el DCD a `+ confirmar(monto: Decimal): void` si el monto es requerido por la regla de negocio, o remover el argumento en el DSD si el pedido ya conoce su importe.

---

## 4. Elementos No Verificables o Fuera de Alcance
- **Elemento 1:** {{Artefacto en formato de imagen ilegible o sin texto verificable}}.
