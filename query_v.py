from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

@app.get('/items/max/')
async def read_query_one(q: Optional[str] = Query(None, max_lenght=50)):
	result = { "items": "No item" }
	if q:
		return result.update({"q": q })

	return result

@app.get('/items/min/')
async def read_query_two(q: Optional[str] = Query(None, min_length=3, max_lenght=50)):
	result = { "items": "No item" }
	if q:
		return result.update({"q": q })

	return result


# if we have a required query 
@app.get('/items/required/')
async def read_query_two_required(q: Optional[str] = Query(..., min_length=3, max_lenght=50)):
	result = { "items": "No item" }
	if q:
		return result.update({"q": q })

	return result


@app.get('/items/list/')
async def read_items_list(q: Optional[List[str]] = Query(None)):
	query_items = {"q": q}
	return query_items