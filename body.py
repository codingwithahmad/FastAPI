from typing import Optional

from fastapi import FastAPI, Query, Path, Body

from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None

class User(BaseModel):
	username: str
	full_name: Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(
	*,
	item_id: int = Path(..., ge=0, le=1000),
	q: Optional[str] = None,
	item: Optional[Item] = None
):
	result = {"item_id": item_id}

	if q:
		result.update({"q": q})

	if item:
		result.update({"item": item })

	return result

@app.put("/items/update/{item_id}")
async def update(
	*,
	item_id: int = Path(..., ge=0, le=1000),
	q: Optional[str] = None,
	item: Optional[Item] = Body(..., embed=True)
):
	result = {"item_id": item_id }

	if q:
		result.update({"q": q})

	if item:
		result.update({"item": item})

	return result

@app.put("/items/update/user/{item_id}")
async def update_user(
	*,
	item_id: int,
	item: Item,
	user: User
):
	results = {"item_id": item_id, "item": item, "user": user}

	return results