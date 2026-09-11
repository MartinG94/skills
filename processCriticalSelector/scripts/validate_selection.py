#!/usr/bin/env python3
"""
validate_selection.py - Validador determinista para matrices de selección de proceso crítico (GMP Etapa 1)

Valida que el archivo entregable 'seleccion_proceso.md' cumpla estrictamente con:
1. Existencia del archivo y contenido no vacío.
2. Detección de placeholders sin completar en el documento.
3. Presencia de las 7 secciones obligatorias de cátedra.
4. Consistencia del vector de ponderación (suma de pesos = 1.00 / 100%) con soporte para decimales (.) y (,).
5. Puntuaciones enteras dentro del rango discreto [1, 5] para los 5 factores de cátedra.
6. Verificación matemática exacta del puntaje ponderado: S_p = sum(w_i * C_i).
7. Validación del ranking y singularidad del ganador.
8. Aplicación y verificación rigurosa del mecanismo objetivo de desempate: C3 -> C1 -> C4.
"""

import sys
import re
from pathlib import Path

REQUIRED_SECTIONS = [
    r"1\.\s+Encuadre\s+Organizacional",
    r"2\.\s+Inventario\s+de\s+Procesos\s+Candidatos",
    r"3\.\s+(?:Factores|Criterios)\s+de\s+(?:Evaluación|Ponderación)",
    r"4\.\s+Matriz\s+(?:Multicriterio\s+de\s+)?Selección\s+Ponderada",
    r"5\.\s+Justificación\s+Cualitativa\s+y\s+Cuantitativa",
    r"6\.\s+Análisis\s+(?:Comparativo|de\s+Procesos\s+No\s+Seleccionados)",
    r"7\.\s+Delimitación\s+de\s+Fronteras|Handoff\s+a\s+Etapa\s+2"
]

DEFAULT_WEIGHTS = {
    "C1": 0.25,
    "C2": 0.20,
    "C3": 0.25,
    "C4": 0.20,
    "C5": 0.10
}

PLACEHOLDER_PATTERN = r"\[(?:Nombre|Sector|Ámbito|Tipo|Misión|Visión|Propuesta|Objetivo|OE-|Propósito|Proceso|Estratégico|Evento|Entregable|Área|Rol|1-5|0\.00|S_p|Nota|Evidencias|Oportunidades|Fallas|Reclamos|Párrafo|Puntaje|Diferencia|Ej\.|Definición|Declaración|Descripción|Listado)[^\]]*\]"

def extract_weights(text: str):
    """
    Extrae los pesos de los 5 factores normativos:
    1. Desde la tabla en la Sección 3 (admite `0.25`, 0.25, **0.25**, 0,25 o 25%).
    2. Desde los encabezados de la Matriz en Sección 4 (ej. w=0.25, w=25%).
    3. Fallback a DEFAULT_WEIGHTS.
    """
    sec3_match = re.search(r"##\s*3\..*?(?=##\s*4\.|\Z)", text, re.DOTALL | re.IGNORECASE)
    found_weights = {}
    if sec3_match:
        sec3_text = sec3_match.group(0)
        for line in sec3_text.splitlines():
            line_str = line.strip()
            if not line_str.startswith("|") or "Total" in line_str or "---" in line_str:
                continue
            c_code_match = re.search(r"\bC([1-5])\b", line_str)
            if not c_code_match:
                continue
            code = f"C{c_code_match.group(1)}"
            cells = [c.strip() for c in line_str.split("|")[1:-1]]
            val = None
            for cell in cells:
                dec_match = re.search(r"\b(0[.,][0-9]{1,3})\b", cell)
                if dec_match:
                    val = float(dec_match.group(1).replace(",", "."))
                    break
                pct_match = re.search(r"\b([1-9][0-9]?)\s*%", cell)
                if pct_match:
                    val = float(pct_match.group(1)) / 100.0
                    break
            if val is not None:
                found_weights[code] = val

    if len(found_weights) == 5:
        return found_weights, "tabla_seccion_3"

    hw_matches = re.findall(r"C([1-5])[^|]*?w\s*=\s*([0-9]+(?:[.,][0-9]+)?%?)", text, re.IGNORECASE)
    if hw_matches:
        header_weights = {}
        for c_idx, w_str in hw_matches:
            if "%" in w_str:
                w_val = float(w_str.replace("%", "").strip()) / 100.0
            else:
                w_val = float(w_str.replace(",", ".").strip())
            header_weights[f"C{c_idx}"] = w_val
        if len(header_weights) == 5:
            return header_weights, "encabezados_matriz"

    return DEFAULT_WEIGHTS.copy(), "default"

def parse_selection_file(file_path: Path):
    if not file_path.exists():
        return False, {"errors": [f"El archivo '{file_path}' no existe."]}
    
    text = file_path.read_text(encoding="utf-8")
    if not text.strip():
        return False, {"errors": ["El archivo está vacío."]}

    errors = []
    warnings = []
    
    # 1. Detección de Placeholders no completados
    placeholders = re.findall(PLACEHOLDER_PATTERN, text, re.IGNORECASE)
    if placeholders:
        sample_ph = placeholders[:3]
        errors.append(
            f"Se detectaron {len(placeholders)} placeholders sin completar en el documento (ej. {sample_ph}). "
            f"El entregable debe completarse con datos reales del caso."
        )

    # 2. Verificar Secciones Requeridas
    missing_sections = []
    for pattern in REQUIRED_SECTIONS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing_sections.append(pattern)
    
    if missing_sections:
        errors.append(f"Faltan secciones requeridas o los encabezados no coinciden: {missing_sections}")

    # 3. Extraer y verificar Ponderaciones (Weights)
    weights, weights_source = extract_weights(text)
    sum_w = sum(weights.values())
    if abs(sum_w - 1.00) > 0.005:
        errors.append(f"La suma de ponderaciones ({weights_source}) es {sum_w:.4f}, debe ser exactamente 1.00.")

    # 4. Extraer y evaluar filas de la Matriz Multicriterio (Sección 4)
    lines = text.splitlines()
    in_matrix = False
    matrix_rows = []

    for line in lines:
        if re.search(r"4\.\s+Matriz", line, re.IGNORECASE):
            in_matrix = True
            continue
        if in_matrix and re.search(r"^##\s+5\.", line):
            in_matrix = False
            break
        if in_matrix:
            clean_line = line.strip()
            if not clean_line.startswith("|") or "---" in clean_line or re.search(r"^\|\s*(?:ID|#|C[oó]digo|Cod|Proceso)\s*\|", clean_line, re.IGNORECASE):
                continue
            cells = [c.strip() for c in clean_line.split("|")[1:-1]]
            if len(cells) >= 8:
                matrix_rows.append(cells)

    if not matrix_rows:
        errors.append("No se encontraron filas de datos en la Matriz Multicriterio (Sección 4).")
        return False, {"errors": errors, "warnings": warnings}

    candidates_evaluated = []
    selected_count = 0
    winner = None

    for row in matrix_rows:
        row_str = " | ".join(row)
        try:
            p_id = row[0].replace("*", "").strip()
            p_name = row[1].replace("*", "").strip()
            
            c_vals = []
            for i in range(2, 7):
                val_match = re.search(r"([0-9]+(?:[.,][0-9]+)?)", row[i])
                if val_match:
                    num_val = float(val_match.group(1).replace(",", "."))
                    c_vals.append(num_val)
                    if not (1.0 <= num_val <= 5.0):
                        errors.append(f"Fila '{p_name}': Calificación C{i-1}={num_val} fuera de rango permitido [1, 5].")
                    elif not num_val.is_integer():
                        errors.append(f"Fila '{p_name}': Calificación C{i-1}={num_val} debe ser un entero discreto [1..5] según la rúbrica oficial.")
                else:
                    c_vals.append(None)

            score_match = re.search(r"([0-9]+(?:[.,][0-9]+)?)", row[7])
            declared_score = float(score_match.group(1).replace(",", ".")) if score_match else None

            # Ranking declarado (columna 8 si existe)
            declared_rank = None
            if len(row) >= 9:
                rank_match = re.search(r"#?([1-9][0-9]*)", row[8])
                if rank_match:
                    declared_rank = int(rank_match.group(1))

            decision = row[-1].upper()
            is_selected = ("SELECCIONADO" in decision) and ("NO SELECCIONADO" not in decision) and ("NO" not in decision)

            if any(v is None for v in c_vals):
                warnings.append(f"Fila '{p_name}': calificaciones no numéricas o incompletas en C1..C5: {row[2:7]}")
                continue

            expected_score = (
                weights["C1"] * c_vals[0] +
                weights["C2"] * c_vals[1] +
                weights["C3"] * c_vals[2] +
                weights["C4"] * c_vals[3] +
                weights["C5"] * c_vals[4]
            )

            if declared_score is not None:
                if abs(declared_score - expected_score) > 0.05:
                    errors.append(
                        f"Fila '{p_name}': Error de cálculo. Puntaje declarado={declared_score:.2f}, "
                        f"pero el cálculo formal sum(w_i * C_i)={expected_score:.2f}."
                    )
            else:
                errors.append(f"Fila '{p_name}': No se pudo extraer el puntaje total declarado.")

            cand_data = {
                "id": p_id,
                "name": p_name,
                "scores": c_vals,
                "declared_score": declared_score,
                "expected_score": expected_score,
                "declared_rank": declared_rank,
                "is_selected": is_selected
            }
            candidates_evaluated.append(cand_data)

            if is_selected:
                selected_count += 1
                winner = cand_data

        except Exception as e:
            errors.append(f"Error parseando fila de matriz: '{row_str}'. Detalle: {e}")

    # 5. Validación de Selección, Ranking y Desempate
    tie_resolution_info = None
    if selected_count == 0:
        errors.append("No se ha marcado ningún proceso como 'SELECCIONADO (Proceso Crítico)'.")
    elif selected_count > 1:
        errors.append(f"Se encontraron {selected_count} procesos marcados como SELECCIONADOS. Debe seleccionarse exactamente uno.")
    else:
        if candidates_evaluated:
            def candidate_sort_key(c):
                return (
                    round(c["expected_score"], 4),
                    c["scores"][2],  # C3: Problemas, costos y fallas (1er criterio de desempate)
                    c["scores"][0],  # C1: Impacto en estrategia (2do criterio de desempate)
                    c["scores"][3],  # C4: Cliente (3er criterio de desempate)
                    c["scores"][4],  # C5: Producto / Servicio
                    c["scores"][1]   # C2: Tendencias / SDL
                )

            sorted_candidates = sorted(candidates_evaluated, key=candidate_sort_key, reverse=True)
            top_candidate = sorted_candidates[0]

            if winner["id"] != top_candidate["id"]:
                max_score = top_candidate["expected_score"]
                if winner["expected_score"] < (max_score - 0.01):
                    errors.append(
                        f"El proceso seleccionado '{winner['name']}' tiene puntaje {winner['expected_score']:.2f}, "
                        f"inferior al máximo obtenido ({max_score:.2f}) por '{top_candidate['name']}'."
                    )
                else:
                    errors.append(
                        f"Empate en puntaje ({winner['expected_score']:.2f}): El proceso seleccionado '{winner['name']}' "
                        f"pierde el desempate jerárquico normativo frente a '{top_candidate['name']}'. "
                        f"Regla de desempate oficial de cátedra: C3 (urgencia/costos) -> C1 (estrategia) -> C4 (cliente). "
                        f"Comparación: {top_candidate['name']} [C3={top_candidate['scores'][2]}, C1={top_candidate['scores'][0]}, C4={top_candidate['scores'][3]}] "
                        f"vs {winner['name']} [C3={winner['scores'][2]}, C1={winner['scores'][0]}, C4={winner['scores'][3]}]."
                    )
            else:
                if len(sorted_candidates) > 1 and abs(sorted_candidates[1]["expected_score"] - top_candidate["expected_score"]) <= 0.01:
                    runner_up = sorted_candidates[1]
                    tie_resolution_info = (
                        f"Empate resuelto por criterio normativo: '{top_candidate['name']}' y '{runner_up['name']}' "
                        f"empataron con puntaje {top_candidate['expected_score']:.2f}. "
                        f"Desempate dirimido por C3 ({top_candidate['scores'][2]} vs {runner_up['scores'][2]}) "
                        f"/ C1 ({top_candidate['scores'][0]} vs {runner_up['scores'][0]}) "
                        f"/ C4 ({top_candidate['scores'][3]} vs {runner_up['scores'][3]})."
                    )

            for expected_rank, cand in enumerate(sorted_candidates, start=1):
                if cand.get("declared_rank") is not None:
                    if cand["declared_rank"] != expected_rank:
                        warnings.append(
                            f"Fila '{cand['name']}': Ranking declarado #{cand['declared_rank']} no coincide "
                            f"con el orden de mérito matemático #{expected_rank}."
                        )

    success = len(errors) == 0
    return success, {
        "errors": errors,
        "warnings": warnings,
        "weights": weights,
        "weights_source": weights_source,
        "candidates": candidates_evaluated,
        "winner": winner,
        "tie_resolution": tie_resolution_info
    }

def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    target_path = Path("seleccion_proceso.md")
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])

    print(f"=== Validando Matriz de Seleccion: {target_path} ===")
    success, result = parse_selection_file(target_path)

    if not success:
        print("[FAIL] Se detectaron errores en el archivo:")
        for err in result.get("errors", []):
            print(f"  - [ERROR] {err}")
        for w in result.get("warnings", []):
            print(f"  - [WARN]  {w}")
        sys.exit(1)
    else:
        print(f"[PASS] Archivo '{target_path}' validado con exito.")
        print(f"[PASS] Ponderaciones verificadas: {result['weights']} (Fuente: {result.get('weights_source', 'desconocida')}, Suma = {sum(result['weights'].values()):.2f})")
        print(f"[PASS] Total candidatos evaluados: {len(result['candidates'])}")
        for c in result['candidates']:
            status = "SELECCIONADO" if c['is_selected'] else "No seleccionado"
            print(f"  - [{c['id']}] {c['name']}: Puntaje = {c['expected_score']:.2f} ({status})")
        if result['winner']:
            print(f"[PASS] Proceso Critico Ganador: '{result['winner']['name']}' (Puntaje: {result['winner']['expected_score']:.2f})")
        if result.get('tie_resolution'):
            print(f"[INFO] {result['tie_resolution']}")
        for w in result.get("warnings", []):
            print(f"  - [WARN]  {w}")
        print("RESULTADO: MATRIZ DE SELECCION VALIDA.")
        sys.exit(0)

if __name__ == "__main__":
    main()
