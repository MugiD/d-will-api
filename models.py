from array import array
from xmlrpc.client import boolean
from pydantic import BaseModel
from enum import Enum
from typing import Optional

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    pirate = "pirate"   
    marine = "marine" 

class Status(str, Enum):
    alive = "alive"
    dead = "dead"
    unknown = "unknown"

class OnePiece(BaseModel):
    image: str
    first_name: str
    last_name: str
    gender: Gender
    role: Role
    race: str
    fruit: Optional[str]
    fruit_image: Optional[str]
    status: Optional[Status]

