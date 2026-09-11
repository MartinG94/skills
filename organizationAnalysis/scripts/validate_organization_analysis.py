#!/usr/bin/env python3
"""
Validador determinista de Matriz de Cadena de Valor Virtual (virtualValueChain) — GMP Etapa 1.
Basado en los lineamientos metodológicos de Rayport & Sviokla (1995), el apunte de cátedra
APU_U1_Cadena_de_Valor_Virtual.pdf y la Planilla de Matrices TPI 2026 (Etapa 1 Matriz 1).

Verifica:
1. Existencia del archivo y estructura de las 4 secciones canónicas obligatorias.
2. Encuadre organizacional completo (campos de Matriz 1: Organización, Misión, Visión, Objetivos, etc.).
3. Presencia y orden secuencial estricto de los 5 procesos de información de Rayport & Sviokla:
   - 1. Recopilar (Gather)
   - 2. Organizar (Organize)
   - 3. Seleccionar (Select)
   - 4. Sintetizar (Synthesize)
   - 5. Distribuir (Distribute)
4. Mapeo riguroso de fases de madurez digital de cátedra:
   - Fase 1: Visibilidad
   - Fase 2: Proyección de la Capacidad (Capacidad de Reflejo)
   - Fase 3: La Matriz del Valor (Nuevas Relaciones con Clientes)
5. Especificación técnica de atributos de datos (no vacíos ni genéricos).
6. Diagnóstico de madurez global, cuello de botella y alineación con SDL (recursos operandos vs operantes).
7. Acciones prioritarias de intervención digital para Etapa 3 GMP.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

CANONICAL_STAGES = [
    ("recopilar", "gather"),
    ("organizar", "organize"),
    ("seleccionar", "select"),
    ("sintetizar", "synthesize"),
    ("distribuir", "distribute"),
]

VALID_MATURITY_PHASES = [
    "fase 1",
    "fase 2",
    "fase 3",
    "visibilidad",
    "proyección de la capacidad",
    "proyeccion de la capacidad",
    "capacidad de reflejo",
    "matriz del valor",
    "nuevas relaciones",
    "nuevas relaciones con clientes",
    "nuevas relaciones de clientes",
]

REQUIRED_SECTIONS = [
    (1, r"(?:encuadre|organizaci[oó]n|espejo\s+f[ií]sico)"),
    (2, r"(?:matriz.*(?:5\s+etapas|cadena\s+de\s+valor\s+virtual))"),
    (3, r"(?:diagn[oó]stico.*madurez)"),
    (4, r"(?:acciones\s+prioritarias|intervenci[oó]n\s+digital)"),
]

REQUIRED_FRAMING_FIELDS = [
    (r"(?:organizaci[oó]n|nombre)", "Nombre de la Organización"),
    (r"(?:misi[oó]n)", "Misión"),
    (r"(?:visi[oó]n)", "Visión"),
    (r"(?:objetivos?\s+estrat[eé]gicos?)", "Objetivos Estratégicos"),
    (r"(?:cliente)", "Cliente de la Organización"),
    (r"(?:producto|servicio)", "Producto / Servicio"),
    (r"(?:proceso|cadena.*f[ií]sica)", "Proceso Seleccionado / Cadena Física Subyacente"),
]


def parse_markdown_tables(content: str) -> List[List[List[str]]]:
    """Extrae todas las tablas Markdown del contenido como listas de filas (listas de celdas)."""
    tables = []
    current_table = []
    in_table = False

    for line in content.splitlines():
        line = line.strip()
        if line.startswith("|") and line.endswith("|"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            # Ignorar línea divisoria |---|---|
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


def find_canonical_matrix_table(tables: List[List[List[str]]]) -> Optional[Tuple[List[str], List[List[str]]]]:
    """Identifica la tabla canónica de las 5 etapas de la Cadena de Valor Virtual."""
    for table in tables:
        if not table or len(table) < 2:
            continue
        header = [h.lower() for h in table[0]]
        has_etapa = any("etapa" in h or "proceso" in h for h in header)
        has_asis = any("as-is" in h or "actual" in h or "práctica" in h or "practica" in h for h in header)
        has_tobe = any("to-be" in h or "digital" in h or "oportunidad" in h for h in header)
        has_datos = any("dato" in h or "atributo" in h for h in header)
        has_madurez = any("madurez" in h or "fase" in h for h in header)

        if has_etapa and (has_asis or has_tobe) and (has_datos or has_madurez):
            return table[0], table[1:]
    return None


def validate_content(content: str, filename: str = "cadena_valor_virtual.md") -> Dict[str, Any]:
    """Ejecuta la validación integral del entregable de Cadena de Valor Virtual."""
    results: Dict[str, Any] = {
        "file": filename,
        "valid": True,
        "errors": [],
        "warnings": [],
        "metrics": {
            "stages_found": [],
            "missing_stages": [],
            "framing_fields_found": [],
            "missing_framing_fields": [],
            "tables_found": 0,
            "has_cross_matrix": False,
            "has_sdl_analysis": False,
            "has_bottleneck": False,
            "has_priority_actions": False,
        }
    }

    # 1. Validación de Secciones Obligatorias
    for sec_num, sec_pattern in REQUIRED_SECTIONS:
        if not re.search(r"^##\s+.*" + sec_pattern, content, re.IGNORECASE | re.MULTILINE):
            results["errors"].append(f"Falta la Sección Obligatoria {sec_num} ({sec_pattern})")
            results["valid"] = False

    # 2. Validación de Campos de Encuadre (Matriz 1 Cátedra)
    for field_pat, field_name in REQUIRED_FRAMING_FIELDS:
        if re.search(r"[-*]\s+\*\*" + field_pat, content, re.IGNORECASE) or re.search(r"###?\s+.*" + field_pat, content, re.IGNORECASE):
            results["metrics"]["framing_fields_found"].append(field_name)
        else:
            results["metrics"]["missing_framing_fields"].append(field_name)
            results["warnings"].append(f"Campo de Encuadre Organizacional no identificado: '{field_name}'")

    # 3. Extracción y validación de tablas
    tables = parse_markdown_tables(content)
    results["metrics"]["tables_found"] = len(tables)

    # Detectar si existe matriz cruzada físico-virtual (Porter vs 5 etapas)
    for t in tables:
        header = [h.lower() for h in t[0]]
        if any("porter" in h or "cadena física" in h or "cadena fisica" in h or "etapa de la cadena" in h for h in header):
            results["metrics"]["has_cross_matrix"] = True
            break

    canonical_table = find_canonical_matrix_table(tables)
    if not canonical_table:
        results["errors"].append("No se encontró la tabla canónica de las 5 Etapas de la Cadena de Valor Virtual")
        results["valid"] = False
        return results

    headers, rows = canonical_table
    header_lower = [h.lower() for h in headers]

    col_etapa_idx = next((i for i, h in enumerate(header_lower) if "etapa" in h or "proceso" in h), 0)
    col_asis_idx = next((i for i, h in enumerate(header_lower) if "as-is" in h or "actual" in h), None)
    col_tobe_idx = next((i for i, h in enumerate(header_lower) if "to-be" in h or "digital" in h), None)
    col_datos_idx = next((i for i, h in enumerate(header_lower) if "dato" in h or "atributo" in h), None)
    col_madurez_idx = next((i for i, h in enumerate(header_lower) if "madurez" in h or "fase" in h), None)

    # 4. Validar las 5 Etapas Canónicas en Orden
    detected_stages = []
    for row_idx, row in enumerate(rows):
        if col_etapa_idx >= len(row):
            continue
        cell_text = row[col_etapa_idx].lower()
        matched_stage = None
        for es_term, en_term in CANONICAL_STAGES:
            if es_term in cell_text or en_term in cell_text:
                matched_stage = es_term
                break
        if matched_stage:
            detected_stages.append((matched_stage, row_idx, row))

    stage_names_only = [s[0] for s in detected_stages]
    results["metrics"]["stages_found"] = stage_names_only

    expected_names = [s[0] for s in CANONICAL_STAGES]
    missing = [s for s in expected_names if s not in stage_names_only]
    results["metrics"]["missing_stages"] = missing

    if missing:
        results["errors"].append(f"Etapas de información faltantes en la matriz: {', '.join(missing)}")
        results["valid"] = False

    # Verificar orden secuencial
    if len(stage_names_only) == 5 and stage_names_only != expected_names:
        results["warnings"].append(
            f"El orden de las etapas no coincide con la secuencia canónica: encontradas {stage_names_only}, esperadas {expected_names}"
        )

    # Validar celdas de cada fila encontrada
    for stage_name, row_idx, row in detected_stages:
        # AS-IS no vacío
        if col_asis_idx is not None and col_asis_idx < len(row):
            asis_text = row[col_asis_idx].strip()
            if not asis_text or asis_text in ["[...]", "TBD", "-"]:
                results["warnings"].append(f"Fila '{stage_name}': Práctica operativa actual (AS-IS) vacía o genérica")

        # TO-BE no vacío
        if col_tobe_idx is not None and col_tobe_idx < len(row):
            tobe_text = row[col_tobe_idx].strip()
            if not tobe_text or tobe_text in ["[...]", "TBD", "-"]:
                results["warnings"].append(f"Fila '{stage_name}': Oportunidad digital (TO-BE) vacía o genérica")

        # Datos Clave Involucrados
        if col_datos_idx is not None and col_datos_idx < len(row):
            datos_text = row[col_datos_idx].strip()
            if not datos_text or datos_text in ["[...]", "TBD", "-"]:
                results["errors"].append(f"Fila '{stage_name}': 'Datos Clave Involucrados' no especifica atributos técnicos")
                results["valid"] = False
            elif not re.search(r"(`[^`]+`|[a-z0-9_]+|[A-Z0-9_]+)", datos_text):
                results["warnings"].append(f"Fila '{stage_name}': Se recomienda especificar atributos técnicos exactos en 'Datos Clave'")

        # Fase de Madurez
        if col_madurez_idx is not None and col_madurez_idx < len(row):
            madurez_text = row[col_madurez_idx].lower().strip()
            valid_phase_match = any(phase in madurez_text for phase in VALID_MATURITY_PHASES)
            if not valid_phase_match:
                results["errors"].append(
                    f"Fila '{stage_name}': Fase de madurez inválida '{row[col_madurez_idx]}'. "
                    f"Debe corresponder a Fase 1 (Visibilidad), Fase 2 (Capacidad de Reflejo) o Fase 3 (Nuevas Relaciones / Matriz del Valor)"
                )
                results["valid"] = False

    # 5. Validación de Diagnóstico, SDL y Cuello de Botella
    if re.search(r"(?:l[oó]gica\s+dominante|sdl|recurso.*operan|co-creaci[oó]n|value-in-use)", content, re.IGNORECASE):
        results["metrics"]["has_sdl_analysis"] = True
    else:
        results["warnings"].append("No se detectó un análisis explícito de la Lógica Dominante del Servicio (SDL) o recursos operantes")

    if re.search(r"(?:cuello\s+de\s+botella|quiebre|fricci[oó]n|demora\s+cr[ií]tica)", content, re.IGNORECASE):
        results["metrics"]["has_bottleneck"] = True
    else:
        results["warnings"].append("No se detectó la identificación explícita del cuello de botella en el flujo de información")

    if re.search(r"(?:acci[oó]n\s+de|iniciativa|intervenci[oó]n\s+digital|apalancamiento)", content, re.IGNORECASE):
        results["metrics"]["has_priority_actions"] = True
    else:
        results["warnings"].append("No se detectaron acciones prioritarias de intervención digital para alimentar la Etapa 3")

    return results


def print_report(results: Dict[str, Any]) -> None:
    """Imprime un informe amigable en consola."""
    print(f"\n=======================================================")
    print(f" VALIDACIÓN DE CADENA DE VALOR VIRTUAL (Rayport & Sviokla)")
    print(f" Archivo: {results['file']}")
    print(f"=======================================================")

    status_str = "APROBADO" if results["valid"] else "RECHAZADO"
    print(f"Estado de Conformidad: {status_str}\n")

    m = results["metrics"]
    print("Métricas Clave:")
    print(f"  - Tablas encontradas: {m['tables_found']}")
    print(f"  - Matriz cruzada físico-virtual (Porter x 5 etapas): {'Sí' if m['has_cross_matrix'] else 'No (Opcional)'}")
    print(f"  - Etapas identificadas: {len(m['stages_found'])}/5 ({', '.join(m['stages_found'])})")
    print(f"  - Campos de encuadre identificados: {len(m['framing_fields_found'])}/7")
    print(f"  - Diagnóstico SDL presente: {'Sí' if m['has_sdl_analysis'] else 'No'}")
    print(f"  - Cuello de botella identificado: {'Sí' if m['has_bottleneck'] else 'No'}")
    print(f"  - Acciones prioritarias identificadas: {'Sí' if m['has_priority_actions'] else 'No'}\n")

    if results["errors"]:
        print(f"Errores Críticos ({len(results['errors'])}):")
        for err in results["errors"]:
            print(f"  [ERROR] {err}")
        print()

    if results["warnings"]:
        print(f"Advertencias Metodológicas ({len(results['warnings'])}):")
        for warn in results["warnings"]:
            print(f"  [WARN] {warn}")
        print()


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Validador de Cadena de Valor Virtual (Rayport & Sviokla) — GMP Etapa 1")
    parser.add_argument("file", nargs="?", default="cadena_valor_virtual.md", help="Ruta al archivo Markdown entregable")
    parser.add_argument("--json", action="store_true", help="Emitir informe en formato JSON")
    args = parser.parse_args()

    filepath = Path(args.file)
    if not filepath.exists():
        if args.json:
            print(json.dumps({"valid": False, "errors": [f"El archivo '{args.file}' no existe."]}, indent=2))
        else:
            print(f"[ERROR FATAL] El archivo '{args.file}' no existe.", file=sys.stderr)
        sys.exit(1)

    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        if args.json:
            print(json.dumps({"valid": False, "errors": [f"Error al leer archivo: {str(e)}"]}, indent=2))
        else:
            print(f"[ERROR FATAL] Error al leer archivo: {str(e)}", file=sys.stderr)
        sys.exit(1)

    results = validate_content(content, filename=str(filepath))

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print_report(results)

    sys.exit(0 if results["valid"] else 1)


if __name__ == "__main__":
    main()
