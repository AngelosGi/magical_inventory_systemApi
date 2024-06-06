from typing import List, Dict, Any, Optional
from repositories.magic_item_repository import MagicItemRepository
import random


class MagicItemService:

    @staticmethod
    def generate_random_values(item_data: dict) -> dict:
        """
        Generate random values for weight, durability, and rarity for a magic item.
        Args:
            item_data (dict): The data of the magic item.
        Returns:
            dict: The updated item data with generated random values.
        Raises:
            Exception: If an error occurs during the generation process.
        """
        try:
            item_data['weight'] = random.uniform(0.1, 10.0)
            item_data['durability'] = random.uniform(0.1, 0.9)
            item_data['rarity_value'] = random.uniform(0.0, 100.0)
            return MagicItemRepository.create_item(item_data)
        except Exception as e:
            raise Exception("Error generating random values: " + str(e))

    @staticmethod
    def update_item(item_id: int, update_data: dict) -> Optional[dict]:
        """
        Update an item in the database with the given item ID and update data.
        Args:
            item_id (int): The ID of the item to update.
            update_data (dict): A dictionary containing the updated data for the item.
        Returns:
            Optional[dict]: The updated item data if the update was successful, None otherwise.
        """
        try:
            update_data = {key: value for key, value in update_data.items() if value is not None}
            return MagicItemRepository.update_item(item_id, update_data)
        except Exception as e:
            raise Exception("Error updating item: " + str(e))

    @staticmethod
    def get_all_items() -> list[dict[Any, Any]]:
        """
        Get all magic items from the database.
        Returns:
            list[dict[Any, Any]]: A list of magic items.
        Raises:
            Exception: If an error occurs during the retrieval process.
        """
        try:
            return MagicItemRepository.get_all_items()
        except Exception as e:
            raise Exception("Error retrieving all items: " + str(e))

    @classmethod
    def get_item_by_id(cls, item_id: int) -> Optional[dict[Any, Any]]:
        """
        Get a magic item from the database by its ID.
        Args:
            item_id (int): The ID of the magic item.
        Returns:
            Optional[dict[Any, Any]]: The magic item if found, None otherwise.
        Raises:
            Exception: If an error occurs during the retrieval process.
        """
        try:
            item = MagicItemRepository.get_item_by_id(item_id)
            if item:
                item['id'] = item_id
            return item
        except Exception as e:
            raise Exception("Error retrieving item by ID: " + str(e))

    @staticmethod
    def search_items(search_criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Search for magic items based on specified criteria.
        """
        try:
            return MagicItemRepository.search_items(search_criteria)
        except Exception as e:
            raise Exception("Error searching items: " + str(e))

    @staticmethod
    def increase_stock(item_id: int, quantity: int) -> dict:
        """
        Increase the stock of a specific item.
        """
        try:
            return MagicItemRepository.update_stock(item_id, quantity, operation='increase')
        except Exception as e:
            raise Exception("Error increasing stock: " + str(e))

    @staticmethod
    def decrease_stock(item_id: int, quantity: int) -> dict:
        """
        Decrease the stock of a specific item.
        """
        try:
            return MagicItemRepository.update_stock(item_id, quantity, operation='decrease')
        except Exception as e:
            raise Exception("Error decreasing stock: " + str(e))

    @staticmethod
    def get_inventory_statistics() -> Dict[str, Any]:
        """
        Get inventory statistics.
        """
        try:
            all_items = MagicItemRepository.get_all_items()
            total_items = len(all_items)
            total_stock = sum(item['stock'] for item in all_items)
            total_value = sum(item['value'] * item['stock'] for item in all_items if item['value'] is not None)

            most_expensive_item = max(all_items, key=lambda x: x['value'], default=None)
            cheapest_item = min(all_items, key=lambda x: x['value'], default=None)
            most_stocked_item = max(all_items, key=lambda x: x['stock'], default=None)
            highest_level_item = max(all_items, key=lambda x: x['level'], default=None)

            statistics = {
                "total_items": total_items,
                "total_stock": total_stock,
                "total_value": total_value,
                "most_expensive_item": most_expensive_item,
                "cheapest_item": cheapest_item,
                "most_stocked_item": most_stocked_item,
                "highest_level_item": highest_level_item,
            }
            return statistics
        except Exception as e:
            raise Exception("Error calculating inventory statistics: " + str(e))

    @staticmethod
    def delete_item(item_id: int) -> Optional[dict]:
        """
        Delete an item from the database by its ID.
        Args:
            item_id (int): The ID of the item to delete.
        Returns:
            Optional[dict]: The deleted item data if deletion was successful, None otherwise.
        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            return MagicItemRepository.delete_item(item_id)
        except Exception as e:
            raise Exception("Error deleting item: " + str(e))

# create a sell method to "sell items"  (reduce stock by INT and add the value of items sold to a "wallet")
# create a buy option,
# create something to convert rarity to text, Common/Rare etc.
# create something like "use_item" or "test_item" with each use/test reduce durability in items or reduce stock in
# consumables (potions) in items, if the durability reaches <0 then reduce stock by 1.
