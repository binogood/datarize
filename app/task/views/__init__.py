from fastapi import APIRouter

from .task import task_router

sub_router = APIRouter()
sub_router.include_router(task_router, prefix="", tags=["Task"])

__all__ = ["sub_router"]