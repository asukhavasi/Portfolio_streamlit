import streamlit as st
import pandas as pd


st.set_page_config(layout = "wide")
col1, col2  = st.columns(2)

with col1:
    st.image('data/Images/Abi.png',width=600)

with col2:
    st.write("<h6>Abilash Sukhavasi</h6>",unsafe_allow_html=True)
    content = """
    Hi, I am Abilash! I am a software enthusiast, a Data engineer by profession, and enjoys training my body and loves to help poeple maintain an active lifestyle..
    """
    st.info(content)

st.write("<h6>Below you can find some of the apps I have build in python. Feel free to contact me!</h6>", unsafe_allow_html=True)


col3, col4 ,col5= st.columns([1.5,0.5,1.5])

df = pd.read_csv("data/data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"data/images/{row["image"]}")
        st.write("[Source Code](https://www.google.com)")

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"data/images/{row["image"]}")
        st.write(f"[Source Code]({row['url']})")

