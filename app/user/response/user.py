from datetime import datetime

from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    id: int
    email: str
    password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "email": "test@gmail.com",
                "password": "11223344"
            }
        }


class GetUserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "email": "test@gmail.com",
            }
        }
