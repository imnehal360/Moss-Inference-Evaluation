
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load root .env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")

BASE_URL = "https://inference.moss.dev/v1"

TASK_ID = "task_ffaf1e0ad50d4dfea782758683d4d9ef"

FILE_PATH = "screenshots/agent/ses_de46dbf8dffeSkAl76nNEXq8FD-1795758906749-000.png"

headers = {
    "Authorization": f"Bearer {PROJECT_ID}:{PROJECT_KEY}"
}

# Download task file
response = requests.get(
    f"{BASE_URL}/tasks/{TASK_ID}/files/{FILE_PATH}",
    headers=headers
)

print("Status Code:", response.status_code)

if response.status_code == 200:

    # Create downloads directory
    download_dir = Path(__file__).parent / "downloads"
    download_dir.mkdir(exist_ok=True)

    # Save downloaded file
    file_name = Path(FILE_PATH).name
    file_path = download_dir / file_name

    with open(file_path, "wb") as file:
        file.write(response.content)

    print("\nFile downloaded successfully!")
    print("File Name:", file_name)
    print("File Size:", len(response.content), "bytes")
    print("Saved Location:", file_path)

else:
    print("\nDownload failed!")
    print("Response:", response.text)
