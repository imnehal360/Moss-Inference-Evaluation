
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

BASE_URL = "https://inference.moss.dev/v1"

TASK_ID = "task_ffaf1e0ad50d4dfea782758683d4d9ef"

headers = {
    "Authorization": f"Bearer {PROJECT_ID}:{PROJECT_KEY}"
}

# Retrieve task metadata
response = requests.get(
    f"{BASE_URL}/tasks/{TASK_ID}",
    headers=headers
)

print("HTTP Status:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Task Status:", data.get("status"))
    print("Files Expire At:", data.get("files_expire_at"))
    print("Content Expires At:", data.get("content_expires_at"))
else:
    print(response.text)
