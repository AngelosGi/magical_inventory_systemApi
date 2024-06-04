from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from services.magic_item_service import MagicItemService
from domain.magic_item import CreateItemRequest, MagicItemRead
from typing import List

router = APIRouter()


@router.get("/")
async def root():
    """
    Welcome message.
    """
    return {"message": "Welcome to my Inventory, all things magical!"}


@router.get("/all", response_model=List[MagicItemRead])
async def get_all_items():
    """
    Fetch all magic items.
    """
    all_items = MagicItemService.get_all_items()
    return all_items


@router.get("/{item_id}", response_model=MagicItemRead)
async def get_item_by_id(item_id: int):
    """
    Fetch a magic item by its ID.
    """
    item = MagicItemService.get_item_by_id(item_id)
    if item:
        return item


@router.post("/create")
async def create_item(item_data: CreateItemRequest):
    """
    Create a new magic item with random values for weight, durability, and rarity.
    """
    # Convert Pydantic model to dictionary
    item_data_dict = item_data.dict()

    # Call the service to "check item" generate random values
    created_item = MagicItemService.generate_random_values(item_data_dict)
    return created_item
