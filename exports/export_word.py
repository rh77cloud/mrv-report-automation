"""Word export helpers."""

from pathlib import Path


def export_word(report_text: str, output_path: str | Path) -> Path:
    """Return the output path for a future Word export implementation."""
    return Path(output_path)
