from google import genai


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=""
        )

    def ask(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
