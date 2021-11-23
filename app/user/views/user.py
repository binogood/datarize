from fastapi import APIRouter, Depends

from app.user.request.user import CreateUserRequest
from app.user.response.user import CreateUserResponse, GetUserResponse
from app.user.service.user import UserService

from core.fastapi.schemas.response import ExceptionResponseSchema

user_router = APIRouter()


@user_router.post(
    "",
    response_model=CreateUserResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create User"
)
async def create_user(request: CreateUserRequest):
    return await UserService().create_user(**request.dict())


@user_router.get(
    "/{user_id}",
    response_model=GetUserResponse,
    responses={"404": {"model":ExceptionResponseSchema}},
    summary="Get User"
)
async def get_user(user_id: int):
    return await UserService().get_user(user_id=user_id)