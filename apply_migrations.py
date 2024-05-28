from db import get_connection


def apply_migrations():
    try:
        with open('create_schema.sql', 'r') as f:
            sql = f.read()

        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                # Drop the "items" table if it exists
                cursor.execute("DROP TABLE IF EXISTS items;")
                # Create the "items" table
                cursor.execute(sql)
            conn.commit()
            print('Migrations successful!')
        except Exception as e:
            conn.rollback()
            print("Migrations Failed :(", e)
        finally:
            conn.close()
    except FileNotFoundError:
        print("Error: create_schema.sql not found")


if __name__ == "__main__":
    apply_migrations()
