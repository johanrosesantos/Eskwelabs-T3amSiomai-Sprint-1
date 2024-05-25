import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="Golden Years, Golden Opportunities",
    layout="wide"
)

# Sidebar content
st.sidebar.image('images/grouplogo.png', use_column_width=True)
st.sidebar.write("Abby | Eugene | Gab | Johan | Nicole")

# Main content image
st.image('images/1.png')

# Main app content
st.title("Adobo Advantage Cards")
st.write("This is a sample Streamlit app with a logo in the sidebar and a main image.")

st.title("Challenge")
st.write("This is a sample Streamlit app with a logo in the sidebar and a main image.")
