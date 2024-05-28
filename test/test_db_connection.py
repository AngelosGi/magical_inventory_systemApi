from db import get_connection


def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print("Connection successful, test query result:", result)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Failed to connect to the database:", e)


if __name__ == "__main__":
    test_connection()
