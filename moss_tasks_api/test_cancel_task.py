
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load root .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

BASE_URL = "https://inference.moss.dev/v1"

TASK_ID = "task_c891f8928c7940e1b1a85b768db95bee"

headers = {
    "Authorization": f"Bearer {PROJECT_ID}:{PROJECT_KEY}"
}

# Cancel task
response = requests.post(
    f"{BASE_URL}/tasks/{TASK_ID}/cancel",
    headers=headers
)

print("Status Code:", response.status_code)
print("\nResponse:")

try:
    data = response.json()
    print(data)

    if response.status_code == 200:
        print("\nCancellation request successful!")
        print("Task ID:", data.get("id"))
        print("Task Status:", data.get("status"))
        print("Cancel Requested:", data.get("cancel_requested"))

except ValueError:
    print(response.text)
