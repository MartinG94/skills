# Guía Canónica: RFC 7807 / RFC 9457 (Problem Details for HTTP APIs)

Esta referencia estandariza las respuestas de error estructuradas en servicios HTTP/REST.

## 1. Encabezado de Contenido Obligatorio

Toda respuesta de error bajo este estándar debe servirse con el encabezado:
`Content-Type: application/problem+json`

## 2. Miembros Estándar del Esquema RFC 9457

| Miembro | Tipo | Requerido | Propósito |
|---|---|:---:|---|
| `type` | URI | Sí | Identifica el tipo de problema. Puede ser absoluta o relativa; sirve de documentación del error. |
| `title` | String | Sí | Resumen corto y legible por humanos. No debe variar entre ocurrencias del mismo error. |
| `status` | Integer | Sí | Código de estado HTTP generado por el servidor (`4xx` o `5xx`). |
| `detail` | String | No | Explicación legible por humanos específica de esta ocurrencia puntual. |
| `instance` | URI | No | URI que identifica la ocurrencia concreta del error (ej. la ruta solicitada). |

## 3. Extensiones Recomendadas de Calidad

- `invalidParams`: Lista de errores puntuales a nivel de atributo para respuestas `422 Unprocessable Entity` o `400 Bad Request`.
- `traceId`: Identificador W3C Trace Context o UUID para correlacionar el error en logs del backend.

> [!SECURITY]
> **Protección de Datos Internos:** Los campos `detail`, `reason` o `rejectedValue` **jamás** deben volcar stack traces, nombres de tablas/columnas de BD, contraseñas, tokens o PII.

---

## 4. Ejemplos Canónicos Listos para Usar

### A. Error de Validación de Campos (`422 Unprocessable Entity`)
```json
{
  "type": "https://api.ejemplo.com/errors/validation-error",
  "title": "Error de Validación en la Solicitud",
  "status": 422,
  "detail": "Uno o más atributos enviados no satisfacen las reglas de validación.",
  "instance": "/recursos",
  "traceId": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "invalidParams": [
    {
      "name": "monto",
      "reason": "El monto debe ser un valor positivo mayor a 0.01.",
      "rejectedValue": -5.0
    },
    {
      "name": "nombre",
      "reason": "El nombre es obligatorio y debe tener al menos 2 caracteres.",
      "rejectedValue": ""
    }
  ]
}
```

### B. Conflicto de Regla de Negocio o Unicidad (`409 Conflict`)
```json
{
  "type": "https://api.ejemplo.com/errors/recurso-duplicado",
  "title": "Conflicto de Estado de Negocio",
  "status": 409,
  "detail": "Ya existe un recurso activo con el identificador fiscal proporcionado.",
  "instance": "/recursos/9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "traceId": "00-7c2a1104e4c9472ba1880491a92e1045-873bce99a09142f1-01"
}
```

### C. Recurso Inexistente (`404 Not Found`)
```json
{
  "type": "https://api.ejemplo.com/errors/recurso-no-encontrado",
  "title": "Recurso No Encontrado",
  "status": 404,
  "detail": "No se encontró ningún recurso con el ID especificado en el sistema.",
  "instance": "/recursos/3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```
