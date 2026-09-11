#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador determinista del Mapa de Procesos Institucional (GMP Etapa 1 - 'mapa_procesos.md').

Verifica el cumplimiento de los estándares de cátedra (SLI_U1_C03 y PlanillaMATRICES-TPI 2026):
- Estructura canónica en 5 secciones.
- Clasificación estricta en los 3 niveles: Estratégicos (PE-XX), Operativos (PO-XX) y Soporte (PS-XX).
- Existencia de objetivos definidos para cada proceso individual.
- Bloque de diagrama visual Mermaid válido con subgrafos de niveles.
- Fronteras de entrada (Requisitos del Cliente) y salida (Satisfacción del Cliente).
- Conexión e insumos claros hacia 'seleccion_proceso.md'.
"""

import sys
import os
import re
import json
import argparse
from typing import Dict, List, Any, Tuple

REQUIRED_SECTIONS = [
    (1, r"1\.\s*identificaci[oó]n\s+y\s+encuadre\s+institucional"),
    (2, r"2\.\s*diagrama\s+visual\s+del\s+mapa\s+de\s+procesos"),
    (3, r"3\.\s*inventario\s+estructurado\s+de\s+procesos"),
    (4, r"4\.\s*matriz\s+de\s+relaciones\s+sist[eé]micas|interacciones"),
    (5, r"5\.\s*insumos\s+para\s+la\s+selecci[oó]n\s+del\s+proceso\s+cr[ií]tico|candidatos")
]

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

def validate_process_map_file(file_path: str) -> Dict[str, Any]:
    """Valida exhaustivamente un archivo mapa_procesos.md."""
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
            "critical_selection_link": False
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
            result["errors"].append(f"Sección obligatoria {sec_num} faltante o mal titulada (patrón esperado: '{pattern}').")

    result["stats"]["sections_found"] = len(found_sections)

    # 2. Validación de Diagrama Visual Mermaid
    mermaid_blocks = re.findall(r"```mermaid([\s\S]*?)```", content)
    if mermaid_blocks:
        result["stats"]["has_mermaid_diagram"] = True
        diag = mermaid_blocks[0].lower()
        if "subgraph" not in diag:
            result["warnings"].append("El diagrama Mermaid no utiliza 'subgraph' para estructurar visualmente los niveles del mapa de procesos.")
        if not ("req" in diag or "requisito" in diag or "cliente" in diag):
            result["warnings"].append("El diagrama Mermaid no explicita el nodo de entrada de Requisitos/Clientes a la izquierda.")
        if not ("sat" in diag or "satisfacci" in diag or "valor" in diag):
            result["warnings"].append("El diagrama Mermaid no explicita el nodo de salida de Satisfacción/Valor a la derecha.")
    else:
        result["errors"].append("No se encontró el bloque obligatorio de diagrama visual en Mermaid (```mermaid ... ```).")

    # 3. Validación de Códigos e Inventario de Procesos
    pe_matches = set(re.findall(r"PE-\d+", content))
    po_matches = set(re.findall(r"PO-\d+", content))
    ps_matches = set(re.findall(r"PS-\d+", content))

    result["stats"]["strategic_processes_count"] = len(pe_matches)
    result["stats"]["operational_processes_count"] = len(po_matches)
    result["stats"]["support_processes_count"] = len(ps_matches)
    result["stats"]["total_processes_count"] = len(pe_matches) + len(po_matches) + len(ps_matches)

    if len(pe_matches) < 2:
        result["errors"].append(f"Se deben identificar al menos 2 Procesos Estratégicos con código 'PE-XX'. Detectados: {len(pe_matches)} ({list(pe_matches)}).")

    if len(po_matches) < 2:
        result["errors"].append(f"Se deben identificar al menos 2 Procesos Operativos/Misionales con código 'PO-XX'. Detectados: {len(po_matches)} ({list(po_matches)}).")

    if len(ps_matches) < 2:
        result["errors"].append(f"Se deben identificar al menos 2 Procesos de Soporte con código 'PS-XX'. Detectados: {len(ps_matches)} ({list(ps_matches)}).")

    # 4. Validación de Objetivos por Proceso
    tables = extract_tables(content)
    if len(tables) < 4:
        result["warnings"].append(f"Se detectaron {len(tables)} tablas Markdown. Se recomiendan al menos 4 tablas (Estratégicos, Operativos, Soporte y Relaciones).")

    # Verificar mención de requisitos y satisfacción
    if any(k in lower_content for k in ["requisito", "necesidad del cliente", "demanda"]):
        result["stats"]["customer_requirements_detected"] = True
    else:
        result["warnings"].append("No se detecta mención explícita a requisitos o necesidades de clientes como disparador del mapa.")

    if any(k in lower_content for k in ["satisfacci", "valor entregado", "impacto"]):
        result["stats"]["customer_satisfaction_detected"] = True
    else:
        result["warnings"].append("No se detecta mención explícita a la satisfacción del cliente o valor entregado como salida final del mapa.")

    # 5. Trazabilidad con Selección del Proceso Crítico
    if any(k in lower_content for k in ["seleccion_proceso", "candidato", "proceso cr[ií]tico", "etapa 2"]):
        result["stats"]["critical_selection_link"] = True
    else:
        result["warnings"].append("Se sugiere explicitar la preselección de procesos operativos candidatos para su pase a 'seleccion_proceso.md'.")

    if result["errors"]:
        result["valid"] = False

    return result

def main():
    parser = argparse.ArgumentParser(description="Validador determinista del Mapa de Procesos Institucional (GMP Etapa 1)")
    parser.add_argument("file_path", help="Ruta al archivo mapa_procesos.md")
    parser.add_argument("--json", action="store_true", help="Emitir resultado exclusivamente en formato JSON")
    args = parser.parse_args()

    res = validate_process_map_file(args.file_path)

    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print("================================================================================")
        print("  VALIDADOR DETERMINISTA DEL MAPA DE PROCESOS INSTITUCIONAL (GMP ETAPA 1)")
        print("================================================================================")
        print(f"Archivo analizado: {res['file_path']}")
        print(f"Estado: {'[VALIDO]' if res['valid'] else '[INVALIDO]'}")
        print("--------------------------------------------------------------------------------")
        print(f"Estadísticas:")
        print(f"  - Secciones requeridas: {res['stats']['sections_found']}/5")
        print(f"  - Diagrama Mermaid detectado: {'Si' if res['stats']['has_mermaid_diagram'] else 'No'}")
        print(f"  - Procesos Estratégicos (PE-XX): {res['stats']['strategic_processes_count']}")
        print(f"  - Procesos Operativos (PO-XX): {res['stats']['operational_processes_count']}")
        print(f"  - Procesos de Soporte (PS-XX): {res['stats']['support_processes_count']}")
        print(f"  - Total Procesos Identificados: {res['stats']['total_processes_count']}")
        print(f"  - Requisitos de Entrada / Satisfacción de Salida: {'Si' if res['stats']['customer_requirements_detected'] and res['stats']['customer_satisfaction_detected'] else 'Parcial/Incompleto'}")
        print(f"  - Conexión a Selección Crítica: {'Si' if res['stats']['critical_selection_link'] else 'No'}")

        if res["errors"]:
            print("\n[ERRORES CRÍTICOS]:")
            for err in res["errors"]:
                print(f"  ❌ {err}")

        if res["warnings"]:
            print("\n[ADVERTENCIAS / RECOMENDACIONES]:")
            for warn in res["warnings"]:
                print(f"  ⚠️  {warn}")

        if res["valid"]:
            print("\nResultado: Cumple satisfactoriamente los estándares de cátedra (SLI_U1_C03).")
        print("================================================================================")

    sys.exit(0 if res["valid"] else 1)

if __name__ == "__main__":
    main()
