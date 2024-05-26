import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
    DATABASE_USER = os.getenv("DATABASE_USER", "your_user")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "your_password")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "your_database")