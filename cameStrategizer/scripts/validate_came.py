#!/usr/bin/env python3
"""
Validador determinista de consistencia, reglas de oro y cruces formales de la Matriz CAME.
Gestión y Mejora de Procesos (GMP) - Etapa 3 Matriz 1.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Tipos de cuadrantes canónicos y factores internos/externos permitidos
QUADRANT_TYPES = {
    "FO": {
        "name": "Ofensiva (FO)",
        "allowed_cross": ({"F"}, {"O"}),
        "keywords": ["ofensiv", "mantener-explotar", "mantener y explotar", "max-max", "f-o"],
    },
    "FA": {
        "name": "Defensiva (FA)",
        "allowed_cross": ({"F"}, {"A"}),
        "keywords": ["defensiv", "mantener-afrontar", "mantener y afrontar", "max-min", "f-a"],
    },
    "DO": {
        "name": "Reorientación (DO)",
        "allowed_cross": ({"D"}, {"O"}),
        "keywords": ["reorientaci", "corregir-explotar", "corregir y explotar", "min-max", "d-o", "adaptativ"],
    },
    "DA": {
        "name": "Supervivencia (DA)",
        "allowed_cross": ({"D"}, {"A"}),
        "keywords": ["supervivencia", "corregir-afrontar", "corregir y afrontar", "min-min", "d-a"],
    },
}

# Regex robusto para tokens de factores FODA (ej. F1, D2, O3, A1, F-1, D_02, F.1, F_tech_01, D-RRHH-02)
FACTOR_TOKEN_REGEX = re.compile(
    r"(?i)\b([FDOA](?:[-_][a-zA-Z0-9]+)*[-_.]?\d+)\b"
)


def split_markdown_cells(line: str) -> list[str]:
    """Divide una línea de tabla Markdown respetando pipes escapados (\\|)."""
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|") and not stripped.endswith(r"\|"):
        stripped = stripped[:-1]

    raw_cells = re.split(r"(?<!\\)\|", stripped)
    return [c.replace(r"\|", "|").strip() for c in raw_cells]


def classify_quadrant_type(raw_type: str) -> str | None:
    """
    Identifica el cuadrante formal (FO, FA, DO, DA) a partir de una cadena.
    Usa límites de palabra exactos para acrónimos de 2 letras y raíces semánticas
    para evitar colisiones con palabras del español (ej. 'orientada', 'rápido', 'fase').
    """
    if not raw_type:
        return None

    cleaned = raw_type.strip().lower()

    # 1. Búsqueda de acrónimo exacto delimitado (ej. 'FO', '**FO**', '(FA)', '[DO]', 'EST-DA-01')
    m = re.search(r"(?:^|[\s_(\[-])(FO|FA|DO|DA)(?:[\s_)\]:\-]|$)", raw_type, re.IGNORECASE)
    if m:
        return m.group(1).upper()

    # 2. Búsqueda por palabras clave inequívocas
    for q_code, q_info in QUADRANT_TYPES.items():
        for kw in q_info["keywords"]:
            if kw in cleaned:
                return q_code

    return None


def infer_quadrant_from_factors(internal_factors: list[str], external_factors: list[str]) -> str | None:
    """
    Deduce matemáticamente el cuadrante a partir de los factores cruzados:
    - F x O => FO (Ofensiva)
    - F x A => FA (Defensiva)
    - D x O => DO (Reorientación)
    - D x A => DA (Supervivencia)
    """
    if not internal_factors or not external_factors:
        return None

    int_prefixes = {f[0].upper() for f in internal_factors}
    ext_prefixes = {f[0].upper() for f in external_factors}

    if int_prefixes == {"F"} and ext_prefixes == {"O"}:
        return "FO"
    if int_prefixes == {"F"} and ext_prefixes == {"A"}:
        return "FA"
    if int_prefixes == {"D"} and ext_prefixes == {"O"}:
        return "DO"
    if int_prefixes == {"D"} and ext_prefixes == {"A"}:
        return "DA"

    return None


def extract_factors_from_cell(cell_text: str) -> tuple[list[str], list[str]]:
    """Extrae factores internos (F, D) y externos (O, A) de una celda de cruce."""
    factors = [f.upper() for f in FACTOR_TOKEN_REGEX.findall(cell_text)]
    internal = [f for f in factors if f.startswith(("F", "D"))]
    external = [f for f in factors if f.startswith(("O", "A"))]
    return internal, external


def extract_declared_foda_factors(content: str) -> dict[str, set[str]]:
    """
    Extrae los factores declarados formalmente en la Sección 1 (Línea Base FODA)
    si dicha sección está presente en el documento.
    """
    declared = {"F": set(), "D": set(), "O": set(), "A": set()}
    lines = content.splitlines()
    in_factor_table = False
    id_col_idx = 0

    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            in_factor_table = False
            continue

        cells = split_markdown_cells(s)
        if not in_factor_table:
            hdr = " ".join(cells).lower()
            if any(k in hdr for k in ["id factor", "factor id", "código factor", "codigo factor"]) or (
                "factor" in hdr and any(k in hdr for k in ["tipo", "denominación", "denominacion"])
            ):
                in_factor_table = True
                for i, c in enumerate(cells):
                    c_clean = c.lower()
                    if any(k in c_clean for k in ["id", "factor", "código", "codigo"]):
                        id_col_idx = i
                        break
            continue

        if all(re.match(r"^:?-+:?$", c) for c in cells):
            continue

        if len(cells) > id_col_idx:
            cell_val = cells[id_col_idx]
            found = FACTOR_TOKEN_REGEX.findall(cell_val)
            for f in found:
                p = f[0].upper()
                if p in declared:
                    declared[p].add(f.upper())

    return declared


def is_came_strategy_table_header(header_cells: list[str]) -> bool:
    """
    Determina si un encabezado corresponde a una tabla tabular de estrategias CAME,
    descartando registros de factores FODA, matrices conceptuales 2x2 y tablas EERR.
    """
    header_text = " ".join(header_cells).lower()

    # 1. Descartar tablas exclusivas de registro de factores FODA
    if any(k in header_text for k in ["id factor", "factor id", "denominación", "denominacion", "evidencia de auditoría", "tendencia del entorno"]):
        return False

    # 2. Descartar matriz conceptual 2x2 (cuyas columnas son las dos variables externas O y A)
    has_oportunidades = any(k in header_text for k in ["oportunidad", "oportunidades"])
    has_amenazas = any(k in header_text for k in ["amenaza", "amenazas"])
    if has_oportunidades and has_amenazas:
        return False

    # 3. Descartar tablas downstream de Acciones de Valor EERR o Filtro de Restricciones
    if any(k in header_text for k in ["eerr", "acción de valor", "accion de valor", "acciones de valor", "filtro de restricciones", "restricciones operativas", "medida de mitigación"]):
        return False

    # 4. Requiere columnas características de una tabla de estrategias o cruces CAME
    has_cross_col = any(k in header_text for k in ["cruce", "factor", "cruzad"])
    has_strat_or_came = any(k in header_text for k in ["came", "estrategia", "cuadrante", "tipo", "enunciado", "acción", "accion", "propuesta", "iniciativa"])

    return has_cross_col and has_strat_or_came


def parse_markdown_table_rows(markdown_content: str) -> list[dict]:
    """
    Parsea las filas de todas las tablas Markdown del documento que contengan estrategias CAME,
    preservando el contexto del encabezado de sección y los nombres de columnas.
    """
    rows = []
    lines = markdown_content.splitlines()

    in_table = False
    headers = []
    current_heading = ""

    for line in lines:
        stripped = line.strip()

        # Rastrear títulos de sección (Markdown headings #, ##, ###)
        if stripped.startswith("#"):
            current_heading = stripped.lstrip("#").strip()
            in_table = False
            headers = []
            continue

        if not stripped.startswith("|"):
            in_table = False
            headers = []
            continue

        cells = split_markdown_cells(stripped)

        if not in_table:
            if is_came_strategy_table_header(cells):
                headers = [c.lower() for c in cells]
                in_table = True
            continue

        # Ignorar fila separadora |---|---|...
        if all(re.match(r"^:?-+:?$", c) for c in cells):
            continue

        # Ignorar filas vacías o con una sola celda poblada (subencabezados / separadores de cuadrante)
        non_empty_cells = [c for c in cells if c.strip()]
        if len(non_empty_cells) <= 1:
            # Si contiene un cuadrante, actualizar el contexto de encabezado
            if non_empty_cells and classify_quadrant_type(non_empty_cells[0]):
                current_heading = non_empty_cells[0]
            continue

        # Parsear fila de datos
        if len(cells) >= 2:
            row_dict = {}
            for i, cell in enumerate(cells):
                if i < len(headers):
                    row_dict[headers[i]] = cell
                else:
                    row_dict[f"col_{i}"] = cell
            row_dict["_raw_cells"] = cells
            row_dict["_raw_line"] = stripped
            row_dict["_section_heading"] = current_heading
            rows.append(row_dict)

    return rows


def validate_came_content(content: str, filename: str = "came.md") -> dict:
    """
    Valida exhaustivamente el contenido de un archivo CAME contra las reglas de oro de cátedra:
    - 4 cuadrantes obligatorios (FO, FA, DO, DA).
    - Citación explícita de factores (IDs Fi x Oj).
    - Coherencia matemática entre factores y cuadrante asignado.
    - Detección de texto de plantilla sin reemplazar.
    - Trazabilidad con factores FODA declarados (si existen en Sección 1).
    """
    errors = []
    warnings = []
    detected_strategies = []
    quadrant_counts = {"FO": 0, "FA": 0, "DO": 0, "DA": 0}

    # 1. Validación de presencia de contenido básico
    if not content.strip():
        return {
            "valid": False,
            "filename": filename,
            "errors": ["El archivo está completamente vacío."],
            "warnings": warnings,
            "quadrant_counts": quadrant_counts,
            "total_strategies": 0,
            "strategies": [],
            "declared_factors": {},
        }

    # 2. Extraer factores declarados en Sección 1 (si existen)
    declared_factors = extract_declared_foda_factors(content)
    has_declared_baseline = any(len(s) > 0 for s in declared_factors.values())

    # 3. Parseo de tablas de estrategias CAME
    table_rows = parse_markdown_table_rows(content)

    if not table_rows:
        errors.append(
            "No se encontró ninguna tabla Markdown con columnas de estrategias CAME (ID, Tipo, Cruce de Factores)."
        )

    current_quadrant_context = None

    for idx, row in enumerate(table_rows, start=1):
        cells = row.get("_raw_cells", [])
        row_line = row.get("_raw_line", "")
        heading = row.get("_section_heading", "")

        id_val = ""
        type_val = ""
        cross_val = ""
        desc_val = ""
        statement_val = ""
        action_val = ""

        # Mapeo semántico de celdas según encabezados detectados
        for k, v in row.items():
            if k.startswith("_"):
                continue
            k_lower = k.lower()
            if "descripci" in k_lower and "factor" in k_lower:
                desc_val = v
            elif "cruce" in k_lower or "factor" in k_lower:
                cross_val = v
            elif "tipo" in k_lower or "cuadrante" in k_lower:
                type_val = v
            elif re.search(r"\b(id|código|codigo|n°|nro|#)\b", k_lower) and "factor" not in k_lower:
                id_val = v
            elif "enunciado" in k_lower or "directriz" in k_lower:
                statement_val = v
            elif "acción" in k_lower or "accion" in k_lower or "iniciativa" in k_lower or "propuesta" in k_lower:
                action_val = v
            elif "descripci" in k_lower and not statement_val:
                statement_val = v

        # Fallbacks por posición si los encabezados no eran estándar
        if not type_val and len(cells) >= 2 and not cross_val:
            type_val = cells[1]
        if not cross_val and len(cells) >= 3:
            cross_val = cells[2]
        elif not cross_val and len(cells) >= 2:
            cross_val = cells[1]

        if not id_val and len(cells) >= 1:
            id_val = cells[0]

        if not statement_val and len(cells) >= 4:
            statement_val = cells[3]
        if not action_val and len(cells) >= 5:
            action_val = cells[-1]

        # Verificar si la fila contiene texto de plantilla sin reemplazar
        placeholder_indicators = [
            "[directriz de", "[iniciativa", "[nombre corto", "[nombre f",
            "[nombre d", "[nombre o", "[nombre a", "[proceso primario",
            "[objetivo estratégico"
        ]
        if any(ph in row_line.lower() for ph in placeholder_indicators):
            warnings.append(
                f"Fila {idx} contiene texto de plantilla sin reemplazar: '{row_line[:65]}...'"
            )
            continue

        # Extraer factores citados
        internal_factors, external_factors = extract_factors_from_cell(cross_val)
        if not internal_factors or not external_factors:
            # Intentar extraer de celdas adyacentes si cross_val estaba desfasada
            int_alt, ext_alt = extract_factors_from_cell(f"{id_val} {type_val} {row_line}")
            if int_alt and ext_alt:
                internal_factors, external_factors = int_alt, ext_alt

        # Clasificación del cuadrante:
        # Prioridad 1: Columna 'Tipo CAME' / 'Cuadrante'
        quadrant = classify_quadrant_type(type_val)
        # Prioridad 2: Columna ID (ej. EST-FO-01)
        if not quadrant:
            quadrant = classify_quadrant_type(id_val)
        # Prioridad 3: Título de la sección Markdown precedente
        if not quadrant and heading:
            quadrant = classify_quadrant_type(heading)
        # Prioridad 4: Deducción matemática unívoca a partir de los factores cruzados (Fi x Oj => FO)
        if not quadrant and internal_factors and external_factors:
            quadrant = infer_quadrant_from_factors(internal_factors, external_factors)

        if not quadrant:
            warnings.append(
                f"Fila {idx} ({id_val}): No se pudo determinar el cuadrante CAME (FO, FA, DO, DA) desde el valor '{type_val}'."
            )
            continue

        # Normalizar ID de estrategia si era genérico o faltaba
        if not id_val or id_val.strip() == type_val.strip():
            id_val = f"EST-{quadrant}-{quadrant_counts[quadrant] + 1:02d}"

        # Validar citación explícita de factores
        if not internal_factors or not external_factors:
            errors.append(
                f"Estrategia '{id_val}' ({quadrant}): Cruce de factores inválido '{cross_val}'. "
                f"Debe citar explícitamente al menos un factor interno (F o D) y uno externo (O o A), ej. 'F1 x O2'."
            )
            continue

        # Validar coherencia matemática entre factores y cuadrante (Regla de Oro de Cátedra)
        allowed_int, allowed_ext = QUADRANT_TYPES[quadrant]["allowed_cross"]
        for int_f in internal_factors:
            prefix = int_f[0].upper()
            if prefix not in allowed_int:
                errors.append(
                    f"Estrategia '{id_val}' clasificada como {quadrant} pero cruza el factor interno '{int_f}', "
                    f"el cual no corresponde al cuadrante (debe ser {' o '.join(allowed_int)})."
                )
        for ext_f in external_factors:
            prefix = ext_f[0].upper()
            if prefix not in allowed_ext:
                errors.append(
                    f"Estrategia '{id_val}' clasificada como {quadrant} pero cruza el factor externo '{ext_f}', "
                    f"el cual no corresponde al cuadrante (debe ser {' o '.join(allowed_ext)})."
                )

        # Validar trazabilidad con factores FODA declarados en Sección 1 (si existe la tabla)
        if has_declared_baseline:
            for int_f in internal_factors:
                p = int_f[0].upper()
                if p in declared_factors and declared_factors[p] and int_f.upper() not in declared_factors[p]:
                    warnings.append(
                        f"Trazabilidad: El factor interno '{int_f}' en '{id_val}' no fue declarado formalmente "
                        f"en el Registro de Factores FODA de entrada (factores conocidos: {', '.join(sorted(declared_factors[p]))})."
                    )
            for ext_f in external_factors:
                p = ext_f[0].upper()
                if p in declared_factors and declared_factors[p] and ext_f.upper() not in declared_factors[p]:
                    warnings.append(
                        f"Trazabilidad: El factor externo '{ext_f}' en '{id_val}' no fue declarado formalmente "
                        f"en el Registro de Factores FODA de entrada (factores conocidos: {', '.join(sorted(declared_factors[p]))})."
                    )

        quadrant_counts[quadrant] += 1
        detected_strategies.append(
            {
                "id": id_val,
                "quadrant": quadrant,
                "cross": f"{','.join(internal_factors)} x {','.join(external_factors)}",
                "statement": statement_val,
                "action": action_val,
            }
        )

    # 4. Verificación de cobertura obligatoria de los 4 cuadrantes
    missing_quadrants = [q for q, count in quadrant_counts.items() if count == 0]
    if missing_quadrants:
        errors.append(
            f"Faltan estrategias para los siguientes cuadrantes obligatorios: {', '.join(missing_quadrants)}. "
            f"Las reglas de cátedra exigen poblar FO, FA, DO y DA."
        )

    # 5. Recomendación de umbral mínimo de estrategias
    total_strategies = sum(quadrant_counts.values())
    if total_strategies < 4 and not errors:
        warnings.append(
            f"Se detectaron solo {total_strategies} estrategias. Se recomienda un mínimo de 4 a 8 estrategias (al menos 1-2 por cuadrante)."
        )

    valid = len(errors) == 0

    return {
        "valid": valid,
        "filename": filename,
        "errors": errors,
        "warnings": warnings,
        "quadrant_counts": quadrant_counts,
        "total_strategies": total_strategies,
        "strategies": detected_strategies,
        "declared_factors": {k: sorted(list(v)) for k, v in declared_factors.items()},
    }


def run_self_tests() -> int:
    """Ejecuta pruebas automáticas unitarias sobre casos borde, sintaxis flexible y reglas de cátedra."""
    print("=== Ejecutando Suite de Pruebas Unitarias de validate_came.py ===")
    test_cases_passed = 0
    total_cases = 0

    # Caso 1: Archivo vacío
    total_cases += 1
    res1 = validate_came_content("", "empty.md")
    assert not res1["valid"], "Caso 1 falló: Archivo vacío debería ser inválido"
    assert "vacío" in res1["errors"][0]
    test_cases_passed += 1
    print("[PASS] Caso 1: Detección de archivo vacío.")

    # Caso 2: Markdown sin tablas
    total_cases += 1
    res2 = validate_came_content("# Just text\nNo tables here", "notables.md")
    assert not res2["valid"], "Caso 2 falló: Texto sin tablas debería ser inválido"
    test_cases_passed += 1
    print("[PASS] Caso 2: Detección de ausencia de tablas CAME.")

    # Caso 3: Cuadrante faltante (solo FO y DO)
    total_cases += 1
    partial_table = """
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO (Ofensiva) | F1 x O1 | Apalancar flota | Servicio premium |
| EST-DO-01 | DO (Reorientación) | D1 x O2 | Digitalizar | App móvil |
"""
    res3 = validate_came_content(partial_table, "partial.md")
    assert not res3["valid"], "Caso 3 falló: Cuadrantes faltantes FA y DA deben provocar error"
    assert any("FA" in e for e in res3["errors"])
    assert any("DA" in e for e in res3["errors"])
    test_cases_passed += 1
    print("[PASS] Caso 3: Detección de cuadrantes incompletos (FA, DA faltantes).")

    # Caso 4: Cruce de factores incongruente con el cuadrante (D1 x O1 en FO)
    total_cases += 1
    incongruent_table = """
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO (Ofensiva) | D1 x O1 | Enunciado | Acción |
| EST-FA-01 | FA (Defensiva) | F1 x A1 | Enunciado | Acción |
| EST-DO-01 | DO (Reorientación) | D2 x O2 | Enunciado | Acción |
| EST-DA-01 | DA (Supervivencia) | D3 x A2 | Enunciado | Acción |
"""
    res4 = validate_came_content(incongruent_table, "incongruent.md")
    assert not res4["valid"], "Caso 4 falló: Cruce D1 x O1 en FO debe ser rechazado"
    assert any("clasificada como FO pero cruza el factor interno 'D1'" in e for e in res4["errors"])
    test_cases_passed += 1
    print("[PASS] Caso 4: Detección de cruce de factores incongruente con el cuadrante.")

    # Caso 5: Matriz completa conforme con los 4 cuadrantes (8 estrategias)
    total_cases += 1
    valid_table = """
# Matriz CAME

| ID Estrategia | Tipo CAME | Cruce de Factores (IDs) | Enunciado Estratégico | Acción de Mejora Concreta Derivada |
|---|---|---|---|---|
| `EST-FO-01` | **FO (Ofensiva)** | `F1 x O1` | Apalancar capacidad de flota moderna | Desplegar nuevo servicio farmacéutico |
| `EST-FO-02` | **FO (Ofensiva)** | `F2 x O2` | Integrar APIs de cotización | Conectar cotizador automático |
| `EST-FA-01` | **FA (Defensiva)** | `F1 x A1` | Blindar cuota de mercado ante low-cost | Certificar ISO 9001 en trazabilidad |
| `EST-FA-02` | **FA (Defensiva)** | `F2 x A2` | Retener cuentas corporativas clave | Contratos SLA de cumplimiento estricto |
| `EST-DO-01` | **DO (Reorientación)** | `D1 x O1` | Eliminar gestión de remitos en papel | App móvil para transportistas con firma digital |
| `EST-DO-02` | **DO (Reorientación)** | `D2 x O2` | Conectar silos de almacén con ERP | Integración por API REST en tiempo real |
| `EST-DA-01` | **DA (Supervivencia)** | `D1 x A1` | Segregar roles críticos de recepción | Reestructurar funciones en almacén |
| `EST-DA-02` | **DA (Supervivencia)** | `D2 x A2` | Rediseñar planes de contingencia | Auditorías cruzadas quincenales |
"""
    res5 = validate_came_content(valid_table, "valid.md")
    assert res5["valid"], f"Caso 5 falló: Matriz conforme no fue validada. Errores: {res5['errors']}"
    assert res5["quadrant_counts"]["FO"] == 2
    assert res5["quadrant_counts"]["FA"] == 2
    assert res5["quadrant_counts"]["DO"] == 2
    assert res5["quadrant_counts"]["DA"] == 2
    assert res5["total_strategies"] == 8
    test_cases_passed += 1
    print("[PASS] Caso 5: Matriz completa conforme validada con éxito (8/8 estrategias válidas).")

    # Caso 6: Cruce multivariable y sintaxis flexible con corchetes/paréntesis
    total_cases += 1
    multi_table = """
# Matriz CAME Multivariable

| ID Estrategia | Tipo CAME | Cruce de Factores (IDs) | Enunciado Estratégico | Acción de Mejora Concreta Derivada |
|---|---|---|---|---|
| EST-FO-01 | FO | [F1, F2 x O1] | Enunciado multivariable | Acción FO |
| EST-FA-01 | FA | (F1) x (A1, A2) | Enunciado multivariable | Acción FA |
| EST-DO-01 | DO | D1 + D2 x O1 | Enunciado multivariable | Acción DO |
| EST-DA-01 | DA | [D1 x A1, A2] | Enunciado multivariable | Acción DA |
"""
    res6 = validate_came_content(multi_table, "multi.md")
    assert res6["valid"], f"Caso 6 falló: Cruces multivariables no fueron aceptados: {res6['errors']}"
    assert res6["total_strategies"] == 4
    test_cases_passed += 1
    print("[PASS] Caso 6: Soporte de cruces multivariables y notación flexible comprobado.")

    # Caso 7: Factores con IDs no estándar (F-1, D_02, F.1, F_tech_01, D-RRHH-02)
    total_cases += 1
    custom_ids_table = """
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO | F_tech_01 x O_market_02 | Enunciado | Acción |
| EST-FA-01 | FA | F-1 x A-EXT-01 | Enunciado | Acción |
| EST-DO-01 | DO | D_02 x O.1 | Enunciado | Acción |
| EST-DA-01 | DA | D-RRHH-02 x A-01 | Enunciado | Acción |
"""
    res7 = validate_came_content(custom_ids_table, "custom_ids.md")
    assert res7["valid"], f"Caso 7 falló: IDs no estándar provocaron error: {res7['errors']}"
    assert res7["total_strategies"] == 4
    test_cases_passed += 1
    print("[PASS] Caso 7: Soporte de IDs alfanuméricos extendidos (F-1, D_02, F_tech_01, D-RRHH-02).")

    # Caso 8: Prevención de colisión con palabras en español en clasificación de cuadrante
    total_cases += 1
    assert classify_quadrant_type("Estrategia orientada a oportunidades") is None, "Caso 8 falló: 'orientada' no debe ser DA"
    assert classify_quadrant_type("Estrategia de Crecimiento Rápido") is None, "Caso 8 falló: 'rápido' no debe ser DO"
    assert classify_quadrant_type("Fase 1: Implementación") is None, "Caso 8 falló: 'fase' no debe ser FA"
    assert classify_quadrant_type("Foco de inversión") is None, "Caso 8 falló: 'foco' no debe ser FO"
    test_cases_passed += 1
    print("[PASS] Caso 8: Prevención de colisiones con palabras en español (orientada, rápido, fase, foco).")

    # Caso 9: Convivencia con matriz conceptual 2x2 sin falsos errores
    total_cases += 1
    coexist_doc = """
# Matriz CAME

## 2. Matriz Conceptual CAME (2x2)

| Matriz CAME | Oportunidades (O) | Amenazas (A) |
|---|---|---|
| Fortalezas (F) | FO Ofensiva: F1 x O1 | FA Defensiva: F1 x A1 |
| Debilidades (D) | DO Reorientación: D1 x O1 | DA Supervivencia: D1 x A1 |

## 3. Matriz CAME Consolidada

| ID Estrategia | Tipo CAME | Cruce de Factores (IDs) | Enunciado Estratégico | Acción de Mejora Concreta Derivada |
|---|---|---|---|---|
| EST-FO-01 | FO (Ofensiva) | F1 x O1 | Enunciado FO | Acción FO |
| EST-FA-01 | FA (Defensiva) | F1 x A1 | Enunciado FA | Acción FA |
| EST-DO-01 | DO (Reorientación) | D1 x O1 | Enunciado DO | Acción DO |
| EST-DA-01 | DA (Supervivencia) | D1 x A1 | Enunciado DA | Acción DA |
"""
    res9 = validate_came_content(coexist_doc, "coexist.md")
    assert res9["valid"], f"Caso 9 falló: Matriz 2x2 provocó colisión de tabla: {res9['errors']}"
    assert res9["total_strategies"] == 4
    test_cases_passed += 1
    print("[PASS] Caso 9: Convivencia armónica de matriz conceptual 2x2 con tabla de estrategias.")

    # Caso 10: Deducción automática del cuadrante cuando falta la columna 'Tipo CAME'
    total_cases += 1
    no_type_table = """
| ID Estrategia | Cruce de Factores | Enunciado Estratégico | Acción Concreta |
|---|---|---|---|
| 1 | F1 x O1 | Enunciado FO | Acción FO |
| 2 | F1 x A1 | Enunciado FA | Acción FA |
| 3 | D1 x O1 | Enunciado DO | Acción DO |
| 4 | D1 x A1 | Enunciado DA | Acción DA |
"""
    res10 = validate_came_content(no_type_table, "no_type.md")
    assert res10["valid"], f"Caso 10 falló: Inferencia por cruce falló: {res10['errors']}"
    assert res10["quadrant_counts"]["FO"] == 1
    assert res10["quadrant_counts"]["FA"] == 1
    assert res10["quadrant_counts"]["DO"] == 1
    assert res10["quadrant_counts"]["DA"] == 1
    test_cases_passed += 1
    print("[PASS] Caso 10: Deducción matemática automática del cuadrante a partir de los factores.")

    # Caso 11: Soporte de pipes escapados dentro de celdas
    total_cases += 1
    escaped_pipe_table = """
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO | F1 x O1 | Enunciado con formula $F \\| O$ | CREAR: Plataforma \\| Módulo web |
| EST-FA-01 | FA | F1 x A1 | Enunciado FA | Acción FA |
| EST-DO-01 | DO | D1 x O1 | Enunciado DO | Acción DO |
| EST-DA-01 | DA | D1 x A1 | Enunciado DA | Acción DA |
"""
    res11 = validate_came_content(escaped_pipe_table, "escaped_pipe.md")
    assert res11["valid"], f"Caso 11 falló: Pipe escapado desalineó columnas: {res11['errors']}"
    assert res11["total_strategies"] == 4
    test_cases_passed += 1
    print("[PASS] Caso 11: Soporte de pipes escapados (\\|) dentro de celdas Markdown.")

    # Caso 12: Filas separadoras / subencabezados dentro de la tabla
    total_cases += 1
    divider_table = """
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| **Estrategias Ofensivas (FO)** | | | | |
| EST-FO-01 | FO | F1 x O1 | Enunciado FO | Acción FO |
| **Estrategias Defensivas (FA)** | | | | |
| EST-FA-01 | FA | F1 x A1 | Enunciado FA | Acción FA |
| **Estrategias de Reorientación (DO)** | | | | |
| EST-DO-01 | DO | D1 x O1 | Enunciado DO | Acción DO |
| **Estrategias de Supervivencia (DA)** | | | | |
| EST-DA-01 | DA | D1 x A1 | Enunciado DA | Acción DA |
"""
    res12 = validate_came_content(divider_table, "divider.md")
    assert res12["valid"], f"Caso 12 falló: Fila separadora provocó error: {res12['errors']}"
    assert res12["total_strategies"] == 4
    test_cases_passed += 1
    print("[PASS] Caso 12: Omisión transparente de filas separadoras de cuadrante dentro de la tabla.")

    # Caso 13: Trazabilidad contra factores FODA declarados en Sección 1
    total_cases += 1
    foda_doc = """
# Matriz CAME

## 1. Registro de Factores FODA de Entrada
| ID Factor | Tipo | Denominación Corta | Descripción |
|---|---|---|---|
| F1 | Fortaleza | Flota moderna | Descripción F1 |
| D1 | Debilidad | Silos TI | Descripción D1 |
| O1 | Oportunidad | Nuevos mercados | Descripción O1 |
| A1 | Amenaza | Competencia digital | Descripción A1 |

## 3. Matriz CAME Consolidada
| ID Estrategia | Tipo CAME | Cruce de Factores | Enunciado | Acción |
|---|---|---|---|---|
| EST-FO-01 | FO | F1 x O1 | Enunciado FO | Acción FO |
| EST-FA-01 | FA | F1 x A1 | Enunciado FA | Acción FA |
| EST-DO-01 | DO | D1 x O1 | Enunciado DO | Acción DO |
| EST-DA-01 | DA | D1 x A1 | Enunciado DA | Acción DA |
| EST-FO-02 | FO | F9 x O1 | Factor F9 no declarado | Acción FO2 |
"""
    res13 = validate_came_content(foda_doc, "foda_trace.md")
    assert res13["valid"], "Caso 13 falló: Estrategias válidas no deben bloquearse"
    assert any("F9" in w and "no fue declarado" in w for w in res13["warnings"]), "Caso 13 falló: Factor F9 no declarado debió emitir advertencia"
    test_cases_passed += 1
    print("[PASS] Caso 13: Trazabilidad estricta contra registro de factores FODA declarados.")

    print(f"\nResultado de la suite: {test_cases_passed}/{total_cases} pruebas aprobadas exitosamente.")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Validador de consistencia y reglas de oro de la Matriz CAME (GMP Etapa 3)."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="came.md",
        help="Ruta al archivo came.md a validar (por defecto: ./came.md)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emitir resultado en formato JSON estructurado.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Ejecutar la suite interna de pruebas unitarias y salir.",
    )

    args = parser.parse_args()

    if args.self_test:
        sys.exit(run_self_tests())

    target_path = Path(args.path)

    if not target_path.exists():
        msg = f"Error: No se encontró el archivo '{target_path.resolve()}'."
        if args.json:
            print(json.dumps({"valid": False, "error": msg}))
        else:
            print(f"[ERROR] {msg}", file=sys.stderr)
        sys.exit(1)

    try:
        content = target_path.read_text(encoding="utf-8")
    except Exception as e:
        msg = f"Error al leer archivo '{target_path}': {e}"
        if args.json:
            print(json.dumps({"valid": False, "error": msg}))
        else:
            print(f"[ERROR] {msg}", file=sys.stderr)
        sys.exit(1)

    result = validate_came_content(content, filename=target_path.name)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"=== Validación de Matriz CAME: '{target_path.name}' ===")
        if result["valid"]:
            print("[OK] Archivo validado exitosamente. Estado: CONFORME.")
        else:
            print("[FAIL] Fallos detectados en las reglas de cátedra.", file=sys.stderr)

        print("\nDistribución por Cuadrantes:")
        for q, count in result["quadrant_counts"].items():
            status = "[OK]" if count > 0 else "[FALTA]"
            print(f"  {status} {q} ({QUADRANT_TYPES[q]['name']}): {count} estrategias")

        print(f"\nTotal de estrategias válidas detectadas: {result['total_strategies']}")

        if result.get("declared_factors") and any(result["declared_factors"].values()):
            print("\nFactores FODA Declarados en Entrada:")
            for p, facts in result["declared_factors"].items():
                p_label = {"F": "Fortalezas (F)", "D": "Debilidades (D)", "O": "Oportunidades (O)", "A": "Amenazas (A)"}.get(p, p)
                if facts:
                    print(f"  - {p_label}: {', '.join(facts)}")

        if result["errors"]:
            print("\nErrores Bloqueantes:")
            for err in result["errors"]:
                print(f"  - [ERROR] {err}", file=sys.stderr)

        if result["warnings"]:
            print("\nAdvertencias:")
            for w in result["warnings"]:
                print(f"  - [ADVERTENCIA] {w}")

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
