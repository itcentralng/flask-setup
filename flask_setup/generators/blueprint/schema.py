from app import ma
from app.__blueprint__.model import *

class __Blueprint__Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = __Blueprint__
        exclude = ('is_deleted',)