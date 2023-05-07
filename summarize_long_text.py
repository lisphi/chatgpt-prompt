import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")


def summarize_content(content, lang, stream_on):
    messages = [
        {
            "role": "user", 
            "content": f"""Summarize the highlights of the content which is delimited with triple backticks and output a useful summary in a few sentences. Please write in {lang} language. Content: ```{content}```"""
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=stream_on
    )
    if stream_on:
        collected_messages = []
        for chunk in response:
            chunk_message = chunk['choices'][0]['delta']  # extract the message
            if 'content' in chunk_message:
                content = chunk_message['content']
                collected_messages.append(content)
                print(content, end="", flush=True)
        print(flush=True)
        return ''.join(collected_messages)
    else:
        messages = response['choices'][0].message["content"].strip()
        print(messages, flush=True)
        return messages


def summarize_paragraphs(paragraphs, lang, stream_on, final_summary_on):
    summarized_contents_str = '\n'.join([summarize_content(paragraph, lang, stream_on) for paragraph in paragraphs])
    if not final_summary_on:
        return summarized_contents_str

    print("\n\n===== final summary =====", flush=True)
    return summarize_content(summarized_contents_str, lang, stream_on)


source_file = './resources/test.resource.txt'
paragraph_separator = '\n\n\n'
lang = 'zh-CN'
stream_on = True
final_summary_on = True

with open(source_file, "r") as f:
    summarize_paragraphs(f.read().split(paragraph_separator), lang, stream_on, final_summary_on)

