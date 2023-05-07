import openai
from dotenv import load_dotenv
import os
import sys


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")


def get_completion(prompt, model="gpt-3.5-turbo", stream=False):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        stream=stream,
    )
    if stream:
        collected_messages = []
        for chunk in response:
            chunk_message = chunk['choices'][0]['delta']  # extract the message
            if 'content' in chunk_message:
                content = chunk_message['content']
                collected_messages.append(content)
                print(content, end="", flush=True)
        return "".join(collected_messages)
    else:
        content = response.choices[0].message["content"]
        print(content, flush=True)
        return content


model = 'gpt-3.5-turbo'
stream = True
prompt = 'tell me a joke'

response = get_completion(prompt, model, stream)

