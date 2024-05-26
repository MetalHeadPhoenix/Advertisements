from src.models.base import BaseModel
from sqlalchemy import Column, String, select, ForeignKey, update
from src.extensions import db
from flask_babel import gettext




class AdvertisementModel(BaseModel):
    __tablename__ = 'advertisements'
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    imageURL = Column(String, nullable=True)
    comments = db.relationship('CommentModel', backref='advertisement')


    @classmethod
    def create(cls, args):
        advertisement = cls(**args)
        db.session.add(advertisement)
        try:
            db.session.commit()
            return {'msg': gettext('advertisement.create.success')}, 201
        except:
            return {'msg': gettext('error.server.internal')}, 500

    @classmethod
    def read_list(cls, args):
        list_of_ads = db.session.execute(
            select(cls.user_id, cls.created_at, cls.id, cls.content, cls.imageURL, cls.title)
            .order_by(cls.created_at.desc())
            .limit(args['page']*10))
        
        result = [ row._asdict() for  row in list_of_ads]
        return result

    @classmethod
    def get_by_id(cls, id):
        advertisement = cls.query.filter_by(id=id).first()
        if advertisement is not None:
            return advertisement
        return {'msg':gettext('advertisement.not_found')}, 404

    @classmethod
    def update(cls, args):
        cls.query.filter_by(id=args['id']).update(dict(title=args['new_value']))
        try:
            db.session.commit()
        except:
            {'msg': 'internal server error'}
     
        

    @classmethod
    def delete(cls, args):
        advertisement = cls.query.filter_by(id=args['id']).one()
        db.session.delete(advertisement)
        try:
            db.session.commit()
        except:
            {'msg': 'internal server error'}







