

# Autify Test

This repository contains the  FastAPI application that provides access to the Facebook LLM (Large Language Model) for coding, known as `codeLama-7b-hf`.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/saad1725/autify-test.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure you have Python version 3.11.8 installed.

## Usage

### Running with Uvicorn

You can run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will start running at [http://localhost:8000](http://localhost:8000). You can access the API endpoints using a web browser or API client.

### Running with Docker

Alternatively, you can run the application with Docker:

1. Build the Docker image:

    ```bash
    docker build -f codelama-fastapi.Dockerfile -t my-fastapi-app .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 my-fastapi-app
    ```

The application will start running inside the Docker container and will be accessible at [http://localhost:8000](http://localhost:8000).

## Feedback Logging

The feedback log file can be used to improve the model for future generations. The information saved in the file is formatted for easy analysis and refinement of the model.

---
