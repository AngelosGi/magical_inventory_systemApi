from repositories.magic_item_repository import MagicItemRepository
import random


class MagicItemService:
    @staticmethod
    def create_random_item(item_data: dict) -> dict:
        # Generate random values for weight, durability, and rarity
        item_data['weight'] = random.uniform(0.1, 10.0)
        item_data['durability'] = random.uniform(0.1, 0.9)
        item_data['rarity_value'] = random.uniform(0.0, 100.0)

        # Call the repository to create the item in the database
        return MagicItemRepository.create_item(item_data)
