import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mahmudur Mahid")
    content = """
    Hi, I am Mahmudur. A Junior Full Stack Developer with a keen interest in Muay Thai Boxing and BJJ. I am transitioning from a successful career in tech recruitment to software development due to my interest in problem-solving, need for continuous learning, and passion to build innovative projects.
    """
    st.info(content)
