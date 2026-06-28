import requests
from PIL import Image
from io import BytesIO
import urllib.parse


class ImageService:

    def generate(self, prompt):

        prompt = urllib.parse.quote(prompt)

        url = f"https://image.pollinations.ai/prompt/{prompt}"

        response = requests.get(url, timeout=60)

        response.raise_for_status()

        image = Image.open(BytesIO(response.content))

        return image