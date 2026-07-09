# 🎯 AI Interview Agent

An AI-powered Interview Agent developed as part of the **Rooman Technologies 24-Hour AI Agent Challenge**.

The application generates role-specific interview questions, accepts candidate responses, evaluates each answer using a Large Language Model (Groq Llama 3.3), and provides detailed feedback, an overall score, strengths, weaknesses, and a hiring recommendation.

---

# Features

- Generates 5 interview questions based on the selected job role
- Accepts candidate answers
- Evaluates each answer using AI
- Provides a score for every answer
- Generates detailed feedback
- Identifies strengths and weaknesses
- Gives an overall interview score
- Recommends Hire / Consider / Reject
- Simple and interactive Streamlit interface

---

# Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile Model
- Python-dotenv
- Git
- GitHub

---

# Project Structure

```
AI-Interview-Agent/
│
├── app.py
├── interview.py
├── evaluator.py
├── prompts.py
├── database.py
├── .env
├── requirements.txt
├── README.md
├── data/
├── transcripts/
└── screenshots/
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Anusha-1323/AI-Interview-Agent.git
```

Move into the project folder

```bash
cd AI-Interview-Agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# Configure API Key

Create a file named `.env` in the project folder.

Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

---

# Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# How It Works

1. Enter the desired job role.
2. Click **Generate Questions**.
3. The AI generates five interview questions.
4. Enter answers for all questions.
5. Click **Evaluate Interview**.
6. The AI evaluates every answer.
7. View the final interview report.

---

# Sample Input

**Job Role**

```
Python Developer
```

---

# Sample Output

### Interview Questions

1. What is Object-Oriented Programming?
2. Explain Inheritance in Python.
3. What is Exception Handling?
4. Difference between List and Tuple.
5. Explain Python Decorators.

---

### Evaluation

Question 1

Score: 8/10

Feedback:
Good understanding of the concept with minor improvements needed.

Question 2

Score: 9/10

Feedback:
Excellent explanation with relevant examples.

Question 3

Score: 7/10

Feedback:
Correct answer but could include practical examples.

Question 4

Score: 8/10

Feedback:
Well explained.

Question 5

Score: 9/10

Feedback:
Strong conceptual understanding.

Overall Score

41/50

Strengths

- Strong Python fundamentals
- Good explanation skills
- Clear understanding of OOP

Weaknesses

- Needs improvement in advanced concepts
- Could provide more real-world examples

Final Recommendation

**Consider**

---

# Design Choices

- Used Groq's Llama 3.3 70B model for fast and high-quality interview generation.
- Used Streamlit to build a lightweight interactive interface.
- Stored API keys securely using environment variables.
- Followed a modular architecture by separating question generation and evaluation logic.
- Built an end-to-end AI workflow with minimal dependencies.

---

# Trade-offs

- Uses an online API and therefore requires internet access.
- Evaluation depends on the quality of the LLM response.
- Current version supports only text-based interviews.
- Questions are generated dynamically and may vary between runs.

---

# Future Improvements

- Voice-based interview support
- Resume upload and analysis
- Resume-based interview question generation
- PDF interview report generation
- SQLite database for interview history
- Authentication and user profiles
- Interview analytics dashboard

---

# Author

**Anusha B**

Rooman Technologies

Junior AI Research Associate

24-Hour AI Agent Challenge

---

# License

This project is created for educational and evaluation purposes as part of the Rooman Technologies AI Agent Challenge.

---

## Screenshots

### Home Page
![Home](screenshots/home.png)

### Generated Questions
![Questions](screenshots/questions.png)

### Evaluation
![Evaluation](screenshots/evaluation.png)