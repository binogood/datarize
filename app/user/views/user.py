from fastapi import APIRouter, Depends

from app.user.request.user import CreateUserRequest, LoginUserRequest
from app.user.response.user import CreateUserResponse, LoginUserResponse
from app.user.service.user import UserService

from core.fastapi.schemas.response import ExceptionResponseSchema

user_router = APIRouter()


@user_router.post(
    "/create",
    response_model=CreateUserResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create User",
)
async def create_user(request: CreateUserRequest):
    return await UserService().create_user(**request.dict())


@user_router.post(
    "/login",
    response_model=LoginUserResponse,
    responses={"404": {"model": ExceptionResponseSchema}},
    summary="Login User",
)
async def login_user(request: LoginUserRequest):
    return await UserService().login_user(**request.dict())
