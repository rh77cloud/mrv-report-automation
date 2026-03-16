"""Main entry point for the MRV report automation Streamlit app."""

from pathlib import Path
from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
import streamlit as st

from ingestion.parse_word import parse_word_file
from ingestion.parse_pdf import parse_pdf_file
from ingestion.chunk_sections import chunk_word_paragraphs, chunk_pdf_pages


# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Model Validation Report Automation", layout="wide")
st.title("Model Validation Report Automation")
st.caption("Prototype v1 - Validation intake + document ingestion + section extraction")


# -----------------------------
# Session state initialization
# -----------------------------
def initialize_session_state() -> None:
    """Initialize session state keys used by the app."""
    defaults: Dict[str, Any] = {
        "intake_data": {},
        "uploaded_file_name": None,
        "raw_records": [],
        "sections": [],
        "document_type": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


initialize_session_state()


# -----------------------------
# Helpers
# -----------------------------
def build_intake_context(intake_data: Dict[str, Any]) -> str:
    """
    Convert intake data into a structured text block that can later be injected
    into prompts for section drafting, testing analysis, or finding generation.
    """
    if not intake_data:
        return "No validation intake data captured yet."

    lines: List[str] = [
        "Validation Intake Context",
        "-------------------------",
        f"Model Name: {intake_data.get('model_name', '')}",
        f"Model ID: {intake_data.get('model_id', '')}",
        f"Model Tier: {intake_data.get('model_tier', '')}",
        f"Model Type: {intake_data.get('model_type', '')}",
        f"Validation Type: {intake_data.get('validation_type', '')}",
        f"Methodology Changed: {intake_data.get('methodology_changed', '')}",
        f"New Data Appended: {intake_data.get('data_appended', '')}",
        f"Data Source Changed: {intake_data.get('data_source_changed', '')}",
        f"Latest Monitoring Reviewed: {intake_data.get('latest_monitoring_reviewed', '')}",
        f"Latest Testing Reviewed: {intake_data.get('latest_testing_reviewed', '')}",
        "",
        "What Changed Since Prior Review:",
        intake_data.get("what_changed", "") or "[Not provided]",
        "",
        "What Stayed the Same:",
        intake_data.get("what_stayed_same", "") or "[Not provided]",
        "",
        "Key Concerns Identified This Cycle:",
        intake_data.get("key_concerns", "") or "[Not provided]",
        "",
        "Potential Findings Under Consideration:",
        intake_data.get("potential_findings", "") or "[Not provided]",
        "",
        "Additional Drafting Notes:",
        intake_data.get("additional_notes", "") or "[Not provided]",
    ]

    return "\n".join(lines)


def save_intake_to_session(intake_data: Dict[str, Any]) -> None:
    """Save intake data and derived prompt context into session state."""
    st.session_state["intake_data"] = intake_data
    st.session_state["intake_context_text"] = build_intake_context(intake_data)


def clear_document_state() -> None:
    """Clear document-related state while preserving intake data."""
    st.session_state["uploaded_file_name"] = None
    st.session_state["raw_records"] = []
    st.session_state["sections"] = []
    st.session_state["document_type"] = None


# -----------------------------
# Sidebar: session summary
# -----------------------------
st.sidebar.header("Session Status")

if st.session_state["intake_data"]:
    st.sidebar.success("Validation intake captured")
    st.sidebar.write(f"**Model:** {st.session_state['intake_data'].get('model_name', '')}")
    st.sidebar.write(f"**Model ID:** {st.session_state['intake_data'].get('model_id', '')}")
    st.sidebar.write(f"**Tier:** {st.session_state['intake_data'].get('model_tier', '')}")
else:
    st.sidebar.info("No intake data saved yet")

if st.session_state["uploaded_file_name"]:
    st.sidebar.success("Document parsed")
    st.sidebar.write(f"**File:** {st.session_state['uploaded_file_name']}")
    st.sidebar.write(f"**Sections:** {len(st.session_state['sections'])}")
else:
    st.sidebar.info("No document parsed yet")


# -----------------------------
# Validation intake form
# -----------------------------
st.header("1. Validation Intake")

existing_intake = st.session_state.get("intake_data", {})

with st.form("validation_intake_form"):
    col1, col2 = st.columns(2)

    with col1:
        model_name = st.text_input(
            "Model Name",
            value=existing_intake.get("model_name", ""),
        )
        model_id = st.text_input(
            "Model ID",
            value=existing_intake.get("model_id", ""),
        )
        model_tier = st.selectbox(
            "Model Tier",
            ["", "Tier 1", "Tier 2", "Tier 3", "Tier 4", "Tier 5"],
            index=["", "Tier 1", "Tier 2", "Tier 3", "Tier 4", "Tier 5"].index(
                existing_intake.get("model_tier", "")
            )
            if existing_intake.get("model_tier", "") in ["", "Tier 1", "Tier 2", "Tier 3", "Tier 4", "Tier 5"]
            else 0,
        )
        model_type = st.text_input(
            "Model Type",
            value=existing_intake.get("model_type", ""),
        )
        validation_type = st.selectbox(
            "Validation Type",
            ["", "Full Validation", "Annual Review", "Targeted Review", "Change Review", "Ongoing Monitoring Review"],
            index=[
                "",
                "Full Validation",
                "Annual Review",
                "Targeted Review",
                "Change Review",
                "Ongoing Monitoring Review",
            ].index(existing_intake.get("validation_type", ""))
            if existing_intake.get("validation_type", "")
            in [
                "",
                "Full Validation",
                "Annual Review",
                "Targeted Review",
                "Change Review",
                "Ongoing Monitoring Review",
            ]
            else 0,
        )

    with col2:
        methodology_changed = st.selectbox(
            "Methodology Changed?",
            ["", "Yes", "No", "Unknown"],
            index=["", "Yes", "No", "Unknown"].index(existing_intake.get("methodology_changed", ""))
            if existing_intake.get("methodology_changed", "") in ["", "Yes", "No", "Unknown"]
            else 0,
        )
        data_appended = st.selectbox(
            "New Data Appended?",
            ["", "Yes", "No", "Unknown"],
            index=["", "Yes", "No", "Unknown"].index(existing_intake.get("data_appended", ""))
            if existing_intake.get("data_appended", "") in ["", "Yes", "No", "Unknown"]
            else 0,
        )
        data_source_changed = st.selectbox(
            "Data Source Changed?",
            ["", "Yes", "No", "Unknown"],
            index=["", "Yes", "No", "Unknown"].index(existing_intake.get("data_source_changed", ""))
            if existing_intake.get("data_source_changed", "") in ["", "Yes", "No", "Unknown"]
            else 0,
        )
        latest_monitoring_reviewed = st.selectbox(
            "Latest Monitoring Results Reviewed?",
            ["", "Yes", "No", "Not Available"],
            index=["", "Yes", "No", "Not Available"].index(existing_intake.get("latest_monitoring_reviewed", ""))
            if existing_intake.get("latest_monitoring_reviewed", "") in ["", "Yes", "No", "Not Available"]
            else 0,
        )
        latest_testing_reviewed = st.selectbox(
            "Latest Testing Outputs Reviewed?",
            ["", "Yes", "No", "Not Available"],
            index=["", "Yes", "No", "Not Available"].index(existing_intake.get("latest_testing_reviewed", ""))
            if existing_intake.get("latest_testing_reviewed", "") in ["", "Yes", "No", "Not Available"]
            else 0,
        )

    what_changed = st.text_area(
        "What changed since the prior review?",
        value=existing_intake.get("what_changed", ""),
        height=120,
        placeholder="Example: new data appended through Q4 2025; no methodology changes; monitoring refreshed.",
    )

    what_stayed_same = st.text_area(
        "What stayed the same?",
        value=existing_intake.get("what_stayed_same", ""),
        height=120,
        placeholder="Example: core methodology, intended use, and implementation platform remain unchanged.",
    )

    key_concerns = st.text_area(
        "Key concerns identified this cycle",
        value=existing_intake.get("key_concerns", ""),
        height=140,
        placeholder="List concerns, challenges, or issues noted during review.",
    )

    potential_findings = st.text_area(
        "Potential findings under consideration",
        value=existing_intake.get("potential_findings", ""),
        height=140,
        placeholder="List issues that may need to be structured into findings.",
    )

    additional_notes = st.text_area(
        "Additional drafting notes",
        value=existing_intake.get("additional_notes", ""),
        height=120,
        placeholder="Anything else the drafting tool should know for this review cycle.",
    )

    intake_submitted = st.form_submit_button("Save Intake")

if intake_submitted:
    intake_data = {
        "model_name": model_name,
        "model_id": model_id,
        "model_tier": model_tier,
        "model_type": model_type,
        "validation_type": validation_type,
        "methodology_changed": methodology_changed,
        "data_appended": data_appended,
        "data_source_changed": data_source_changed,
        "latest_monitoring_reviewed": latest_monitoring_reviewed,
        "latest_testing_reviewed": latest_testing_reviewed,
        "what_changed": what_changed,
        "what_stayed_same": what_stayed_same,
        "key_concerns": key_concerns,
        "potential_findings": potential_findings,
        "additional_notes": additional_notes,
    }
    save_intake_to_session(intake_data)
    st.success("Validation intake captured and saved to session state.")


# -----------------------------
# Display saved intake context
# -----------------------------
if st.session_state["intake_data"]:
    st.subheader("Saved Intake Summary")
    st.json(st.session_state["intake_data"])

    with st.expander("Prompt-Ready Intake Context"):
        st.code(
            st.session_state.get("intake_context_text", ""),
            language="text",
        )


# -----------------------------
# Document upload and ingestion
# -----------------------------
st.header("2. Document Ingestion")

st.markdown(
    """
Upload a model-related document to test ingestion and section extraction.

Currently supported:
- `.docx`
- `.pdf`
"""
)

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["docx", "pdf"],
)

col_parse, col_clear = st.columns([1, 1])

with col_parse:
    parse_clicked = st.button("Parse Uploaded Document", type="primary")

with col_clear:
    clear_clicked = st.button("Clear Parsed Document")

if clear_clicked:
    clear_document_state()
    st.success("Parsed document state cleared.")

if uploaded_file is not None and parse_clicked:
    suffix = Path(uploaded_file.name).suffix.lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    try:
        if suffix == ".docx":
            raw_records = parse_word_file(tmp_path)
            sections = chunk_word_paragraphs(raw_records)
            document_type = "word"

        elif suffix == ".pdf":
            raw_records = parse_pdf_file(tmp_path)
            sections = chunk_pdf_pages(raw_records)
            document_type = "pdf"

        else:
            st.error("Unsupported file type.")
            st.stop()

        st.session_state["uploaded_file_name"] = uploaded_file.name
        st.session_state["raw_records"] = raw_records
        st.session_state["sections"] = sections
        st.session_state["document_type"] = document_type

        st.success(f"Parsed {uploaded_file.name}")

    except Exception as exc:
        st.error(f"An error occurred while parsing the file: {exc}")

    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


# -----------------------------
# Display parsed output
# -----------------------------
if st.session_state["raw_records"]:
    st.subheader("Raw Parsed Records")
    st.write(f"Total raw records: {len(st.session_state['raw_records'])}")

    raw_df = pd.DataFrame(st.session_state["raw_records"])
    st.dataframe(raw_df, use_container_width=True)

if st.session_state["sections"]:
    st.subheader("Extracted Sections")
    st.write(f"Total sections: {len(st.session_state['sections'])}")

    for i, section in enumerate(st.session_state["sections"], start=1):
        with st.expander(f"{i}. {section['section_title']}"):
            st.text_area(
                label=f"Content {i}",
                value=section["content"],
                height=220,
                key=f"section_{i}",
            )


# -----------------------------
# Generation prep preview
# -----------------------------
st.header("3. Generation Prep Preview")

if st.session_state["intake_data"] and st.session_state["sections"]:
    st.success("The app has both intake context and parsed document content.")
    st.write("This is enough to support the next step: section-specific draft generation.")

    section_titles = [section["section_title"] for section in st.session_state["sections"]]
    selected_section_title = st.selectbox(
        "Select a parsed section to preview as generation input",
        section_titles,
    )

    selected_section = next(
        (section for section in st.session_state["sections"] if section["section_title"] == selected_section_title),
        None,
    )

    if selected_section:
        st.subheader("Selected Section Content")
        st.text_area(
            "Section text that could be passed into a future generation prompt",
            value=selected_section["content"],
            height=250,
        )

        combined_preview = (
            f"{st.session_state.get('intake_context_text', '')}\n\n"
            f"Document Section Title: {selected_section['section_title']}\n"
            f"Document Section Content:\n{selected_section['content']}"
        )

        with st.expander("Combined Prompt Input Preview"):
            st.code(combined_preview, language="text")
else:
    st.info("Save intake data and parse a document to preview generation inputs.")