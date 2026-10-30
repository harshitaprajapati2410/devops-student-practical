from pydantic import BaseModel, Field

class Student(BaseModel):
    id: int
    name: str
    course: str
    marks: float = Field(..., ge=0, le=100)