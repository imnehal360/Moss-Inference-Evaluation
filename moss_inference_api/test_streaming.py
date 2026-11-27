
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = OpenAI(
    base_url="https://inference.moss.dev/v1",
    api_key=f"{os.getenv('MOSS_PROJECT_ID')}:{os.getenv('MOSS_PROJECT_KEY')}"
)

start_time = time.time()
first_token_time = None

stream = client.responses.create(
    model="moss/fastlane-1",
    input="Explain how RAG works in simple words.",
    stream=True
)

print("Streaming response:\n")

for event in stream:
    if event.type == "response.output_text.delta":
        if first_token_time is None:
            first_token_time = time.time()

        print(event.delta, end="", flush=True)

end_time = time.time()

print("\n\n--- Metrics ---")

if first_token_time:
    print("Time to first token:",
          round(first_token_time - start_time, 2), "seconds")

print("Total response time:",
      round(end_time - start_time, 2), "seconds")
