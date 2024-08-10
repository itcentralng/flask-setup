from app import app, db

@app.errorhandler(Exception)
def handle_exception(error):
    db.session.rollback()
    return {
        'status': 'error',
        'message': str(error)
    }, 400