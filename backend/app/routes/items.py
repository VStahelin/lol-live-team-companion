from fastapi import APIRouter, Request

from database.daos.item import (
    get as get_item,
    create as create_item,
    get_all as get_all_items,
    update as update_item,
    delete as delete_item,
)

router = APIRouter()


@router.post("/")
async def post_item(request: Request):
    body_as = await request.json()
    item = create_item(**body_as)

    return {"message": item}


@router.get("/{item_id}")
async def get(item_id: int):
    return get_item(item_id=item_id)


@router.get("/")
async def get_all():
    return get_all_items()


@router.put("/{item_id}")
async def update(item_id: int, request: Request):
    body_as = await request.json()
    return update_item(item_id=item_id, **body_as)


@router.delete("/{item_id}")
async def delete(item_id: int):
    return delete_item(item_id=item_id)
