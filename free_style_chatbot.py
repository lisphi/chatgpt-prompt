import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")

class Chat:
    def __init__(self):
        self.context = [{"role": "system", "content": "You are friendly chatbot."}]
        self.model = "gpt-3.5-turbo"
        self.temperature = 1

    def start(self):
        print("*****************************************")
        print("You are chatting with a friendly chatbot.")
        print("*****************************************")
        while True:
            user_input = input("You: ")
            self.context.append({"role": "user", "content": user_input})
            choice = self.get_completion_from_messages(self.context, self.model, self.temperature)
            print("Bot: " + choice.message["content"])
            self.context.append(choice.message)

    def get_completion_from_messages(self, messages, model, temperature):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, # this is the degree of randomness of the model's output
        )
        return response.choices[0]

chat = Chat()
chat.start()