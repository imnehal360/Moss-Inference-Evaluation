
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")




project_id = os.getenv("MOSS_PROJECT_ID")
project_key = os.getenv("MOSS_PROJECT_KEY")

if not project_id or not project_key:
    raise ValueError("Missing Moss API credentials in .env")

# Initialize Moss client
client = OpenAI(
    base_url="https://inference.moss.dev/v1",
    api_key=f"{project_id}:{project_key}"
)

# Send inference request
start_time = time.time()

response = client.responses.create(
    model="moss/fastlane-1",
    input="Explain what a LLM is in simple words."
)

end_time = time.time()

# Display results---------

print("\nMoss Inference Result\n")
print("Model:", response.model)
print("Response:")

for item in response.output:
    if item.type == "message":
        for content in item.content:
            if content.type == "output_text":
                print(content.text)

print("\nResponse Time:", round(end_time - start_time, 2), "seconds")
print("Token Usage:", response.usage)
