from openai import OpenAI

client = OpenAI()

response = client.responses.create(
  model="gpt-4o-mini",
  input="Quem é o CEO da openai?",
  store=True,
)

print(response.output_text);
