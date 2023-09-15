import streamlit as st
import pandas as pd


st.set_page_config(page_title="Contact Me",
                   page_icon ="📊",
                   layout="wide")

st.title("From Data to Viz")

pbi = f"[Power BI]({'https://www.data-to-viz.com'})"

viz = f"""
Welcome to my portfolio of data visualizations created with R and Python. 
These visualizations speak for themselves, offering a straightforward and 
effective way to convey data-driven insights, they can seamlessly integrate into 
{pbi}, enhancing your data analytics capabilities. 
Should you require any code or customization to leverage these visuals for your specific 
needs, please feel free to reach out to me.
"""

st.write(viz)

col3, space_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_excel("data/viz.xlsx", sheet_name="data")

with col3:
    for idx, row in df[:7].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/vizualizations/" + row["image"])


with col4:
    for idx, row in df[7:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/vizualizations/" + row["image"])