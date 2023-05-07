import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")



def summarize_content(content, lang):
    messages = [
        {
            "role": "user", 
            "content": f"""Summarize the highlights of the content which is delimited with triple backticks and output a useful summary in a few sentences. 
Please write in {lang} language. Content: ```{content}```"""
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0].message["content"].strip()

def summarize_chunks(chunks, lang="zh-CN", final_summary_enabled=False):
    summarized_chunks = []
    for chunk in chunks:
        summarized_chunk = summarize_content(chunk, lang)
        summarized_chunks.append(summarized_chunk) 

    concatenated_summaries = "\n".join(summarized_chunks)
    if final_summary_enabled:
        final_summary = summarize_content(concatenated_summaries, lang)
        return final_summary
    else:
        return concatenated_summaries


source_file = 'carbon_neutral.source.txt'

with open(source_file, "r") as f:
    print(summarize_chunks(f.read().split('\n\n\n'), "zh-CN", True))


