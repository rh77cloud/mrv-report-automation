"""Utilities for mapping generated text back to evidence."""


def build_evidence_trace(section_name: str, evidence: list[dict]) -> dict:
    """Return a minimal evidence trace object."""
    return {"section": section_name, "sources": evidence}
