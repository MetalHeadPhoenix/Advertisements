from src.database import convention, Base
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_babel import Babel





db = SQLAlchemy(model_class=Base)
migrate = Migrate()
api = Api()
bcrypt = Bcrypt()
jwt = JWTManager()
ma = Marshmallow()
babel = Babel()
