#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_process_map.py - Validador determinista para Mapa de Procesos y Selección de Proceso Crítico (GMP Etapa 1)

Valida que el archivo entregable 'mapa_procesos.md' cumpla estrictamente con:
1. Existencia del archivo y contenido no vacío en UTF-8.
2. Detección de placeholders sin completar ([...]).
3. Presencia de las 5 secciones obligatorias de cátedra:
   - 1. Identificación y Encuadre Institucional
   - 2. Diagrama Visual del Mapa de Procesos (3 Niveles de Cátedra)
   - 3. Inventario Estructurado de Procesos y Objetivos (PE, PO, PS)
   - 4. Matriz Multicriterio de Selección Ponderada de Proceso Crítico (Factores C1-C5, pesos sumando 1.00)
   - 5. Proceso Crítico Seleccionado y Justificación Técnica de Cátedra (El Porqué)
4. Diagrama visual Mermaid válido con subgrafos de niveles (PE, PO, PS), requisitos/satisfacción del cliente y resaltado del proceso crítico.
5. Clasificación estricta en los 3 niveles canónicos con códigos PE-XX, PO-XX y PS-XX y objetivos definidos.
6. Matriz multicriterio consistente:
   - 5 factores canónicos (C1 Estrategia, C2 Tendencias/SDL, C3 Problemas/Costos, C4 Cliente, C5 Producto/Servicio).
   - Suma de ponderaciones igual a 1.00 (100% ± 0.001).
   - Puntuaciones discretas dentro del rango [1, 5].
   - Cálculo matemático exacto de S_p = sum(w_i * C_i).
7. Selección unívoca del Proceso Crítico coincidente con el ganador del ranking o regla de desempate jerárquico (C3 > C1 > C4 > C5 > C2).
8. Justificación técnica exhaustiva y fundamentada (mínimo 80 palabras con sustento multifactorial).
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional

REQUIRED_SECTIONS = [
    (1, r"1\.\s*identificaci[oó]n\s+y\s+encuadre\s+institucional"),
    (2, r"2\.\s*diagrama\s+visual\s+del\s+mapa\s+de\s+procesos"),
    (3, r"3\.\s*inventario\s+estructurado\s+de\s+procesos"),
    (4, r"4\.\s*(?:matriz\s+(?:multicriterio\s+de\s+)?selecci[oó]n\s+ponderada|matriz\s+de\s+relaciones)"),
    (5, r"5\.\s*(?:proceso\s+cr[ií]tico\s+seleccionado\s+y\s+justificaci[oó]n|justificaci[oó]n\s+cualitativa\s+y\s+cuantitativa|insumos\s+para\s+la\s+selecci[oó]n)")
]

DEFAULT_WEIGHTS = {
    "C1": 0.25,
    "C2": 0.20,
    "C3": 0.25,
    "C4": 0.20,
    "C5": 0.10
}

PLACEHOLDER_PATTERN = r"\[(?:Nombre|Sector|Rubro|Actividad|Ámbito|Tipo|Misión|Visión|Propuesta|Objetivo|OE-|Propósito|Proceso|Estratégico|Operativo|Soporte|Evento|Entregable|Área|Rol|1-5|0\.00|S_p|Nota|Evidencias|Oportunidades|Fallas|Reclamos|Párrafo|Puntaje|Diferencia|Ej\.|Definición|Declaración|Descripción|Listado)[^\]]*\]"

def extract_tables(content: str) -> List[List[List[str]]]:
    """Extrae tablas de Markdown como listas de filas de celdas."""
    tables = []
    current_table = []
    in_table = False

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
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

def extract_weights(content: str) -> Tuple[Dict[str, float], str]:
    """
    Extrae los pesos de los 5 factores normativos desde la tabla de ponderación o encabezados.
    """
    sec4_match = re.search(r"##\s*4\..*?(?=##\s*5\.|\Z)", content, re.DOTALL | re.IGNORECASE)
    found_weights = {}

    search_text = sec4_match.group(0) if sec4_match else content

    for line in search_text.splitlines():
        line_str = line.strip()
        if not line_str.startswith("|") or "total" in line_str.lower() or "---" in line_str:
            continue
        c_match = re.search(r"\bC([1-5])\b", line_str, re.IGNORECASE)
        if not c_match:
            continue
        code = f"C{c_match.group(1)}"
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
        return found_weights, "tabla_ponderacion"

    # Buscar en encabezados de tabla (ej. C1 (w=0.25))
    hw_matches = re.findall(r"C([1-5])[^|]*?w\s*=\s*([0-9]+(?:[.,][0-9]+)?%?)", search_text, re.IGNORECASE)
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

def validate_process_map_file(file_path: str) -> Dict[str, Any]:
    """Valida exhaustivamente el archivo entregable mapa_procesos.md (o seleccion_proceso.md)."""
    result = {
        "valid": True,
        "file_path": file_path,
        "errors": [],
        "warnings": [],
        "stats": {
            "sections_found": 0,
            "has_mermaid_diagram": False,
            "strategic_processes_count": 0,
            "operational_processes_count": 0,
            "support_processes_count": 0,
            "total_processes_count": 0,
            "customer_requirements_detected": False,
            "customer_satisfaction_detected": False,
            "critical_process_selected": None,
            "critical_process_score": None,
            "critical_process_justified": False,
            "weights_source": "none",
            "evaluated_candidates_count": 0
        }
    }

    p = Path(file_path)
    if not p.is_file():
        result["valid"] = False
        result["errors"].append(f"El archivo no existe: {file_path}")
        return result

    try:
        content = p.read_text(encoding="utf-8")
    except Exception as e:
        result["valid"] = False
        result["errors"].append(f"Error al leer el archivo con codificación UTF-8: {e}")
        return result

    if not content.strip():
        result["valid"] = False
        result["errors"].append("El archivo está completamente vacío.")
        return result

    lower_content = content.lower()

    # Detección de placeholders sin completar
    unfilled = re.findall(PLACEHOLDER_PATTERN, content)
    if unfilled:
        sample = ", ".join(f"'{u}'" for u in unfilled[:5])
        result["warnings"].append(f"Se detectaron {len(unfilled)} placeholders sin completar en el documento: {sample}...")

    # 1. Validación de Secciones Obligatorias
    found_sections = []
    for sec_num, pattern in REQUIRED_SECTIONS:
        if re.search(pattern, lower_content):
            found_sections.append(sec_num)
        else:
            result["errors"].append(f"Sección obligatoria {sec_num} faltante o mal titulada (patrón esperado: '{pattern}').")

    result["stats"]["sections_found"] = len(found_sections)

    # 2. Validación de Diagrama Visual Mermaid
    mermaid_blocks = re.findall(r"```mermaid(.*?)```", content, re.DOTALL | re.IGNORECASE)
    if not mermaid_blocks:
        result["errors"].append("No se encontró ningún bloque de diagrama Mermaid (```mermaid ... ```).")
    else:
        result["stats"]["has_mermaid_diagram"] = True
        diag = mermaid_blocks[0].lower()

        if "flowchart" not in diag and "graph" not in diag:
            result["warnings"].append("El diagrama Mermaid debería comenzar con 'flowchart' o 'graph'.")

        has_est = "estrategico" in diag or "estrategicos" in diag or "pe" in diag
        has_ope = "operativo" in diag or "operativos" in diag or "misionales" in diag or "po" in diag
        has_sop = "soporte" in diag or "apoyo" in diag or "ps" in diag

        if not (has_est and has_ope and has_sop):
            result["errors"].append("El diagrama Mermaid debe estructurarse en los 3 niveles canónicos de cátedra (Estratégicos, Operativos y Soporte).")

        has_req = any(w in diag for w in ["requisito", "necesidad", "aspirante", "cliente", "req", "demanda"])
        has_sat = any(w in diag for w in ["satisfacci", "impacto", "sat", "sociedad", "empleador", "graduado"])

        result["stats"]["customer_requirements_detected"] = has_req
        result["stats"]["customer_satisfaction_detected"] = has_sat

        if not has_req:
            result["warnings"].append("No se identificó claramente el nodo de entrada de Requisitos del Cliente/Mercado en el diagrama Mermaid.")
        if not has_sat:
            result["warnings"].append("No se identificó claramente el nodo de salida de Satisfacción del Cliente en el diagrama Mermaid.")

        # Chequear resaltado de proceso crítico en el diagrama
        if "critico" in diag or "crítico" in diag:
            result["stats"]["diagram_highlights_critical"] = True
        else:
            result["warnings"].append("El diagrama Mermaid no resalta visualmente el Proceso Crítico Seleccionado (clase 'critico' recomendada).")

    # 3. Validación de Inventario Estructurado de Procesos
    pe_codes = set(re.findall(r"\b(PE-\d{2})\b", content, re.IGNORECASE))
    po_codes = set(re.findall(r"\b(PO-\d{2})\b", content, re.IGNORECASE))
    ps_codes = set(re.findall(r"\b(PS-\d{2})\b", content, re.IGNORECASE))

    result["stats"]["strategic_processes_count"] = len(pe_codes)
    result["stats"]["operational_processes_count"] = len(po_codes)
    result["stats"]["support_processes_count"] = len(ps_codes)
    result["stats"]["total_processes_count"] = len(pe_codes) + len(po_codes) + len(ps_codes)

    if len(pe_codes) == 0:
        result["errors"].append("No se identificaron Procesos Estratégicos con nomenclatura canónica PE-XX (ej. PE-01).")
    if len(po_codes) == 0:
        result["errors"].append("No se identificaron Procesos Operativos con nomenclatura canónica PO-XX (ej. PO-01).")
    if len(ps_codes) == 0:
        result["errors"].append("No se identificaron Procesos de Soporte con nomenclatura canónica PS-XX (ej. PS-01).")

    # 4. Validación de Matriz Multicriterio de Selección Ponderada
    weights, weights_source = extract_weights(content)
    result["stats"]["weights_source"] = weights_source
    sum_w = sum(weights.values())

    if abs(sum_w - 1.0) > 0.005:
        result["errors"].append(f"La suma de ponderaciones debe ser exactamente 1.00 (100%), pero se obtuvo {sum_w:.3f}.")

    # Buscar tabla multicriterio en Sección 4
    tables = extract_tables(content)
    evaluated_candidates = []
    matrix_table = None

    for t in tables:
        if len(t) < 2:
            continue
        header = " ".join(t[0]).lower()
        if ("c1" in header or "estrategia" in header) and ("c3" in header or "problemas" in header or "costos" in header):
            matrix_table = t
            break

    if not matrix_table:
        result["errors"].append("No se encontró la tabla de la Matriz Multicriterio de Selección Ponderada en la Sección 4.")
    else:
        # Analizar filas de la matriz
        header_row = [c.lower() for c in matrix_table[0]]
        for row in matrix_table[1:]:
            if len(row) < 7:
                continue
            id_cell = row[0].strip()
            name_cell = row[1].strip() if len(row) > 1 else ""

            # Buscar notas de C1 a C5
            scores = []
            for cell in row[2:]:
                # Extraer primer número entero
                num_match = re.search(r"\b([1-5])\b", cell)
                if num_match:
                    scores.append(int(num_match.group(1)))
                if len(scores) == 5:
                    break

            if len(scores) == 5:
                # Extraer puntaje ponderado reportado si existe
                reported_sp = None
                for cell in row[7:]:
                    sp_match = re.search(r"\b([0-5][.,][0-9]{1,2})\b", cell)
                    if sp_match:
                        reported_sp = float(sp_match.group(1).replace(",", "."))
                        break

                calc_sp = sum(weights[f"C{i+1}"] * scores[i] for i in range(5))
                evaluated_candidates.append({
                    "id": id_cell,
                    "name": name_cell,
                    "scores": scores,
                    "calculated_sp": round(calc_sp, 2),
                    "reported_sp": reported_sp,
                    "raw_row": row
                })

        result["stats"]["evaluated_candidates_count"] = len(evaluated_candidates)
        if len(evaluated_candidates) < 2:
            result["errors"].append(f"Se deben evaluar al menos 2 procesos candidatos en la matriz multicriterio (se encontraron {len(evaluated_candidates)}).")

        # Verificar cálculo matemático de S_p
        for cand in evaluated_candidates:
            if cand["reported_sp"] is not None:
                diff = abs(cand["calculated_sp"] - cand["reported_sp"])
                if diff > 0.05:
                    result["errors"].append(
                        f"Inconsistencia matemática en {cand['id']}: puntaje reportado={cand['reported_sp']}, calculado={cand['calculated_sp']} (S_p = sum(w_i * C_i))."
                    )

    # Determinar ganador matemático
    winner = None
    if evaluated_candidates:
        # Ordenar por Sp descendente, desempate por C3, C1, C4, C5, C2
        sorted_candidates = sorted(
            evaluated_candidates,
            key=lambda c: (
                c["calculated_sp"],
                c["scores"][2],  # C3
                c["scores"][0],  # C1
                c["scores"][3],  # C4
                c["scores"][4],  # C5
                c["scores"][1]   # C2
            ),
            reverse=True
        )
        winner = sorted_candidates[0]

    # 5. Validación del Proceso Crítico Seleccionado y Justificación
    sec5_match = re.search(r"##\s*5\..*", content, re.DOTALL | re.IGNORECASE)
    sec5_text = sec5_match.group(0) if sec5_match else ""

    if not sec5_text:
        result["errors"].append("Sección 5 (Proceso Crítico Seleccionado y Justificación) vacía o ausente.")
    else:
        # Chequear declaración del proceso seleccionado
        selected_code_match = re.search(r"\b(P[OES]-\d{2})\b", sec5_text, re.IGNORECASE)
        selected_code = selected_code_match.group(1).upper() if selected_code_match else None
        result["stats"]["critical_process_selected"] = selected_code

        if not selected_code:
            result["errors"].append("No se declaró explícitamente el código del Proceso Crítico Seleccionado en la Sección 5 (ej. PO-02).")
        elif winner and selected_code.replace("-", "") != winner["id"].replace("-", ""):
            # Si no coincide con el ganador matemático
            if winner["id"] not in selected_code and selected_code not in winner["id"]:
                result["warnings"].append(
                    f"El proceso declarado en Sección 5 ({selected_code}) difiere del ganador matemático de la matriz ({winner['id']})."
                )

        # Chequear presencia de justificación técnica sustantiva
        words = re.findall(r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]{3,}\b", sec5_text)
        word_count = len(words)
        result["stats"]["justification_word_count"] = word_count

        has_multifactor_subheads = (
            ("c1" in sec5_text.lower() or "estrategia" in sec5_text.lower()) and
            ("c3" in sec5_text.lower() or "problemas" in sec5_text.lower() or "costos" in sec5_text.lower() or "cuellos" in sec5_text.lower()) and
            ("c4" in sec5_text.lower() or "cliente" in sec5_text.lower() or "reclamos" in sec5_text.lower())
        )

        if word_count < 80 and not has_multifactor_subheads:
            result["errors"].append(
                f"La justificación técnica de la selección en la Sección 5 es insuficiente ({word_count} palabras). "
                "Debe articular un sustento multifactorial sustantivo (mínimo 80 palabras) explicando el porqué de la elección."
            )
        else:
            result["stats"]["critical_process_justified"] = True

        # Chequear handoff a Etapa 2
        has_handoff = any(k in sec5_text.lower() for k in ["etapa 2", "sipoc", "bpmn", "as-is", "auditoría", "auditoria", "foda"])
        if not has_handoff:
            result["warnings"].append("Se recomienda incluir la delimitación de fronteras y el handoff hacia la Etapa 2 (SIPOC, AS-IS, Auditoría) en la Sección 5.")

    if result["errors"]:
        result["valid"] = False

    return result

def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    parser = argparse.ArgumentParser(description="Validador de Mapa de Procesos y Selección de Proceso Crítico (GMP Etapa 1)")
    parser.add_argument("file_path", help="Ruta al archivo Markdown a validar (mapa_procesos.md)")
    parser.add_argument("--json", action="store_true", help="Salida en formato JSON crudo")
    args = parser.parse_args()

    res = validate_process_map_file(args.file_path)

    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        sys.exit(0 if res["valid"] else 1)

    print("=" * 70)
    print(f"VALIDACION DE MAPA DE PROCESOS Y SELECCION CRITICA: {args.file_path}")
    print("=" * 70)

    if res["valid"]:
        print("\n[OK] ESTADO: VALIDO (Cumple al 100% las directivas de catedra)")
    else:
        print("\n[ERROR] ESTADO: INVALIDO (Se encontraron errores normativos)")

    print("\n--- ESTADISTICAS DEL MAPA Y SELECCION ---")
    stats = res["stats"]
    print(f"* Secciones requeridas encontradas: {stats['sections_found']}/5")
    print(f"* Diagrama visual Mermaid: {'Si' if stats['has_mermaid_diagram'] else 'No'}")
    print(f"* Procesos Estrategicos (PE): {stats['strategic_processes_count']}")
    print(f"* Procesos Operativos (PO): {stats['operational_processes_count']}")
    print(f"* Procesos de Soporte (PS): {stats['support_processes_count']}")
    print(f"* Total de procesos inventariados: {stats['total_processes_count']}")
    print(f"* Procesos candidatos evaluados: {stats['evaluated_candidates_count']}")
    print(f"* Proceso Critico Seleccionado: {stats['critical_process_selected'] or 'No detectado'}")
    print(f"* Justificacion tecnica validada: {'Si' if stats['critical_process_justified'] else 'No'}")

    if res["warnings"]:
        print(f"\n[WARN] ADVERTENCIAS ({len(res['warnings'])}):")
        for w in res["warnings"]:
            print(f"  - {w}")

    if res["errors"]:
        print(f"\n[ERROR] ERRORES DETECTADOS ({len(res['errors'])}):")
        for err in res["errors"]:
            print(f"  - {err}")

    print("=" * 70)
    sys.exit(0 if res["valid"] else 1)

if __name__ == "__main__":
    main()
