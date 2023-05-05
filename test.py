import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")

def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion2(prompt_sys, prompt_user, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content": prompt_sys},
        {"role": "user", "content": prompt_user}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


prompt_system = "你一个处理人际职场关系的专家，请为用户提出的问题提供建议和帮助。"
prompt_user = """
我的同事一直搭乘我的私家车上下班，已经一个多月了，在她搭乘之前，我再上下班的路上会听一些音频以及和我的好友打电话，
现在我只能和她聊天，我感觉到生活的空间被侵入了，我该如何委婉得拒绝她搭乘我的车
"""
response = get_completion2(prompt_system, prompt_user, "gpt-3.5-turbo-0301")
print(response)

 

