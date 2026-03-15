"""Utilities for extracting text and structure from Word documents."""

from pathlib import Path


def parse_word(document_path: str | Path) -> dict:
    """Return a minimal placeholder payload for a Word document."""
    path = Path(document_path)
    return {"source": str(path), "type": "word", "content": []}
