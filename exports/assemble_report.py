"""Helpers for combining sections into a full report draft."""


def assemble_report(sections: list[str]) -> str:
    """Join sections into a single report body."""
    return "\n\n".join(sections)
