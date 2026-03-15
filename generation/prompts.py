"""Prompt templates for generation tasks."""


SECTION_PROMPT = """
You are drafting a model validation report section.
Use only the supplied evidence and preserve a professional audit-ready tone.
""".strip()


FINDING_PROMPT = """
You are drafting a model validation finding.
Summarize the issue, impact, and recommendation with clear evidence support.
""".strip()
