import streamlit as st

st.set_page_config(
    page_title="What drives AAC user spending?",
    layout="wide"
)
st.sidebar.image('images/adobologo.png', use_column_width=True)

st.markdown("# What drives AAC user spending?")
st.sidebar.header("What drives AAC user spending?")


st.write("We estimated a linear regression model with total spending amount as the dependent variable. For the independent variables, we considered factors such as, the age group, location, the current season (i.e., dry or rainy), the time of day the transaction was made, and the RFM level. ")
st.write("The total spending amount was log transformed, and all the independent variables were one-hot encoded.")

st.image("images/lin_regression2.png", caption="Linear Regression Results", width = 600)

st.markdown("## Interpretation")

st.markdown("### Age Bins:")
st.write("Gen X customers tend to spend less compared to other groups.")
st.write("Silent generation customers tend to spend more.")

st.markdown("### Location")
st.write("Customers in Visayas spend slightly more, but the effect is small.")
st.write("No significant difference for customers in Mindanao.")

st.markdown("### RFM Levels")
st.write("Customers in the middle and top RFM levels spend significantly more, with the top RFM level having the largest positive effect.")

st.markdown("### Other Variables")
st.write("Being a holiday, POS status, rainy season, and time of day do not have a significant impact on spending.")
