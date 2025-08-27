from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI
app = FastAPI()

class Item(BaseModel):
  name: str
  description: str = None


@app.post("/items/")
async def create_item(item: Item):
  return item

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}