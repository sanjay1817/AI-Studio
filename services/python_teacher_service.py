from services.gemini_service import GeminiService


class PythonTeacherService:

    def __init__(self):
        self.ai = GeminiService()

    def teach(self, topic):

        prompt = f"""
You are an expert Python teacher.

Teach the following topic:

{topic}

Your response should include:

1. Simple explanation
2. Syntax
3. Example code
4. Expected output
5. Common mistakes
6. One practice exercise

Use simple English suitable for school students.
"""

        return self.ai.ask(prompt)