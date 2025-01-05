import streamlit as st
from send_email import send_email

st.title("Contact Us")
with st.form(key="email_form"):
    user_email = st.text_input("Enter email address:")

    message = st.text_area("Yor message: ")
    message = message + "\n" + user_email
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
