from .. import ma
from .model import *

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password', 'created_at', 'updated_at')
