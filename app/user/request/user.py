from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"email": "test@gmail.com","password": "11223344"}}


class LoginUserRequest(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {"email": "test@gmail.com","password": "11223344"}}