from src.models.base import BaseModel
from src.extensions import db, bcrypt
from sqlalchemy import Column, String
from flask_babel import gettext




class User(BaseModel):
    __tablename__ = 'users'
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


    @classmethod
    def create(cls, args): 
        from src.blueprints.users.helpler import validate_registration   

        if validate_registration(args)['is_validated']:
            user = cls(**args)
            user.password = cls.create_password(user.password)
            db.session.add(user)
            try:
                db.session.commit()
                return { "msg" : gettext('user.create.success')}
            except:
                db.session.rollback()
                return {'msg': gettext('error.server.internal')}, 500
        else:
            return {'msg':validate_registration(args)['msg']},400
        
    
    @staticmethod
    def create_password(password):
        hashed_password = bcrypt.generate_password_hash(password=password).decode('utf-8')
        return hashed_password


    

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} ({self.id}, {self.username})'
    
    