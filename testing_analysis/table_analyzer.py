"""Helpers for interpreting structured testing tables."""


def analyze_table(rows: list[dict]) -> dict:
    """Return simple summary statistics for table-shaped data."""
    return {"row_count": len(rows)}
