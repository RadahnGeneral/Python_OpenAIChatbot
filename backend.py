import openai
import os
from dotenv import load_dotenv

load_dotenv()
password_env = os.getenv("OPEN_API_KEY")

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(engine="text-davinci-003", prompt=user_input, max_tokens=3000, temperature=0.5).choices[0].text
        return response
    

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("what do you think about Elon Musk?")
    print(response)