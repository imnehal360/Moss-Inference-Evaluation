
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

BASE_URL = "https://inference.moss.dev/v1"

headers = {
    "Authorization": f"Bearer {PROJECT_ID}:{PROJECT_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "goal": "Visit Wikipedia and identify its main heading.",
    "environment": {"type": "browser"},
    "model": "moss-balanced",
    "effort": "medium",
    "limits": {
        "max_runtime_seconds": 600,
        "max_cost_usd": 2
    }
}


# TEST 1: Invalid model
def test_invalid_model():
    print("\nTEST 1: INVALID MODEL:")

    data = payload.copy()
    data["model"] = "invalid-model-nehal"

    response = requests.post(
        f"{BASE_URL}/tasks",
        headers=headers,
        json=data
    )

    print("HTTP Status:", response.status_code)
    print("Response:", response.text)


# TEST 2: Invalid credentials
def test_invalid_credentials():
    print("\nTEST 2: INVALID CREDENTIALS:")

    bad_headers = {
        "Authorization": "Bearer invalid:invalid",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{BASE_URL}/tasks",
        headers=bad_headers,
        json=payload
    )

    print("HTTP Status:", response.status_code)
    print("Response:", response.text)


# TEST 3: Nonexistent task
def test_nonexistent_task():
    print("\nTEST 3: NONEXISTENT TASK:")

    fake_task_id = "task_00000000000000000000000000000000"

    response = requests.get(
        f"{BASE_URL}/tasks/{fake_task_id}",
        headers=headers
    )

    print("HTTP Status:", response.status_code)
    print("Response:", response.text)


# TEST 4: Premature file access

def test_premature_file_access():
    print("\nTEST 4: PREMATURE FILE ACCESS:")

    # Create a fresh task
    response = requests.post(
        f"{BASE_URL}/tasks",
        headers=headers,
        json=payload
    )

    print("Task Creation HTTP Status:", response.status_code)

    if response.status_code != 202:
        print("Task creation failed:", response.text)
        return

    task_id = response.json().get("id")
    print("Created Task ID:", task_id)
    print("Initial Status:", response.json().get("status"))

    # Check its current status
    task_response = requests.get(
        f"{BASE_URL}/tasks/{task_id}",
        headers=headers
    )

    if task_response.status_code != 200:
        print("Task retrieval failed:", task_response.text)
        return

    task_status = task_response.json().get("status")
    print("Current Status:", task_status)

    # Attempt file access while task is not completed
    if task_status in ["queued", "running"]:
        file_path = (
            "screenshots/agent/"
            "ses_de46dbf8dffeSkAl76nNEXq8FD-1795758906749-000.png"
        )

        file_response = requests.get(
            f"{BASE_URL}/tasks/{task_id}/files/{file_path}",
            headers=headers
        )

        print("File Access HTTP Status:", file_response.status_code)
        print("File Access Response:", file_response.text[:1000])

    else:
        print("Task completed too quickly.")
        print("Premature file access could not be tested.")


# Run all tests
if __name__ == "__main__":
    test_invalid_model()
    test_invalid_credentials()
    test_nonexistent_task()
    test_premature_file_access()
