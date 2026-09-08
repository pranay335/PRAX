from openai import OpenAI 
from config import GROQ_API_KEY

class PraxAgent:
    def __init__(self):
        self.client=OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

        self.model="openai/gpt-oss-20b"
        self.system_prompt="""
            You are PRAX, an AI agent designed to help users
            solve problems and complete tasks.

            Be clear, practical, and concise.

            You will gradually gain tools, memory, knowledge,
            planning, and workflow capabilities.
            """

    def chat(self,user_message):
        response=self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role":"system",
                    "content":self.system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response.choices[0].message.content