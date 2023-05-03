import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


prompt = """
the follow python run in jupyter well ,but how to run in python bash environment 
```
from IPython.display import display, HTML 
response = "<div>Hello</div>"
display(HTML(response))
``` 
"""
response = get_completion(prompt)
print(response)

