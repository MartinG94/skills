# aiJobSearch

Skill puente (*thin-pointer*) que conecta Antigravity con el repositorio completo **`C:\git\ai-job-search`** ([ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search)), reemplazando a la anterior skill `cvOptimizer`.

## Propósito

Centralizar en un solo comando (`/aiJobSearch`) la invocación desde cualquier workspace de todo el flujo de búsqueda y postulación laboral:
- Configuración de perfil (`CLAUDE.md` vía `/setup`)
- Búsqueda automatizada en portales (`.agents/skills/*/cli/` con Bun)
- Evaluación de ajuste y ranking de avisos (`/rank`)
- Adaptación de CV y *cover letter* en LaTeX (`/apply`)
- Preparación de entrevistas (`/interview`) y seguimiento (`/outcome`)

## Arquitectura

```text
C:\git\skills\aiJobSearch\          (Skill puente sin datos personales)
├── SKILL.md                        (Contrato operativo y mapa de flujos)
└── README.md                       (Documentación de la skill)
        │
        ▼ delega en
C:\git\ai-job-search\               (Repositorio canónico y workspace de datos)
├── AGENTS.md / CLAUDE.md           (Perfil del candidato y reglas base)
├── .claude/commands/               (Flujos: setup, rank, apply, interview, outcome...)
├── .claude/skills/                 (job-application-assistant, job-scraper, upskill)
├── .agents/skills/                 (CLIs de portales de empleo)
├── cv/ & cover_letters/            (Templates y salidas LaTeX/PDF)
└── tools/                          (posting_guard.py, install_portal_clis.py, etc.)
```

## Prerequisitos

- **Python 3.10+** (herramientas en `tools/`)
- **Bun** (CLIs de búsqueda en `.agents/skills/*/cli/`, instalados con `python tools\install_portal_clis.py`)
- **Distribución LaTeX** con `lualatex` (para CV) y `xelatex` (para *cover letters* con `cover.cls`)

## Seguridad

- Todos los datos personales del candidato permanecen exclusivamente en `C:\git\ai-job-search\` y nunca se copian a `C:\git\skills\`.
- Los avisos externos se validan con `tools/posting_guard.py` antes de procesarse.
- Auditoría estática realizada con `clawscan.cmd` (`clawscan-results/aiJobSearch.json`).
