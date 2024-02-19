from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory storage using Python dictionary
students_db = {}


class Student:
    def __init__(self, id, name, age, sex, height):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


@app.post("/students/")
def create_student(student: Student):
    students_db[student.id] = student
    return {"message": "Student created successfully"}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]


@app.get("/students/")
def get_all_students():
    return students_db


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    students_db[student_id] = student
    return {"message": "Student updated successfully"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}
