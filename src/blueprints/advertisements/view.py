from flask_smorest import Blueprint
from flask.views import MethodView
from src.schemas.advertisement import RequestGetAdsSchema, ResponseGetAdsSchema, AdvertisementSchema, RequestDeleteSchema, RequestUpdateSchema
from src.schemas.general import GeneralResponseSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.models.advertisement import AdvertisementModel

blueprint = Blueprint('advertisements', __name__, url_prefix='/advertisements')


@blueprint.route('')
class AdvertisementView(MethodView):
    @blueprint.arguments(RequestGetAdsSchema, location="query")
    @blueprint.response(200, AdvertisementSchema(many=True))
    def get(self, args):
        """Show advertisement with pagination"""
        ads = AdvertisementModel.read_list(args)
        return ads

    @blueprint.arguments(AdvertisementSchema, location="json")
    @blueprint.response(201, GeneralResponseSchema)
    @jwt_required()
    def post(self, args):
        """Create advertisement"""
        user = get_jwt_identity()
        args['user_id'] = user['id']
        advertisement = AdvertisementModel.create(args)
        return advertisement
    

    @jwt_required()
    @blueprint.arguments(RequestDeleteSchema, location="json")
    def delete(self, args):
        """Delete advertisement"""
        AdvertisementModel.delete(args)
        return {'msg': 'the advertisement deleted successfully'}
    
    @jwt_required()
    @blueprint.arguments(RequestUpdateSchema, location="json")
    def put(self, args):
        """Update advertisement"""
        AdvertisementModel.update(args)
        return {'msg': 'the advertisement updated successfully'}
    

@blueprint.route('/<id>')
class AdvertisementView(MethodView):
    
    @blueprint.response(200, AdvertisementSchema)
    @blueprint.response(404, GeneralResponseSchema)
    def get(self, id):
        """Show advertisement by id"""
        ads = AdvertisementModel.get_by_id(id)
        return ads
    

    @blueprint.arguments(AdvertisementSchema, location='json')
    @blueprint.response(404, GeneralResponseSchema)
    def post(self, id):
        """Update advertisement by id"""
        pass

