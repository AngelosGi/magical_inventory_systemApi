# Magical Inventory System API

This project is a FastAPI-based API for managing a magical inventory system. It  provides endpoints for creating, ~~ reading, updating, and deleting ~~ (WIP) magical items, as well as computing rarity categories based on item rarity values.

## Features

- **CRUD Operations:** Create, read, update, and delete magical items.
- **Rarity Category Computation:** Compute rarity categories based on item rarity values.
- **Swagger Documentation:** Interactive API documentation using Swagger UI.
- **Modular Structure:** Clean and modular project structure for scalability and maintainability.

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

3. Set up the database:

   - Execute `create_schema.sql` to create the database schema.
   - Apply migrations using `apply_migrations.py`.

4. Start the FastAPI server:

   ```bash
    #NOTE: Had browser(?) cashing issues while reloading, i had to change port everytime because the changes where not registering 🤷. 
   
   uvicorn main:app --port 9000 --reload
   ```

5. Access the API at `http://localhost:9000` in your browser or API client.

## Usage

- Access the Swagger documentation at `http://localhost:9000/docs` to explore and interact with the API endpoints.
- Use tools like Postman, to make requests to the API endpoints.
