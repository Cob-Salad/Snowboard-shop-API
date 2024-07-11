import json


from fastapi import FastAPI

from models import Snowboard, SnowboardBrand

with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

app = FastAPI()

snowboards: list[Snowboard] = []
    
for item in snowboard_list:
    s = Snowboard(**item)
    snowboards.append(s)



@app.get("/snowboard")
async def get_snowboard() -> list[Snowboard]:
    return snowboards


@app.get("/snowboards/{brand}")
async def snowboard_by_brand(brands: SnowboardBrand) -> list[Snowboard]:
    brand_list = []
    for i, board in enumerate(snowboards):
        if board.brand == brands:
            brand_list.append(snowboards[i])
    return brand_list


@app.post("/snowboards")
async def create_snowboard(new_board: Snowboard, brand: SnowboardBrand):
    for i, board in enumerate(snowboards):
        if board.id == new_board.id:
            return "Unsuccessfull Integration: snowboard id already in use"

        if board.id != new_board.id:
            new_board.brand = brand
            snowboards.append(new_board)
            return

@app.put("/snowboards/{snowboard_id}")
async def update_snowboard(updated_board: Snowboard, snowboard_id: int, brand: SnowboardBrand):
    for i, board in enumerate(snowboards):
        if board.id == snowboard_id:
            updated_board.id = snowboard_id
            updated_board.brand = brand
            snowboards[i] = updated_board
            return
    
    updated_board.id = snowboard_id
    updated_board.brand = brand
    snowboards.append(updated_board)
    return
        

@app.delete("/snowboards/{snowboard_api}")
async def delete_snowboard(snowboard_id: int):
    for i, board in enumerate(snowboards):
        if board.id == snowboard_id:
            snowboards.pop(i)
        


