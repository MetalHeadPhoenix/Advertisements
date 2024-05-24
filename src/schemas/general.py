from marshmallow.fields import String, Field
from src.extensions import ma
from datetime import datetime




class GeneralResponseSchema(ma.Schema):
    msg = String()
    response_time = Field(dump_default=datetime.now())