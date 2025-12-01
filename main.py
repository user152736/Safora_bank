from fastapi import FastAPI
from  pydantic import BaseModel
from typing import Optional


app = FastAPI()

@app.get('/', tags=['Home'])
def home() -> dict:
    return {'hello':'world'}

user_list = []

wish_list = []

@app.get('/wishlist', tags=['wishlist'])
def wishlist() -> list[str]:
    return wish_list

@app.post('/add_to_wishlist',tags=['wishlist'])
def add_to_wishlist(wish:str) -> dict:
    wish_list.append(wish)
    return {"message":"wish is added to wish list"}

@app.get('/wish/{wish_id}', tags=['wishlist'])
def one_wish(wish_id:int) -> str:
    wish = wish_list[wish_id]
    return wish

@app.delete('/wish_delete/{wish_id}', tags=['wishlist'])
def wish_delete(wish_id:int) -> dict:
    deleted_wish = wish_list.pop(wish_id)
    return {"message":f"'{deleted_wish}' is deleted"}

@app.put('/wish_update', tags=['wishlist'])
def wish_update(wish_id:int, wish:str) -> dict:
    was = wish_list[wish_id]
    wish_list[wish_id] = wish
    return {"was":f"{was}",
            "is":f"{wish}"}


# Base models -----------------------


class User(BaseModel):
    name:str
    nickname: Optional[str]
    password:str
    email: Optional[str] = None

@app.get('/all_users', tags=['BaseModel User'])
def all_users() -> list[dict]:
    return user_list


@app.get('/users/{user_id}', tags=['BaseModel User'])
def get_user(user_id:int) -> dict:
    user = user_list[user_id]
    return user

@app.post('/add_users', tags=['BaseModel User'])
def add_users(user:User) -> User:
    user_list.append(user)
    return user
























