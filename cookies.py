from typing import Optional

from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get('/items/')
async def read_item(asd_id: Optional[str] = Cookie(None)):
	return {"asd_id": asd_id}
