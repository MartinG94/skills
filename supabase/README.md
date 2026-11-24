# Supabase Agent Skill (`supabase`)

Official agent skill from [supabase/agent-skills](https://github.com/supabase/agent-skills) (`v0.1.2`) installed into the local Antigravity skills catalog.

## Propósito

Provee instrucciones operativas actualizadas para trabajar con el ecosistema Supabase: Base de Datos Postgres, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues, librerías cliente (`supabase-js`, `@supabase/ssr`), CLI de Supabase y el servidor MCP de Supabase.

## Estructura del Directorio

- `SKILL.md`: Contrato principal, principios de verificación de changelog/docs, checklist de seguridad (RLS, JWT, `SECURITY DEFINER`, Storage, claves), uso del CLI, troubleshooting del servidor MCP y flujos de migración declarativa/imperativa.
- `references/skill-feedback.md`: Guía para reportar errores o brechas detectadas en la skill.
- `assets/feedback-issue-template.md`: Plantilla de issue para feedback upstream.
- `CHANGELOG.md`: Historial de versiones upstream.

## Prerrequisitos y Uso

- Acceso a documentación en línea (`https://supabase.com/changelog.md`, `https://supabase.com/docs/...`) o servidor MCP `supabase` configurado y autenticado vía OAuth 2.1.
- Invocación mediante `/supabase` o activación automática ante tareas relacionadas con Supabase.

## Entradas y Salidas

- **Entradas:** Requerimientos de desarrollo, migraciones, consultas SQL, políticas RLS, configuración o logs/errores de Supabase.
- **Salidas:** Cambios verificados de esquema/políticas/código, migraciones generadas con Supabase CLI o consultas ejecutadas vía MCP.
