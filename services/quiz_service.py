from services.gemini_service import GeminiService


class QuizService:

    def __init__(self):
        self.ai = GeminiService()

    def generate(self, topic, difficulty, questions):

        prompt = f"""
You are an expert teacher.

Create {questions} multiple choice questions.

Topic:
{topic}

Difficulty:
{difficulty}

Requirements:

1. Number each question.
2. Give four options (A, B, C, D).
3. Mention the correct answer.
4. Give a one-line explanation.
5. Use simple English.
"""

        return self.ai.ask(prompt)