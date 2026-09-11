#!/usr/bin/env python3
"""Validador determinista de Matriz FODA de Proceso (fodaProcess) — GMP Etapa 2.

Verifica:
1. Existencia de los 4 cuadrantes canónicos (Fortalezas, Debilidades, Oportunidades, Amenazas).
2. Cardinalidad canónica de cátedra: entre 4 y 6 factores por cuadrante (4 <= N <= 6).
3. Prefijos y codificación canónica de identificadores (F1..F6, D1..D6, O1..O6, A1..A6).
4. Trazabilidad de Debilidades hacia fuentes de auditoría / evidencia primaria (processAuditor, RCM, SoD, SRC-XX).
5. Heurísticas de frontera interna vs. externa (Principio de Controlabilidad de Cátedra).
6. Compatibilidad con tablas de 2 a 6 columnas (incluyendo los 3 Ejes de Cátedra de PlanillaMATRICES Matriz 3).
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

MIN_FACTORS_PER_QUADRANT = 4
MAX_FACTORS_PER_QUADRANT = 6

QUADRANT_PREFIXES = {
    "fortalezas": "F",
    "debilidades": "D",
    "oportunidades": "O",
    "amenazas": "A",
}

# Heurísticas de advertencia de frontera interna vs externa
INTERNAL_ACTION_VERBS = [
    r"\bcomprar\b",
    r"\badquirir\s+(software|licencias|maquinaria|servidores)\b",
    r"\bdesarrollar\s+(una\s+|un\s+|nuestra\s+)?(app|sistema|plataforma|software|herramienta)\b",
    r"\bimplementar\s+(un\s+|una\s+|nuestro\s+)?(sistema|erp|crm|soluci[oó]n|proceso|m[oó]dulo)\b",
    r"\bcontratar\s+(personal|choferes|operarios|m[aá]s|docentes)\b",
    r"\bcapacitar\s+a\s+(nuestro|los)\b",
    r"\bcrear\s+(un\s+|una\s+)?(departamento|área|comit[eé]|oficina)\b",
]

INTERNAL_STAFF_THREAT_PATTERNS = [
    r"\b(nuestros\s+empleados|operarios\s+nuestros|personal\s+propio|nuestro\s+sistema|nuestros\s+choferes)\b",
    r"\b(nuestros\s+docentes|nuestros\s+equipos\s+internos)\b",
]

MACRO_EXTERNAL_TERMS = [
    r"\binflaci[oó]n\s+(nacional|general|del\s+pa[ií]s)\b",
    r"\btipo\s+de\s+cambio\s+(oficial|paralelo|vol[aá]til)\b",
    r"\bnueva\s+ley\s+(nacional|provincial|general)\b",
    r"\bguerra\s+(comercial|internacional)\b",
    r"\bpol[ií]ticas\s+macroecon[oó]micas\b",
]

EVIDENCE_POSITIVE_PATTERNS = [
    r"\bsrc-",
    r"\brcm(?:-\d+|\b)",
    r"\baud(?:-\d+|\b)",
    r"\bdoc-",
    r"\bit-",
    r"\bent-",
    r"\bstk-",
    r"\bhallazgo\b",
    r"\bevidencia\b",
    r"\bauditor[ií]a\b",
    r"\binforme\b",
    r"\bobservaci[oó]n\b",
    r"\brelevamiento\b",
    r"\bminuta\b",
    r"\bentrevista\b",
    r"\bsod\b",
    r"\bsilo",
    r"\biso\s*\d+",
    r"\botif\b",
    r"\bm[eé]trica\b",
    r"\bregistro\b",
    r"\bexpediente\b",
    r"\br-\d+\b",
]

NEGATIVE_EVIDENCE_PATTERNS = [
    r"\bsin\s+auditor[ií]a\b",
    r"\bsin\s+evidencia\b",
    r"\bsin\s+sustento\b",
    r"\bsin\s+respaldo\b",
    r"\bcarente\s+de\s+auditor[ií]a\b",
    r"\bcarente\s+de\s+evidencia\b",
    r"\bno\s+posee\s+auditor[ií]a\b",
    r"\bno\s+posee\s+evidencia\b",
]


class FodaFactor:
    def __init__(
        self,
        code: str,
        quadrant: str,
        statement: str,
        evidence: str = "",
        details: str = "",
        raw_cells: Optional[List[str]] = None,
        has_dedicated_empty_evidence_cell: bool = False,
    ):
        self.code = code.strip()
        self.quadrant = quadrant.strip().lower()
        self.statement = statement.strip()
        self.evidence = evidence.strip()
        self.details = details.strip()
        self.raw_cells = raw_cells or []
        self.has_dedicated_empty_evidence_cell = has_dedicated_empty_evidence_cell

    def has_evidence_marker(self) -> bool:
        """Verifica si el factor posee evidencia o respaldo probatorio genuino."""
        if self.has_dedicated_empty_evidence_cell:
            for pat in [r"\bsrc-", r"\brcm", r"\baud-", r"\bdoc-", r"\bit-", r"\bent-"]:
                if re.search(pat, f"{self.statement} {self.details}".lower()):
                    return True
            return False

        combined_text = f"{self.statement} {self.evidence} {self.details} {' '.join(self.raw_cells)}".lower()

        sanitized_text = combined_text
        for neg_pat in NEGATIVE_EVIDENCE_PATTERNS:
            sanitized_text = re.sub(neg_pat, " ", sanitized_text)

        return any(re.search(pat, sanitized_text) for pat in EVIDENCE_POSITIVE_PATTERNS)

    def __repr__(self):
        return f"<Factor {self.code} ({self.quadrant}): {self.statement[:30]}...>"


class FodaValidationResult:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.factors: Dict[str, List[FodaFactor]] = {
            "fortalezas": [],
            "debilidades": [],
            "oportunidades": [],
            "amenazas": [],
        }
        self.errors: List[str] = []
        self.warnings: List[str] = []

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0


def _clean_cell(raw: str) -> str:
    """Limpia formato markdown de celda (asteriscos, backticks, tags html)."""
    text = re.sub(r"<br\s*/?>", " ", raw)
    text = re.sub(r"[\*`_]", "", text)
    return text.strip()


def parse_foda_markdown(content: str, file_path: str = "") -> FodaValidationResult:
    """Parsea el contenido Markdown de un archivo FODA extrayendo factores por cuadrante."""
    result = FodaValidationResult(file_path=file_path)

    current_quadrant: Optional[str] = None
    table_header_cols: Optional[List[str]] = None
    evidence_col_idx: Optional[int] = None
    lines = content.splitlines()

    for line in lines:
        stripped = line.strip()
        lower_line = stripped.lower()

        # Detección de encabezados de sección y cuadrantes (admite #, ##, ###, ####)
        if re.search(r"^#{1,4}\s+.*fortaleza|\bfortalezas\s*\(f\)", lower_line):
            if not stripped.startswith("|"):
                current_quadrant = "fortalezas"
                table_header_cols = None
                evidence_col_idx = None
                continue
        elif re.search(r"^#{1,4}\s+.*debilidad|\bdebilidades\s*\(d\)", lower_line):
            if not stripped.startswith("|"):
                current_quadrant = "debilidades"
                table_header_cols = None
                evidence_col_idx = None
                continue
        elif re.search(r"^#{1,4}\s+.*oportunidad|\boportunidades\s*\(o\)", lower_line):
            if not stripped.startswith("|"):
                current_quadrant = "oportunidades"
                table_header_cols = None
                evidence_col_idx = None
                continue
        elif re.search(r"^#{1,4}\s+.*amenaza|\bamenazas\s*\(a\)", lower_line):
            if not stripped.startswith("|"):
                current_quadrant = "amenazas"
                table_header_cols = None
                evidence_col_idx = None
                continue
        elif re.search(r"^#{1,4}\s+(?:[5-9]\.|\bcontrol de calidad\b|\bpuente metodol[oó]gico\b|\bconclusiones\b|\bcame\b)", lower_line):
            current_quadrant = None
            table_header_cols = None
            evidence_col_idx = None
            continue

        if not current_quadrant:
            continue

        prefix = QUADRANT_PREFIXES[current_quadrant]

        # 1. Parsing de filas de tabla Markdown
        if stripped.startswith("|") and stripped.endswith("|"):
            if re.match(r"^\|(?:\s*:?-+:?\s*\|)+$", stripped):
                continue

            raw_cells = [c.strip() for c in stripped.split("|")][1:-1]
            if not raw_cells:
                continue

            cleaned_cells = [_clean_cell(c) for c in raw_cells]
            joined_row = " ".join(cleaned_cells).lower()

            if ("código" in joined_row or "codigo" in joined_row) and any(
                k in joined_row for k in ["factor", "brecha", "oportunidad", "amenaza"]
            ):
                table_header_cols = [c.lower() for c in cleaned_cells]
                evidence_col_idx = None
                for idx, h in enumerate(table_header_cols):
                    if any(k in h for k in ["evidencia", "hallazgo", "eje 3", "respaldo"]):
                        evidence_col_idx = idx
                        break
                continue

            code_found = None
            code_col_idx = -1
            for idx in range(min(2, len(cleaned_cells))):
                match = re.search(r"^\(?(" + prefix + r"\d+)\)?\.?$", cleaned_cells[idx], re.IGNORECASE)
                if match:
                    code_found = match.group(1).upper()
                    code_col_idx = idx
                    break

            if code_found:
                remaining_cells = cleaned_cells[code_col_idx + 1 :]
                statement = remaining_cells[0] if len(remaining_cells) > 0 else ""
                
                details = ""
                evidence = ""
                has_dedicated_empty_evidence_cell = False

                if evidence_col_idx is not None and evidence_col_idx < len(cleaned_cells):
                    evidence_val = cleaned_cells[evidence_col_idx].strip()
                    if evidence_val == "" or evidence_val == "-" or evidence_val == "[]":
                        has_dedicated_empty_evidence_cell = True
                        evidence = ""
                    else:
                        evidence = evidence_val

                    detail_parts = [
                        cleaned_cells[i]
                        for i in range(len(cleaned_cells))
                        if i != code_col_idx and i != evidence_col_idx and i != (code_col_idx + 1)
                    ]
                    details = " | ".join(detail_parts)
                else:
                    if len(remaining_cells) == 1:
                        details = ""
                        evidence = ""
                    elif len(remaining_cells) == 2:
                        details = remaining_cells[1]
                        evidence = remaining_cells[1] if any(re.search(p, remaining_cells[1].lower()) for p in EVIDENCE_POSITIVE_PATTERNS) else ""
                    elif len(remaining_cells) >= 3:
                        details = " | ".join(remaining_cells[1:])
                        for c in remaining_cells[1:]:
                            if any(re.search(p, c.lower()) for p in EVIDENCE_POSITIVE_PATTERNS):
                                evidence = c
                                break
                        if not evidence and len(remaining_cells) >= 4:
                            evidence = remaining_cells[3]

                if not any(f.code == code_found for f in result.factors[current_quadrant]):
                    result.factors[current_quadrant].append(
                        FodaFactor(
                            code=code_found,
                            quadrant=current_quadrant,
                            statement=statement,
                            evidence=evidence,
                            details=details,
                            raw_cells=remaining_cells,
                            has_dedicated_empty_evidence_cell=has_dedicated_empty_evidence_cell,
                        )
                    )
                continue

        # 2. Parsing de listas Markdown: - `F1:` Enunciado, • `F1:` Enunciado, 1. F1: Enunciado
        list_match = re.search(
            r"^(?:[-\*•]|\d+[\.\)])\s+[\*`_\(]*(" + prefix + r"\d+)[\*`_\)]*[:\.\-]\s*(.+)$",
            stripped,
            re.IGNORECASE,
        )
        if list_match:
            code = list_match.group(1).upper()
            statement = list_match.group(2).strip()

            ev_match = re.search(r"\[(?:evidencia|fuente|rcm|src)[^\]]*:\s*([^\]]+)\]", statement, re.IGNORECASE)
            evidence = ev_match.group(1) if ev_match else ""

            if not any(f.code == code for f in result.factors[current_quadrant]):
                result.factors[current_quadrant].append(
                    FodaFactor(code=code, quadrant=current_quadrant, statement=statement, evidence=evidence)
                )

    # 3. Fallback: Si algún cuadrante quedó vacío, escanear la matriz panorámica 2x2 o bullets globales
    for quad_name, pref in QUADRANT_PREFIXES.items():
        if len(result.factors[quad_name]) == 0:
            matches = re.findall(
                r"(?:[•\-\*]|\d+[\.\)])\s*`?\*?(" + pref + r"\d+)\*?`?[:\.\-]\s*([^<\|\n\r]+)",
                content,
                re.IGNORECASE,
            )
            for m in matches:
                code = m[0].upper()
                stmt = m[1].strip()
                if not any(f.code == code for f in result.factors[quad_name]):
                    result.factors[quad_name].append(FodaFactor(code=code, quadrant=quad_name, statement=stmt))

    return result


def validate_foda_structure(result: FodaValidationResult) -> FodaValidationResult:
    """Ejecuta las reglas de validación de conformidad y cátedra sobre el resultado parseado."""

    # 1. Validación de los 4 cuadrantes y cardinalidad canónica (4 a 6 factores)
    for quadrant_name, expected_prefix in QUADRANT_PREFIXES.items():
        factors = result.factors[quadrant_name]
        count = len(factors)

        if count == 0:
            result.errors.append(
                f"Cuadrante ausente o vacío: '{quadrant_name.capitalize()}'. Debe contener entre {MIN_FACTORS_PER_QUADRANT} y {MAX_FACTORS_PER_QUADRANT} factores."
            )
            continue

        if count < MIN_FACTORS_PER_QUADRANT:
            result.errors.append(
                f"Cuadrante '{quadrant_name.capitalize()}' posee sólo {count} factores (mínimo canónico exigido por cátedra: {MIN_FACTORS_PER_QUADRANT}). Códigos presentes: {[f.code for f in factors]}."
            )
        elif count > MAX_FACTORS_PER_QUADRANT:
            result.errors.append(
                f"Cuadrante '{quadrant_name.capitalize()}' excede el límite con {count} factores (máximo canónico permitido por cátedra: {MAX_FACTORS_PER_QUADRANT}). Códigos presentes: {[f.code for f in factors]}."
            )

        # Validación de prefijos
        for factor in factors:
            if not factor.code.startswith(expected_prefix):
                result.errors.append(
                    f"Código inválido '{factor.code}' en cuadrante '{quadrant_name}'. Debe iniciar con '{expected_prefix}'."
                )

    # 2. Validación de Trazabilidad Forense de Debilidades
    for factor in result.factors["debilidades"]:
        if not factor.has_evidence_marker():
            result.errors.append(
                f"Debilidad '{factor.code}' no posee evidencia primaria o hallazgo de auditoría documentado (ej. SRC-AUD-XX, RCM-YY, SoD, silos TI, ruta documental)."
            )

    # 3. Heurísticas de Frontera Interna vs. Externa (Principio de Controlabilidad de Cátedra)
    # 3.1 Oportunidades: no redactar iniciativas o compras de gestión interna
    for factor in result.factors["oportunidades"]:
        text = f"{factor.statement} {factor.details} {' '.join(factor.raw_cells)}".lower()
        for pattern in INTERNAL_ACTION_VERBS:
            if re.search(pattern, text):
                result.warnings.append(
                    f"Posible violación de frontera en Oportunidad '{factor.code}': redactada como acción o compra interna ('{factor.statement[:60]}...'). Las Oportunidades deben ser condiciones externas del mercado, normativa o tecnología, no proyectos internos."
                )
                break

    # 3.2 Amenazas: no culpar al personal interno o fallas operativas propias
    for factor in result.factors["amenazas"]:
        text = f"{factor.statement} {factor.details} {' '.join(factor.raw_cells)}".lower()
        for pattern in INTERNAL_STAFF_THREAT_PATTERNS:
            if re.search(pattern, text):
                result.warnings.append(
                    f"Posible violación de frontera en Amenaza '{factor.code}': involucra personal o sistemas propios ('{factor.statement[:60]}...'). Las fallas del personal o sistemas propios deben clasificarse como Debilidad interna (D)."
                )
                break

    # 3.3 Fortalezas y Debilidades: advertir factores macroeconómicos externos
    for quad_name in ["fortalezas", "debilidades"]:
        for factor in result.factors[quad_name]:
            text = f"{factor.statement} {factor.details} {' '.join(factor.raw_cells)}".lower()
            for macro_pattern in MACRO_EXTERNAL_TERMS:
                if re.search(macro_pattern, text):
                    result.warnings.append(
                        f"Posible violación de frontera en {quad_name.capitalize()} '{factor.code}': hace referencia a evento macroeconómico externo ('{factor.statement[:60]}...'). Las F y D deben ser 100% internas y controlables por el proceso."
                    )
                    break

    return result


def validate_file(file_path: Path) -> FodaValidationResult:
    if not file_path.exists():
        res = FodaValidationResult(str(file_path))
        res.errors.append(f"Archivo no encontrado: {file_path}")
        return res

    content = file_path.read_text(encoding="utf-8")
    result = parse_foda_markdown(content, file_path=str(file_path))
    return validate_foda_structure(result)


def print_report(res: FodaValidationResult) -> None:
    print("=" * 60)
    print("VALIDACIÓN DE MATRIZ FODA DE PROCESO (fodaProcess)")
    print("=" * 60)
    print(f"Archivo analizado: {res.file_path}\n")

    for quad_name, expected_prefix in QUADRANT_PREFIXES.items():
        factors = res.factors[quad_name]
        status = "[OK]" if (MIN_FACTORS_PER_QUADRANT <= len(factors) <= MAX_FACTORS_PER_QUADRANT) else "[ERROR]"
        codes_str = ", ".join([f.code for f in factors]) if factors else "Ninguno"
        print(f"{status} Cuadrante '{quad_name.capitalize()}': {len(factors)} factores detectados ({codes_str}).")

    if res.warnings:
        print("\nADVERTENCIAS METODOLÓGICAS (Frontera y Semántica de Cátedra):")
        for w in res.warnings:
            print(f"  [AVISO] {w}")

    if res.errors:
        print("\nERRORES DE CONFORMIDAD DETECTADOS:")
        for err in res.errors:
            print(f"  [FALLO] {err}")
        print("\n" + "-" * 60)
        print("ESTADO: RECHAZADO. La matriz no cumple con el contrato canónico de GMP.")
        print("=" * 60)
    else:
        print("\n" + "-" * 60)
        print("ESTADO: EXITOSO. La matriz cumple con todos los estándares canónicos.")
        print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Validador determinista de Matriz FODA de Proceso (fodaProcess).")
    parser.add_argument("file", help="Ruta al archivo Markdown foda.md o plantilla a validar.")
    args = parser.parse_args()

    file_path = Path(args.file)
    res = validate_file(file_path)
    print_report(res)

    sys.exit(0 if res.is_valid else 1)


if __name__ == "__main__":
    main()
