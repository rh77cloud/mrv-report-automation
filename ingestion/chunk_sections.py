"""Helpers for splitting parsed documents into section-level chunks."""


def chunk_sections(parsed_document: dict) -> list[dict]:
    """Return section chunks from a parsed document payload."""
    return parsed_document.get("content", [])
