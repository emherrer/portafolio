import streamlit as st
import pandas as pd

st.set_page_config(page_title="Home",
                   page_icon ="🏠",
                   layout="wide")

st.title("Home")
st.subheader("Emmanuel Herrera Flores")

col1, col2 = st.columns([1, 5])

with col1:
    st.image("images/photo.png")

with col2:
    content = """
Hello, my name is Emmanuel Herrera, and I am a dedicated engineer specializing in 
advanced data analytics and visualization techniques. My passion lies in continually 
expanding my knowledge and expertise in the field, constantly learning new techniques 
and exploring advanced data analytics tools.

I believe in the power of applying these skills in various productive environments, 
aiming to assist you in maximizing the value of your data assets. By leveraging these insights,
 we can enable you to make better-informed decisions throughout your processes.

To showcase my abilities, I have developed a range of Python applications, which I invite 
you to explore below. Should you have any questions or require further information, please 
feel free to reach out to me. I look forward to connecting with you!
"""
    st.info(content)

col3, space_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for idx, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for idx, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
