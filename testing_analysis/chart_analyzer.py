"""Helpers for interpreting chart-based testing evidence."""


def analyze_chart(points: list[dict]) -> dict:
    """Return simple summary statistics for chart data."""
    return {"point_count": len(points)}
