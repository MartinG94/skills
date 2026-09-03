param (
    [string]$Path = "DESIGN.md",
    [ValidateSet("json-tailwind", "css-tailwind", "dtcg")]
    [string]$Format = "json-tailwind",
    [string]$Output = ""
)

if (-not (Test-Path $Path)) {
    Write-Error "El archivo '$Path' no existe."
    exit 1
}

if ($Output -eq "") {
    switch ($Format) {
        "json-tailwind" { $Output = "tailwind.theme.json" }
        "css-tailwind"  { $Output = "theme.css" }
        "dtcg"          { $Output = "tokens.json" }
    }
}

Write-Host "Exportando $Path en formato $Format hacia $Output..." -ForegroundColor Cyan
npx.cmd -p @google/design.md designmd export --format $Format $Path | Out-File -FilePath $Output -Encoding utf8
Write-Host "Exportación completada exitosamente en $Output." -ForegroundColor Green
