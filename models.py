from pydantic import BaseModel
from enum import Enum
from typing import Optional, List

class Gender(str, Enum):
    male = "Male"
    female = "Female"

class Role(str, Enum):
    pirate = "Pirate"   
    marine = "Marine"
    revolutinary="Revolutinary"
    unknown="Unknown"

class Status(str, Enum):
    alive = "Alive"
    dead = "Dead"
    unknown = "Unknown"

class OnePiece(BaseModel):
    image: str
    first_name: str
    last_name: str
    gender: Gender
    role: Role
    race: str
    origin: str
    fruit: Optional[List]
    fruit_image: Optional[List]
    status: Status

