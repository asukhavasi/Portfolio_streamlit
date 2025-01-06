import streamlit as st
import send_email
import pandas as p

st.title("Company conatct")

options = p.read_csv("data/topics.csv")

selections = []
for index, row in options.iterrows():
    selections.append(row["topic"])


with st.form("webform"):
    user_email = st.text_input("Enter your Email: ")
    option = st.selectbox("Which topic do you want to discuss",
                          selections,
                          index=None,
                          placeholder="Select a topic...")

    # print(option)

    raw_message = st.text_area("Enter your message")
    message = f"""\
Subject: New email request regarding: {option}

From: {user_email}
topic:{option}
{raw_message}
"""
    submit = st.form_submit_button("Submit")
    if submit:
        send_email.send_email(message)
        st.info("Your email is sent successfully!")