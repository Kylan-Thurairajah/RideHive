from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Any


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema: dict[str, Any], handler: Any) -> dict[str, Any]:
        # Modify the schema to represent an ObjectId as a string
        schema.update(type="string")
        return schema


class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True  # This replaces `allow_population_by_field_name`
        json_encoders = {ObjectId: str}  # Convert ObjectId to string for JSON serialization
