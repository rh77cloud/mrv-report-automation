"""Embedding utilities for report evidence retrieval."""


def embed_text(text: str) -> list[float]:
    """Return a deterministic placeholder embedding."""
    if not text:
        return []
    return [float(len(text))]
