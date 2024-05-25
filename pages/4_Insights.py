import streamlit as st

base="light"

st.markdown(
    """
    <style>
    .reportview-container {
        background: st.image("images/bg.jpg");
    }
   </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="Actionable Insights",
    layout="wide"
)
st.markdown("# What should AAC do?")
st.sidebar.header("What should AAC do?")

#Image
st.image("images/10.png", use_column_width=True)

