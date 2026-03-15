"""Upload page for source documents and supporting artifacts."""

import streamlit as st


st.title("1. Upload")
st.write("Upload model documents, validation evidence, and prior reports here.")

uploaded_files = st.file_uploader(
    "Choose source files",
    accept_multiple_files=True,
    type=["pdf", "docx", "xlsx", "csv"],
)

if uploaded_files:
    st.success(f"Loaded {len(uploaded_files)} file(s).")
