from typing import Optional

from fastapi import FastAPI, Header


app = FastAPI()


@app.get('/items/')
async def read_item(user_agent: Optional[str] = Header(None)):
	return {"user_agent": user_agent }