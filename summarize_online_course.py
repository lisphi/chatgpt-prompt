import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")


def summarize_content(course, lesson, transcript, index, size, lang, stream_on):
    part = ''
    if size > 1:
        part = f', Part {index + 1}'
    
    messages = [
        {
            "role": "user", 
            "content": f"""Your task is generate a short summary for '{lesson}{part}' of the course '{course}'. 
                the transcript of this lesson is delimited with triple backticks. Transcript: ```{transcript}```"""
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


def summarize_paragraphs(course, lesson, paragraphs, lang, stream_on, final_summary_on):
    summarized_contents = []
    for index in range(len(paragraphs)):
        paragraph = paragraphs[index]
        summarized_contents.append(summarize_content(course, lesson, paragraph, index, len(paragraphs), lang, stream_on))
    
    summarized_contents_str = '\n'.join(summarized_contents)
    if not final_summary_on:
        return summarized_contents_str

    print("\n\n===== final summary =====", flush=True)
    return summarize_content(title, summarized_contents_str, 0, 1, lang, stream_on)


source_file = './resources/l4.resource.txt'
paragraph_separator = '\n\n\n'
lang = 'en-US'
stream_on = True
final_summary_on = False

summary = ''
with open(source_file, "r") as f:
    summary = summarize_paragraphs('ChatGPT Prompt Engineering for Developers', \
        'Lesson 4: Summarizing', \
        f.read().split(paragraph_separator), lang, stream_on, final_summary_on)
     
with open(source_file + '.summary', 'w') as f:
    f.write(summary)


