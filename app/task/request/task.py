from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "task 생성",
            }
        }


class UpdateTaskStatusRequest(BaseModel):
    completed: bool

    class Config:
        schema_ext = {
            "example": {
                "completed": True
            }
        }
