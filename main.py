from fastapi import FastAPI
from models import OnePiece, Gender, Role, Status
from typing import List

app = FastAPI()

db: List[OnePiece] = [
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/a/a9/Monkey_D._Luffy_Portrait.png/revision/latest/scale-to-width-down/119?cb=20220801002903",
        first_name="Luffy",
        last_name="Monkey D",
        gender=Gender.male,
        role=Role.pirate,
        race="human",
        fruit="Gomu Gomu no mi",
        fruit_image="none",
        status=Status.alive
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/a/a9/Monkey_D._Luffy_Portrait.png/revision/latest/scale-to-width-down/119?cb=20220801002903",
        first_name="Luffy",
        last_name="Monkey D",
        gender=Gender.male,
        role=Role.pirate,
        race="human",
        fruit="Gomu Gomu no mi",
        fruit_image="none",
        status=Status.alive
    )
]


@app.get("/")
async def willOfD():
    return db
