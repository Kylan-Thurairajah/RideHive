from app.models.common import MongoBaseModel

class ParkingModel(MongoBaseModel):
    availability: bool
    label: str
    priority: int  # Priority levels: 1, 2, 3
    user_id=None
