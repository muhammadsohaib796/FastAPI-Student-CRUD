from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import json

app = FastAPI()


# =====================
# PYDANTIC MODEL
# =====================
class Student(BaseModel):
    name: str
    department: str
    gpa: float
    is_scholarship: bool
    semester: int = Field(ge=1, le=8)


# =====================
# Helper function
# =====================

def load_data():
    with open('students.json', 'r') as f:
        return json.load(f)

def save_data(data):
    with open('students.json', 'w') as f:
        return json.dump(data, f, indent=4)

# =====================
# Home
# =====================

@app.get('/')
def home():
    return {"message": "Wellcome to the Student API"}

# =====================
# GET ALL STUDENTS
# =====================

@app.get('/students')
def get_all_students():
    return load_data()

# =====================
# GET SINGLE STUDENT
# =====================

@app.get('/students/{roll}')
def get_student_by_roll(roll: str):
    data = load_data()
    if roll not in data:
        raise HTTPException(
                status_code=404,
                detail="Student not found"
            )
    return data[roll]


# =====================
# CREATE STUDENT
# =====================

@app.post('/students/{roll}')
def create_student(roll: str, student: Student):

    data = load_data()

    if roll in data:
        raise HTTPException(
            status_code=400,
            detail="Student Already Exists"
        )

    data[roll] = student.model_dump()
    save_data(data)

    return {
        "message": "Student Created Successfully",
        "student": data[roll]
    }


# =====================
# UPDATE STUDENT
# =====================

@app.put('/students/{roll}')
def update_student(roll: str, student: Student):

    data = load_data()

    if roll not in data:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    data[roll] = student.model_dump()
    save_data(data)

    return {
        "message": "Student updated Successfully",
        "student": data[roll]
    }


# =====================
# DELETE STUDENT
# =====================

@app.delete('/students/{roll}')
def deleted_student(roll: str):

    data = load_data()

    if roll not in data:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    deleted_student = data.pop(roll)

    save_data(data)
    return {
        "message": "Student Deleted Successfully",
        "student": deleted_student
    }   