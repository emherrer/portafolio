import streamlit as st
import pandas as pd

st.set_page_config(page_title="Home",
                   page_icon ="🏠",
                   layout="centered")

pbida = f"[_Microsoft certified data analyst_]({'https://learn.microsoft.com/es-mx/users/emmanuelherreraflores-4464/credentials/4795741e626513ec'})"

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/photo.png")
    
content = f"""
#### Hello, my name is Emmanuel Herrera, I am a dedicated engineer specializing in advanced data analytics and visualization techniques. 

#### As a {pbida}, I excel in extracting and transforming raw data into meaningful insights. My expertise spans data extraction, data wrangling, and crafting compelling visualizations, through tools like SQL, Python, R and Power BI. 

#### My passion lies in the realm of data engineering.  In my spare time I like to keep up to date with the many advances in the vast field of data engineering.

#### For more details about my career and experience, feel free to get in touch. 🚀
"""
st.write(content)
