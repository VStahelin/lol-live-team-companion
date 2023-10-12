from fastapi import FastAPI

from routes import items

app = FastAPI(debug=True)

app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/")
async def root():
    return {"message": "Hello stranger"}
