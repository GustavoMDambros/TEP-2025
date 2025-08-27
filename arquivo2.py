
from groq import Groq

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Quem criou o Groq?",
        }
    ],
    model="openai/gpt-oss-20b",
    stream=False,
)

print(chat_completion.choices[0].message.content)
