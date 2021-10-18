from fastapi import FastAPI, Query, Path

from typing import Optional

app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(item_id: int = Path(..., title="The ID of the item to get"),
	q: Optional[str] = Query(None, alias="item-query"),
):
	result = {"item_id": item_id}

	if q:
		result.update({"q": q})

	return result

@app.get('/items/gt/{item_id}')
async def read_item_gt(
	*,
	item_id: int = Path(..., title="The The ID of the item to get v2", gt=0, le=1000),
	q: str = None,
):
	result = {"item_id": item_id}

	if q:
		result.update({"q": q})

	return result		