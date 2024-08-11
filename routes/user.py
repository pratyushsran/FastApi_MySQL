from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.engine import Result
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()

def row_to_dict(row):
    return dict(row._mapping)

@user.get("/")
async def read_data():
    result: Result = conn.execute(users.select())
    return [row_to_dict(row) for row in result]

@user.get("/{id}")
async def read_data(id: int):
    result: Result = conn.execute(users.select().where(users.c.id == id))
    return [row_to_dict(row) for row in result]

@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    result: Result = conn.execute(users.select())
    return [row_to_dict(row) for row in result]

@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    result: Result = conn.execute(users.select())
    return [row_to_dict(row) for row in result]

@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    result: Result = conn.execute(users.select())
    return [row_to_dict(row) for row in result]
