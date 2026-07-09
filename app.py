import streamlit as st
from database import save_transcript
from interview import generate_questions
from evaluator import evaluate_interview

st.set_page_config(page_title="AI Interview Agent")

st.title("🎯 AI Interview Agent")

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = ""

role = st.text_input("Enter the job role")

# Generate Questions
if st.button("Generate Questions"):
    if role:
        st.session_state.questions = generate_questions(role)
    else:
        st.warning("Please enter a job role.")

# Display Questions
if st.session_state.questions:

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

        file = save_transcript(
            role,
            st.session_state.questions,
            answers,
            result
        )

        st.subheader("Interview Evaluation")
        st.write(result)

        st.success("Interview saved successfully!")

        st.write("Transcript saved to:")
        st.code(file)

# Download transcript
        with open(file, "rb") as f:
            st.download_button(
                label="📥 Download Transcript",
                data=f,
                file_name="interview_transcript.json",
                mime="application/json"
            )