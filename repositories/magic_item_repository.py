from typing import List, Dict, Any, Optional
from db import get_connection


class MagicItemRepository:

    @staticmethod
    def create_item(item_data: dict) -> dict:
        """
            Create a new magic item in the database.
            Args:
                item_data (dict): A dictionary containing the data for the new item.
            Returns:
                dict: A dictionary containing the data for the new item, including the generated ID.
            Raises:
                Exception: If there is an error creating the item in the database.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO magic_items
                (name, description, level, type, category, rarity_value, weight, value, durability, stock)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id
            """, (
                item_data['name'], item_data.get('description'), item_data.get('level'), item_data.get('type'),
                item_data.get('category'), item_data['rarity_value'], item_data['weight'], item_data.get('value'),
                item_data['durability'], item_data.get('stock', 1)
            ))
            item_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            return {**item_data, "id": item_id}
        except Exception as e:
            conn.rollback()
            raise e

    @staticmethod
    def get_all_items() -> list[dict[Any, Any]]:
        """
        Get all magic items from the database.
        Returns:
            list[dict[Any, Any]]: A list of dictionaries containing the data for each item.
        Raises:
            Exception: If there is an error fetching the items from the database.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magic_items")
            items = cursor.fetchall()
            cursor.close()
            conn.close()
            column_names = ['id', 'name', 'description', 'level', 'type', 'category', 'rarity_value', 'weight', 'value',
                            'durability', 'stock']
            all_items = [dict(zip(column_names, item)) for item in items]
            return all_items
        except Exception as e:
            raise e

    @staticmethod
    def get_item_by_id(item_id: int) -> Optional[dict[Any, Any]]:
        """
        Get a magic item from the database by its ID.
        Args:
            item_id (int): The ID of the item to fetch.
        Returns:
            Optional[dict[Any, Any]]: A dictionary containing the data for the item, or None if the item does not exist.
        Raises:
            Exception: If there is an error fetching the item from the database.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magic_items WHERE id = %s", (item_id,))
            item = cursor.fetchone()
            cursor.close()
            conn.close()
            if item:
                column_names = ['id', 'name', 'description', 'level', 'type', 'category', 'rarity_value', 'weight',
                                'value', 'durability', 'stock']
                item = dict(zip(column_names, item))
            return item
        except Exception as e:
            raise e
