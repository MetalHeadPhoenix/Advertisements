from marshmallow import validates, ValidationError
from marshmallow_sqlalchemy import auto_field
from src.extensions import ma
from src.models.user import User




class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('updated_at','created_at',)

    id = auto_field(dump_only=True)
    email = auto_field()
    username = auto_field()
    password = auto_field(load_only=True)

    @validates('email')
    def validate_email(self, value):
        if not value or '@' not in value:
            raise ValidationError('Invalid email address.')

    @validates('username')
    def validate_username(self, value):
        if not value or len(value) < 3:
            raise ValidationError('Username must be at least 3 characters long.')


class LoginSchema(UserSchema):
    class Meta:
        exclude = ('email',)