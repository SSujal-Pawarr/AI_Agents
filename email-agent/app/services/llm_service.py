from openai import OpenAI

from app.config import (
    OPENROUTER_API_KEY,
    MODEL,
    BASE_URL,
)

class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=BASE_URL,
        )

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content