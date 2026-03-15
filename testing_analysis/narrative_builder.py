"""Helpers for turning analysis outputs into report-ready prose."""


def build_narrative(summary: dict) -> str:
    """Convert a summary payload into a short narrative."""
    return f"Testing analysis summary: {summary}"
