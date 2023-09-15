import streamlit as st
import pandas as pd


st.set_page_config(page_title="Projects",
                   page_icon ="💼",
                   layout="wide")

st.title("One Project at a Time")
st.write("Welcome to my portfolio of Python projects. I'm on a continuous quest for improvement as I work towards becoming a data engineer. These projects reflect my commitment to learning and mastering the necessary tools to achieve this goal.")

col3, space_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_excel("data/project.xlsx", sheet_name="data")

with col3:
    for idx, row in df[:2].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[App]({row['url']}) - [Source Code]({row['repository']})")


with col4:
    for idx, row in df[2:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[App]({row['url']}) - [Source Code]({row['repository']})")


