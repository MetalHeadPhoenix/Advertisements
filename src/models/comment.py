from src.extensions import db
from src.models.base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from flask_babel import gettext




class CommentModel(BaseModel):
    __tablename__ = 'comments'
    comment = Column(String, nullable=False)
    advertisement_id = Column(Integer, ForeignKey('advertisements.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    @classmethod
    def create(cls, args, advertisement_id, user_id):
        comment = cls(**args, advertisement_id=advertisement_id, user_id=user_id)
        # comment['advertisement_id'] = advertisement_id
        db.session.add(comment)
        try:
            db.session.commit()
            return {'msg': gettext('comment.create.success')}, 201
        except:
            return {'msg': gettext('error.server.internal')}, 500

    @classmethod
    def read(cls, advertisement_id):
        comments = cls.query.filter_by(advertisement_id=advertisement_id)
        result = [ row._asdict() for  row in comments]
        if comments is not None:
            return result
        return {'msg':gettext('comment.not_found')}, 404

    @classmethod
    def update():
        pass

    @classmethod
    def delete():
        pass