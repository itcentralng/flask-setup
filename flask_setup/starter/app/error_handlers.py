from flask import jsonify
from marshmallow import ValidationError
from app import app


@app.errorhandler(ValueError)
def handle_value_error(error):
    response = {
        'status': 'error',
        'message': str(error)
    }
    return response, 400

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = {
        'status': 'error',
        'fields': error.messages

    }
    return response, 400