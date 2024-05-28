from pydantic import BaseModel
from fastapi import APIRouter
from services.magic_item_service import MagicItemService
from domain.magic_item import CreateItemRequest

router = APIRouter()


# @router.get('/')  # getAll
# async def index():
#     return {"message": "Welcome to my Magic Items inventory! "}


@router.post("/create_item")
async def create_item(item_data: CreateItemRequest):
    """
    Create a new magical item with random values for weight, durability, and rarity.
    """
    # Convert Pydantic model to dictionary
    item_data_dict = item_data.dict()

    # Call the service to create the item
    created_item = MagicItemService.create_random_item(item_data_dict)
    return created_item
