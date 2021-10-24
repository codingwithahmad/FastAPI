from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# ! This is for useing Field example attr 
class Item(BaseModel):
	name: str = Field(..., example="Shanpoo")
	description: Optional[str] = Field(None, example="This is good")
	price: float = Field(..., example=22.10)
	tax: Optional[float] = Field(None, example=3.33)


# ! This is for usring config class 
# class Item(BaseModel):
# 	name:str
# 	description: Optional[str] = None
# 	price: float
# 	tax: Optional[float] = None

# 	class Config:
# 		schema_extra = {
# 			"example": {
# 				"name": "foo",
# 				"description": "This is very nice",
# 				"price": 11.99,
# 				"tax": 3.33
# 			}
# 		}



@app.put('/items/{item_id}')
async def update(item_id: int, item: Item):
	results = {"item_id": item_id, "item": item }
	return results