from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Request

app = FastAPI()

class Item(BaseModel):
  name: str
  description: str = None


@app.post("/create_item/")
async def create_item(item: Item):
  return {"item": item}


@app.get("/read_item/{item_id}")
async def read_item(item_id: int, request: Request):
  headers = request.headers
  cookies = request.cookies
  return {"item_id": item_id, "headers": headers, "cookies": cookies}