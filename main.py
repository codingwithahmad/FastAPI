from typing import Optional
from enum import Enum

from fastapi import FastAPI, Query

class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"


app = FastAPI()


@app.get('/')
async def root():
	return { "message": "Hello" }


@app.get('/{item_id}')
async def itme(item_id: int):
	return { "item_id": item_id }


@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
	if model_name == ModelName.alexnet:
		return {"model_name": model_name, "message": "Deep Learning FTW!"}

	if model_name.value == "lenet":
		return {"model_name": model_name, "message": "LeCNN all the images"}

	return {"model_name": model_name, "message": "Have some residuals"}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None):
	if q:
		return { "item_id": item_id, "q": q }

	return { "item_id": item_id }



@app.get('/items/')
async def read_query(q: Optional[str] = Query(None, max_lenght=50)):
	result = { "items": "No item" }
	if q:
		return result.update({"q": q })

	return result


@app.get('/sections/{section_id}')
async def read_section(section_id: int, q: Optional[str] = None, short: bool = False):
	section = {"section_id": section_id}
	if q:
		section.update({"q": q})
	if not short:
		section.update(
			{"description": "This is an amazing section that has a long desc."}
		)
	return section