from generation.evidence_trace import build_evidence_trace
from generation.finding_generator import generate_finding
from generation.section_generator import generate_section


def test_generate_section_mentions_name_and_count() -> None:
    result = generate_section("Summary", [{"id": 1}])
    assert "Summary" in result
    assert "1 evidence item" in result


def test_build_evidence_trace_preserves_sources() -> None:
    evidence = [{"source": "doc-1"}]
    result = build_evidence_trace("Testing", evidence)
    assert result["sources"] == evidence


def test_generate_finding_mentions_title() -> None:
    result = generate_finding("Documentation gap", [])
    assert "Documentation gap" in result
