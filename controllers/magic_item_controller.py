from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from services.magic_item_service import MagicItemService
from domain.magic_item import CreateItemRequest, MagicItemRead, MagicItemUpdate
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
    try:
        all_items = MagicItemService.get_all_items()
        return all_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving all items: {str(e)}")


@router.get("/{item_id}", response_model=MagicItemRead)
async def get_item_by_id(item_id: int):
    """
    Fetch a magic item by its ID.
    """
    try:
        item = MagicItemService.get_item_by_id(item_id)
        if item:
            return item
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving item by ID: {str(e)}")


@router.post("/create")
async def create_item(item_data: CreateItemRequest):
    """
    Create a new magic item with random values for weight, durability, and rarity.
    """
    try:
        # Convert Pydantic model to dictionary
        item_data_dict = item_data.dict()

        # Call the service to create the item and generate random values
        created_item = MagicItemService.generate_random_values(item_data_dict)
        return created_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating item: {str(e)}")


@router.put("/update_item/{item_id}")
async def update_item(item_id: int, update_data: MagicItemUpdate):
    """
    Create a new magic item with random values for weight, durability, and rarity.
    """
    try:
        update_data_dict = update_data.dict(exclude_unset=True)
        updated_item = MagicItemService.update_item(item_id, update_data_dict)
        if updated_item:
            return updated_item
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating item: {str(e)}")


@router.delete("/delete/{item_id}")
async def delete_item(item_id: int):
    """
    Delete a magic item by its ID.
    """
    try:
        deleted_item = MagicItemService.delete_item(item_id)
        if deleted_item:
            return {"message": "Item deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting item: {str(e)}")
