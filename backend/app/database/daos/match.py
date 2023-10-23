from .. import SessionLocal
from ..models.match import Match
from sqlalchemy.exc import IntegrityError

session = SessionLocal()


def create(slug):
    match = Match(slug=slug)
    session.add(match)

    try:
        session.commit()
    except IntegrityError as integrity_error:
        session.rollback()
        return {"integrity_error": integrity_error}
    except Exception as e:
        session.rollback()
        return {"error": e}

    session.refresh(match)
    session.flush()
    return match


def update(match_id, **kwargs):
    try:
        match = session.query(Match).filter(Match.id == match_id).first()
        if match:
            for key, value in kwargs.items():
                setattr(match, key, value)
            session.commit()
            return {"message": f"Match id: {match.id} updated"}
        else:
            return {"error": "Match not found"}
    except Exception as e:
        return {"error": e}


def get_by_slug(slug):
    try:
        match = session.query(Match).filter(Match.slug == slug).first()
        if match:
            return match
        else:
            return {"error": "Match not found"}
    except Exception as e:
        return {"error": e}


def get_by_id(match_id):
    try:
        match = session.query(Match).filter(Match.id == match_id).first()
        if match:
            return match
        else:
            return {"error": "Match not found"}
    except Exception as e:
        return {"error": e}


def get_all():
    try:
        matches = session.query(Match).all()
        if matches:
            return matches
        else:
            return {"error": "Match not found"}
    except Exception as e:
        return {"error": e}


def get_or_create(slug):
    try:
        match = session.query(Match).filter(Match.slug == slug).first()
        if match:
            return match
        else:
            return create(slug)
    except Exception as e:
        return {"error": e}


def delete_by_slug(slug):
    try:
        match = session.query(Match).filter(Match.slug == slug).first()
        if match:
            session.delete(match)
            session.commit()
            return {"message": f"Match slug: {match.slug} deleted"}
        else:
            return {"error": "Match not found"}
    except Exception as e:
        return {"error": e}


def delete_by_id(match_id):
    try:
        match = session.query(Match).filter(Match.id == match_id).first()
        if match:
            session.delete(match)
            session.commit()
            return {"message": f"Match id: {match.id} deleted"}
        else:
            return {"error": "Match not found"}
    except Exception as e:
        return {"error": e}
