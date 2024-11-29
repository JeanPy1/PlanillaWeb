from pydantic import BaseModel
from datetime import date


class UserSchema(BaseModel):

    name: str
    email: str
    username: str
    password: str
    created_at: date = date.today()

    class Config:
        from_attributes = True


class UserSchemaResponse(BaseModel):

    name: str
    email: str

    class Config:
        from_attributes = True
