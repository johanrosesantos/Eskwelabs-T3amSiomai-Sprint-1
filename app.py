
import streamlit as st

st.set_page_config(layout="wide")

list_of_pages = [
    "Golden Years, Golden Opportunities",
    "How powerful is AAC's users spending?",
    "Who are AAC's users by cluster?",
    "What drives AAC user spending?",
    "What should AAC do?"
]

def aac():
    st.title(list_of_pages[0])
    # st.image("title_slide.png", width = 800)
    st.markdown("  ")

def demographics():
    st.title(list_of_pages[1])
    # st.image("title_slide.png", width = 800)
    st.markdown("  ")
    
def kmeans():
    st.title(list_of_pages[2])
    # st.image("title_slide.png", width = 800)
    st.markdown("  ")

def regression():
    st.title(list_of_pages[3])
    # st.image("title_slide.png", width = 800)
    st.markdown("  ")
    
def insights():
    st.title(list_of_pages[4])
    # st.image("title_slide.png", width = 800)
    st.markdown("  ")

st.sidebar.title('Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == list_of_pages[0]:
    aac()

elif selection == list_of_pages[1]:
    demographics()

elif selection == list_of_pages[2]:
    kmeans()

elif selection == list_of_pages[3]:
    regression()

elif selection == list_of_pages[4]:
    insights()