from flask import Blueprint, g, jsonify, request

from app.user.model import User
from app.user.schema import UserSchema
bp = Blueprint('user', __name__)

@bp.post('/login')
def login():
    data = request.json
    
    email = data.get('email')
    user = User.get_by_email(email)
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    if not user.check_password(data.get('password')):
        return jsonify({'message': 'Wrong password'}), 401
    # generate token
    token = user.generate_token()
    return jsonify({'token': token, 'user': UserSchema().dump(user)}), 200

@bp.patch('/update-password')
def update_password():
    data = request.json
    user = User.get_by_email(data.get('email'))
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    if user.update_password(data.get('password'), data.get('new_password')):
        return jsonify({'message': 'Password updated'}), 200
    return jsonify({'message': 'Wrong password'}), 401