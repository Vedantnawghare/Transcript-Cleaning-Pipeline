# Transcript Cleaning Pipeline

## Overview

Transcript Cleaning Pipeline is an NLP-based application designed to improve transcript quality before evaluation.

The system removes unnecessary filler words, normalizes text, preserves technical terminology, handles acronyms, and provides a clean readable transcript through a FastAPI REST API.

---

## Features

- Remove filler words
  - umm
  - uh
  - like
  - basically

- Text normalization

- Automatic punctuation improvement

- Technical terminology preservation

- Acronym handling

- REST API using FastAPI

- Request validation

- Logging support

- Unit and API testing

- Docker container support

---

## Project Structure
Transcript-Cleaning-Pipeline
│
├── app
│ ├── main.py
│ ├── cleaner.py
│ ├── normalizer.py
│ └── filler_remover.py
│
├── tests
│ ├── test_cleaner.py
│ └── test_api.py
│
├── configs
│ └── technical_terms.json
│
├── logs
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Vedantnawghare/Transcript-Cleaning-Pipeline.git
Move into project:

cd Transcript-Cleaning-Pipeline
Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Running Application

Start FastAPI server:

uvicorn app.main:app --reload

Application runs at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
API Usage
Endpoint
POST /clean
Input
{
 "text":"umm i worked on python and docker"
}
Output
{
 "cleaned_text":"I worked on Python and Docker."
}
Running Tests

Run:

pytest

Expected:

4 passed
Docker Usage

Build Docker image:

docker build -t transcript-cleaner .

Run container:

docker run -p 8000:8000 transcript-cleaner

API will be available at:

http://localhost:8000
Technologies Used
Python
FastAPI
spaCy
Pytest
Docker
Git
Future Improvements
AI-based grammar correction
Better punctuation restoration
Multi-language transcript support
Cloud deployment
CI/CD pipeline