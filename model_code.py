from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv('BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY')
)

messages = [
    {"role": "user", "content": "Here are the refined AI agents:\n\nTeam 1: Design and Production Line Specialists..."},
    {"role": "user", "content": "Agent Alpha: Expert in designing production lines for automotive manufacturing..."},
    {"role": "user", "content": "Agent Bravo: Specializes in designing production lines for aerospace engineering..."},
    {"role": "user", "content": "Agent Charlie: Focuses on designing production lines for consumer goods manufacturing..."},
    {"role": "user", "content": "Agent Delta: Expert in designing production lines for pharmaceutical manufacturing..."}
]

completion = client.chat.completions.create(
    model="meta/llama-3.3-70b-instruct",
    messages=messages,
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
    stream=True
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end='')
