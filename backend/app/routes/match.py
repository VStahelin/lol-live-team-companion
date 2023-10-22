from fastapi import APIRouter, Request

from coolname import generate_slug

from database.daos.match import create as create_match

router = APIRouter()


@router.post("/")
async def active_matches_list(request: Request):
    body_as = await request.json()
    return {"message": body_as}


@router.get("/create")
async def create():
    slug = generate_slug(4)
    match = create_match(slug)

    return {"match_slug": match}


@router.get("/connect/{session_id}")
async def connect(session_id: str):
    return {"message": session_id}


@router.get("/close/{session_id}")
async def close(session_id: str):
    return {"message": session_id}
