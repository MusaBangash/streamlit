
import streamlit as st

name = st.text_input("Enter your name:")
#st.write("Name:",name)

age = st.number_input("Enter your age:",min_value=18,max_value=60)
#st.write("Age:",age)

clicked = st.button("Submit")

if clicked:
    st.write("Name:",name)
    st.write("Age:",age)    


st.header("Greeting App")

name2 = st.text_input("Name:")

if st.button("Greet"):
    st.write("Hello ",name2)