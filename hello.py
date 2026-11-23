

from dotenv import load_dotenv
import anthropic

load_dotenv()  # reads ANTHROPIC_API_KEY from .env

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=300,
    messages=[
        {"role": "user", "content": "In two sentences, what is RAG in AI?"}
    ],
)

print(response.content[0].text)
print(response.usage)