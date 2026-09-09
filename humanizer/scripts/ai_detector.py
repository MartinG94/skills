#!/usr/bin/env python3
"""AI Writing Pattern Detector.

Analyzes text to detect statistical markers and stylistic tells of AI-generated content:
- Sentence length uniformity (low burstiness)
- Mechanical transition words (moreover, furthermore, additionally)
- Abstract scaffolding and placeholder phrases
- Copula avoidance (serves as, stands as, boasts)
- Chatbot artifacts and conversational residue
- Low vocabulary diversity (Type-Token Ratio)
- Passive voice frequency

Zero external dependencies (uses Python standard library).
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any


class AIDetector:
    """Detects AI writing patterns across content, language, style, and communication."""

    # Transition words frequently overused at sentence starts
    AI_TRANSITIONS = [
        "moreover",
        "furthermore",
        "additionally",
        "in addition",
        "it is important to note that",
        "it should be noted that",
        "it is worth noting that",
        "notably",
        "significantly",
        "consequently",
        "as a matter of fact",
        "por otra parte",
        "además",
        "asimismo",
        "cabe destacar que",
        "es importante señalar que",
        "en este sentido",
        "por consiguiente",
    ]

    # Abstract scaffolding & placeholder phrases
    ABSTRACT_PHRASES = [
        "various aspects",
        "multiple factors",
        "different perspectives",
        "in terms of",
        "with regard to",
        "with respect to",
        "plays an important role",
        "plays a crucial role",
        "plays a pivotal role",
        "key turning point",
        "evolving landscape",
        "stands as a testament",
        "serves as a reminder",
        "underscores the importance",
        "indelible mark",
        "diversos aspectos",
        "múltiples factores",
        "en términos de",
        "juega un papel fundamental",
        "juega un rol crucial",
        "sirve como testimonio",
        "paisaje en constante evolución",
        "marca indeleble",
    ]

    # Copula avoidance (inflated verbs replacing is/are/has)
    COPULA_AVOIDANCE = [
        "serves as",
        "stands as",
        "boasts a",
        "boasts over",
        "features a",
        "acts as",
        "functions as",
        "sirve como",
        "se erige como",
        "cuenta con",
        "alberga una",
    ]

    # Chatbot residue and sycophancy
    CHATBOT_ARTIFACTS = [
        "i hope this helps",
        "certainly!",
        "of course!",
        "you're absolutely right",
        "great question",
        "let me know if",
        "here is a breakdown",
        "here is an overview",
        "as of my last update",
        "based on available information",
        "espero que esto te sirva",
        "por supuesto",
        "ciertamente",
        "excelente pregunta",
        "hazme saber si",
    ]

    # AI vocabulary frequency list
    AI_VOCABULARY = [
        "delve",
        "tapestry",
        "testament",
        "pivotal",
        "intricate",
        "foster",
        "garner",
        "underscore",
        "showcase",
        "holistic",
        "synergy",
        "multifaceted",
        "beacon",
        "paradigm",
        "ahondar",
        "tapiz",
        "testimonio",
        "crucial",
        "intricado",
        "fomentar",
        "recalcar",
        "holístico",
        "multifacético",
    ]

    def __init__(self, text: str):
        self.raw_text = text
        self.clean_prose = self._extract_clean_prose(text)
        self.paragraphs = self._split_paragraphs()
        self.sentences = self._split_sentences()
        self.words = self._tokenize_words()

    @staticmethod
    def _extract_clean_prose(text: str) -> str:
        """Strip YAML frontmatter, code blocks, inline code, HTML comments, and markdown table rows."""
        # Strip YAML frontmatter at start
        t = re.sub(r"^---\s*\n[\s\S]*?\n---\s*\n", "", text)
        # Strip fenced code blocks (```...```)
        t = re.sub(r"```[\s\S]*?```", "", t)
        # Strip inline code (`...`)
        t = re.sub(r"`[^`\n]+`", "", t)
        # Strip HTML comments
        t = re.sub(r"<!--[\s\S]*?-->", "", t)
        # Strip Markdown table rows
        t = re.sub(r"^\s*\|.*\|\s*$", "", t, flags=re.MULTILINE)
        # Strip Markdown headings (# Header, ## Subheader)
        t = re.sub(r"^#{1,6}\s+.*$", "", t, flags=re.MULTILINE)
        # Strip horizontal rules
        t = re.sub(r"^\s*[-*_]{3,}\s*$", "", t, flags=re.MULTILINE)
        # Strip markdown images and convert links [text](url) to text
        t = re.sub(r"!\[([^\]]*)\]\([^)]+\)", "", t)
        t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
        return t

    def _split_paragraphs(self) -> list[str]:
        paragraphs = [p.strip() for p in self.clean_prose.split("\n\n") if p.strip()]
        return paragraphs if paragraphs else ([self.clean_prose.strip()] if self.clean_prose.strip() else [])

    def _split_sentences(self) -> list[str]:
        if not self.clean_prose.strip():
            return []

        # Protect common abbreviations and citations from premature sentence splits
        abbrevs = [
            r"\bDr\.", r"\bMr\.", r"\bMrs\.", r"\bMs\.", r"\bProf\.",
            r"\bSr\.", r"\bSra\.", r"\bDra\.", r"\bvs\.", r"\betc\.",
            r"\bFig\.", r"\bTab\.", r"\bvol\.", r"\bno\.", r"\bpp\.",
            r"\bpág\.", r"\bpágs\.", r"\bnúm\.", r"\bp\. ej\.",
            r"\be\.g\.", r"\bi\.e\.", r"\bet al\."
        ]

        protected = self.clean_prose
        for pattern in abbrevs:
            def _repl(m: re.Match) -> str:
                return m.group(0).replace(".", "@@DOT@@")
            protected = re.sub(pattern, _repl, protected, flags=re.IGNORECASE)

        # Protect decimals (e.g. 3.14)
        protected = re.sub(r"(?<=\d)\.(?=\d)", "@@DOT@@", protected)

        # Split sentences on terminal punctuation followed by space or newline and uppercase/alphanumeric
        raw_sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑa-záéíóúñ0-9])|\n\n+", protected)

        sentences = []
        for s in raw_sentences:
            s_restored = s.replace("@@DOT@@", ".").strip()
            # Clean leading markdown heading markers (#), list bullets (*, -), or ordered list numbers (1.)
            s_restored = re.sub(r"^[#*\->\d.]+\s+", "", s_restored).strip()
            if s_restored and len(s_restored) > 3:
                sentences.append(s_restored)

        return sentences

    def _tokenize_words(self) -> list[str]:
        return [w.lower() for w in re.findall(r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9'-]+\b", self.clean_prose)]

    def analyze_sentence_uniformity(self) -> dict[str, Any]:
        """Check for uniform sentence lengths (lack of burstiness)."""
        if not self.sentences:
            return {
                "score": 0.0,
                "severity": "baja",
                "avg_sentence_length": 0.0,
                "std_dev": 0.0,
                "variance_ratio": 0.0,
                "issue": "Texto vacío o sin oraciones reconocibles.",
            }

        lengths = [len(s.split()) for s in self.sentences]
        avg_len = statistics.mean(lengths)
        std_dev = statistics.stdev(lengths) if len(lengths) > 1 else 0.0
        variance_ratio = std_dev / avg_len if avg_len > 0 else 0.0

        if len(self.sentences) < 3:
            return {
                "score": 0.0,
                "severity": "baja",
                "avg_sentence_length": round(avg_len, 1),
                "std_dev": round(std_dev, 1),
                "variance_ratio": round(variance_ratio, 2),
                "issue": "Texto breve (< 3 oraciones); muestra reducida para evaluar burstiness.",
            }

        # Uniformity: low variance ratio (< 0.25) signals robotic rhythm
        if variance_ratio < 0.25:
            score = 0.85
            severity = "alta"
            issue = "Ritmo monótono: las oraciones tienen longitudes casi idénticas (baja varianza)."
        elif variance_ratio < 0.35:
            score = 0.5
            severity = "moderada"
            issue = "Variación moderada: se beneficiaría de alternar oraciones cortas (5-10) y largas (25+)."
        else:
            score = 0.1
            severity = "baja"
            issue = "Buena cadencia rítmica y variación de longitud."

        return {
            "score": round(score, 2),
            "severity": severity,
            "avg_sentence_length": round(avg_len, 1),
            "std_dev": round(std_dev, 1),
            "variance_ratio": round(variance_ratio, 2),
            "issue": issue,
        }

    def detect_transitions(self) -> dict[str, Any]:
        """Detect overused transition words at sentence starts."""
        found = []
        for s in self.sentences:
            s_clean = s.strip().lower()
            for t in self.AI_TRANSITIONS:
                if re.match(r"^" + re.escape(t) + r"(?:\b|[.,;:!?\s])", s_clean):
                    found.append((t, s[:60] + "..."))
                    break

        ratio = len(found) / len(self.sentences) if self.sentences else 0.0
        score = min(1.0, ratio * 2.5)

        return {
            "score": round(score, 2),
            "count": len(found),
            "ratio_per_sentence": round(ratio, 2),
            "matches": found,
        }

    def detect_abstract_phrases(self) -> dict[str, Any]:
        """Detect filler, copula avoidance, and abstract scaffolding with boundary precision."""
        text_lower = self.clean_prose.lower()

        def _match(pattern: str) -> bool:
            return bool(re.search(r"(?:\b|^)" + re.escape(pattern) + r"(?:\b|$|[.,;:!?\s])", text_lower))

        found_abstract = [p for p in self.ABSTRACT_PHRASES if _match(p)]
        found_copula = [p for p in self.COPULA_AVOIDANCE if _match(p)]
        found_chatbot = [p for p in self.CHATBOT_ARTIFACTS if _match(p)]
        found_vocab = [w for w in self.AI_VOCABULARY if bool(re.search(r"\b" + re.escape(w) + r"\b", text_lower))]

        total_flags = len(found_abstract) + len(found_copula) + len(found_chatbot) * 2 + len(found_vocab)
        score = min(1.0, total_flags * 0.15)

        return {
            "score": round(score, 2),
            "abstract_scaffolding": found_abstract,
            "copula_avoidance": found_copula,
            "chatbot_artifacts": found_chatbot,
            "ai_vocabulary": found_vocab,
        }

    def compute_type_token_ratio(self) -> dict[str, Any]:
        """Compute vocabulary diversity."""
        if not self.words:
            return {"ttr": 0.0, "unique_words": 0, "total_words": 0, "score": 0.0}
        unique_words = set(self.words)
        ttr = len(unique_words) / len(self.words)
        # TTR < 0.40 in medium/long texts suggests low diversity
        score = 0.7 if ttr < 0.40 and len(self.words) > 100 else 0.2
        return {
            "ttr": round(ttr, 3),
            "unique_words": len(unique_words),
            "total_words": len(self.words),
            "score": score,
        }

    def full_audit(self) -> dict[str, Any]:
        """Run all detectors and aggregate an overall AI likelihood score."""
        uniformity = self.analyze_sentence_uniformity()
        transitions = self.detect_transitions()
        phrasing = self.detect_abstract_phrases()
        ttr = self.compute_type_token_ratio()

        # Weighted composite score (0 to 100)
        composite = (
            uniformity["score"] * 0.30
            + transitions["score"] * 0.25
            + phrasing["score"] * 0.35
            + ttr["score"] * 0.10
        ) * 100

        overall_score = min(100, max(0, round(composite, 1)))

        if overall_score >= 65:
            verdict = "Alta probabilidad de patrones de IA (requiere humanización agresiva o media)"
        elif overall_score >= 35:
            verdict = "Presencia moderada de modismos artificiales (se recomienda revisión de ritmo y vocabulario)"
        else:
            verdict = "Texto predominantemente natural y con rasgos humanos auténticos"

        return {
            "overall_ai_score": overall_score,
            "verdict": verdict,
            "sentence_count": len(self.sentences),
            "word_count": len(self.words),
            "uniformity_analysis": uniformity,
            "transitions_analysis": transitions,
            "phrasing_analysis": phrasing,
            "vocabulary_diversity": ttr,
        }


def format_text_report(audit: dict[str, Any], detailed: bool = False) -> str:
    lines = []
    lines.append("=" * 65)
    lines.append("        INFORME DE DETECCIÓN Y AUDITORÍA DE PATRONES DE IA")
    lines.append("=" * 65)
    lines.append(f"Score Global de IA: {audit['overall_ai_score']} / 100")
    lines.append(f"Diagnóstico:       {audit['verdict']}")
    lines.append(f"Métricas básicas:  {audit['word_count']} palabras | {audit['sentence_count']} oraciones")
    lines.append("-" * 65)

    u = audit["uniformity_analysis"]
    lines.append(f"1. Variación de Ritmo (Burstiness):")
    lines.append(f"   - Longitud media: {u.get('avg_sentence_length', 0)} palabras (Desv. estándar: {u.get('std_dev', 0)})")
    lines.append(f"   - Diagnóstico:    {u.get('issue', '')}")

    t = audit["transitions_analysis"]
    lines.append(f"\n2. Conectores Mecánicos al Inicio de Oración:")
    lines.append(f"   - Conectores detectados: {t['count']} ({t['ratio_per_sentence']*100:.1f}% de las oraciones)")
    if t["matches"]:
        for marker, snippet in t["matches"][:5]:
            lines.append(f"     * [{marker}]: \"{snippet}\"")

    p = audit["phrasing_analysis"]
    lines.append(f"\n3. Expresiones y Clichés de IA:")
    if p["ai_vocabulary"]:
        lines.append(f"   - Vocabulario típico de IA: {', '.join(p['ai_vocabulary'])}")
    if p["copula_avoidance"]:
        lines.append(f"   - Evasión de cópula (serves as / boasts): {', '.join(p['copula_avoidance'])}")
    if p["abstract_scaffolding"]:
        lines.append(f"   - Andamiaje abstracto: {', '.join(p['abstract_scaffolding'])}")
    if p["chatbot_artifacts"]:
        lines.append(f"   - Residuos conversacionales: {', '.join(p['chatbot_artifacts'])}")
    if not (p["ai_vocabulary"] or p["copula_avoidance"] or p["abstract_scaffolding"] or p["chatbot_artifacts"]):
        lines.append("   - No se detectaron expresiones delatoras destacables.")

    v = audit.get("vocabulary_diversity", {})
    unique = v.get("unique_words", 0)
    ttr_val = v.get("ttr", 0.0)
    lines.append(f"\n4. Diversidad Léxica (TTR):")
    lines.append(f"   - Type-Token Ratio: {ttr_val} ({unique} palabras únicas)")

    lines.append("=" * 65)
    return "\n".join(lines)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Detecta patrones de escritura de IA en textos.")
    parser.add_argument("input_file", help="Ruta al archivo de texto a evaluar.")
    parser.add_argument("--detailed", action="store_true", help="Muestra desglose pormenorizado.")
    parser.add_argument("--json", action="store_true", help="Emite salida en formato JSON estructurado.")

    args = parser.parse_args()
    path = Path(args.input_file)
    if not path.is_file():
        sys.stderr.write(f"Error: archivo no encontrado: {path}\n")
        return 1

    text = path.read_text(encoding="utf-8", errors="replace")
    detector = AIDetector(text)
    audit = detector.full_audit()

    if args.json:
        print(json.dumps(audit, indent=2, ensure_ascii=False))
    else:
        print(format_text_report(audit, detailed=args.detailed))

    return 0


if __name__ == "__main__":
    sys.exit(main())
