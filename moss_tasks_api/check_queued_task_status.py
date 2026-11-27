
import os
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

headers = {
    "Authorization": f"Bearer {os.getenv('MOSS_PROJECT_ID')}:{os.getenv('MOSS_PROJECT_KEY')}"
}

task_id = "task_a84020ec53d749f1bd90361f95d38414"
url = f"https://inference.moss.dev/v1/tasks/{task_id}"

for attempt in range(5):
    response = requests.get(url, headers=headers)

    print(f"\nCheck {attempt + 1}")
    print("HTTP Status:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        break

    data = response.json()
    print("Task Status:", data.get("status"))
    print("Cancel Requested:", data.get("cancel_requested"))

    if data.get("status") in ["cancelled", "completed", "failed"]:
        break

    time.sleep(5)
