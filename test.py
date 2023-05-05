import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.75,
    )
    return response.choices[0].message["content"]

prompt = """
我的同事搭我的车上班已经一个多月了，每天在我小区门口等我，我感觉到她侵犯我的私人空间了，该如何委婉地拒绝。
请列出5个方案。
"""
response = get_completion(prompt)
print(response)

 

