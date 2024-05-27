from src.extensions import ma
from src.models.comment import CommentModel


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentModel
        exclude = ('created_at', 'updated_at', 'id',)
        
        
    