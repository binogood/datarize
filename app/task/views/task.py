from fastapi import APIRouter, Header

from app.task.request.task import CreateTaskRequest, UpdateTaskRequest
from app.task.response.task import (
    GetTaskResponse,
    AllGetTaskResponse,
    CreateTaskResponse,
    UpdateTaskResponse
)
from app.task.service.task import TaskService
from core.fastapi.schemas.response import ExceptionResponseSchema

task_router = APIRouter()


@task_router.post(
    "/create",
    response_model=CreateTaskResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create Task"
)
async def create_task(request: CreateTaskRequest, token: str = Header("Authorization")):
    return await TaskService().create_task(**request.dict(), token=token)


@task_router.put(
    "/update",
    response_model=UpdateTaskResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Task Update"
)
async def update_task(request: UpdateTaskRequest, token: str = Header("Authorization")):
    return await TaskService().update_task(**request.dict(), token=token)


@task_router.get(
    "/{task_id}",
    responses={"404": {"model": ExceptionResponseSchema}},
    summary="Task"
)
async def task_get(request: GetTaskResponse, token: str = Header("Authorization")):
    return await TaskService().get_task(**request.dict(), token=token)


@task_router.get(
    "/task_list",
    responses={"404": {"model": ExceptionResponseSchema}},
    summary="Task List"
)
async def task_list_get(request: AllGetTaskResponse, token: str = Header("Authorization")):
    return await TaskService().all_get_task(**request.dict(), token=token)