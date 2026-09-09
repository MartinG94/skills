# Ficha de Escenario de Calidad (SEI - 6 Partes)

**Identificador:** `ESC-{{ATRIBUTO}}-{{NUMERO}}`  
**Atributo ISO/IEC 25010:2011:** {{CARACTERISTICA}} / {{SUBCARACTERISTICA}}  
**Requisito de Origen / Trazabilidad:** `{{RNF-ID}}` (Cita de fuente: {{CITA}})  
**Estado:** `Consensuado` / `Borrador con TBD`  

---

## Especificación Estructurada de las 6 Partes

| Parte del Escenario | Definición Formal | Especificación para este Escenario |
|---|---|---|
| **1. Fuente del Estímulo** | Entidad interna o externa que genera el estímulo. | {{ej. Cliente externo concurrente, Operador del sistema, Sensor}} |
| **2. Estímulo** | Condición o evento que afecta o solicita al sistema. | {{ej. Envía ráfaga de 500 solicitudes POST por segundo}} |
| **3. Entorno / Condición** | Estado operativo del sistema durante la ocurrencia. | {{ej. Operación normal pico / Modo degradado / Conmutación por error}} |
| **4. Artefacto Afectado** | Subsistema, módulo o servicio impactado. | {{ej. API Gateway, Servicio de Pagos, Base de Datos Primaria}} |
| **5. Respuesta Observable** | Comportamiento externo medible del sistema. | {{ej. Procesa las transacciones sin caídas y encola excedentes}} |
| **6. Medida de Respuesta** | Métrica cuantitativa objetiva con umbral verificable. | {{ej. Latencia <= 400 ms en P95, tasa de error <= 0.1% [o TBD]}} |

---

## Respuesta Arquitectónica (Modo `architecture-response`)
*(Completar únicamente si el usuario solicitó diseño de tácticas)*
- **Táctica(s) Seleccionada(s):** {{ej. Rate Limiting + Caching Multinivel + Circuit Breaker}}.
- **Mecanismo de Implementación:** {{Descripción concisa de cómo la táctica satisface la medida}}.
- **Trade-offs / Compromisos Asumidos:** {{ej. Mayor consumo de memoria para cache, posible desactualización de datos secundarios}}.
