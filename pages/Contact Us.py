import streamlit as st

# import smtplib
# import ssl
#
#
# def send_email(message):
#     host = "smtp.gmail.com"
#     port = 465
#
#
#     user_name = "asukhava@gmail.com"
#     password = "lsiwwijnksqaziwg"
#     receiver_email = "sukhavasiabilash@gmail.com"
#     context = ssl.create_default_context()
#
#
#     # message= """\
#     # Subject: This is from webform.
#     # Hi! How are you?
#     # """
#
#     with smtplib.SMTP_SSL(host,port,context=context) as email_server:
#         email_server.login(user_name,password)
#         email_server.sendmail(user_name,receiver_email,message)

from send_email import send_email

st.title("Contact Us")
with st.form(key="email_form"):
    user_email = st.text_input("Enter email address:")

    raw_message = st.text_area("Yor message: ")
    message = f"""\
Subject: New email from {user_email}"

From: {user_email}
{raw_message}"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Email is sent.")
