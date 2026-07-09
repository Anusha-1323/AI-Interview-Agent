import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_questions(role):
    prompt = f"""
    You are an expert interviewer.

    Generate exactly 5 interview questions for the role: {role}.

    The questions should:
    - Start easy and become more challenging.
    - Be relevant to the role.
    - Return only the numbered questions.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional technical interviewer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content