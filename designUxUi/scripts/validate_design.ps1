param (
    [string]$Path = "DESIGN.md"
)

if (-not (Test-Path $Path)) {
    Write-Error "El archivo '$Path' no existe."
    exit 1
}

Write-Host "Validando $Path con @google/design.md..." -ForegroundColor Cyan
npx.cmd -p @google/design.md designmd lint $Path
exit $LASTEXITCODE
