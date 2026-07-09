import json
import os
from datetime import datetime

def save_transcript(role, questions, answers, evaluation):
    os.makedirs("transcripts", exist_ok=True)

    interview = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "role": role,
        "questions": questions,
        "answers": answers,
        "evaluation": evaluation
    }

    filename = f"transcripts/interview_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(interview, f, indent=4)

    return filename