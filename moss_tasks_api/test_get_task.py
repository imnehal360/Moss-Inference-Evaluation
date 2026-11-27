
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load root .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

BASE_URL = "https://inference.moss.dev/v1"

# Existing task ID from test_create_task.py
TASK_ID = "task_f49fbf228d1c49999ec41508f279fe17"

# Authentication headers
headers = {
    "Authorization": f"Bearer {PROJECT_ID}:{PROJECT_KEY}"
}

# Get task details
response = requests.get(
    f"{BASE_URL}/tasks/{TASK_ID}",
    headers=headers
)

print("Status Code:", response.status_code)
print("\nResponse:")

try:
    data = response.json()
    print(data)

    if response.status_code == 200:
        print("\nTask retrieved successfully!")
        print("Task ID:", data.get("id"))
        print("Task Status:", data.get("status"))
        print("Result:", data.get("result"))
        print("Usage:", data.get("usage"))
        
except ValueError:
    print(response.text)
