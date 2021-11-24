from fastapi import APIRouter

from app.task.views import sub_router

task_router = APIRouter()
task_router.include_router(sub_router, prefix="/task", tags=["Task"])

__all__ = ["task_router"]
