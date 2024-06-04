from pydantic import BaseModel
from fastapi import APIRouter
from services.magic_item_service import MagicItemService
from domain.magic_item import CreateItemRequest, MagicItemRead
from typing import List

router = APIRouter()


# @router.get('/')
# async def index():
#     return {"message": "Welcome to my Magic Items inventory! "}

@router.get("/all", response_model=List[MagicItemRead])
async def get_all_items():
    """
    Fetch all magical items.
    """
    all_items = MagicItemService.get_all_items()
    return all_items


@router.post("/create")
async def create_item(item_data: CreateItemRequest):
    """
    Create a new magical item with random values for weight, durability, and rarity.
    """
    # Convert Pydantic model to dictionary
    item_data_dict = item_data.dict()

    # Call the service to generate random values
    created_item = MagicItemService.generate_random_values(item_data_dict)
    return created_item
