import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.proxy = os.getenv("OPENAI_PROXY")


def translate_content(course, lesson, transcript, index, size, lang, stream_on):
    part = ''
    if size > 1:
        part = f', Part {index + 1}'
    
    print(f'\n\nOrigin:\n======\n{transcript}\n\nTranslated:\n===========')

    messages = [
        {
            "role": "user", 
            "content": f"""Translate the following transcript to Chinese, and do not translate people's name.  Transcript:```{transcript}```"""
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


def translate_paragraphs(course, lesson, paragraphs, lang, stream_on):
    translated_contents = []
    for index in range(len(paragraphs)):
        paragraph = paragraphs[index]
        translated_contents.append(translate_content(course, lesson, paragraph, index, len(paragraphs), lang, stream_on))
    
    return '\n'.join(translated_contents)


source_file = './resources/l4.resource.txt'
paragraph_separator = '\n\n'
lang = 'zh-CN'
stream_on = False


lessons = [
    { 'file_path': './resources/prompt_engineering/l1.txt', 'title': 'Lesson 1: Introduction' },
    # { 'file_path': './resources/prompt_engineering/l2.txt', 'title': 'Lesson 2: Guidelines' },
    # { 'file_path': './resources/prompt_engineering/l3.txt', 'title': 'Lesson 3: Iterative' },
    # { 'file_path': './resources/prompt_engineering/l4.txt', 'title': 'Lesson 4: Chatbot' },
    # { 'file_path': './resources/prompt_engineering/l5.txt', 'title': 'Lesson 5: Inferring' },
    # { 'file_path': './resources/prompt_engineering/l6.txt', 'title': 'Lesson 6: Transforming' },
    # { 'file_path': './resources/prompt_engineering/l7.txt', 'title': 'Lesson 7: Explanding' },
    # { 'file_path': './resources/prompt_engineering/l8.txt', 'title': 'Lesson 8: Chatbot' },
    # { 'file_path': './resources/prompt_engineering/l9.txt', 'title': 'Lesson 9: Conclusion' },
]

for lesson in lessons:
    translated = ''
    with open(lesson['file_path'], "r") as f:
        translated = translate_paragraphs('ChatGPT Prompt Engineering for Developers', \
            lesson['title'], \
            f.read().split(paragraph_separator), lang, stream_on)
        
    with open(lesson['file_path'] + f'.{lang}', 'w') as f:
        f.write(translated)


