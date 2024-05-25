import streamlit as st

st.set_page_config(
    page_title="Who are AAC's users by cluster?",
    layout="wide"
)
st.markdown("# Who are AAC's users by cluster?")
# st.sidebar.header("Who are AAC's users by cluster?")
# # st.image("assets/title_slide.png", width = 800)
# st.markdown(
#     """
#     Insert text here in markdown
#     # Heading
#     ## Subheading
#     - Bullets
# """
# )
st.sidebar.header("How did we cluster the AAC users?")
st.write("## How did we cluster the AAC users?")
st.image("images/6.png", caption="Cluster Optimization", use_column_width=True)

st.sidebar.header("3D Scatter Plot Labeled by Cluster")
st.write("## 3D Scatter Plot Labeled by Cluster")
st.image("images/7.png", use_column_width=True)

st.sidebar.header("Customer Segmentation based on Demographic Profile and Spending Behavior")
st.write("## Customer Segmentation based on Demographic Profile and Spending Behavior")
st.image("images/8.png", caption="Overview of Customer Segmentation (green text = highest values or unique attributes, orange text = lowest value)", use_column_width=True)

st.sidebar.header("Further Generalizations per User Segment")
st.write("## Further Generalizations per User Segment ")
st.image("images/9.png", caption="General Characteristics per User Segment ", use_column_width=True)
