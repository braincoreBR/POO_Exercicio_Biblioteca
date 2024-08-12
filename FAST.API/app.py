from fastapi import FastAPI, HTTPException
from typing import Union, List
from pydantic import BaseModel
from models import user, role
from uuid import UUID, uuid4
app = FastAPI()

db: List[user] = [
    user(id = UUID("e22b4787-ed8e-40da-8b41-5f26a7789e59"), first_name="Ana", last_name="Silva", email="ana.silva@gmail.com", role=[role.role_1]),
    user(id = UUID("d6e7edd1-efaa-4fec-87bd-c781480dcf4a"), first_name="Jose", last_name="Silva", email="Jose.silva@gmail.com", role=[role.role_2]),
    user(id = UUID("eaab34c7-c840-4434-a7e3-aacef9ee0ecc"), first_name="caroline", last_name="Silva", email="caroline.silva@gmail.com", role=[role.role_3])
]

@app.get("/api/users/{id}")
async def get_users():
    for user in db:
        if user.id ==id:
            return user
    return{"message": "usuário não encontrado"}

@app.get("/api/users")
async def get_users():
    """_summary_

    Returns:
        _type_: _description_
    """
    return db

@app.post("/api/users")
async def add_users(user:user):
    db.append(user)
    return {"mensagem": "Usuário Criado com sucesso! ID: " + str(user.id) }

@app.delete("/api/users/{id}")
async def delete_users(id:UUID):
    for user in db:
        if user.id ==id:
            db.remove(user)
            return {"messagem": str(user.first_name) + " removido com sucesso"}
    # return{"message": "usuário não encontrado"}
    raise HTTPException(status_code=404,
                        detail= f"usuário com o ID: {id} não encontrado"
                        )

@app.get("/")
async def root():
    return{"message": "Oie"}

