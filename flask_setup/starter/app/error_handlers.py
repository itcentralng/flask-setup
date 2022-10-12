from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, DatabaseError, DataError
from app import app, db


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

@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(error):
    db.session.rollback()
    response = {
        'status': 'error',
        'message': str(error)
    }
    return response, 400

@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    db.session.rollback()
    response = {
        'status': 'error',
        'message': str(error)
    }
    return response, 400

@app.errorhandler(OperationalError)
def handle_operational_error(error):
    db.session.rollback()
    response = {
        'status': 'error',
        'message': str(error)
    }
    return response, 400

@app.errorhandler(DatabaseError)
def handle_database_error(error):
    db.session.rollback()
    response = {
        'status': 'error',
        'message': str(error)
    }
    return response, 400

@app.errorhandler(DataError)
def handle_data_error(error):
    db.session.rollback()
    response = {
        'status': 'error',
        'message': str(error)
    }
    return response, 400

@app.errorhandler(Exception)
def handle_exception(error):
    db.session.rollback()
    response = {
        'status': 'error',
        'message': str(error)
    }
    return response, 400