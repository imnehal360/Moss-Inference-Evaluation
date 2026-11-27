
import os
from dotenv import load_dotenv
from openai import OpenAI

from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = OpenAI(
    base_url="https://inference.moss.dev/v1",
    api_key=f"{os.getenv('MOSS_PROJECT_ID')}:{os.getenv('MOSS_PROJECT_KEY')}"
)

response = client.responses.create(
    model="moss/fastlane-1",
    input="What was my JEE Advanced rank?",
    tools=[
        {
            "type": "moss_search",
            "indexes": ["my-documents"],
            "top_k": 5,
            "description": "Search my uploaded documents and use the retrieved information to answer questions."
        }
    ],
    tool_choice={
        "type": "function",
        "name": "moss_search"
    }
)

print("\nResponse:\n")
print(response.output_text)

print("\n Metrics:")
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
