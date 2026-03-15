"""Helpers for splitting parsed documents into section-level chunks."""

from __future__ import annotations
from typing import List, Dict


def looks_like_heading(text: str) -> bool:
    """
    Heuristic to identify possible section headings.
    This is intentionally simple for v1.
    """
    stripped = text.strip()

    if not stripped:
        return False

    if len(stripped) > 80:
        return False

    if stripped.isupper():
        return True

### UPDATING THIS ###
    heading_keywords = [
        "overview",
        "purpose",
        "scope",
        "data",
        "governance",
        "monitoring",
        "framework",
        "assumptions",
        "overlay",
        "implementation",
        "limitations",
        "methodology",
        "validation",
        "testing",
        "results",
        "conclusion",
        "findings",
    ]

    lower_text = stripped.lower()
    return any(keyword in lower_text for keyword in heading_keywords)


def chunk_word_paragraphs(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Convert paragraph records into section-like chunks.

    If a paragraph looks like a heading, start a new section.
    Otherwise, append text to the current section.
    """
    sections: List[Dict[str, str]] = []
    current_heading = "Introduction"
    current_content: List[str] = []

    for record in records:
        text = record["text"]

        if looks_like_heading(text):
            if current_content:
                sections.append(
                    {
                        "section_title": current_heading,
                        "content": "\n".join(current_content).strip(),
                    }
                )
            current_heading = text
            current_content = []
        else:
            current_content.append(text)

    if current_content:
        sections.append(
            {
                "section_title": current_heading,
                "content": "\n".join(current_content).strip(),
            }
        )

    return sections


def chunk_pdf_pages(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    For PDFs, start with page-level chunks.
    Later you can improve this into section-based chunking.
    """
    sections: List[Dict[str, str]] = []

    for record in records:
        sections.append(
            {
                "section_title": f"Page {record['page_number']}",
                "content": record["text"],
            }
        )

    return sections
