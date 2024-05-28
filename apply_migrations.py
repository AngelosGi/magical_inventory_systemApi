from db import get_connection


def apply_migrations():
    with open('create_schema.sql', 'r') as f:
        sql = f.read()

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
        print('Migrations successful!')
    except Exception as e:
        conn.rollback()
        print("Migrations Failed :(", e)
    finally:
        conn.close()


if __name__ == "__main__":
    apply_migrations()
