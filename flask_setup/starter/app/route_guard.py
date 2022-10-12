from flask import jsonify, request, g
from app import app
import jwt
from jwt import DecodeError, ExpiredSignatureError, InvalidSignatureError

from functools import wraps

from app.user.model import User


def auth_required(*roles_required):
    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({"message": "Missing Authorization Header"}), 401
            try:
                token = auth_header.split(' ')[1]
                payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=["HS256"])
                auth_id = payload['sub']
                roles = payload['roles']
                # check role
                if roles_required:
                    if not any(role in roles for role in roles_required):
                        return jsonify({"message": "Unauthorized to perform action"}), 401
            except ExpiredSignatureError:
                return jsonify({"message": "Expired or Invalid Token"}), 401
            except InvalidSignatureError:
                return jsonify({"message": "Invalid Token"}), 401
            except DecodeError:
                return jsonify({"message": "Malformed Token"}), 401
            except Exception as e:
                return jsonify({"message": "Unknown Error"}), 401
            g.user = User.get_by_id(auth_id)
            return f(*args, **kwargs)
        return decorated
    return requires_auth