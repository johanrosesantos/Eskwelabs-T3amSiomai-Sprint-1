import streamlit as st

st.set_page_config(
    page_title="How powerful is AAC's users spending?",
    layout="wide"
)
st.markdown("# How powerful is AAC's users spending?")
st.sidebar.header("How powerful is AAC's users spending?")
# st.image("title_slide.png", width = 800)

st.header("Male users dominate the AAC users by 94%")
st.image("images/gender.png")

st.header("AAC users hail from Region III, IV-A & IV-B")
st.image("images/cities.png")

st.header("Top job categories are from tourism, engineering and medical fields")
st.image("images/job.png")

st.markdown(
    """
    Insert text here in markdown
    # Heading
    ## Subheading
    - Bullets
"""
)
