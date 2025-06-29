# llm_engine.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GenAILLM:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_response(self, prompt):
        data = {
            "model": "mistralai/mistral-7b-instruct",  # or any supported model
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(self.api_url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            return f"API Error: {response.status_code} - {response.text}"
