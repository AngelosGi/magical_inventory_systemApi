from fastapi import APIRouter

router = APIRouter()


@router.get('/')  # getAll
async def index():
    return {"message": "Welcome to my Magic Items inventory! "}
