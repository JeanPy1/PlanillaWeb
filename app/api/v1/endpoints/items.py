from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_items():    
    return [{"id":1,"item":"item1"},{"id":2,"item":"item2"}]

@router.post("/")
async def register_item(item:str):
    return {"id":3,"item":item}
