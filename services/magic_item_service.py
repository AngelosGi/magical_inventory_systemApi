from typing import List, Dict, Any

from repositories.magic_item_repository import MagicItemRepository
import random


class MagicItemService:

    @staticmethod
    def generate_random_values(item_data: dict) -> dict:
        # Generate random values for weight, durability, and rarity
        item_data['weight'] = random.uniform(0.1, 10.0)
        item_data['durability'] = random.uniform(0.1, 0.9)
        item_data['rarity_value'] = random.uniform(0.0, 100.0)

        # Call the repository to create the item in the database
        return MagicItemRepository.create_item(item_data)

    @staticmethod
    def get_all_items() -> list[dict[Any, Any]]:
        # Call the repository to get all items from the database
        return MagicItemRepository.get_all_items()

# create something to convert rarity to Common Rare etc.
# create something like test_item to lower the durability after each test.
# create something that when the durability reaches below 0 to be "destroyed"
