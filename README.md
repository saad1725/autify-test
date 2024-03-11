# autify-test
This the respository for Technical Assignment for the Senior Machine Learning Engineer, LLMs &amp; Prompt Engineering





FastAPI Application
Overview

This repository contains a FastAPI application that provides [brief description of your application].
Installation

    Clone the repository:

    bash

git clone <repository-url>

Install dependencies:

bash

    pip install -r requirements.txt

Usage
Running with Uvicorn

    Run the FastAPI application with Uvicorn:

    bash

    uvicorn main:app --reload

    The application will start running at http://localhost:8000.

    Access the API endpoints using a web browser or API client.

Running with Docker

    Build the Docker image:

    bash

docker build -t my-fastapi-app .

Run the Docker container:

bash

    docker run -d -p 8000:8000 my-fastapi-app

    The application will start running inside the Docker container and will be accessible at http://localhost:8000.

API Endpoints

    /: [Description of the root endpoint]
    /endpoint1: [Description of endpoint 1]
    /endpoint2: [Description of endpoint 2]
    ...


