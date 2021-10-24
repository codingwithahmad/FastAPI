from typing import Optional, List, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


app = FastAPI()

class Image(BaseModel):
	url: HttpUrl
	name: str 

class Item(BaseModel):
	name: str
	description: Optional[str] = None
	price: float
	image: Optional[Image] = None
	tax: Optional[float] = None
	tags: Set[str] = set() # we use sets for haveing a list of unique tags because duplicate is not allowed in sets 

@app.put('/items/{item_id}')
async def update(item_id: int, item: Item):
	results = {"item_id": item_id, "item": item}
	return result