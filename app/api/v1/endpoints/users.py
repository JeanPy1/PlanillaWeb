from fastapi import APIRouter
from app.db.models import Users

router = APIRouter()

@router.get("/")
async def list_users():
    users = await Users.all()
    return users

@router.post("/")
async def create_user(name: str):
    user = await Users.create(name=name)
    return {"id":user.id, "name":user.name}