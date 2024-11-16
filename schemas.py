from datetime import datetime

from pydantic import BaseModel, ConfigDict




class DogCreate(BaseModel):
    name: str
    age: float
    species: str
    price: float

class Dog(BaseModel):
    id: int
    name: str
    age: float
    species: str
    price: float
    model_config = ConfigDict(from_attributes=True)