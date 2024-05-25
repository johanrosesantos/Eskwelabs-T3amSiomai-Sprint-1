import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="Golden Years, Golden Opportunities",
    layout="wide"
)

# Sidebar content
st.sidebar.image(sidebar_image_path, use_column_width=True)
st.sidebar.write("Abby | Eugene | Gab | Johan | Nicole")

# Main content image
st.image(main_image_path)

# Main app content
st.title("Adobo Advantage Cards")
st.write("This is a sample Streamlit app with a logo in the sidebar and a main image.")

st.title("Challenge")
st.write("This is a sample Streamlit app with a logo in the sidebar and a main image.")
