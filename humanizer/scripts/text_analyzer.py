#!/usr/bin/env python3
"""Text Quality and Metric Analyzer.

Provides quantitative text metrics:
- Word and sentence counts
- Sentence length distributions (min, max, mean, standard deviation)
- Readability scores (Flesch Reading Ease estimate)
- Type-Token Ratio (lexical diversity)
- Comparison mode (`--compare original.txt revised.txt`) to measure before/after improvements.

Zero external dependencies (uses Python standard library).
"""

from __future__ import annotations

import argparse
import math
import re
import statistics
import sys
from pathlib import Path
from typing import Any


def extract_clean_prose(text: str) -> str:
    """Strip YAML frontmatter, fenced code blocks, inline code, HTML comments, and markdown table rows."""
    t = re.sub(r"^---\s*\n[\s\S]*?\n---\s*\n", "", text)
    t = re.sub(r"```[\s\S]*?```", "", t)
    t = re.sub(r"`[^`\n]+`", "", t)
    t = re.sub(r"<!--[\s\S]*?-->", "", t)
    t = re.sub(r"^\s*\|.*\|\s*$", "", t, flags=re.MULTILINE)
    t = re.sub(r"^#{1,6}\s+.*$", "", t, flags=re.MULTILINE)
    t = re.sub(r"^\s*[-*_]{3,}\s*$", "", t, flags=re.MULTILINE)
    t = re.sub(r"!\[([^\]]*)\]\([^)]+\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return t


def is_spanish_text(text: str) -> bool:
    spanish_markers = {"de", "la", "en", "el", "los", "las", "un", "una", "por", "para", "con", "que", "del", "al", "es"}
    sample_words = set(re.findall(r"\b[a-záéíóúüñ]+\b", text.lower()[:1500]))
    return len(sample_words.intersection(spanish_markers)) >= 2


def split_sentences(text: str) -> list[str]:
    if not text.strip():
        return []

    abbrevs = [
        r"\bDr\.", r"\bMr\.", r"\bMrs\.", r"\bMs\.", r"\bProf\.",
        r"\bSr\.", r"\bSra\.", r"\bDra\.", r"\bvs\.", r"\betc\.",
        r"\bFig\.", r"\bTab\.", r"\bvol\.", r"\bno\.", r"\bpp\.",
        r"\bpág\.", r"\bpágs\.", r"\bnúm\.", r"\bp\. ej\.",
        r"\be\.g\.", r"\bi\.e\.", r"\bet al\."
    ]

    protected = text
    for pattern in abbrevs:
        def _repl(m: re.Match) -> str:
            return m.group(0).replace(".", "@@DOT@@")
        protected = re.sub(pattern, _repl, protected, flags=re.IGNORECASE)

    protected = re.sub(r"(?<=\d)\.(?=\d)", "@@DOT@@", protected)
    raw_sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑa-záéíóúñ0-9])|\n\n+", protected)

    sentences = []
    for s in raw_sentences:
        s_restored = s.replace("@@DOT@@", ".").strip()
        s_restored = re.sub(r"^[#*\->\d.]+\s+", "", s_restored).strip()
        if s_restored and len(s_restored) > 3:
            sentences.append(s_restored)
    return sentences


def estimate_syllables(word: str, is_spanish: bool = False) -> int:
    """Syllable count heuristic for English/Spanish words."""
    w = word.lower().strip(".:;?!'\"-")
    if len(w) <= 3:
        return 1
    # Count vowel groups
    vowels = re.findall(r"[aeiouyáéíóúü]+", w)
    count = len(vowels)
    # In English, silent trailing 'e' does not count as a syllable.
    # In Spanish, trailing 'e' is always voiced ('grande', 'padre', 'informe').
    if not is_spanish and w.endswith("e") and not w.endswith("le") and count > 1:
        count -= 1
    return max(1, count)


def analyze_text(text: str) -> dict[str, Any]:
    prose = extract_clean_prose(text)
    words = re.findall(r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9'-]+\b", prose)
    sentences = split_sentences(prose)

    if not words:
        return {
            "words": 0,
            "sentences": 0,
            "avg_sentence_len": 0.0,
            "std_dev_len": 0.0,
            "variance_ratio": 0.0,
            "ttr": 0.0,
            "flesch_reading_ease": 0.0,
            "short_sentences (<12w)": 0,
            "medium_sentences (12-24w)": 0,
            "long_sentences (>24w)": 0,
            "sentence_lengths": [],
        }

    sentence_lens = [len(s.split()) for s in sentences] if sentences else [len(words)]
    avg_len = statistics.mean(sentence_lens)
    std_dev = statistics.stdev(sentence_lens) if len(sentence_lens) > 1 else 0.0

    is_sp = is_spanish_text(prose)
    syllables = sum(estimate_syllables(w, is_spanish=is_sp) for w in words)
    syllables_per_word = syllables / len(words)
    words_per_sentence = len(words) / max(1, len(sentences))

    # Flesch Reading Ease formula
    flesch = 206.835 - (1.015 * words_per_sentence) - (84.6 * syllables_per_word)
    flesch = round(max(0.0, min(100.0, flesch)), 1)

    unique_words = set(w.lower() for w in words)
    ttr = round(len(unique_words) / len(words), 3)

    return {
        "words": len(words),
        "sentences": len(sentences),
        "avg_sentence_len": round(avg_len, 1),
        "std_dev_len": round(std_dev, 1),
        "variance_ratio": round(std_dev / avg_len if avg_len > 0 else 0.0, 2),
        "ttr": ttr,
        "flesch_reading_ease": flesch,
        "short_sentences (<12w)": sum(1 for l in sentence_lens if l < 12),
        "medium_sentences (12-24w)": sum(1 for l in sentence_lens if 12 <= l <= 24),
        "long_sentences (>24w)": sum(1 for l in sentence_lens if l > 24),
    }


def compare_texts(original: dict[str, Any], revised: dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 65)
    lines.append("       COMPARATIVA ANTES Y DESPUÉS DE LA HUMANIZACIÓN")
    lines.append("=" * 65)
    lines.append(f"{'Métrica':<30} | {'Original':<12} | {'Humanizado':<12}")
    lines.append("-" * 65)
    lines.append(f"{'Total de palabras':<30} | {original['words']:<12} | {revised['words']:<12}")
    lines.append(f"{'Total de oraciones':<30} | {original['sentences']:<12} | {revised['sentences']:<12}")
    lines.append(f"{'Longitud media de oraciones':<30} | {original['avg_sentence_len']:<12} | {revised['avg_sentence_len']:<12}")
    lines.append(f"{'Desviación estándar (Rhythm)':<30} | {original['std_dev_len']:<12} | {revised['std_dev_len']:<12}")
    lines.append(f"{'Ratio de varianza (Burstiness)':<30} | {original['variance_ratio']:<12} | {revised['variance_ratio']:<12}")
    lines.append(f"{'Diversidad léxica (TTR)':<30} | {original['ttr']:<12} | {revised['ttr']:<12}")
    lines.append(f"{'Flesch Reading Ease':<30} | {original['flesch_reading_ease']:<12} | {revised['flesch_reading_ease']:<12}")
    lines.append("-" * 65)
    lines.append("Distribución de longitud de oraciones:")
    lines.append(f"  - Cortas (<12 palabras):      {original['short_sentences (<12w)']:<12} -> {revised['short_sentences (<12w)']}")
    lines.append(f"  - Medias (12-24 palabras):    {original['medium_sentences (12-24w)']:<12} -> {revised['medium_sentences (12-24w)']}")
    lines.append(f"  - Largas (>24 palabras):      {original['long_sentences (>24w)']:<12} -> {revised['long_sentences (>24w)']}")
    lines.append("=" * 65)

    burst_diff = revised["variance_ratio"] - original["variance_ratio"]
    if burst_diff > 0.08:
        lines.append("[OK] Mejora significativa en la cadencia ritmica (mayor burstiness natural).")
    elif burst_diff < -0.05:
        lines.append("[!] Advertencia: la varianza de oraciones disminuyo, revisa posibles oraciones monotonas.")
    else:
        lines.append("[i] Ritmo equilibrado.")

    return "\n".join(lines)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Analiza y compara metricas cuantitativas de texto.")
    parser.add_argument("input_file", help="Ruta al archivo de texto principal.")
    parser.add_argument("input_file2", nargs="?", help="Segundo archivo para comparativa (--compare).")
    parser.add_argument("--compare", action="store_true", help="Modo comparacion entre original y revisado.")

    args = parser.parse_args()
    p1 = Path(args.input_file)
    if not p1.is_file():
        sys.stderr.write(f"Error: archivo no encontrado: {p1}\n")
        return 1

    t1 = p1.read_text(encoding="utf-8", errors="replace")
    m1 = analyze_text(t1)

    if args.compare or args.input_file2:
        if not args.input_file2:
            sys.stderr.write("Error: para comparar se requieren dos archivos (original y revisado).\n")
            return 1
        p2 = Path(args.input_file2)
        if not p2.is_file():
            sys.stderr.write(f"Error: archivo no encontrado: {p2}\n")
            return 1
        t2 = p2.read_text(encoding="utf-8", errors="replace")
        m2 = analyze_text(t2)
        print(compare_texts(m1, m2))
    else:
        print("=" * 60)
        print("           MÉTRICAS CUANTITATIVAS DEL TEXTO")
        print("=" * 60)
        for k, v in m1.items():
            print(f"{k:<32}: {v}")
        print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
