
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

# Create a new task
payload = {
    "goal": "Visit https://www.wikipedia.org and identify its main heading.",
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

create_response = requests.post(
    f"{BASE_URL}/tasks",
    headers=headers,
    json=payload
)

print("Create Status Code:", create_response.status_code)

if create_response.status_code != 202:
    print("Task creation failed:", create_response.text)
    exit()

task = create_response.json()
task_id = task.get("id")

print("Task ID:", task_id)
print("Initial Status:", task.get("status"))

# Immediately request cancellation
cancel_response = requests.post(
    f"{BASE_URL}/tasks/{task_id}/cancel",
    headers=headers
)

print("\nCancel Status Code:", cancel_response.status_code)

try:
    cancel_data = cancel_response.json()
    print("Cancellation Response:", cancel_data)

    if cancel_response.status_code == 200:
        print("\nReturned Task Status:", cancel_data.get("status"))
        print("Cancel Requested:", cancel_data.get("cancel_requested"))

except ValueError:
    print(cancel_response.text)
