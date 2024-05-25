from flask import Flask
from src.extensions import api, db, bcrypt, jwt, ma, babel, migrate


def create_app(config):

    app = Flask(__name__)

    #Config
    app.config.from_object(config)


    #Extentions
    api.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    babel.init_app(app)
    migrate.init_app(app, db)

    #Models
    from src.models.base import BaseModel
    from src.models.user import User
    from src.models.advertisement import AdvertisementModel
    from src.models.comment import CommentModel


    #Blueprints
    from src.blueprints.users.view import blueprint as users_blueprint
    from src.blueprints.advertisements.view import blueprint as advertisements_blueprint
    api.register_blueprint(users_blueprint)
    api.register_blueprint(advertisements_blueprint)
    

    return app


