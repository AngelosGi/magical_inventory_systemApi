# Magic Inventory System API
This project is a FastAPI-based API for managing a magical inventory system. It provides endpoints for creating, reading, updating, and deleting magical items, as well as some work-in-progress features like search functionality, inventory management, calculating rarity based on numerical rarity values like `rare`, `legendary`, etc., buying and selling methods, and a use/test item functionality that affects durability and inventory.

---

## Technologies Used

- **FastAPI:** FastAPI is used as the primary web framework for building the API endpoints, providing high performance and easy-to-use features for request handling and response generation.
- **PostgreSQL:** PostgreSQL serves as the relational database management system for storing and managing the data of magical items. It provides robust features for data integrity and scalability.
- **Pydantic:** Pydantic is leveraged for data validation and serialization, ensuring that incoming requests and outgoing responses adhere to defined schemas. It helps maintain consistency and correctness in data handling.
- **uvicorn:** Uvicorn is utilized as the ASGI server implementation to serve the FastAPI application, providing fast and efficient handling of HTTP requests.
- **Swagger UI:** Swagger UI is integrated to provide interactive documentation for the API endpoints, allowing users to explore and test the available functionalities visually.
- **Docker:** Docker is employed to containerize the PostgreSQL database, allowing for easy setup and management of the database environment. It ensures consistency and portability across different development and deployment environments.

---

## Features

- **CRUD Operations:** Create, read, update, and delete magical items.
- ~~**Rarity Category Computation:** Compute rarity categories based on item rarity values.~~ not yet working on it.
- **Interactive Documentation:** Swagger UI provides an interactive API documentation interface for easy exploration and testing.
- **Modular Structure:** The project follows a clean and modular structure for scalability and maintainability.

---

## Installation

To run the Magical Inventory System API locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/magical_inventory_systemApi.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup:**

   - **Database Connection:** Ensure that you have a PostgreSQL database set up and running. Update the database connection details in the `db.py` file to match your database configuration.
   - **Fresh Setup:** Run the `create_schema.sql` script to create the initial database schema.
   - **Existing Database:** If you're working with an existing database or need to manage migrations:
     - Ensure that you have the appropriate permissions and access to the database.
     - Run the `apply_migrations.py` script to apply migrations to the database.

     ```bash
     python apply_migrations.py
     ```

4. Start the FastAPI server:

   ```bash
   uvicorn main:app --port 9000 --reload
    # I had to change ports every now and then because it wouldn't register the changes, maybe a cashing issue
    # refreshing/F5, ctrl+F5 etc dint work, If you change the ports, you will need to adjust the next steps in the same way.
   ```

5. Access the API at `http://localhost:9000` in your browser or API client.

---

## Usage

- Access the Swagger documentation at `http://localhost:9000/docs` to explore and interact with the API endpoints.
- Use tools like Postman to make requests to the API endpoints.

---

When creating a new magic item, the system automatically generates random values for certain attributes such as weight, durability, and rarity. This ensures variety and uniqueness in the items created.


```create
#/items/create input

{
  "name": "Staff of Eternal Wisdom",
  "description": "A staff imbued with the wisdom of the ancients.",
  "level": 10,
  "type": "Staff",
  "category": "Majesteak",
  "value": 1312,
  "stock": 1
}
```
```created item
#created item with some random values.

{
  "name": "Staff of Eternal Wisdom",
  "description": "A staff imbued with the wisdom of the ancients.",
  "level": 10,
  "type": "Staff",
  "category": "Majesteak",
  "weight": 9.94431284764603,
  "durability": 0.379109043351363,
  "value": 1312,
  "stock": 1,
  "id": 1,
  "rarity_value": 17.520679710089127
}
```