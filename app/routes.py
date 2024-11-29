from fastapi import APIRouter
from app.routers import items, user_route

router = APIRouter()

router.include_router(items.router, prefix="/items", tags=["Items"])
router.include_router(user_route.router, prefix="/users", tags=["Users"])
