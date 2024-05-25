from src.extensions import ma
from src.models.advertisement import AdvertisementModel
from marshmallow import Schema
from marshmallow.fields import Int, String, DateTime, Field
from marshmallow_sqlalchemy import auto_field
from datetime import datetime

class AdvertisementSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdvertisementModel
        exclude =  ('publisher', 'created_at', 'updated_at', )
        
    id = auto_field(dump_only=True)  
    publisher = auto_field()
    title = auto_field()
    content = auto_field()
    imageURL = auto_field()
    created_at = auto_field(dump_only=True)

class RequestDeleteSchema(Schema):
    id = Int()

class RequestUpdateSchema(Schema):
    id = Int()
    field = String()
    new_value = String()

    


class RequestGetAdsSchema(Schema):
    page = Int()

class ResponseGetAdsSchema(Schema):
    publisher = String()
    title = String()
    content = String()
    imageURL = String()
    created_at = DateTime()


class RequestPostAdSchema(Schema):
    publisher = String()
    
    
class ResponsePostAdSchema(Schema):
    publisher = String()

    
class GeneralResponseSchema(ma.Schema):
    msg = String()
    response_time = Field(dump_default=datetime.now())