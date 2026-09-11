#!/usr/bin/env python3
"""
Validador de Gobernanza, Trazabilidad CAME y Filtro de Restricciones Operativas
para entregables de Acciones de Valor (acciones_valor.md) - GMP Etapa 3.
"""

import argparse
import json
import re
import sys
from pathlib import Path

VALID_EERR_LEVERS = {"eliminar", "reducir", "incrementar", "crear"}
VALID_CAME_TYPES = {"do", "fo", "fa", "da"}
VALID_DICTAMENES_ORDERED = [
    "aprobada con mitigación",
    "aprobada con mitigacion",
    "aprobada condicionada",
    "aprobada",
    "desechada",
    "pospuesta",
    "rechazada"
]

def parse_markdown_tables(content: str) -> list[list[list[str]]]:
    """Extrae todas las tablas Markdown del contenido como listas de filas (listas de celdas)."""
    tables = []
    current_table = []
    in_table = False

    for line in content.splitlines():
        line = line.strip()
        if line.startswith("|") and line.endswith("|"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            # Ignorar línea separadora |---|---|...
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                continue
            current_table.append(cells)
            in_table = True
        else:
            if in_table and len(current_table) >= 2:
                tables.append(current_table)
            current_table = []
            in_table = False

    if in_table and len(current_table) >= 2:
        tables.append(current_table)

    return tables

def find_eerr_table(tables: list[list[list[str]]]) -> tuple[list[str], list[list[str]]] | None:
    """Identifica la tabla del inventario EERR de acciones de valor basándose en sus encabezados."""
    for table in tables:
        headers = [h.lower() for h in table[0]]
        has_id = any("id" in h for h in headers)
        has_palanca = any("palanca" in h or "eerr" in h or "clasificación" in h or "clasificacion" in h for h in headers)
        has_came = any("came" in h or "cruce" in h for h in headers)
        if (has_id or len(headers) >= 5) and has_palanca and has_came:
            return table[0], table[1:]
    return None

def find_filter_table(tables: list[list[list[str]]]) -> tuple[list[str], list[list[str]]] | None:
    """Identifica la tabla del filtro de restricciones operativas basándose en sus encabezados."""
    for table in tables:
        headers = [h.lower() for h in table[0]]
        has_plazos = any("plazo" in h or "tiempo" in h for h in headers)
        has_costos = any("costo" in h or "presupuesto" in h or "financier" in h for h in headers)
        has_ti = any("tecnol" in h or "ti" in h or "sistemas" in h for h in headers)
        has_resistencia = any("resist" in h or "cambio" in h or "humano" in h for h in headers)
        has_dictamen = any("dictamen" in h or "viabilidad" in h for h in headers)
        if (has_plazos or has_costos) and (has_ti or has_resistencia) and has_dictamen:
            return table[0], table[1:]
    return None

def normalize_text(text: str) -> str:
    """Limpia caracteres de formato Markdown como backticks, negrita y asteriscos."""
    return re.sub(r"[*`_]", "", text).strip()

def validate_value_actions_file(file_path: Path) -> dict:
    result = {
        "file": str(file_path),
        "valid": False,
        "errors": [],
        "warnings": [],
        "actions_found": 0,
        "eerr_breakdown": {"eliminar": 0, "reducir": 0, "incrementar": 0, "crear": 0},
        "dictamen_breakdown": {},
        "mitigated_actions": []
    }

    if not file_path.exists():
        result["errors"].append(f"El archivo objetivo no existe: {file_path}")
        return result

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        result["errors"].append(f"No se pudo leer el archivo: {e}")
        return result

    if not content.strip():
        result["errors"].append("El archivo está vacío.")
        return result

    tables = parse_markdown_tables(content)
    if not tables:
        result["errors"].append("No se detectaron tablas Markdown en el documento.")
        return result

    # 1. Validar Tabla EERR
    eerr_data = find_eerr_table(tables)
    if not eerr_data:
        result["errors"].append("No se encontró la tabla de Inventario de Acciones de Valor (EERR) con encabezados requeridos (Palanca EERR, Cruce CAME).")
        return result

    eerr_headers, eerr_rows = eerr_data
    headers_lower = [h.lower() for h in eerr_headers]

    # Mapeo de columnas EERR
    id_idx = next((i for i, h in enumerate(headers_lower) if "id" in h), 0)
    palanca_idx = next((i for i, h in enumerate(headers_lower) if "palanca" in h or "eerr" in h or "clasificación" in h or "clasificacion" in h), None)
    came_idx = next((i for i, h in enumerate(headers_lower) if "came" in h or "cruce" in h), None)
    proc_prim_idx = next((i for i, h in enumerate(headers_lower) if "primario" in h or "proceso" in h), None)
    proc_afec_idx = next((i for i, h in enumerate(headers_lower) if "afectado" in h or "adyacente" in h), None)

    if palanca_idx is None or came_idx is None:
        result["errors"].append("La tabla de Acciones de Valor carece de columnas indispensables para Palanca EERR o Cruce CAME.")
        return result

    action_ids = set()
    for row_idx, row in enumerate(eerr_rows, start=1):
        if len(row) <= max(id_idx, palanca_idx, came_idx):
            result["errors"].append(f"Fila {row_idx} de Acciones de Valor tiene menos columnas de las esperadas.")
            continue

        raw_id = normalize_text(row[id_idx])
        raw_palanca = normalize_text(row[palanca_idx]).lower()
        raw_came = normalize_text(row[came_idx])

        if not raw_id:
            result["errors"].append(f"Fila {row_idx}: ID de Acción de Valor vacío.")
            continue
        action_ids.add(raw_id)

        # Validar palanca EERR (determinar la palanca principal por orden de aparición en el texto)
        matched_lever = None
        min_pos = float("inf")
        for lever in ["eliminar", "reducir", "incrementar", "crear"]:
            m = re.search(r"\b" + lever + r"\b", raw_palanca)
            if m and m.start() < min_pos:
                min_pos = m.start()
                matched_lever = lever

        if matched_lever:
            result["eerr_breakdown"][matched_lever] += 1
        else:
            result["errors"].append(f"Acción [{raw_id}]: Palanca EERR inválida '{row[palanca_idx]}'. Debe ser Eliminar, Reducir, Incrementar o Crear.")

        # Validar trazabilidad CAME
        came_found = any(ct in raw_came.lower() for ct in VALID_CAME_TYPES)
        if not came_found:
            result["errors"].append(f"Acción [{raw_id}]: No especifica un cruce CAME válido (DO, FO, FA, DA) en '{raw_came}'.")

    result["actions_found"] = len(action_ids)
    if result["actions_found"] == 0:
        result["errors"].append("No se extrajeron acciones de valor válidas de la tabla EERR.")
        return result

    # Verificar si alguna palanca EERR quedó en 0
    missing_levers = [lever.capitalize() for lever, count in result["eerr_breakdown"].items() if count == 0]
    if missing_levers:
        result["warnings"].append(f"Las siguientes palancas EERR no tienen acciones asignadas: {', '.join(missing_levers)}.")

    # 2. Validar Tabla Filtro de Restricciones
    filter_data = find_filter_table(tables)
    if not filter_data:
        result["errors"].append("No se encontró la Matriz del Filtro de Restricciones Operativas (Plazos, Costos, TI, Resistencia, Dictamen).")
        return result

    filter_headers, filter_rows = filter_data
    f_headers_lower = [h.lower() for h in filter_headers]

    f_id_idx = next((i for i, h in enumerate(f_headers_lower) if "id" in h), 0)
    plazos_idx = next((i for i, h in enumerate(f_headers_lower) if "plazo" in h or "tiempo" in h), None)
    costos_idx = next((i for i, h in enumerate(f_headers_lower) if "costo" in h or "presupuesto" in h or "financier" in h), None)
    ti_idx = next((i for i, h in enumerate(f_headers_lower) if "tecnol" in h or "ti" in h or "sistemas" in h), None)
    resistencia_idx = next((i for i, h in enumerate(f_headers_lower) if "resist" in h or "cambio" in h or "humano" in h), None)
    dictamen_idx = next((i for i, h in enumerate(f_headers_lower) if "dictamen" in h or "viabilidad" in h), None)
    mitigacion_idx = next((i for i, h in enumerate(f_headers_lower) if "mitigaci" in h or "ajuste" in h or "condici" in h), None)

    if any(idx is None for idx in (plazos_idx, costos_idx, ti_idx, resistencia_idx, dictamen_idx)):
        missing = []
        if plazos_idx is None: missing.append("Plazos y Tiempos")
        if costos_idx is None: missing.append("Costos/Presupuesto")
        if ti_idx is None: missing.append("Dependencia TI")
        if resistencia_idx is None: missing.append("Resistencia al Cambio")
        if dictamen_idx is None: missing.append("Dictamen de Viabilidad")
        result["errors"].append(f"La tabla del Filtro de Restricciones carece de columnas obligatorias: {', '.join(missing)}.")
        return result

    filter_action_ids = set()
    for row_idx, row in enumerate(filter_rows, start=1):
        if len(row) <= max(f_id_idx, plazos_idx, costos_idx, ti_idx, resistencia_idx, dictamen_idx):
            result["errors"].append(f"Fila {row_idx} del Filtro de Restricciones tiene menos columnas de las esperadas.")
            continue

        raw_fid = normalize_text(row[f_id_idx])
        if not raw_fid:
            continue
        filter_action_ids.add(raw_fid)

        raw_dictamen = normalize_text(row[dictamen_idx]).lower()
        matched_dictamen = None
        for vd in VALID_DICTAMENES_ORDERED:
            if vd in raw_dictamen:
                matched_dictamen = vd
                break

        if not matched_dictamen:
            result["errors"].append(f"Fila {row_idx} [{raw_fid}]: Dictamen inválido '{row[dictamen_idx]}'. Debe ser APROBADA, APROBADA CON MITIGACIÓN o DESECHADA/POSPUESTA.")
        else:
            std_dictamen = "APROBADA CON MITIGACIÓN" if "mitiga" in matched_dictamen or "condic" in matched_dictamen else matched_dictamen.upper()
            result["dictamen_breakdown"][std_dictamen] = result["dictamen_breakdown"].get(std_dictamen, 0) + 1

            # Si es con mitigación, validar que la columna de mitigación no esté vacía ni sea N/A
            if "mitiga" in matched_dictamen or "condic" in matched_dictamen:
                result["mitigated_actions"].append(raw_fid)
                if mitigacion_idx is not None and mitigacion_idx < len(row):
                    mitigacion_val = normalize_text(row[mitigacion_idx])
                    if not mitigacion_val or mitigacion_val.lower() in {"n/a", "no aplica", "-", "ninguna"}:
                        result["errors"].append(f"Acción [{raw_fid}] está 'APROBADA CON MITIGACIÓN' pero no define una medida de mitigación concreta en la columna correspondiente.")
                else:
                    result["errors"].append(f"Acción [{raw_fid}] está condicionada/con mitigación pero falta la columna de mitigaciones.")

    # 3. Conciliación entre Tabla EERR y Filtro
    missing_in_filter = action_ids - filter_action_ids
    if missing_in_filter:
        result["errors"].append(f"Acciones en tabla EERR ausentes en el Filtro de Restricciones: {', '.join(sorted(missing_in_filter))}.")

    missing_in_eerr = filter_action_ids - action_ids
    if missing_in_eerr:
        result["warnings"].append(f"Acciones en Filtro ausentes en la tabla EERR: {', '.join(sorted(missing_in_eerr))}.")

    if not result["errors"]:
        result["valid"] = True

    return result

def main():
    parser = argparse.ArgumentParser(description="Validador de Gobernanza para Acciones de Valor EERR y Filtro Operativo (acciones_valor.md)")
    parser.add_argument("file", nargs="?", default="acciones_valor.md", help="Ruta al archivo Markdown a validar (default: acciones_valor.md)")
    parser.add_argument("--json", action="store_true", help="Salida en formato JSON estructurado")
    args = parser.parse_args()

    file_path = Path(args.file)
    res = validate_value_actions_file(file_path)

    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print("=" * 70)
        print("  VALIDADOR DE ACCIONES DE VALOR EERR Y FILTRO DE RESTRICCIONES (GMP E3)")
        print("=" * 70)
        print(f"Archivo analizado: {res['file']}")
        print(f"Acciones evaluadas: {res['actions_found']}")
        print("Distribución EERR:")
        for lever, count in res["eerr_breakdown"].items():
            print(f"  - {lever.capitalize()}: {count}")
        print("Dictámenes de Viabilidad:")
        for dictamen, count in res["dictamen_breakdown"].items():
            print(f"  - {dictamen}: {count}")

        if res["mitigated_actions"]:
            print(f"Acciones con Mitigación Requerida: {', '.join(res['mitigated_actions'])}")

        if res["warnings"]:
            print("\nADVERTENCIAS:")
            for w in res["warnings"]:
                print(f"  [!] {w}")

        if res["errors"]:
            print("\nERRORES CRÍTICOS DE GOBERNANZA:")
            for e in res["errors"]:
                print(f"  [X] {e}")
            print("\nRESULTADO: RECHAZADO (No cumple los estándares de gobernanza)")
            sys.exit(1)
        else:
            print("\nRESULTADO: APROBADO (Estructura, trazabilidad y filtros validados con éxito)")
            sys.exit(0)

if __name__ == "__main__":
    main()
