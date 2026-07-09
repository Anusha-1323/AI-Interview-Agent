import streamlit as st
from interview import generate_questions

st.set_page_config(page_title="AI Interview Agent")

st.title("🎯 AI Interview Agent")

role = st.text_input("Enter the job role")

if st.button("Generate Questions"):
    if role:
        questions = generate_questions(role)
        st.subheader("Interview Questions")
        st.write(questions)
    else:
        st.warning("Please enter a job role.")