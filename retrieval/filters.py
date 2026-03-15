"""Filtering helpers for retrieval results."""


def filter_by_tag(records: list[dict], tag: str) -> list[dict]:
    """Filter records by a string tag."""
    return [record for record in records if tag in record.get("tags", [])]
