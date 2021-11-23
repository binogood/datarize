from fastapi import APIRouter

from app.user.views import sub_router

router = APIRouter()
router.include_router(sub_router, prefix="/users", tags=["User"])

__all__ = ["router"]