from .. import SessionLocal
from ..models.item import Item

session = SessionLocal()


def create(name, description):
    item = Item(name=name, description=description)
    session.add(item)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"error": e}

    session.refresh(item)
    session.flush()
    return item


def get(item_id):
    try:
        item = session.query(Item).filter(Item.id == item_id).first()
        if item:
            return item
        else:
            return {"error": "Item not found"}
    except Exception as e:
        return {"error": e}


def get_all():
    try:
        items = session.query(Item).all()
        if items:
            return items
        else:
            return {"error": "Item not found"}
    except Exception as e:
        return {"error": e}


def update(item_id, name, description):
    try:
        item = session.query(Item).filter(Item.id == item_id).first()
        if item:
            item.name = name
            item.description = description
            session.commit()
            return {"message": f"Item id: {item.id} updated"}
        else:
            return {"error": "Item not found"}
    except Exception as e:
        return {"error": e}


def delete(item_id):
    try:
        item = session.query(Item).filter(Item.id == item_id).first()
        if item:
            session.delete(item)
            session.commit()
            return {"message": "Item deleted"}
        else:
            return {"error": "Item not found"}
    except Exception as e:
        return {"error": e}
