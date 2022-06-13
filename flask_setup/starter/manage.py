from datetime import datetime
from app import app
from app.user.model import User

with app.app_context():
    pass
    # TODO:
    # Remove the pass keyword and
    # Run some actions you want to be be performed
    # on your server either when deployed or locally.
    # TODO: WARNING: This will also execute when deployed
    print('Ready!')