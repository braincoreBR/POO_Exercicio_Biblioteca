from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
app = FastAPI()

class item(BaseModel):
    name:str
    price:float
    is_offer:Union[bool,None]

@app.get("/")
async def root():
    return{"message": "Oie"}

@app.get("/itens/{item_id}")
async def read_item(item_id: int, busca: Union[int, str] = None):
    return{"item_id": item_id, "busca": busca}

@app.put("/itens/{item_id}")
def update_item(item_id: int, item:item):
    return{"item_id": item_id, "item_name": item.name}