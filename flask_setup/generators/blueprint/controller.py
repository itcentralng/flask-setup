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
    return {'data':__Blueprint__Schema().dump(__blueprint__), 'message': '__Blueprint__ created successfully', 'status':'success'}, 201

@bp.get('/__blueprint__/<id>')
@auth_required()
def get___blueprint__(id):
    __blueprint__ = __Blueprint__.get_by_id(id)
    if __blueprint__ is None:
        return {'message': '__Blueprint__ not found'}, 404
    return {'data':__Blueprint__Schema().dump(__blueprint__), 'message': '__Blueprint__ fetched successfully', 'status':'success'}, 200

@bp.put('/__blueprint__/<id>')
@auth_required()
def update___blueprint__(id):
    __blueprint__ = __Blueprint__.get_by_id(id)
    if __blueprint__ is None:
        return {'message': '__Blueprint__ not found'}, 404
    __request_fields__
    __blueprint__.update(__args__)
    return {'data':__Blueprint__Schema().dump(__blueprint__), 'message': '__Blueprint__ updated successfully', 'status':'success'}, 200

@bp.patch('/__blueprint__/<id>')
@auth_required()
def patch___blueprint__(id):
    __blueprint__ = __Blueprint__.get_by_id(id)
    if __blueprint__ is None:
        return {'message': '__Blueprint__ not found'}, 404
    __request_fields__
    __blueprint__.update(__args__)
    return {'data':__Blueprint__Schema().dump(__blueprint__), 'message': '__Blueprint__ updated successfully', 'status':'success'}, 200

@bp.delete('/__blueprint__/<id>')
@auth_required()
def delete___blueprint__(id):
    __blueprint__ = __Blueprint__.get_by_id(id)
    if __blueprint__ is None:
        return {'message': '__Blueprint__ not found'}, 404
    __blueprint__.delete()
    return {'message': '__Blueprint__ deleted successfully', 'status':'success'}, 200

@bp.get('/__blueprint__')
@auth_required()
def get_all___blueprint__():
    __blueprint__s = __Blueprint__.get_all()
    return {'data':__Blueprint__Schema(many=True).dump(__blueprint__s), 'message': '__Blueprint__ fetched successfully', 'status':'success'}, 200