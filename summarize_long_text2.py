
import openai
from dotenv import load_dotenv
import os
import time
import sys


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")

content_format1 = """Summarize the highlights of the content which is delimited with triple backticks 
and output a useful summary in a few sentences. Please write in {lang} language. 
Content: ```{content}```"""

content_format2 = """Summarize the highlights of the content which is delimited with triple backticks, 
generate a mind map, and output it in Markdown format, and the output language is {lang}. 
Content: ```{content}```"""


def summarize_content(content, lang):
    messages = [
        {
            "role": "user", 
            "content": content_format2.format(content=content, lang=lang)
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    collected_messages = []
    for chunk in response:
        chunk_message = chunk['choices'][0]['delta']  # extract the message
        if 'content' in chunk_message:
            content = chunk_message['content']
            collected_messages.append(content)
            print(content, end="")
            sys.stdout.flush()
    
    print();
    return "".join(collected_messages)


def summarize_chunks(chunks, lang="zh-CN"):
    return "\n".join([summarize_content(chunk, lang) for chunk in chunks])



with open("carbon_neutral.source.txt", "r") as f:
    summarize_chunks(f.read().split('\n\n\n'))
