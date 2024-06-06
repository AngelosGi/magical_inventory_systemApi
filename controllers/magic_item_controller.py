from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from services.magic_item_service import MagicItemService
from domain.magic_item import CreateItemRequest, MagicItemRead, MagicItemUpdate
from typing import List, Dict, Any, Union, Optional

router = APIRouter()


@router.get("/")
async def root():
    """
    Welcome message.
    """
    return {"message": "Welcome to my Inventory, all things magical!"}, {"GitHub plug": "https://github.com/AngelosGi"
                                                                                        "/magical_inventory_systemApi"}


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


@router.get("/statistics", response_model=Dict[str, Any])
async def get_inventory_statistics():
    """
    Get inventory statistics.
    """
    try:
        statistics = MagicItemService.get_inventory_statistics()
        return statistics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search", response_model=List[MagicItemRead])
async def search_items(
        name: Optional[str] = None,
        category: Optional[str] = None,
        type: Optional[str] = None,
        min_level: Optional[int] = None,
        max_level: Optional[int] = None,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None,
        min_stock: Optional[int] = None,
        max_stock: Optional[int] = None
):
    """
    Search for magic items based on specified criteria.
    """
    try:
        search_criteria = {}

        if name:
            search_criteria['name'] = name
        if category:
            search_criteria['category'] = category
        if type:
            search_criteria['type'] = type
        if min_level is not None:
            search_criteria['level__gte'] = min_level
        if max_level is not None:
            search_criteria['level__lte'] = max_level
        if min_value is not None:
            search_criteria['value__gte'] = min_value
        if max_value is not None:
            search_criteria['value__lte'] = max_value
        if min_stock is not None:
            search_criteria['stock__gte'] = min_stock
        if max_stock is not None:
            search_criteria['stock__lte'] = max_stock
        # add later min/max weight, durability, rarity search criteria

        matched_items = MagicItemService.search_items(search_criteria)
        return matched_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching items: {str(e)}")


# if i want to add search criteria from magic_item.py (it changes to POST request)
# @router.post("/search", response_model=List[MagicItemRead])
# async def search_items(search_criteria: SearchCriteria):
#     """
#     Search for magic items based on specified criteria.
#     """
#     try:
#         matched_items = MagicItemService.search_items(search_criteria.dict())
#         return matched_items
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error searching items: {str(e)}")


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
async def create_item(item_data: Union[CreateItemRequest, List[CreateItemRequest]]):
    """
    Create new magic items with random values for weight, durability, and rarity.
    Can add single item or a list of items
    """
    try:
        # If a single item is provided, convert it to a list with one item
        if isinstance(item_data, CreateItemRequest):
            item_data = [item_data]

        created_items = []
        for data in item_data:
            # Convert Pydantic model to dictionary
            item_data_dict = data.dict()

            # Call the service to create the item and generate random values
            created_item = MagicItemService.generate_random_values(item_data_dict)
            created_items.append(created_item)

        # If only one item was provided, return it instead of a list
        if len(created_items) == 1:
            return created_items[0]
        else:
            return created_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating item: {str(e)}")


@router.post("/{item_id}/increase_stock")
async def increase_stock(item_id: int, quantity: int):
    """
    Increase the stock of a specific item (id).
    """
    try:
        updated_item = MagicItemService.increase_stock(item_id, quantity)
        if updated_item:
            return updated_item
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error increasing stock: {str(e)}")


@router.post("/{item_id}/decrease_stock")
async def decrease_stock(item_id: int, quantity: int):
    """
    decrease the stock of a specific item (id).
    """
    try:
        updated_item = MagicItemService.decrease_stock(item_id, quantity)
        if updated_item:
            return updated_item
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error decreasing stock: {str(e)}")


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
