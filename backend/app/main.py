import atexit

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cache_manager import get_cache
from constants import CACHE_KEYS
from routes import items, data_stream, match
from runners.run_mqtt_connection import run_mqtt_connection

app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Set the mqtt client and subscriber thread in cache
run_mqtt_connection()


def cleanup_function():
    running_matches = get_cache(CACHE_KEYS.RUNNING_MATCHES)
    for match_slug in running_matches:
        thread = running_matches[match_slug]
        thread.stop()

    subscriber_thread = get_cache(CACHE_KEYS.SUBSCRIBER_THREAD)
    subscriber_thread.stop()


atexit.register(cleanup_function)

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(data_stream.router, prefix="/data_stream", tags=["data_stream"])
app.include_router(match.router, prefix="/match", tags=["match"])


@app.get("/")
async def root():
    return {"message": "Hello stranger"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
