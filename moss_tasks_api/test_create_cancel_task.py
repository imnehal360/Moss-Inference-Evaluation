
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load root .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

BASE_URL = "https://inference.moss.dev/v1"

headers = {
    "Authorization": f"Bearer {PROJECT_ID}:{PROJECT_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "goal": "Visit https://www.wikipedia.org and explore its different language editions. Identify at least five language editions and their corresponding links.",
    "environment": {
        "type": "browser"
    },
    "model": "moss-balanced",
    "effort": "high",
    "limits": {
        "max_runtime_seconds": 1200,
        "max_cost_usd": 2
    }
}

response = requests.post(
    f"{BASE_URL}/tasks",
    headers=headers,
    json=payload
)

print("Status Code:", response.status_code)
print("\nResponse:")

try:
    data = response.json()
    print(data)

    if response.status_code == 202:
        print("\nCancellation test task created!")
        print("Task ID:", data.get("id"))
        print("Task Status:", data.get("status"))

except ValueError:
    print(response.text)
