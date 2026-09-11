#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador determinista para la Matriz de Motivaciones de la Organización
e Impulsores de Mejora (GMP Etapa 1 - 'motivaciones.md').

Verifica el cumplimiento de los estándares de cátedra:
- Estructura canónica en 5 secciones.
- Encuadre institucional y objetivos SMART.
- Cobertura de macro-sectores del Mapa de Tendencias SDLI y sus 3 dimensiones.
- Perspectiva de Lógica Dominante del Servicio (SDL - Co-creación de valor).
- Matriz de tendencias y fricciones del cliente.
- Impulsores de mejora causales y trazables a los procesos.
"""

import sys
import os
import re
import json
import argparse
from typing import Dict, List, Any, Tuple

# Macro-sectores oficiales del Mapa de Tendencias SDLI
SDLI_MACRO_SECTORS = [
    "conciencia medio ambiental",
    "post capitalismo",
    "digitalizaci",
    "vida datificada",
    "cultura de la inmediatez",
    "nuevas narrativas digitales",
    "diy",
    "bienestar integral",
    "inclusi",
    "slow life"
]

# 3 Dimensiones analíticas transversales
SDLI_DIMENSIONS = [
    "sociedad",
    "cultura",
    "tecnolog",
    "ciencia",
    "econom",
    "mercado"
]

REQUIRED_SECTIONS = [
    (1, r"1\.\s*identificaci[oó]n\s+institucional|encuadre\s+estrat[eé]gico"),
    (2, r"2\.\s*matriz\s+de\s+tendencias\s+del\s+entorno|mapa\s+(de\s+tendencias\s+)?sdli"),
    (3, r"3\.\s*matriz\s+de\s+tendencias\s+(o\s+necesidades\s+)?del\s+cliente|necesidades\s+emergentes"),
    (4, r"4\.\s*impulsores\s+y\s+demandas\s+de\s+mejora|drivers\s+de\s+redise[ñn]o"),
    (5, r"5\.\s*s[ií]ntesis|conclusiones\s+de\s+encuadre")
]

def parse_markdown_tables(content: str) -> List[List[List[str]]]:
    """Extrae tablas de Markdown como listas de filas de celdas."""
    tables = []
    lines = content.splitlines()
    current_table = []
    in_table = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            # Separador |---|---|
            if re.match(r"^\|(\s*:?-+:?\s*\|)+$", stripped):
                continue
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            current_table.append(cells)
            in_table = True
        else:
            if in_table and len(current_table) > 1:
                tables.append(current_table)
            current_table = []
            in_table = False

    if in_table and len(current_table) > 1:
        tables.append(current_table)

    return tables

def validate_motivations_file(file_path: str) -> Dict[str, Any]:
    """Valida exhaustivamente un archivo motivaciones.md."""
    result = {
        "valid": True,
        "file_path": file_path,
        "errors": [],
        "warnings": [],
        "stats": {
            "sections_found": 0,
            "trends_count": 0,
            "macro_sectors_detected": [],
            "dimensions_detected": [],
            "customer_needs_count": 0,
            "drivers_count": 0,
            "smart_objectives_found": False,
            "sdl_alignment_found": False
        }
    }

    if not os.path.isfile(file_path):
        result["valid"] = False
        result["errors"].append(f"El archivo no existe: {file_path}")
        return result

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        result["valid"] = False
        result["errors"].append(f"Error al leer el archivo con codificación UTF-8: {e}")
        return result

    lower_content = content.lower()

    # 1. Validación de Secciones Obligatorias
    found_sections = []
    for sec_num, pattern in REQUIRED_SECTIONS:
        if re.search(pattern, lower_content):
            found_sections.append(sec_num)
        else:
            result["errors"].append(f"Sección obligatoria {sec_num} faltante o mal titulada (patrón esperado: {pattern}).")

    result["stats"]["sections_found"] = len(found_sections)

    # 2. Validación de Encuadre Institucional (Sección 1)
    institutional_keywords = ["misi[oó]n", "visi[oó]n", "objetivo", "cliente", "propuesta de valor"]
    missing_inst = [kw for kw in institutional_keywords if not re.search(kw, lower_content)]
    if missing_inst:
        result["warnings"].append(f"Campos institucionales recomendados no detectados en Sección 1: {missing_inst}")

    if re.search(r"smart", lower_content):
        result["stats"]["smart_objectives_found"] = True
    else:
        result["warnings"].append("No se explicita la formulación SMART en los objetivos estratégicos de la Sección 1.")

    # 3. Validación de Tablas y Contenidos Específicos
    tables = parse_markdown_tables(content)
    if len(tables) < 3:
        result["errors"].append(f"Se esperaban al menos 3 tablas formales (Tendencias Entorno, Necesidades Cliente, Impulsores Mejora). Se detectaron {len(tables)}.")

    # Detectar Macro-Sectores SDLI presentes
    detected_sectors = []
    for sector in SDLI_MACRO_SECTORS:
        if sector in lower_content:
            detected_sectors.append(sector)
    result["stats"]["macro_sectors_detected"] = detected_sectors

    if len(detected_sectors) < 3:
        result["errors"].append(f"Se requiere evaluar al menos 3 macro-sectores del Mapa SDLI. Solo se detectaron {len(detected_sectors)}: {detected_sectors}.")
    elif len(detected_sectors) < 5:
        result["warnings"].append(f"Cobertura SDLI moderada ({len(detected_sectors)} macro-sectores detectados). Se sugiere analizar al menos 4 a 6 macro-sectores para un relevamiento exhaustivo.")

    # Detectar Dimensiones SDLI
    detected_dims = set()
    for dim in SDLI_DIMENSIONS:
        if dim in lower_content:
            detected_dims.add(dim)
    result["stats"]["dimensions_detected"] = list(detected_dims)

    # Cobertura de dimensiones mínimas (Sociedad, Tecnología, Economía)
    has_soc = any(d in detected_dims for d in ["sociedad", "cultura"])
    has_tec = any(d in detected_dims for d in ["tecnolog", "ciencia"])
    has_eco = any(d in detected_dims for d in ["econom", "mercado"])

    if not (has_soc and has_tec and has_eco):
        missing_dims = []
        if not has_soc: missing_dims.append("Sociedad-Cultura")
        if not has_tec: missing_dims.append("Tecnología-Ciencia")
        if not has_eco: missing_dims.append("Economía-Mercado")
        result["warnings"].append(f"No se cubren las 3 dimensiones del Mapa SDLI de forma equilibrada. Dimensiones faltantes o poco claras: {missing_dims}.")

    # Perspectiva SDL (Service-Dominant Logic / Co-creación)
    sdl_patterns = [
        r"\bco-creaci[oó]n\b",
        r"\bcocreaci[oó]n\b",
        r"l[oó]gica\s+dominante\s+del\s+servicio",
        r"\bsdl\b",
        r"service-dominant\s+logic",
        r"valor\s+en\s+el\s+uso",
        r"value-in-use",
        r"servitizaci[oó]n"
    ]
    if any(re.search(p, lower_content) for p in sdl_patterns):
        result["stats"]["sdl_alignment_found"] = True
    else:
        result["errors"].append("No se encontró evidencia del marco de Lógica Dominante del Servicio (SDL / Co-creación de valor) exigido por cátedra.")

    # Conteo de ítems en tablas (IDs estándar: TND-, CLI-, DRV-)
    trend_ids = set(re.findall(r"TND-\d+", content))
    client_ids = set(re.findall(r"CLI-\d+", content))
    driver_ids = set(re.findall(r"DRV-\d+", content))

    result["stats"]["trends_count"] = len(trend_ids)
    result["stats"]["customer_needs_count"] = len(client_ids)
    result["stats"]["drivers_count"] = len(driver_ids)

    if len(trend_ids) < 3:
        result["errors"].append(f"La Matriz de Tendencias del Entorno debe contener al menos 3 tendencias identificadas con código 'TND-XX'. Encontradas: {len(trend_ids)}.")

    if len(client_ids) < 2:
        result["errors"].append(f"La Matriz de Necesidades del Cliente debe contener al menos 2 requerimientos identificados con código 'CLI-XX'. Encontrados: {len(client_ids)}.")

    if len(driver_ids) < 2:
        result["errors"].append(f"La tabla de Impulsores y Demandas de Mejora debe contener al menos 2 drivers identificados con código 'DRV-XX'. Encontrados: {len(driver_ids)}.")

    # Trazabilidad con Etapas GMP
    if not any(k in lower_content for k in ["seleccion_proceso", "criterio 2", "factor 2", "foda", "etapa 2", "etapa 3"]):
        result["warnings"].append("Se recomienda explicitar la trazabilidad de los impulsores hacia el Factor 2 de 'seleccion_proceso.md' y las Oportunidades en 'foda.md'.")

    if result["errors"]:
        result["valid"] = False

    return result

def main():
    parser = argparse.ArgumentParser(description="Validador determinista de la Matriz de Motivaciones de la Organización (GMP Etapa 1)")
    parser.add_argument("file_path", help="Ruta al archivo motivaciones.md")
    parser.add_argument("--json", action="store_true", help="Emitir resultado exclusivamente en formato JSON")
    args = parser.parse_args()

    res = validate_motivations_file(args.file_path)

    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print("================================================================================")
        print("  VALIDADOR DE MATRIZ DE MOTIVACIONES DE LA ORGANIZACIÓN (GMP ETAPA 1)")
        print("================================================================================")
        print(f"Archivo analizado: {res['file_path']}")
        print(f"Estado: {'[VALIDO]' if res['valid'] else '[INVALIDO]'}")
        print("--------------------------------------------------------------------------------")
        print(f"Estadísticas:")
        print(f"  - Secciones requeridas: {res['stats']['sections_found']}/5")
        print(f"  - Tendencias del entorno (TND-XX): {res['stats']['trends_count']}")
        print(f"  - Macro-sectores SDLI identificados: {len(res['stats']['macro_sectors_detected'])}")
        print(f"  - Necesidades emergentes del cliente (CLI-XX): {res['stats']['customer_needs_count']}")
        print(f"  - Impulsores de mejora (DRV-XX): {res['stats']['drivers_count']}")
        print(f"  - Alineación SDL (Co-creación de valor): {'Si' if res['stats']['sdl_alignment_found'] else 'No'}")
        print(f"  - Objetivos SMART explicitados: {'Si' if res['stats']['smart_objectives_found'] else 'No'}")

        if res["errors"]:
            print("\n[ERRORES CRÍTICOS]:")
            for err in res["errors"]:
                print(f"  ❌ {err}")

        if res["warnings"]:
            print("\n[ADVERTENCIAS / RECOMENDACIONES]:")
            for warn in res["warnings"]:
                print(f"  ⚠️  {warn}")

        if res["valid"]:
            print("\nResultado: Cumple satisfactoriamente los estándares de cátedra para GMP Etapa 1.")
        print("================================================================================")

    sys.exit(0 if res["valid"] else 1)

if __name__ == "__main__":
    main()
