from sqlalchemy import Column, Integer, String, Sequence, DateTime, func, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Match(Base):
    __tablename__ = "matches"

    id = Column(
        Integer,
        Sequence("match_id_seq"),
        primary_key=True,
        index=True,
        autoincrement=True,
    )
    slug = Column(String, index=True, unique=True)

    player_1 = Column(JSON)
    player_2 = Column(JSON)
    player_3 = Column(JSON)
    player_4 = Column(JSON)
    player_5 = Column(JSON)

    created_at = Column(DateTime, default=func.now())
