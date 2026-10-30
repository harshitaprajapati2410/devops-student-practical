from model.studentModel import Student
from fastapi import HTTPException

students = []

def add_student(student: Student):
    students.append(student)
    return student

def get_students(course: str = None):
    if course:
        return [
            student for student in students
            if student.course.lower() == course.lower()
        ]

    return students

def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student

    raise HTTPException(status_code=404, detail="Student not found")


def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")
