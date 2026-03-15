"""Utilities for extracting text and structure from PDF documents."""

from pathlib import Path


def parse_pdf(document_path: str | Path) -> dict:
    """Return a minimal placeholder payload for a PDF document."""
    path = Path(document_path)
    return {"source": str(path), "type": "pdf", "content": []}
