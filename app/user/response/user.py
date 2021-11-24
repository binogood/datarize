from datetime import datetime

from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    id: int
    email: str
    password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "email": "test@gmail.com",
                "password": "11223344",
                "created_at": "2021-11-11T07:50:54.289Z",
                "updated_at": "2021-11-11T07:50:54.289Z",
            }
        }

