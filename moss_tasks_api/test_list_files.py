
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load root .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

BASE_URL = "https://inference.moss.dev/v1"

# Previously completed Wikipedia task
TASK_ID = "task_ffaf1e0ad50d4dfea782758683d4d9ef"

headers = {
    "Authorization": f"Bearer {PROJECT_ID}:{PROJECT_KEY}"
}

# List task files
response = requests.get(
    f"{BASE_URL}/tasks/{TASK_ID}/files",
    headers=headers
)

print("Status Code:", response.status_code)
print("\nResponse:")

try:
    data = response.json()
    print(data)

    if response.status_code == 200:
        print("\nFiles retrieved successfully!")

        for file in data.get("data", []):
            print("File Path:", file.get("path"))
            print("File Size:", file.get("bytes"), "bytes")

except ValueError:
    print(response.text)
