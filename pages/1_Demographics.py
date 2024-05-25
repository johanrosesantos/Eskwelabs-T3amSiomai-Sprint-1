import streamlit as st

st.set_page_config(
    page_title="How powerful is AAC's users spending?",
    layout="wide"
)
st.sidebar.image('images/adobologo.png', use_column_width=True)

st.markdown("# How powerful is AAC's users spending?")
st.sidebar.header("How powerful is AAC's users spending?")

st.write("AAC reported that about 6.49M USD was generated from transactions made between Jan. 1, 2020 to Dec. 7, 2021.")
st.write("This is around Php 377M with an exchange rate of 1 USD=Php58.")

st.write(" ")
st.write(" ")

st.markdown("# Who are the AAC users?")
st.sidebar.header("Who are the AAC users?")

st.header("Male users dominate the AAC clients by 94%")
st.image("images/gender.png")

st.header("Majority of AAC users hail from cities in Region III, IV-A & IV-B")
st.image("images/cities.png")

st.header("Top job categories of AAC users are from tourism, engineering and medical fields")
st.image("images/job.png", width=800)

st.markdown("# What are the spending behavior of AAC users?")
st.sidebar.header("What are the spending behavior of AAC users?")

st.write(" ")
st.write(" ")

st.header("Users spend the most on essentials including groceries, kids, pets and gas")
st.image("images/catamt.png")

st.header("They also transact frequently on groceries, shopping and gas")
st.image("images/catvol.png")
st.write("Users also frequently spend onsite rather than online.")
