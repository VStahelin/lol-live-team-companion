from coolname import generate_slug
from fastapi import APIRouter, Request

from cache_manager import get_cache, add_to_cached_dict, remove_from_cached_dict
from constants import CACHE_KEYS
from database.daos import match as match_dao
from runners.run_match import MatchThread

router = APIRouter()


@router.post("/")
async def active_matches_list(request: Request):
    body_as = await request.json()
    return {"message": body_as}


@router.get("/create")
async def create():
    slug = generate_slug(4)
    match = match_dao.get_or_create(slug=slug)
    runner = MatchThread(match_slug=slug)
    if runner.run():
        print(match)
        match_dao.update(match_id=match.id, runner=runner)
        add_to_cached_dict(CACHE_KEYS.RUNNING_MATCHES, slug, runner)
        return {"message": "Match created successfully!"}
    else:
        return {"error": "Error creating match!"}


@router.get("/connect/{session_id}")
async def connect(session_id: str):
    return {"message": session_id}


@router.get("/close/{session_slug}")
async def close(session_slug: str):
    runners = get_cache(CACHE_KEYS.RUNNING_MATCHES)

    if session_slug in runners:
        thread = runners[session_slug]
        thread.stop()
        match_dao.update(match_id=thread.match_slug, running=False)
        remove_from_cached_dict(CACHE_KEYS.RUNNING_MATCHES, session_slug)
        return {"message": f"Match `{session_slug}` closed successfully!"}

    return {"error": "Error closing match!"}


@router.get("/list")
async def all_matches():
    matches = match_dao.get_all()

    return {"matches": matches}


@router.get("/running")
async def get_running_matches():
    running_matches = get_cache(CACHE_KEYS.RUNNING_MATCHES)
    return {"running_matches": str(running_matches)}
