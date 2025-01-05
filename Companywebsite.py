import streamlit as st
import pandas as pd

st.set_page_config("wide")
st.title("Sukhavasi Inc")
st.write("Lorem ipsum dolor, sit amet consectetur adipisicing elit. Saepe placeat repellendus repellat, sed magnam consequuntur sequi optio voluptatibus nam vero debitis fuga veritatis deserunt? Cupiditate eum cum soluta molestias corrupti.")

st.write("<h4>Our Team</h4>",unsafe_allow_html=True)

col1,col2,col3,col4,col5= st.columns([1.0,0.5,1.0,0.5,1.0])

df = pd.read_csv("/Users/asukh/Documents/Portfolio/data/Comapnydata.csv")

with col1:
    for index, row in df[:4].iterrows():
        employee_name = f"{row['first name']} {row["last name"]}"
        employee_name = employee_name.title()
        st.write(f"<h4>{employee_name}</h4>",unsafe_allow_html=True)
        st.write(row["role"])
        st.image(f"/Users/asukh/Documents/Portfolio/data/Company Images/{row['image']}")


with col3:
    for index, row in df[4:8].iterrows():
        employee_name = f"{row['first name']} {row["last name"]}"
        employee_name = employee_name.title()
        st.write(f"<h4>{employee_name}</h4>",unsafe_allow_html=True)
        st.write(row["role"])
        st.image(f"/Users/asukh/Documents/Portfolio/data/Company Images/{row['image']}")

with col5:
    for index, row in df[8:].iterrows():
        employee_name = f"{row['first name']} {row["last name"]}"
        employee_name = employee_name.title()
        st.write(f"<h4>{employee_name}</h4>",unsafe_allow_html=True)
        st.write(row["role"])
        st.image(f"/Users/asukh/Documents/Portfolio/data/Company Images/{row['image']}")