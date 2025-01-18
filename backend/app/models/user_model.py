from app.models.common import MongoBaseModel  # Import your base model
from pydantic import EmailStr, Field
from typing import Optional
from bson import ObjectId

class UserModel(MongoBaseModel):
    name: str
    email: EmailStr
    password: str  # Store hashed passwords
    address: str
    # student_id_file_id: Optional[ObjectId] = Field(default=None, alias="id_card_file_id")  # GridFS file ID for student ID
    # license_file_id: Optional[ObjectId] = Field(default=None)  # GridFS file ID for driver's license
    rating: float  # Average out of 5
    role: str  # Driver or Passenger
    max_capacity: int = None # Drivers have a max capacity in the car

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
