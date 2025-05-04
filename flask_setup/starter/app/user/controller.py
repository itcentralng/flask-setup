from flask import Blueprint, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.helpers.model import paginate

from app.user.model import User
from app.user.schema import UserSchema
from app.route_guard import auth_required
bp = Blueprint('user', __name__)

@bp.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.get_by_username(username)
    
    if user is None:
        return {'message': 'User not found'}, 404
    if not user.check_password(password):
        return {'message': 'Wrong password'}, 401
    # generate token
    access_token = user.generate_access_token()
    refresh_token = user.generate_refresh_token()
    return {"status": "success", "message": "Request processed succesfully", 'access_token': access_token, "refresh_token":refresh_token, 'data': UserSchema().dump(user)}, 200

@bp.patch('/reset-password')
@auth_required()
def reset_password():
    new_password = request.json.get('password')
    if not new_password:
        return {'message': 'Password is required'}, 400
    elif len(new_password) < 6:
        return {'message': 'Password must be at least 6 characters'}, 400
    g.user.reset_password(new_password)
    return {'message': 'Password updated successfully', 'status':'success'}, 200

@bp.post('/register')
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')
    user = User.get_by_username(username)
    if user is not None:
        return {'message': 'User already exists', 'status':'failed'}, 400
    user = User.create(username, password, role)
    if user is not None:
        return {'message': 'User created successfully', 'status':'success'}, 201
    return {'message': 'User not created successfully', 'status':'failed'}, 400

@bp.post('/refresh')
@jwt_required(refresh=True)
def refresh():
    user = User.get_by_id(get_jwt_identity())
    # generate token
    access_token = user.generate_refreshed_access_token()
    return {"status": "success", "message": "Request processed succesfully", 'access_token': access_token}, 200

@bp.get('/users')
@auth_required()
def get_all_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    query = User.get_all()
    items, pagination = paginate(query, page=page, per_page=per_page)
    
    return {
        'data': UserSchema(many=True).dump(items), 
        'pagination': pagination,
        'message': 'Users fetched successfully', 
        'status': 'success'
    }, 200