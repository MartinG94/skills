# Matriz de Escenarios de Calidad RNF (Estándar DSI)

**Sistema / Proyecto:** {{NOMBRE_SISTEMA}}  
**Perfil de Trabajo:** `course-3-field` (Atributo — Estímulo — Respuesta)  
**Fecha:** {{FECHA}}  

---

| ID | RNF Origen | Atributo ISO 25010 | Estímulo | Respuesta Observable Esperada | Medida de Respuesta / SLO | SPA (Sí/No) | Prioridad | Dudas / TBD |
|---|---|---|---|---|---|:---:|:---:|---|
| `ESC-01` | `RNF-01` | Rendimiento / Comportamiento temporal | Petición de cálculo de cotización | El sistema emite el resultado sin bloquear la UI | Latencia $\le 1.5\text{ s (P95)}$ | Sí | Alta | Confirmar volumen de usuarios |
| `ESC-02` | `RNF-02` | Fiabilidad / Disponibilidad | Falla imprevista del nodo principal de base de datos | Conmutación por error a réplica y reintento automático | Tiempo de recuperación $\le 30\text{ s}$; Cero pérdida de datos confirmados | Sí | Alta | TBD ventana de mantenimiento |
| `ESC-03` | `RNF-03` | Seguridad / Confidencialidad | Acceso a endpoints de liquidación por usuario no autenticado | Rechazo inmediato y registro de intento en auditoría | Código HTTP 401; Alerta generada $\le 1\text{ s}$ | No | Media | Ninguna |
