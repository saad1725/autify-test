# autify-test
This the respository for Technical Assignment for the Senior Machine Learning Engineer, LLMs &amp; Prompt Engineering





FastAPI Application
Overview

This repository contains a FastAPI application that provides access to the facebook LLM for coding known as codeLama-7b-hf.
Installation

    Clone the repository: git clone https://github.com/saad1725/autify-test.git

    
Python version 3.11.8


Install dependencies:


    pip install -r requirements.txt

Usage
Running with Uvicorn


    uvicorn main:app --reload
    
The application will start running at http://localhost:8000.

Access the API endpoints using a web browser or API client.

Running with Docker

    Build the Docker image: docker build -f codelama-fastapi.Dockerfile -t my-fastapi-app .




Run the Docker container:



    docker run -d -p 8000:8000 my-fastapi-app

    The application will start running inside the Docker container and will be accessible at http://localhost:8000.






