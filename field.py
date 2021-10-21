from typing import Optional

from fastapi import Body, FastAPI
from pydantic import Field, BaseModel

app = FastAPI()


class Item(BaseModel):
	name: str
	description: Optional[str] = Field(
		None, title="The description of item", max_lenght=300
	)
	price: float = Field(..., gt=0, description="The price must greater than zero")
	tax: Optional[float] = None

@app.put('/items/{item_id}')
async def update(
	*,
	item_id: int,
	item: Item = Body(..., embed=True)
):
	results = {"item_id": item_id, "item": item}

	return results