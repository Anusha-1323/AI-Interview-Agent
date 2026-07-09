import streamlit as st
from interview import generate_questions
from evaluator import evaluate_interview

st.set_page_config(page_title="AI Interview Agent")

st.title("🎯 AI Interview Agent")

role = st.text_input("Enter the job role")

# Generate Questions
if st.button("Generate Questions"):
    if role:
        st.session_state.questions = generate_questions(role)
    else:
        st.warning("Please enter a job role.")

# Display Questions
if "questions" in st.session_state:

    st.subheader("Interview Questions")

    st.write(st.session_state.questions)

    st.subheader("Candidate Answers")

    answer1 = st.text_area("Answer 1")
    answer2 = st.text_area("Answer 2")
    answer3 = st.text_area("Answer 3")
    answer4 = st.text_area("Answer 4")
    answer5 = st.text_area("Answer 5")

    if st.button("Evaluate Interview"):

        answers = f"""
1. {answer1}
2. {answer2}
3. {answer3}
4. {answer4}
5. {answer5}
"""

        result = evaluate_interview(
            role,
            st.session_state.questions,
            answers
        )

        st.subheader("Interview Evaluation")

        st.write(result)