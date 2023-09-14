import streamlit as st
import pandas as pd


st.set_page_config(page_title="Projects",
                   page_icon ="💼",
                   layout="wide")

st.title("Projects")

col3, space_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_excel("projects.xlsx", sheet_name="data")

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


