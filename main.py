from fastapi import FastAPI
from app.routes import router
from app.config import init_db

app = FastAPI(title="Jean")

app.include_router(router)


@app.get("/")
async def home():
    return {"msg": "OK"}


init_db(app)
