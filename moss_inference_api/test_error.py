
import os
from dotenv import load_dotenv
from openai import OpenAI, APIStatusError

from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")



client = OpenAI(
    base_url="https://inference.moss.dev/v1",
    api_key=f"{os.getenv('MOSS_PROJECT_ID')}:{os.getenv('MOSS_PROJECT_KEY')}"
)

try:
    response = client.responses.create(
        model="Nehal-llm",
        input="Explain RAG in simple words."
    )

    print(response)

except APIStatusError as e:
    print("Error occurred!")
    print("Status Code:", e.status_code)
    print("Error Details:", e.response.text)

except Exception as e:
    print("Unexpected Error:", str(e))
