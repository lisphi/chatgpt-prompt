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

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    print(str(response))
    return response.choices[0].message["content"]


# messages =  [  
# {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
# {'role':'user', 'content':'tell me a joke'},   
# {'role':'assistant', 'content':'Why did the chicken cross the road'},   
# {'role':'user', 'content':'I don\'t know'}  ]

# response = get_completion_from_messages(messages, temperature=1)
# print(response)


messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},    
{'role':'user', 'content':'Hi, my name is Isa'}  ]
response = get_completion_from_messages(messages, temperature=1)

print(response)