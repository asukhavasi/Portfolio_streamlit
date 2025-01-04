import streamlit as st

st.set_page_config(layout = "wide")
col1, col2  = st.columns(2)

with col1:
    st.image('data/Images/Abi.png')

with col2:
    st.write("Abilash Sukhavasi")
    content = """
    Hi, I am Abilash! I am a software enthusiast, a Data engineer by profession, and enjoys training my body and loves to help poeple maintain an active lifestyle..
    """
    st.info(content)
