from flask import Blueprint, request
from app.route_guard import auth_required

from app.__blueprint__.model import *
from app.__blueprint__.schema import *

bp = Blueprint('__blueprint__', __name__)

@bp.post('/__blueprint__')
@auth_required()
def create___blueprint__():
    __request_fields__
    __blueprint__ = __Blueprint__.create(__args__)
    return __Blueprint__Schema().dump(__blueprint__), 201

@bp.get('/__blueprint__/<int:id>')
@auth_required()
def get___blueprint__(id):
    __blueprint__ = __Blueprint__.get_by_id(id)
    if __blueprint__ is None:
        return {'message': '__Blueprint__ not found'}, 404
    return __Blueprint__Schema().dump(__blueprint__), 200

@bp.put('/__blueprint__/<int:id>')
@auth_required()
def update___blueprint__(id):
    __blueprint__ = __Blueprint__.get_by_id(id)
    if __blueprint__ is None:
        return {'message': '__Blueprint__ not found'}, 404
    __request_fields__
    __blueprint__.update(__args__)
    return __Blueprint__Schema().dump(__blueprint__), 200

@bp.delete('/__blueprint__/<int:id>')
@auth_required()
def delete___blueprint__(id):
    __blueprint__ = __Blueprint__.get_by_id(id)
    if __blueprint__ is None:
        return {'message': '__Blueprint__ not found'}, 404
    __blueprint__.delete()
    return {'message': '__Blueprint__ deleted successfully'}, 200

@bp.get('/__blueprint__s')
@auth_required()
def get___blueprint__s():
    __blueprint__s = __Blueprint__.get_all()
    return __Blueprint__Schema(many=True).dump(__blueprint__s), 200