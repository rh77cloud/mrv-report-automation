"""Metadata helpers for source documents."""

from pathlib import Path


def build_metadata(document_path: str | Path) -> dict:
    """Create lightweight document metadata."""
    path = Path(document_path)
    return {"filename": path.name, "suffix": path.suffix.lower()}
