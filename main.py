from fastapi import FastAPI
from models import OnePiece, Gender, Role, Status
from typing import List

app = FastAPI()

db: List[OnePiece] = [
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/a/a9/Monkey_D._Luffy_Portrait.png/revision/latest/scale-to-width-down/119?cb=20220801002903",
        first_name="Luffy",
        last_name="Monkey D.",
        gender=Gender.male,
        role=Role.pirate,
        race="Human",
        origin="East Blue",
        fruit=["Gomu Gomu no mi"],
        fruit_image=[
            "https://static.wikia.nocookie.net/onepiece/images/1/12/Gomu_Gomu_no_Mi_Infobox.png/revision/latest/scale-to-width-down/81?cb=20190419140206"],
        status=Status.alive
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/e/e6/Monkey_D._Garp_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112090224",
        first_name="Garp",
        last_name="Monkey D.",
        gender=Gender.male,
        role=Role.marine,
        race="Human",
        origin="East Blue",
        status=Status.alive
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/4/41/Monkey_D._Dragon_Portrait.png/revision/latest/scale-to-width-down/119?cb=20190805043305",
        first_name="Dragon",
        last_name="Monkey D.",
        gender=Gender.male,
        role=Role.revolutinary,
        race="Human",
        origin="East Blue",
        fruit=["Unknown"],
        status=Status.alive
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/e/e2/Marshall_D._Teach_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200112052537",
        first_name="Teach",
        last_name="Marshall D.",
        gender=Gender.male,
        role=Role.pirate,
        race="Human",
        origin="Grand Line",
        fruit=["Yami Yami no mi", "Gura Gura no mi"],
        fruit_image=[
            "https://static.wikia.nocookie.net/onepiece/images/f/f5/Yami_Yami_no_Mi_Infobox.png/revision/latest/scale-to-width-down/100?cb=20160123174331"
        ],
        status=Status.alive
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/3/31/Trafalgar_D._Water_Law_Portrait.png/revision/latest/scale-to-width-down/119?cb=20200207042244",
        first_name="Law",
        last_name="Trafalgar D. Water",
        gender=Gender.male,
        role=Role.pirate,
        race="Human",
        origin="North Blue",
        fruit=["Ope Ope no mi"],
        fruit_image=[
            "https://static.wikia.nocookie.net/onepiece/images/0/0e/Ope_Ope_no_Mi_Infobox.png/revision/latest/scale-to-width-down/94?cb=20210409181034"],
        status=Status.alive
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/6/6c/Gol_D._Roger_Portrait.png/revision/latest/scale-to-width-down/119?cb=20210321125524",
        first_name="Roger",
        last_name="Gol D.",
        gender=Gender.male,
        role=Role.pirate,
        race="Human",
        origin="East Blue",
        status=Status.dead
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/f/f0/Jaguar_D._Saul_Portrait.png/revision/latest/scale-to-width-down/119?cb=20180623061016",
        first_name="Saul",
        last_name="Jaguar D.",
        gender=Gender.male,
        role=Role.marine,
        race="Giant",
        origin="South Blue",
        status=Status.dead
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/8/82/Portgas_D._Rouge_Portrait.png/revision/latest/scale-to-width-down/119?cb=20180823224941",
        first_name="Rouge",
        last_name="Portgas D.",
        gender=Gender.female,
        role=Role.unknown,
        race="Human",
        origin="Unknown",
        status=Status.dead
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/8/8f/Portgas_D._Ace_Portrait.png/revision/latest/scale-to-width-down/119?cb=20190928095940",
        first_name="Ace",
        last_name="Portgas D.",
        gender=Gender.male,
        role=Role.pirate,
        race="Human",
        origin="South BLue",
        fruit=["Mera Mera no mi"],
        fruit_image=[
            "https://static.wikia.nocookie.net/onepiece/images/8/8c/Mera_Mera_no_Mi_Infobox.png/revision/latest/scale-to-width-down/98?cb=20151123200729"],
        status=Status.dead
    ),
    OnePiece(
        image="https://static.wikia.nocookie.net/onepiece/images/6/65/Rocks_D._Xebec_Portrait.png/revision/latest/scale-to-width-down/119?cb=20220509092258",
        first_name="Xebec",
        last_name="Rocks D.",
        gender=Gender.male,
        role=Role.pirate,
        race="Human",
        origin="Unknown",
        status=Status.dead
    ),
]


@app.get("/")
async def willOfD():
    return db
