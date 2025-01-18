from pymongo import MongoClient
from gridfs import GridFS
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "rideHiveDb" 

print(f"MONGO URI: {MONGO_URI}")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# Initialize GridFS
fs = GridFS(db)

users_collection = db["Users"]
parking_collection = db["Parking"]

print(f"users_collection: {users_collection}")

print(f"database: {db}")