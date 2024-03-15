import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ["OPENAI_API_KEY"]

# messages = [{"role": "user", "content": "What is the capital of New York?"}]
# try:
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         temperature=0,
#     )

#     print(response.choices[0].message["content"])
# except Exception as e:
#     print(e)
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    print("Response object:", response)
    return response.choices[0].message["content"]
# Example usage:
prompt = "Give me 10 most marketable programming languages"
completion = get_completion(prompt)
print(completion)