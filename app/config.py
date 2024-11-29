from pydantic_settings import BaseSettings
from tortoise.contrib.fastapi import register_tortoise


class Settings(BaseSettings):

    PROJECT_NAME: str
    DATABASE_URL: str
    ENVIRONMENT: str
    GENERATE_SCHEMAS: bool
    SECRET_KEY: str

    class Config:

        env_file = ".env"


settings = Settings()


def init_db(app):
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": ["app.models.user_model"]},
        generate_schemas=settings.GENERATE_SCHEMAS,
        add_exception_handlers=True,
    )
