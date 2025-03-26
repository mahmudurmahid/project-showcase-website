import streamlit as st
import pandas

st.set_page_config(layout="wide")

# Columns 1 and 2
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mahmudur Mahid")
    content = """
    Hi, I am Mahmudur. A Junior Full Stack Developer with a keen interest in Muay Thai Boxing and BJJ. I am transitioning from a successful career in tech recruitment to software development due to my interest in problem-solving, need for continuous learning, and passion to build innovative projects.
    """
    st.info(content)

content2 = """
Below are some apps I have built using Python. Please feel free to contact me about them!
"""
st.write(content2)

# Columns 3 and 4
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

