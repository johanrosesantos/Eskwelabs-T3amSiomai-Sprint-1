import streamlit as st

st.set_page_config(
    page_title="How powerful is AAC's users spending?",
    layout="wide"
)
st.markdown("# How powerful is AAC's users spending?")
st.sidebar.header("How powerful is AAC's users spending?")
# st.image("title_slide.png", width = 800)

st.header("AAC reported that **6.49M USD** was generated from Jan. 1, 2020 to Dec. 7, 2021.")
st.write("This is around Php 377M with an exchange rate of 1 USD=Php58.")

st.markdown("# Who are the AAC users?")
st.sidebar.header("Who are the AAC users?")
# st.image("title_slide.png", width = 800)

st.header("Male users dominate the AAC users by 94%")
st.image("images/gender.png")

st.header("AAC users hail from Region III, IV-A & IV-B")
st.image("images/cities.png")

st.header("Top job categories are from tourism, engineering and medical fields")
st.image("images/job.png")

