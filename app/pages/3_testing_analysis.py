"""Testing analysis review page."""

import streamlit as st


st.title("3. Testing Analysis")
st.write("Review parsed tables, charts, and testing narratives.")

st.selectbox(
    "Analysis mode",
    options=["Table analyzer", "Chart analyzer", "Narrative builder"],
)
st.text_area("Analysis notes", height=240)
