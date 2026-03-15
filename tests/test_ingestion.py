from ingestion.chunk_sections import chunk_sections
from ingestion.metadata import build_metadata
from ingestion.parse_pdf import parse_pdf
from ingestion.parse_word import parse_word


def test_parse_word_returns_expected_shape() -> None:
    result = parse_word("sample.docx")
    assert result["type"] == "word"
    assert result["content"] == []


def test_parse_pdf_returns_expected_shape() -> None:
    result = parse_pdf("sample.pdf")
    assert result["type"] == "pdf"
    assert result["content"] == []


def test_chunk_sections_returns_content_list() -> None:
    assert chunk_sections({"content": [{"section": "Overview"}]}) == [{"section": "Overview"}]


def test_build_metadata_extracts_filename() -> None:
    metadata = build_metadata("raw/report.pdf")
    assert metadata["filename"] == "report.pdf"
