from fastapi import APIRouter
from model.studentModel import Student
from controller.studentcontroller import add_student, get_students, get_student, update_student, delete_student

srouter = APIRouter()

@srouter.post("/students")
def create_student(student: Student):
    return add_student(student)

@srouter.get("/students")
def read_students(course: str = None):
    return get_students(course)

@srouter.get("/student/{id}")
def read_student(id: int):
    return get_student(id)

@srouter.put("/students/{id}")
def update_student_data(id: int, student: Student):
    return update_student(id, student)


@srouter.delete("/students/{id}")
def delete_student_data(id: int):
    return delete_student(id)