import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from humanizer.scripts.ai_detector import AIDetector, format_text_report
from humanizer.scripts.text_analyzer import analyze_text, compare_texts, estimate_syllables, is_spanish_text
from humanizer.scripts.check_upstream import (
    compute_sha256,
    find_lockfile,
    check_all_upstreams,
    format_report,
)

def test_empty_string_ai_detector():
    d = AIDetector("")
    audit = d.full_audit()
    report = format_text_report(audit)
    assert audit["word_count"] == 0
    assert audit["sentence_count"] == 0
    assert audit["overall_ai_score"] == 0
    assert "INFORME DE DETECCIÓN" in report
    print("test_empty_string_ai_detector: PASS")

def test_empty_string_text_analyzer():
    m1 = analyze_text("")
    m2 = analyze_text("")
    assert m1["words"] == 0
    assert m1["sentences"] == 0
    assert "variance_ratio" in m1
    cmp_report = compare_texts(m1, m2)
    assert "COMPARATIVA ANTES Y DESPUÉS" in cmp_report
    print("test_empty_string_text_analyzer: PASS")

def test_abbreviation_splitting():
    text = "According to Smith et al. the study by Dr. Jones and Mrs. Gable was rigorous. For e.g. see Fig. 4. The velocity reached 3.14 m/s."
    d = AIDetector(text)
    assert len(d.sentences) == 3, f"Expected 3 sentences, got {len(d.sentences)}: {d.sentences}"
    m = analyze_text(text)
    assert m["sentences"] == 3, f"Expected 3 sentences in text_analyzer, got {m['sentences']}"
    print("test_abbreviation_splitting: PASS")

def test_false_positive_copula():
    text = "These impacts as reported are severe. Eran cincuenta condecorados en la reunión."
    d = AIDetector(text)
    audit = d.full_audit()
    copula = audit["phrasing_analysis"]["copula_avoidance"]
    assert not copula, f"Expected no copula avoidance, got: {copula}"
    print("test_false_positive_copula: PASS")

def test_true_positive_copula():
    text = "El nuevo servidor se erige como una solución y cuenta con dos interfaces. The gateway serves as a proxy."
    d = AIDetector(text)
    audit = d.full_audit()
    copula = audit["phrasing_analysis"]["copula_avoidance"]
    assert "se erige como" in copula
    assert "cuenta con" in copula
    assert "serves as" in copula
    print("test_true_positive_copula: PASS")

def test_markdown_code_block_stripping():
    doc = """# Tool Documentation

This tool analyzes user data accurately. It provides helpful outputs.

```python
import sys
import os

def run_app():
    if obj.is_valid():
        print("Valid!")
    return True
```

You can install it using the standard package manager.
"""
    d = AIDetector(doc)
    # The code block should NOT generate fake sentences
    for s in d.sentences:
        assert "def run_app" not in s
        assert "import sys" not in s
    assert len(d.sentences) == 3, f"Expected 3 prose sentences, got {len(d.sentences)}: {d.sentences}"

    m = analyze_text(doc)
    assert m["sentences"] == 3, f"Expected 3 sentences in text_analyzer, got {m['sentences']}"
    print("test_markdown_code_block_stripping: PASS")

def test_spanish_syllables():
    assert is_spanish_text("El informe de la comisión fue presentado para su aprobación.")
    assert not is_spanish_text("The report of the commission was submitted for final approval.")

    # In Spanish, 'grande' has 2 syllables
    assert estimate_syllables("grande", is_spanish=True) == 2
    # In English, 'make' has 1 syllable
    assert estimate_syllables("make", is_spanish=False) == 1
    # In English, 'active' has 2 syllables
    assert estimate_syllables("active", is_spanish=False) == 2
    print("test_spanish_syllables: PASS")

def test_sample_files():
    sample_ai = Path("humanizer/examples/sample_texts/sample_ai_text.txt").read_text(encoding="utf-8")
    sample_hum = Path("humanizer/examples/sample_texts/sample_humanized_text.txt").read_text(encoding="utf-8")

    d_ai = AIDetector(sample_ai).full_audit()
    d_hum = AIDetector(sample_hum).full_audit()

    assert d_ai["overall_ai_score"] > 60, f"Expected AI score > 60, got {d_ai['overall_ai_score']}"
    assert d_hum["overall_ai_score"] < 20, f"Expected human score < 20, got {d_hum['overall_ai_score']}"

    m_ai = analyze_text(sample_ai)
    m_hum = analyze_text(sample_hum)
    assert m_hum["variance_ratio"] > m_ai["variance_ratio"]
    print("test_sample_files: PASS")

def test_check_upstream_sha256():
    digest = compute_sha256(b"hello world")
    assert digest == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    print("test_check_upstream_sha256: PASS")

def test_check_upstream_find_lockfile():
    lock = find_lockfile()
    assert lock is not None
    assert lock.name == "skills-lock.json"
    assert lock.is_file()
    print("test_check_upstream_find_lockfile: PASS")

def test_check_upstream_offline_verification():
    lock = find_lockfile()
    assert lock is not None
    results = check_all_upstreams(lock, offline=True)
    assert len(results) == 5, f"Expected 5 sources, got {len(results)}"
    for r in results:
        assert r.skill_name in (
            "human-writing",
            "humanize",
            "humanize-academic-writing",
            "humanizer",
            "technical-writing",
        )
        assert r.status in ("UP_TO_DATE", "CHANGED", "LOCAL_ONLY")
        assert r.local_hash is not None
    rep = format_report(results, lock)
    assert "VERIFICACION DE FUENTES UPSTREAM" in rep
    assert "human-writing" in rep
    assert "technical-writing" in rep
    print("test_check_upstream_offline_verification: PASS")

def test_check_upstream_missing_lockfile():
    fake_path = Path("nonexistent_lockfile_12345.json")
    try:
        check_all_upstreams(fake_path)
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        pass
    print("test_check_upstream_missing_lockfile: PASS")

if __name__ == "__main__":
    test_empty_string_ai_detector()
    test_empty_string_text_analyzer()
    test_abbreviation_splitting()
    test_false_positive_copula()
    test_true_positive_copula()
    test_markdown_code_block_stripping()
    test_spanish_syllables()
    test_sample_files()
    test_check_upstream_sha256()
    test_check_upstream_find_lockfile()
    test_check_upstream_offline_verification()
    test_check_upstream_missing_lockfile()
    print("\nALL 12 REGRESSION AND EDGE CASE TESTS PASSED!")
