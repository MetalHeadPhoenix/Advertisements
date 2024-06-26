from src.extensions import db
from sqlalchemy import Column, Integer, DateTime, func


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())