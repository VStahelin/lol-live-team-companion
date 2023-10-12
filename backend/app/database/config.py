from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
