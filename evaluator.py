import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def evaluate_interview(role, questions, answers):
    prompt = f"""
You are an expert technical interviewer.

Role: {role}

Questions:
{questions}

Candidate Answers:
{answers}

Evaluate each answer.

For each question provide:
- Score out of 10
- Short feedback

Finally provide:
1. Overall Score out of 50
2. Strengths
3. Weaknesses
4. Final Recommendation (Hire / Consider / Reject)

Return the result in a clean format.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert technical interviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content