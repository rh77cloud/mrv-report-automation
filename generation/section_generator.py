"""Section generation entry points."""


def generate_section(section_name: str, evidence: list[dict]) -> str:
    """Build a minimal placeholder section draft."""
    return f"Draft for {section_name} using {len(evidence)} evidence item(s)."
