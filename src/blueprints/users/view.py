from flask_smorest import Blueprint
from flask.views import MethodView
from src.schemas.user import UserSchema, LoginSchema
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
        


@blueprint.route('/login')
class ProtectedView(MethodView):
    @blueprint.arguments(LoginSchema, location='json')
    def post(self,args):
        user = User.login(args)
        if user is not None:
            access_token = create_access_token(identity=user)
            return {'access_token': access_token}
        else:
            return {'msg' : gettext('login.wrong_credential')}, 401
        
    