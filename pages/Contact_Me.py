import streamlit as st

st.title("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address:")
    message = st.text_area("Your message:")
    button = st.form_submit_button("Submit")
    if button:
        print("Hello World")