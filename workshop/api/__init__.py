from fastapi import APIRouter
from .users import router as user_router
from .user_list import router as user_list_router

router = APIRouter()
router.include_router(user_router)
router.include_router(user_list_router)
