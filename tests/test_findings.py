from exports.assemble_report import assemble_report
from exports.export_word import export_word
from testing_analysis.chart_analyzer import analyze_chart
from testing_analysis.narrative_builder import build_narrative
from testing_analysis.table_analyzer import analyze_table


def test_analyze_table_counts_rows() -> None:
    assert analyze_table([{"row": 1}, {"row": 2}])["row_count"] == 2


def test_analyze_chart_counts_points() -> None:
    assert analyze_chart([{"x": 1}, {"x": 2}, {"x": 3}])["point_count"] == 3


def test_build_narrative_returns_text() -> None:
    assert "row_count" in build_narrative({"row_count": 2})


def test_assemble_report_joins_sections() -> None:
    assert assemble_report(["A", "B"]) == "A\n\nB"


def test_export_word_returns_output_path() -> None:
    assert export_word("report", "output.docx").name == "output.docx"
