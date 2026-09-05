# mermaidDiagramGen

Skill de representación para generar, reparar y revisar diagramas Mermaid sin asumir autoridad sobre el dominio modelado.

El entrypoint [SKILL.md](SKILL.md) contiene el flujo de decisión y los controles de calidad. `references/` conserva un snapshot de sintaxis por familia para consulta progresiva: debe cargarse solo el archivo del tipo de diagrama solicitado. Algunos enlaces e imágenes del material upstream no forman parte de este repositorio; el contenido local no sustituye comprobar la versión del renderer disponible.

La validación distingue:

1. preflight textual;
2. render ejecutado con una versión concreta;
3. fidelidad del diagrama respecto de su fuente semántica.

La skill puede expresar una máquina de estados cuando el ciclo de vida está documentado, pero no decide que toda entidad necesite una ni obliga una MTE en otras clases de diagrama.
