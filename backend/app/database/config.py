from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from .models.item import Item
from .models.match import Match

from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# Create tables:
inspector = inspect(engine)

if not inspector.has_table(Item.__tablename__):
    Item.__table__.create(bind=engine)

if not inspector.has_table(Match.__tablename__):
    Match.__table__.create(bind=engine)
