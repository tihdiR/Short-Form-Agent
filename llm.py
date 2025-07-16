import os
from google import genai
from google.genai import types

class LLMClient:
    def __init__(self, api_key=None, model="gemini-2.0-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def generate(self, prompt: str, temperature=0.7, max_tokens=150) -> str:
        generation_config = types.GenerateContentConfig(
            temperature=temperature, 
            max_output_tokens=max_tokens, 
            )
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config = generation_config
        )
        return response.text.strip()
