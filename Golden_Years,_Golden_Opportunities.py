import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="Golden Years, Golden Opportunities",
    layout="wide"
)

# Sidebar content
st.sidebar.image('images/grplogo.png', use_column_width=True)
st.sidebar.write("Abby | Eugene | Gab | Johan | Nicole")

# Main content image
st.image('images/1.png')

# Main app content
st.title("Adobo Advantage Cards' (AAC) Challenge")
st.write("AAC is a credit card provider seeking the help of a consultant, aiming to enhance customer satisfaction and drive business growth by understanding its customer behavior thru customer segmentation and its correlation to spending.")
