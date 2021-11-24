from datetime import datetime

from pydantic import BaseModel


class CreateTaskResponse(BaseModel):
    id: int
    user_id: int
    name: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "user_id": 1,
                "name": "TaskName",
                "completed": False,
                "created_at": "2021-11-11T07:50:54.289Z",
                "updated_at": "2021-11-11T07:50:54.289Z",
            }
        }


class GetTaskResponse(BaseModel):
    id: int
    name: str
    completed: bool

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "TaskName",
                "completed": False,
            }
        }


class AllGetTaskResponse(BaseModel):
    id: int
    name: str
    completed: bool

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "TaskName",
                "completed": False,
            }
        }


class UpdateTaskResponse(BaseModel):
    id: int
    name: str
    completed: bool

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "TaskName",
                "completed": True,
            }
        }