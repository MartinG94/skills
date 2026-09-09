#!/usr/bin/env python3
"""Validador de Gobernanza, Sintaxis SMART y Fórmulas Dimensionales de KPIs."""

import argparse
import json
import re
import sys
from pathlib import Path

SMART_VERB_REGEX = r"^(Aumentar|Incrementar|Reducir|Disminuir|Mejorar|Optimizar|Alcanzar|Mantener|Bajar|Subir|Elevar|Acortar|Acelerar|Maximizar|Minimizar|Duplicar|Triplicar|Lograr)\b"
BASELINE_TARGET_REGEX = r"\b(de|del|desde)\s+(un\s+|una\s+|aproximadamente\s+)?[\$]?[\d\.,]+.*?\s+(a|al|hasta)\s+(menos\s+de\s+|m[aá]s\s+de\s+|un\s+m[aá]ximo\s+de\s+|un\s+m[ií]nimo\s+de\s+|al\s+menos\s+|no\s+m[aá]s\s+de\s+|un\s+|una\s+)?[\$]?[\d\.,]+"
TIMEFRAME_REGEX = r"\b((en|dentro\s+de)\s+\d+\s+(d[ií]as|meses|semanas|a[nñ]os)|(para|al|hacia|antes\s+de|antes\s+del|al\s+cierre\s+de|al\s+cierre\s+del|al\s+finalizar\s+el|al\s+t[eé]rmino\s+de|durante\s+el)\s+(el\s+)?(\d{1,2}\s+de\s+[a-zñ]+|\d{4}|fin\s+de\s+a[nñ]o|fines\s+de\s+[a-z0-9ñ]+|ejercicio|[a-zñ]+\s+de\s+\d{4}|[a-zñ]+|Q[1-4]|semestre|trimestre)|(en|para)\s+el\s+(Q[1-4]|primer|segundo|tercer|cuarto)|(en|para)\s+\d{4})\b"

REQUIRED_FIELDS = [
    "id",
    "nombre",
    "dominio",
    "clasificacion",
    "objetivo_smart",
    "formula",
    "unidad_medida",
    "polaridad",
    "frecuencia",
    "fuente_primaria"
]

DOMINIOS_VALIDOS = ["operaciones", "negocio", "software_devops", "producto_ux"]

def validate_smart_string(text: str) -> list[str]:
    errors = []
    text = text.strip()
    if not re.search(SMART_VERB_REGEX, text, re.IGNORECASE):
        errors.append("Objetivo SMART debe iniciar con un verbo de acción en infinitivo (ej: Reducir, Incrementar, Optimizar).")
    if not re.search(BASELINE_TARGET_REGEX, text, re.IGNORECASE):
        errors.append("Objetivo SMART debe especificar el cambio cuantitativo de Línea Base a Meta (ej: 'de X a Y', 'del 15% al 2%').")
    if not re.search(TIMEFRAME_REGEX, text, re.IGNORECASE):
        errors.append("Objetivo SMART debe incluir un plazo temporal o fecha límite explícita (ej: 'para el 31 de diciembre', 'en 6 meses', 'al cierre de 2026').")
    return errors

def validate_kpi_entry(kpi: dict) -> list[str]:
    errors = []
    kpi_id = kpi.get("id", "SIN_ID")

    for field in REQUIRED_FIELDS:
        if field not in kpi or not str(kpi[field]).strip():
            errors.append(f"[{kpi_id}] Campo obligatorio faltante: '{field}'")

    dominio = str(kpi.get("dominio", "")).lower()
    if dominio and dominio not in DOMINIOS_VALIDOS:
        errors.append(f"[{kpi_id}] Dominio inválido: '{dominio}'. Debe ser uno de {DOMINIOS_VALIDOS}")

    smart = kpi.get("objetivo_smart", "")
    if smart:
        smart_errs = validate_smart_string(smart)
        for err in smart_errs:
            errors.append(f"[{kpi_id}] {err}")

    polaridad = str(kpi.get("polaridad", "")).lower()
    if polaridad and polaridad not in ["positiva", "negativa", "rango"]:
        errors.append(f"[{kpi_id}] Polaridad inválida: '{polaridad}'. Debe ser 'positiva', 'negativa' o 'rango'.")

    formula = str(kpi.get("formula", "")).lower()
    if formula and not any(op in formula for op in ["/", "*", "-", "+", "sum", "avg", "min", "max", "%"]):
        errors.append(f"[{kpi_id}] Advertencia: La fórmula '{formula}' parece carecer de operadores matemáticos explícitos.")

    return errors

def main():
    parser = argparse.ArgumentParser(description="Validador de especificaciones de KPIs")
    parser.add_argument("file", nargs="?", default=None, help="Ruta a archivo JSON con catálogo de KPIs")
    parser.add_argument("--test-smart", help="Cadena de texto para probar validación SMART directa")
    args = parser.parse_args()

    if args.test_smart:
        errs = validate_smart_string(args.test_smart)
        if not errs:
            print("OK: Objetivo SMART sintácticamente conforme.")
            sys.exit(0)
        else:
            print("FALLO:")
            for e in errs:
                print(f" - {e}")
            sys.exit(1)

    if not args.file:
        parser.print_help()
        sys.exit(1)

    path = Path(args.file)
    if not path.exists():
        print(f"Error: No se encontró el archivo {path}", file=sys.stderr)
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    kpis = data if isinstance(data, list) else data.get("kpis", [data])
    total_errors = []

    for item in kpis:
        total_errors.extend(validate_kpi_entry(item))

    if not total_errors:
        print(f"EXITO: {len(kpis)} KPI(s) validados con éxito. Todos cumplen gobernanza, SMART y dimensionalidad.")
        sys.exit(0)
    else:
        print(f"ERRORES ENCONTRADOS ({len(total_errors)}):", file=sys.stderr)
        for err in total_errors:
            print(f" - {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
