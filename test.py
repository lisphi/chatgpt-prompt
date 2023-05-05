import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")

def get_completion(prompt_sys, prompt_user, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content": prompt_sys},
        {"role": "user", "content": prompt_user}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.2,
    )
    return response.choices[0].message["content"]


prompt_system = "你是一个资深的Python游戏开发者，你的任务是根据用户的需求写Python程序。"
prompt_user = """
贪吃蛇游戏
"""
response = get_completion(prompt_system, prompt_user, "gpt-3.5-turbo-0301")
print(response)

 

