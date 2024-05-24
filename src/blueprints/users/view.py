from flask_smorest import Blueprint
from flask.views import MethodView
from src.schemas.user import UserSchema
from src.models.user import User
from src.schemas.general import GeneralResponseSchema
from flask_jwt_extended import create_access_token
from flask_babel import gettext



blueprint = Blueprint('users', __name__, url_prefix='/users')

@blueprint.route('')
class UserView(MethodView):
    @blueprint.arguments(UserSchema, location='json')
    @blueprint.response(201, GeneralResponseSchema)
    def post(self, args):
        return User.create(args)
        

