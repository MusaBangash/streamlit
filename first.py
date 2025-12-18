import streamlit as st

st.title("Basic User Form")

with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    email = st.text_input("Email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Form submitted successfully!")
    st.write("### Submitted Data")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Email:", email)
    st.write("Message:", message)
