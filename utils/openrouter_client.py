import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenRouterClient:
    def __init__(self, model="openai/gpt-4-turbo"):
        # Configure OpenAI client to use OpenRouter API
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        self.model = model

    def generate_completion(self, messages, temperature=0.7, max_tokens=2000):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                extra_headers={
                    "HTTP-Referer": "https://github.com/manus-ai/doc-gen-system",
                    "X-Title": "Multi-Agent Doc Gen System",
                }
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating completion: {e}")
            return None
