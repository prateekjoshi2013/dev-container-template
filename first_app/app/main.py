from fastapi import FastAPI
from app.router_example import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}