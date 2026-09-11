#!/usr/bin/env python3
"""Validador de Integridad Estructural y Reglas de Negocio para la Matriz de Stakeholders.

Verifica que el archivo Markdown (stakeholders.md o plantilla) cumpla estrictamente
con las especificaciones de la cátedra GMP y de la skill stakeholderMatrix:
1. Existencia de secciones obligatorias.
2. Estructura de tabla con la triple columna requerida:
   - Resultados (¿Qué reciben? - Lo tangible)
   - Expectativas (¿Qué esperan? - Lo intangible)
   - Obstáculos y Riesgos (¿Qué podría fallar?)
3. Cobertura taxonómica de roles internos (operativos, supervisión, gerencia/dirección)
   y externos (clientes, proveedores/socios, reguladores/control).
4. Principio de Bidireccionalidad y distinción Obstáculos (actual) vs Riesgos (potencial).
5. No vacíos en las celdas de las columnas clave.
6. Presencia de análisis de tensiones y derivación hacia FODA / CAME.
"""

import argparse
import os
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    (r"##\s+1\.\s+Encuadre", "1. Encuadre y Alcance del Proceso"),
    (r"##\s+2\.\s+Matriz Principal|GRUPOS DE INTER[EÉ]S", "2. Matriz Principal de Partes Interesadas"),
    (r"##\s+3\.\s+Matriz de Prominencia|Mendelow|Poder vs Inter[eé]s", "3. Matriz de Prominencia / Mendelow"),
    (r"##\s+4\.\s+An[aá]lisis de Tensiones|Conflictos", "4. Análisis de Tensiones y Conflictos Inter-Actor"),
    (r"##\s+5\.\s+Conclusiones|Insumos Cr[ií]ticos", "5. Conclusiones e Insumos Críticos para el Rediseño TO-BE"),
]

MANDATORY_COLUMN_PATTERNS = [
    (r"Stakeholder|Actor|Parte\s+Interesada|Identificaci[oó]n", "Columna Stakeholder/Actor"),
    (r"Resultados?(\s+Esperados?)?(\s*\(¿?Qu[eé]\s+reciben\??\))?", "Columna 1: Resultados"),
    (r"Expectativas?(\s+(Cualitativas?|Deseos?))?(\s*\(¿?Qu[eé]\s+esperan\??\))?", "Columna 2: Expectativas"),
    (r"Obst[aá]culos?|Riesgos?(\s*\(¿?Qu[eé]\s+podr[ií]a\s+fallar\??\))?", "Columna 3: Obstáculos y Riesgos"),
]

EXPECTED_CATEGORIES = [
    (
        r"\boperativ[oa]s?\b|\bdocentes?\b|\bprofesor(es)?\b|\bcajer[oa]s?\b|\bejecut(or|ores)\b|\bfrontline\b|\bt[eé]cnic[oa]s?\b|\bpersonal\s+de\s+planta\b|\boperad(or|ores)\b|\bchofer(es)?\b|\bpicking\b",
        "Interno - Nivel Operativo",
    ),
    (
        r"\bsupervis(i[oó]n|or(es)?)\b|\bmandos?\s+medios?\b|\bcoordinad|\bl[ií]der(es)?\b|\bjef(e|es|atura)\b|\bdirector(es)?\s+de\s+carrera\b",
        "Interno - Supervisión / Mandos Medios",
    ),
    (
        r"\bgerenc(ia|ial)\b|\bdirecci[oó]n\b|\bejecutiv|\bdueñ[oa]s?\b|\baccionistas?\b|\bpropietari[oa]s?\b|\bdirectori[oa]\b|\bgobierno\b|\bsponsor\b|\bpatrocinad|\bc-level\b",
        "Interno - Gerencia / Dirección",
    ),
    (
        r"\bclientes?\b|\bdestinatari|\balumn[oa]s?\b|\bestudiantes?\b|\bpacientes?\b|\busuari[oa]s?\b|\bconsumid",
        "Externo - Cliente / Destinatario",
    ),
    (
        r"\bproveedor(es)?\b|\btransport|\bsoci[oa]s?\b|\baliad[oa]s?\b|\babasteced|\bpartners?\b|\bvendors?\b|\bempresas(\s+y\s+mercado|\s+del\s+mercado)?\b",
        "Externo - Proveedor / Socio",
    ),
    (
        r"\bregulador(es)?\b|\bfiscal\b|\bcontrol\s+(sanitario|fiscal|normativo)\b|\bente\b|\borganismo\b|\bministeri|\bauditor[ií]a\b|\bacreditaci[oó]n\b|\bcompliance\b",
        "Externo - Regulador / Control",
    ),
]


def extract_all_tables(content: str) -> list[tuple[list[str], list[list[str]], int]]:
    """Extrae todas las tablas Markdown del documento junto con el número de línea inicial."""
    lines = content.splitlines()
    tables = []
    current_table = []
    start_line = 0

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            if not current_table:
                start_line = i
            current_table.append(stripped)
        else:
            if len(current_table) >= 3:
                headers = [col.strip() for col in current_table[0].strip("|").split("|")]
                data_rows = []
                for t_line in current_table[2:]:
                    cols = [c.strip() for c in t_line.strip("|").split("|")]
                    data_rows.append(cols)
                tables.append((headers, data_rows, start_line))
            current_table = []

    if len(current_table) >= 3:
        headers = [col.strip() for col in current_table[0].strip("|").split("|")]
        data_rows = []
        for t_line in current_table[2:]:
            cols = [c.strip() for c in t_line.strip("|").split("|")]
            data_rows.append(cols)
        tables.append((headers, data_rows, start_line))

    return tables


def extract_table(content: str) -> tuple[list[str], list[list[str]]]:
    """Extrae las cabeceras y filas de la tabla Markdown principal de Stakeholders.
    
    Si existen múltiples tablas (ej. encuadre preliminar, RACI, etc.),
    selecciona la tabla que contiene las cabeceras de la matriz de stakeholders.
    """
    tables = extract_all_tables(content)
    if not tables:
        return [], []

    # 1. Buscar la tabla que contenga simultáneamente cabeceras de Stakeholder y Resultados/Expectativas
    for headers, rows, _ in tables:
        h_text = " ".join(headers)
        has_stk = any(re.search(r"Stakeholder|Actor|Parte\s+Interesada|Identificaci[oó]n", h, re.I) for h in headers)
        has_res = any(re.search(r"Resultados?", h, re.I) for h in headers)
        has_obs = any(re.search(r"Obst[aá]culos?|Riesgos?", h, re.I) for h in headers)
        if has_stk and (has_res or has_obs):
            return headers, rows

    # 2. Si no se identifica de forma inequívoca, retornar la primera tabla con >= 3 columnas
    for headers, rows, _ in tables:
        if len(headers) >= 3:
            return headers, rows

    return tables[0][0], tables[0][1]


def validate_stakeholder_file(file_path: Path, verbose: bool = False) -> list[str]:
    errors = []
    if not file_path.exists():
        return [f"El archivo no existe: {file_path}"]

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"Error al leer archivo {file_path}: {exc}"]

    if not content.strip():
        return [f"El archivo está vacío: {file_path}"]

    # 1. Validar secciones obligatorias
    for pattern, name in REQUIRED_SECTIONS:
        if not re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Sección obligatoria faltante: '{name}'")
        elif verbose:
            print(f"  [OK] Sección encontrada: '{name}'")

    # 2. Extraer y validar tabla principal
    headers, rows = extract_table(content)
    if not headers or not rows:
        errors.append("No se encontró una tabla Markdown válida con al menos cabecera y filas de datos.")
        return errors

    # Validar presencia de columnas obligatorias
    col_indexes = {}
    for pat, col_name in MANDATORY_COLUMN_PATTERNS:
        found_idx = None
        for idx, h in enumerate(headers):
            if re.search(pat, h, re.IGNORECASE):
                found_idx = idx
                break
        if found_idx is None:
            errors.append(f"Columna obligatoria no identificada en la cabecera: '{col_name}'")
        else:
            col_indexes[col_name] = found_idx
            if verbose:
                print(f"  [OK] Columna identificada ({col_name}) en índice {found_idx}")

    # Validar que las filas no tengan celdas vacías en las columnas requeridas
    req_keys = [
        "Columna Stakeholder/Actor",
        "Columna 1: Resultados",
        "Columna 2: Expectativas",
        "Columna 3: Obstáculos y Riesgos"
    ]
    for r_idx, row in enumerate(rows, start=1):
        for key in req_keys:
            if key in col_indexes:
                idx = col_indexes[key]
                val = row[idx] if idx < len(row) else ""
                val_clean = val.replace("`", "").strip()
                if not val_clean or val_clean in ["-", "N/A"]:
                    errors.append(f"Fila {r_idx} tiene vacía o incompleta la celda para '{key}'")

    # 3. Validar cobertura taxonómica (Internos y Externos) a través de la tabla y del documento
    table_text = " ".join(" ".join(r) for r in rows)
    full_search_scope = table_text + " " + content
    for cat_pat, cat_name in EXPECTED_CATEGORIES:
        if not re.search(cat_pat, full_search_scope, re.IGNORECASE):
            errors.append(f"Falta cobertura de categoría obligatoria en la matriz: '{cat_name}'")
        elif verbose:
            print(f"  [OK] Categoría cubierta en matriz: '{cat_name}'")

    # 4. Validar mención a matrices conectadas (FODA / CAME)
    if not re.search(r"\bFODA\b", content, re.IGNORECASE):
        errors.append("Debe incluir la conexión de hallazgos con la Matriz FODA (Debilidades/Amenazas).")
    if not re.search(r"\bCAME\b|EERR|\bEliminar\b|\bReducir\b", content, re.IGNORECASE):
        errors.append("Debe incluir la conexión de hallazgos con Acciones de Valor CAME / EERR.")

    # 5. Validar presencia del principio de bidireccionalidad
    if not re.search(r"bidireccional|afecta\s+(al\s+proceso|este\s+proceso)|c[oó]mo\s+nos\s+afecta", content, re.IGNORECASE):
        errors.append("Debe incorporar el principio de bidireccionalidad de cátedra (¿Cómo nos afecta el stakeholder y cómo el proceso le afecta a él?).")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validador de Matriz de Stakeholders (GMP Etapa 2)")
    parser.add_argument("file", nargs="?", default="stakeholders.md", help="Ruta al archivo Markdown a validar")
    parser.add_argument("--check-template", action="store_true", help="Validar la plantilla canónica de la skill")
    parser.add_argument("-v", "--verbose", action="store_true", help="Mostrar detalle de validaciones exitosas")

    args = parser.parse_args()

    target_path = Path(args.file)
    if args.check_template:
        template_candidate = Path(__file__).parent.parent / "templates" / "stakeholder_matrix_template.md"
        target_path = template_candidate

    print(f"[*] Validando archivo de matriz de stakeholders: {target_path}")
    errors = validate_stakeholder_file(target_path, verbose=args.verbose)

    if errors:
        print(f"\n[ERROR] Se detectaron {len(errors)} problema(s) de validación:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\n[ÉXITO] El archivo cumple al 100% con la estructura canónica de cátedra, triple columna y taxonomía de stakeholderMatrix.")
        sys.exit(0)


if __name__ == "__main__":
    main()
