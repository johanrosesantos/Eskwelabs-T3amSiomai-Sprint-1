import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="Golden Years, Golden Opportunities",
    layout="wide"
)

# Get the absolute paths of the images for debugging
sidebar_image_path = os.path.abspath('images/adobologo.png')
main_image_path = os.path.abspath('images/1.png')

# Sidebar content
try:
    st.sidebar.image(sidebar_image_path, use_column_width=True)
    st.sidebar.write(f"Sidebar image loaded from: {sidebar_image_path}")
except Exception as e:
    st.sidebar.write(f"Error loading sidebar image: {e}")

# Main content image
try:
    st.image(main_image_path)
    st.write(f"Main image loaded from: {main_image_path}")
except Exception as e:
    st.write(f"Error loading main image: {e}")

# Main app content
st.title("Golden Years, Golden Opportunities")
st.write("This is a sample Streamlit app with a logo in the sidebar and a main image.")
