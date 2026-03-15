"""Retrieval helpers for section and finding generation."""


def retrieve_top_k(records: list[dict], k: int = 3) -> list[dict]:
    """Return the top-k records from a simple list-backed store."""
    return records[:k]
