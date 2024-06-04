from typing import List, Dict, Any

from db import get_connection


class MagicItemRepository:
    @staticmethod
    def create_item(item_data: dict) -> dict:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO magic_items
                (name, description, level, type, category, rarity_value, weight, value, durability)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id
            """, (
                item_data['name'], item_data.get('description'), item_data.get('level'), item_data.get('type'),
                item_data.get('category'), item_data['rarity_value'], item_data['weight'], item_data.get('value'),
                item_data['durability']
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
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM magic_items")
            items = cursor.fetchall()

            cursor.close()
            conn.close()

            # Assuming your table has columns in this specific order
            column_names = ['id', 'name', 'description', 'level', 'type', 'category', 'rarity_value', 'weight', 'value',
                            'durability']
            all_items = [dict(zip(column_names, item)) for item in items]

            return all_items
        except Exception as e:
            raise e
