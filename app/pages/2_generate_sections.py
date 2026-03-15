"""Section generation workspace."""

import streamlit as st


st.title("2. Generate Sections")
st.write("Generate draft report sections grounded in retrieved evidence.")

section_name = st.text_input("Section name", placeholder="Executive Summary")

if st.button("Generate draft"):
    if section_name:
        st.text_area("Draft output", value=f"Draft placeholder for: {section_name}", height=240)
    else:
        st.warning("Enter a section name before generating.")
