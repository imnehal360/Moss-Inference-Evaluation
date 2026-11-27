
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from root .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

BASE_URL = "https://inference.moss.dev/v1"

# Authentication headers
headers = {
    "Authorization": f"Bearer {PROJECT_ID}:{PROJECT_KEY}",
    "Content-Type": "application/json"
}

# Task details
payload = {
    "goal": "Visit https://www.wikipedia.org and identify the main heading displayed on its homepage.",
    "environment": {
        "type": "browser"
    },
    "model": "moss-balanced",
    "effort": "medium",
    "limits": {
        "max_runtime_seconds": 600,
        "max_cost_usd": 2
    }
}

# Create task
response = requests.post(
    f"{BASE_URL}/tasks",
    headers=headers,
    json=payload
)

# Display response
print("Status Code:", response.status_code)
print("\nResponse:")

try:
    data = response.json()
    print(data)

    if response.status_code == 202:
        print("\nTask created successfully!")
        print("Task ID:", data.get("id"))
        print("Task Status:", data.get("status"))

except ValueError:
    print(response.text)
