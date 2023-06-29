import streamlit as st
import pandas as pd

st.set_page_config(page_title="Home",
                   page_icon ="🏠",
                   layout="wide")

st.title("Home")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Emmanuel Herrera")
    content = """
    Hi, my name is Emmanuel Herrera, I'am an engineer passionate 
    about advanced data analytics and visualization techniques, committed 
    to mastering all aspects of data.  I love learning new techniques and 
    advanced data analytics tools to put them into practice in different
    productive environments to make better and more informed process decisions.
    I invite you to review a sample of my projects, any feedback will be welcome. 
    Regards.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.subheader(content2)

col3, space_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for idx, row in df[:10].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for idx, row in df[10:].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
