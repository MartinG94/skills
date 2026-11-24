# Supabase Postgres Best Practices (`supabasePostgresBestPractices`)

Official agent skill from [supabase/agent-skills](https://github.com/supabase/agent-skills) (`supabase-postgres-best-practices`, `v1.1.1`) installed into the local Antigravity skills catalog in camelCase.

## Propósito

Guía de optimización de rendimiento y buenas prácticas para PostgreSQL (en Supabase o Postgres estándar), organizada en 8 categorías priorizadas por impacto desde crítico (rendimiento de consultas, gestión de conexiones, seguridad y RLS) hasta incremental (funciones avanzadas).

## Estructura del Directorio

- `SKILL.md`: Índice principal de disparo (`name: supabasePostgresBestPractices`) y tabla de prioridades por categoría.
- `references/`: Reglas detalladas con ejemplos SQL incorrectos vs. correctos, análisis `EXPLAIN` y notas específicas para Supabase:
  - `query-*`: Índices faltantes, parciales, compuestos, cubrientes y tipos de índice.
  - `conn-*`: Pooling, límites, idle timeout y prepared statements.
  - `security-*`: Fundamentos de RLS, rendimiento de políticas RLS y privilegios.
  - `schema-*`: Tipos de datos, llaves primarias, índices en claves foráneas, restricciones, identificadores en minúscula y particionamiento.
  - `lock-*`: Transacciones cortas, prevención de deadlocks, `SKIP LOCKED` y advisory locks.
  - `data-*`: N+1, inserciones por lotes, upsert y paginación.
  - `monitor-*`: `EXPLAIN ANALYZE`, `pg_stat_statements` y `VACUUM ANALYZE`.
  - `advanced-*`: Búsqueda de texto completo e indexado JSONB.
  - `_sections.md`, `_template.md`, `_contributing.md`: Metadatos y plantillas de reglas.
- `CHANGELOG.md`: Historial de versiones upstream.

## Prerrequisitos y Uso

- Se activa automáticamente al diseñar esquemas, escribir SQL/migraciones, definir RLS o diagnosticar consultas lentas en PostgreSQL/Supabase, o mediante `/supabasePostgresBestPractices` (alias `supabase-postgres-best-practices`).

## Entradas y Salidas

- **Entradas:** Consultas SQL, definiciones de tablas/índices/políticas RLS o métricas/planes `EXPLAIN` a diagnosticar.
- **Salidas:** Recomendaciones concretas, DDL/SQL optimizado y políticas RLS seguras y performantes según las reglas de `references/`.
