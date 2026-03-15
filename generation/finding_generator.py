"""Finding generation entry points."""


def generate_finding(title: str, evidence: list[dict]) -> str:
    """Build a minimal placeholder finding draft."""
    return f"Finding: {title} ({len(evidence)} supporting item(s))"
