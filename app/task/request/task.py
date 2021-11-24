from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    name: str

    class Config:
        schema_extra = {"example": {"name": "task 생성",}}


class UpdateTaskRequest(BaseModel):
    name: str
    completed: bool

    class Config:
        schema_ext = {"example": {"name": "task 변경","completed": True,}}
