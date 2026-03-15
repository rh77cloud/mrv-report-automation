"""Main entry point for the MRV report automation Streamlit app."""

from pathlib import Path

import streamlit as st


st.set_page_config(page_title="MRV Report Automation", layout="wide")

st.title("MRV Report Automation")
st.caption("Draft model validation reports with retrieval, generation, and QA workflows.")

st.markdown(
    """
    Use the sidebar to move through the workflow:

    - Upload source reports and artifacts
    - Generate draft report sections
    - Analyze testing evidence
    - Draft and refine findings
    """
)

project_root = Path(__file__).resolve().parents[1]
st.info(f"Project root: `{project_root}`")
