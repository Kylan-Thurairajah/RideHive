from faker import Faker
from dotenv import load_dotenv
from database import users_collection  # Import from database.py
from user_model import UserModel       # Import the UserModel
import os

# Load environment variables from .env file
load_dotenv()

# Use Faker to generate fake data
fake = Faker()

def populate_users(count=10):
    """
    Populates the users collection with sample data.
    :param count: Number of users to insert.
    """
    users = []
    for _ in range(count):
        # Generate random data for a user
        user_data = {
            "name": fake.name(),
            "email": fake.email(),
            "password": fake.password(length=12),  # You should hash passwords in real apps
            "student_id_file_id": None,  # Placeholder for GridFS file ID
            "license_file_id": None,  # Placeholder for GridFS file ID
            "rating": round(fake.pyfloat(left_digits=1, right_digits=2, positive=True, max_value=5.0), 2),
            "role": fake.random_element(elements=("Driver", "Passenger")),
            "address": fake.address(),  # Add a random address
        }

        # Validate and parse the data with UserModel
        user = UserModel(**user_data)
        users.append(user.model_dump(by_alias=True))  # Convert to dict for MongoDB

    # Insert users into the collection
    result = users_collection.insert_many(users)
    print(f"Inserted {len(result.inserted_ids)} users into the database.")


if __name__ == "__main__":
    # Specify the number of users to generate
    populate_users(count=10)
