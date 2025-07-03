# app/db/mongodb.py

from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import get_settings

settings = get_settings()

# Create a single shared MongoDB client
client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.DB_NAME]

def get_database():
    return database
