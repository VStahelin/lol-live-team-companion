from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import items, data_stream
from routes import items, data_stream, match


app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(data_stream.router, prefix="/data_stream", tags=["data_stream"])
app.include_router(match.router, prefix="/match", tags=["match"])


@app.get("/")
async def root():
    return {"message": "Hello stranger"}
