from fastapi import FastAPI

from app.server.routes.resource import router as ResourceRouter

app = FastAPI()

app.include_router(ResourceRouter, tags=["Resource"], prefix="/resource")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
