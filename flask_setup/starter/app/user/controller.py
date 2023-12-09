from flask import Blueprint, g, request

from app.user.model import User
from app.user.schema import UserSchema
from app.route_guard import auth_required
bp = Blueprint('user', __name__)

@bp.post('/login')
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    
    user = User.get_by_email(email)
    
    if user is None:
        return {'message': 'User not found'}, 404
    if not user.check_password(password):
        return {'message': 'Wrong password'}, 401
    # generate token
    token = user.generate_token()
    return {'token': token, 'user': UserSchema().dump(user)}, 200

@bp.patch('/reset-password')
@auth_required()
def reset_password():
    new_password = request.json.get('password')
    if not new_password:
        return {'message': 'Password is required'}, 400
    elif len(new_password) < 6:
        return {'message': 'Password must be at least 6 characters'}, 400
    g.user.reset_password(new_password)
    return {'message': 'Password updated successfully'}, 200
    

@bp.post('/register')
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    role = request.json.get('role')
    user = User.get_by_email(email)
    if user is not None:
        return {'message': 'User already exists'}, 400
    user = User.create(email, password, role)
    if user is not None:
        return {'message': 'User created'}, 201
    return {'message': 'User not created'}, 400