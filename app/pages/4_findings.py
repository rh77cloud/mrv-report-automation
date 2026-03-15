"""Findings drafting page."""

import streamlit as st


st.title("4. Findings")
st.write("Draft findings linked to testing evidence and report sections.")

severity = st.selectbox("Severity", options=["Low", "Moderate", "High"])
st.text_area("Finding draft", height=220, placeholder="Describe the issue, impact, and recommendation.")
st.caption(f"Selected severity: {severity}")
