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
            raise e

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
            raise e

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
            raise e

# create something to convert rarity to text, Common/Rare etc.
# create something like use_item or test_item
# with each use/test reduce durability in items or reduce stock in consumables (potions)
# in items, if the durability reaches <0 then reduce stock by 1
