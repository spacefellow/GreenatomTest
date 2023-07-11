from typing import Optional, Annotated
from sqlalchemy import Column, ForeignKey, Integer, String, UUID, TEXT, Double
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4

from src.database import Base


class FilmModel(Base):
    __tablename__ = 'film'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False)
    rating = Column(Double, nullable=True)


class ReviewModel(Base):
    __tablename__ = 'review'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    text = Column(TEXT, nullable=False)
    film_id = Column(UUID(as_uuid=True), ForeignKey('film.id', ondelete='CASCADE'))
    score = Column(Integer, nullable=True)
