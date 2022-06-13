from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

# Configure app
app = Flask(__name__, )
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

from config import secret
app.secret_key = secret
migrate = Migrate(app, db)


# Register controllers
from app.user.controller import bp as user_bp
app.register_blueprint(user_bp)

# Error handlers
from .error_handlers import *