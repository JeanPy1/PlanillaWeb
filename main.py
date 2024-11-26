from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.core.config import settings
from app.api.v1.routers import router

app = FastAPI(title="Jean")

app.include_router(router)

@app.get("/")
async def home():    
    return {"msg": "OK"}

register_tortoise(
    app,
    db_url = settings.DATABASE_URL,
    modules={"models": ["app.db.models"]},  # Usa el nombre del archivo donde están tus modelos (sin .py)
    generate_schemas = settings.GENERATE_SCHEMAS,
    add_exception_handlers=True,  # Maneja errores de la base de datos
)
