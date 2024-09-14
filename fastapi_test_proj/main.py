from typing import Union

import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sync-task")
def sync_task():
    time.sleep(15)  # This is a blocking operation
    return {"message": "Task completed after 15 seconds"}


@app.get("/long-task")
async def long_task():
    await asyncio.sleep(15)  # Simulate a long task by waiting for 5 seconds
    return {"message": "Task completed after 15 seconds"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
