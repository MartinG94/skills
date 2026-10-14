# gen-skill-commands.ps1
# Regenera los atajos `/` (comandos de OpenCode) para todas las skills de C:\git\skills
# y los escribe en el directorio GLOBAL de comandos (aplican a todos los proyectos).
#
# Uso:
#   powershell -NoLogo -ExecutionPolicy Bypass -File "C:\git\skills\scripts\gen-skill-commands.ps1"
#
# Reglas:
#   - Solo carpetas de C:\git\skills que contengan SKILL.md con `description` en frontmatter.
#   - ID del comando = nombre de la carpeta (sensitivo a mayusculas), NO el campo `name`.
#   - El `description` del comando se toma del frontmatter de la skill (truncado a ~160 chars).

$skillsRoot = "C:\git\skills"
$cmdDir = "C:\Users\diego\.config\opencode\commands"
New-Item -ItemType Directory -Force -Path $cmdDir | Out-Null
$enc = New-Object System.Text.UTF8Encoding($false)
$created = 0
foreach ($d in (Get-ChildItem -Path $skillsRoot -Directory -Force)) {
    if ($d.Name.StartsWith('.')) { continue }
    $f = Join-Path $d.FullName "SKILL.md"
    if (-not (Test-Path $f)) { continue }
    $lines = Get-Content -Path $f -Encoding UTF8
    $end = $null
    for ($i = 1; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match '^\s*---\s*$') { $end = $i; break }
    }
    if ($null -eq $end) { continue }
    $descLines = @(); $inDesc = $false
    for ($i = 0; $i -lt $end; $i++) {
        $ln = $lines[$i]
        if ($ln -match '^description:\s*') {
            $val = ($ln -replace '^description:\s*', '').Trim()
            if ($val -ne '' -and $val -ne '>-' -and $val -ne '|' -and $val -ne '>') { $descLines += $val }
            elseif ($val -in @('>','>-','|')) { $inDesc = $true }
            continue
        }
        if ($inDesc) {
            if ($ln -match '^[A-Za-z][A-Za-z0-9_-]*\s*:') { $inDesc = $false; continue }
            if ($ln.Trim() -ne '') { $descLines += $ln.Trim() }
        }
    }
    $desc = ($descLines -join ' ').Trim()
    if ($desc -eq '') { continue }
    if ($desc.Length -gt 160) {
        $c = $desc.Substring(0,160)
        $pos = $c.LastIndexOf(' ')
        if ($pos -gt 40) { $desc = $c.Substring(0,$pos) + '...' } else { $desc = $c }
    }
    $safe = $desc.Replace("'", "''")
    $yamlDesc = "'" + $safe + "'"
    $tpl = "---" + "`n" + "description: " + $yamlDesc + "`n" + "`n" + "Usa la skill " + $d.Name + " para la siguiente tarea:" + "`n" + "`n" + '$ARGUMENTS' + "`n"
    $p = Join-Path $cmdDir ($d.Name + ".md")
    [System.IO.File]::WriteAllText($p, $tpl, $enc)
    $created++
}
"Creados: $created en $cmdDir"
