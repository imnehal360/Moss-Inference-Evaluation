
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

# Create a fresh task
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

# Step 1: Create task
create_response = requests.post(
    f"{BASE_URL}/tasks",
    headers=headers,
    json=payload
)

print("CREATE STATUS:", create_response.status_code)
print(create_response.text)

if create_response.status_code != 202:
    print("Task creation failed. Cannot continue.")
    exit()

task_data = create_response.json()
task_id = task_data.get("id")

print("\nCreated Task ID:", task_id)
print("Initial Task Status:", task_data.get("status"))

# Step 2: Immediately request cancellation
cancel_response = requests.post(
    f"{BASE_URL}/tasks/{task_id}/cancel",
    headers=headers
)

print("\nCANCEL STATUS:", cancel_response.status_code)
print(cancel_response.text)

# Step 3: Retrieve final task status
get_response = requests.get(
    f"{BASE_URL}/tasks/{task_id}",
    headers=headers
)

print("\nRETRIEVE STATUS:", get_response.status_code)
print(get_response.text)

if get_response.status_code == 200:
    final_data = get_response.json()
    print("\nFinal Task Status:", final_data.get("status"))
