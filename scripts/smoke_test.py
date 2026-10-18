import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
model = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

response = client.models.generate_content(
    model=model,
    contents="In one sentence, what is a p-value?",
)

print(response.text)
print("model:", model)
usage = response.usage_metadata
print("input tokens:", usage.prompt_token_count)
print("output tokens:", usage.candidates_token_count)
