
# Moss Inference API Evaluation

A hands-on technical evaluation of the **Moss Inference Platform**, focusing on its Inference API, Tasks API, developer experience, and API reliability.

This repository contains Python-based test scripts developed to explore and evaluate real-world API behavior, including inference requests, streaming responses, RAG functionality, asynchronous task execution, cancellation workflows, file management, and error handling.

## Overview

The evaluation covers three key areas:

- **Developer Portal:** Usability, documentation, configuration, and overall developer experience.
- **Inference API:** Model inference, streaming, RAG functionality, and error handling.
- **Tasks API:** Asynchronous task creation, status tracking, cancellation, file downloads, and expiration behavior.

## Tech Stack

- Python 3
- REST APIs
- OpenAI Python SDK
- Requests
- python-dotenv
- JSON

## Project Structure

```text
Moss/
│
├── moss_inference_api/
│   ├── test_error.py
│   ├── test_inference.py
│   ├── test_rag.py
│   └── test_streaming.py
│
├── moss_tasks_api/
│   ├── check_queued_task_status.py
│   ├── test_cancel_queued_task.py
│   ├── test_cancel_running_task.py
│   ├── test_cancel_task.py
│   ├── test_create_cancel_task.py
│   ├── test_create_task.py
│   ├── test_download_file.py
│   ├── test_error_handling.py
│   ├── test_file_expiration.py
│   ├── test_get_task.py
│   └── test_list_files.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9+
- A Moss Inference project with valid API credentials
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/imnehal360/Moss-Inference-Evaluation.git
cd Moss
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory using `.env.example` as a reference.

```env
MOSS_PROJECT_ID=your_project_id
MOSS_PROJECT_KEY=your_project_key
```

Use the actual variable names required by the individual test scripts.

**Important:** Never commit API keys, project credentials, or other sensitive information.

## Test Coverage

### 1. Inference API

Located in `moss_inference_api/`.

| Test Script | Purpose |
|---|---|
| `test_inference.py` | Basic inference requests and response handling |
| `test_error.py` | API error handling and invalid request scenarios |
| `test_rag.py` | Retrieval-Augmented Generation functionality |
| `test_streaming.py` | Streaming response behavior |

### 2. Tasks API

Located in `moss_tasks_api/`.

| Test Script | Purpose |
|---|---|
| `test_create_task.py` | Asynchronous task creation |
| `test_get_task.py` | Retrieving task details |
| `check_queued_task_status.py` | Checking queued task status |
| `test_cancel_task.py` | Task cancellation behavior |
| `test_cancel_queued_task.py` | Cancellation of queued tasks |
| `test_cancel_running_task.py` | Cancellation of running tasks |
| `test_create_cancel_task.py` | Task creation followed by cancellation |
| `test_error_handling.py` | Error handling and invalid API operations |
| `test_download_file.py` | Downloading generated task files |
| `test_list_files.py` | Listing available files |
| `test_file_expiration.py` | File expiration behavior |

## Running the Tests

Execute individual scripts from the project root.

**Inference API:**

```bash
python moss_inference_api/test_inference.py
python moss_inference_api/test_error.py
python moss_inference_api/test_rag.py
python moss_inference_api/test_streaming.py
```

**Tasks API:**

```bash
python moss_tasks_api/test_create_task.py
python moss_tasks_api/test_get_task.py
python moss_tasks_api/check_queued_task_status.py
python moss_tasks_api/test_cancel_task.py
python moss_tasks_api/test_cancel_queued_task.py
python moss_tasks_api/test_cancel_running_task.py
python moss_tasks_api/test_create_cancel_task.py
python moss_tasks_api/test_error_handling.py
python moss_tasks_api/test_download_file.py
python moss_tasks_api/test_list_files.py
python moss_tasks_api/test_file_expiration.py
```

Some tests may depend on existing task IDs, task states, or previously generated files. Configure the required inputs before running them.

## Evaluation Focus

The evaluation examines:

- API usability and developer experience.
- Inference request and response behavior.
- Streaming and RAG functionality.
- Error responses and edge cases.
- Asynchronous task lifecycle management.
- Task cancellation under different execution states.
- File retrieval, listing, and expiration behavior.

## Security

- Credentials are managed through environment variables.
- `.env` files are excluded from version control.
- Downloaded API artifacts are excluded from the repository.
- No production credentials should be committed.

## Purpose

This project demonstrates practical API exploration, integration testing, edge-case analysis, and hands-on evaluation of the Moss Inference Platform.

---

**Python | REST APIs | API Testing | Moss Inference**
