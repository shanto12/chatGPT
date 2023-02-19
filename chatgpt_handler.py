# chatGPT_handler.py

import openai

class ChatGPT_Handler:
    def __init__(self, prompt):
        self.prompt = prompt

    def get_response(self):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=self.prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text
        return response
