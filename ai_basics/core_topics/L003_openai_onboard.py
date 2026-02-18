from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from os import environ as env

load_dotenv(find_dotenv())

client = OpenAI(
    api_key=env.get("GEMINI_API_KEY"),
    base_url=env.get("GEMINI_API_URL"),
)

# noinspection PyTypeChecker
response = client.chat.completions.create(
    model=env.get("GEMINI_MODEL"),
    messages=[
        {
            "role": "user",
            "content": "Hey, I'm Adam Jensen. Available for chat ?"
        },
    ]
)

print(response.choices[0].message.content)

