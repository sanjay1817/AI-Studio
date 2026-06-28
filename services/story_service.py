from services.gemini_service import GeminiService


class StoryService:

    def __init__(self):
        self.ai = GeminiService()

    def generate(self, topic, genre, length):

        prompt = f"""
You are an expert children's story writer.

Write a {length} {genre} story about:

{topic}

Requirements:

- Easy English
- Interesting beginning
- Good moral
- Creative ending
- Suitable for school students
"""

        return self.ai.ask(prompt)