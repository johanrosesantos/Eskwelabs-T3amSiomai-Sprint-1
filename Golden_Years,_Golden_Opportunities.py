
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
    page_title="Golden Years, Golden Opportunities",
    layout="wide"
)

st.write("# Golden Years, Golden Opportunities")
st.image("assets/Title - Abby.png", use_column_width=True)
