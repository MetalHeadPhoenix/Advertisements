from src.extensions import db
from src.models.base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey




class CommentModel(BaseModel):
    __tablename__ = 'comments'
    comment = Column(String, nullable=False)
    advertisement_id = Column(Integer, ForeignKey('advertisements.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    @classmethod
    def create():
        pass

    @classmethod
    def read():
        pass

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass