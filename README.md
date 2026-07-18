# FastAPI Student CRUD API

A simple CRUD API built with FastAPI to manage student records,
using JSON file storage and Pydantic for validation.

## Features
- GET all students
- GET a student by roll number
- POST (create) a student
- PUT (update) a student
- DELETE a student

## Tech Stack
- FastAPI
- Pydantic
- Python 3.x

## Setup
\`\`\`bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn pydantic_json_crud:app --reload
\`\`\`

## Notes
Started with `main.py` (basic CRUD, no validation), then built
`pydantic_json_crud.py` (added Pydantic models, Field validation,
and HTTPException error handling).

