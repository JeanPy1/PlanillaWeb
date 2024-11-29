from fastapi import APIRouter
from app.models.user_model import UserModel
from app.schemas.user_schema import UserSchema, UserSchemaResponse
from typing import List

router = APIRouter()


@router.get("/", response_model=List[UserSchemaResponse])
async def list_users():

    users = await UserModel.all()
    return users


@router.post("/", response_model=UserSchemaResponse)
async def create_user(user: UserSchema):

    user_dict = user.model_dump()
    new_user = await UserModel.create(**user_dict)

    return new_user
