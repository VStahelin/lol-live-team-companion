import asyncio
import json
import random
import sys
import time

from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

router = APIRouter()


async def while_event_generator():
    i = 0
    while True:
        await asyncio.sleep(0.5)  # Sleep for 500ms
        i = i + 1
        data = {
            "event": random.randint(a=0, b=sys.maxsize),
            "timestamp": time.time(),
            "data": "some data",
        }
        yield json.dumps(data)


@router.get("/events")
async def sse_stream():
    return EventSourceResponse(while_event_generator(), media_type="text/event-stream")
