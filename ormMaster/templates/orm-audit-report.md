# Informe de Auditoría y Diagnóstico de Rendimiento ORM

**Proyecto / Módulo:** {{NOMBRE_PROYECTO}}  
**ORM y Versión:** {{ORM_Y_VERSION}} (ej. Hibernate 6.x, EF Core 8/9, Prisma 5.x, SQLAlchemy 2.x)  
**Motor de Base de Datos:** {{MOTOR_BD}} (ej. PostgreSQL 16, SQL Server 2022, MySQL 8)  
**Caso de Uso / Endpoint Auditado:** {{CASO_USO_O_ENDPOINT}}  
**Fecha:** {{FECHA}}  

---

## 1. Evidencia Observable y Comportamiento Inicial

- **Síntoma Clínico:** {{ej. Latencia de 1200ms en listado, saturación de conexiones en BD, etc.}}.
- **Registro de Consultas SQL (Log / Profiler):**
  ```sql
  -- Consulta inicial padre
  SELECT p.id, p.fecha, p.cliente_id FROM pedidos p WHERE p.estado = 'PENDIENTE';
  -- Bucle N consultas subsecuentes (Problema N+1)
  SELECT c.id, c.nombre FROM clientes c WHERE c.id = 101;
  SELECT c.id, c.nombre FROM clientes c WHERE c.id = 102;
  -- (... repetido N veces ...)
  ```

---

## 2. Diagnóstico de Causa Raíz y Patología
- **Patología Identificada:** {{Problema N+1 / Explosión Cartesiana / Bloqueo por Concurrencia / Open Session in View}}.
- **Causa Raíz en el Código / Mapeo:** {{ej. Propiedad `Cliente` configurada perezosamente pero accedida en loop dentro de un DTO assembler}}.

---

## 3. Matriz Comparativa Antes vs. Después

| Métrica de Rendimiento | Comportamiento Inicial (Antes) | Propuesta Optimizada (Después) | Delta / Mejora Obtenida |
|---|:---:|:---:|:---:|
| **Número de Consultas SQL emitidas** | {{ej. 101 queries}} | {{ej. 1 query}} | **-99% consultas** |
| **Tiempo de Ejecución / Latencia** | {{ej. 450 ms}} | {{ej. 18 ms}} | **-96% latencia** |
| **Volumen de Filas Transferidas** | {{ej. 100 filas}} | {{ej. 100 filas}} | Igual volumen útil |
| **Estado en Contexto de Persistencia** | Entidades gestionadas en memoria | Proyección DTO de solo lectura | Cero sobrecarga de dirty checking |

---

## 4. Estrategia de Optimización Aplicada
- **Técnica Seleccionada:** {{Fetch Join / Entity Graph / Split Queries / Constructor Projection / AsNoTracking}}.
- **Justificación:** {{Por qué esta técnica resuelve el problema sin provocar productos cartesianos}}.
- **Snippet de Consulta / Mapeo Corregido:**
  ```csharp
  // Ejemplo ilustrativo adaptado al stack del proyecto
  var resultado = await context.Pedidos
      .AsNoTracking()
      .Where(p => p.Estado == EstadoPedido.Pendiente)
      .Select(p => new PedidoResumenDto(p.Id, p.Fecha, p.Cliente.Nombre))
      .ToListAsync();
  ```

---

## 5. Plan de Verificación y Pruebas
- [ ] La consulta optimizada se verificó con el profiler de SQL o logging habilitado.
- [ ] Se ejecutaron pruebas unitarias/integración garantizando que los datos devueltos coinciden exactamente.
- [ ] No se detectaron productos cartesianos (multiplicación de filas) en relaciones 1:N.
