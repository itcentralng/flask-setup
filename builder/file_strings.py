configuration = "THIS_IS_A_SAMPLE_CONFIG_VARIABLE = \'this is a _sample Config VALUE\'"

app_run = """
from **project import app
if __name__ =='__main__':
    app.run()
        """

basic_app = """
'''
API APP
--------------
BASIC APP INITIALIZER.
'''
#Basic Flask Requirements
from flask import Flask, request, render_template, url_for, redirect, session, flash

import os

#instance of app
app = Flask(__name__)

#cookie generator
app.secret_key = os.urandom(24)

#configs
app.config.from_pyfile('config.cfg')

@app.context_processor
def app_wide_variables():
    '''
    Function takes no argument,
    returns variables that are accessible everywhere in the app

    #TODO: pass *kwargs to dict
    '''
    return dict()


@app.route('/')
def index():
    return render_template('index.html')

#A Simple 404 error page
@app.errorhandler(404)
def page404(e):
    return render_template('404.html')
        """

web_app = """
'''
    app
    --------------
    Main app initializer.
'''
#Basic Flask Requirements
from flask import Flask, request, render_template, url_for, redirect, session, flash, Response, make_response, send_file, send_from_directory, make_response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

import os

from **project.model import db

#instance of app
app = Flask(__name__)

#cookie generator
app.secret_key = os.urandom(24)

#configs
app.config.from_pyfile('config.cfg')

db.init_app(app)

from **project import filters
from **project.model import User
from **project.methods import do_login

#Flask Login Setup
LOGINMANAGER = LoginManager()
LOGINMANAGER.init_app(app)
LOGINMANAGER.login_view = 'index'

#Loading Users to Flask-Login
@LOGINMANAGER.user_loader
def load_user(username):
    '''
    Queries and loads all users from the db module.
    '''
    #Getting all users from the database
    return User.query.get(username)

@app.context_processor
def app_wide_variables():
    '''
    Function takes no argument,
    returns variables that are accessible everywhere in the app

    #TODO: pass *kwargs to dict
    '''
    return dict()

#Index Route or Login Route
@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    Index function takes no argument,
    routes to the '/' page and holds the login logic.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('protected_route'))
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        if do_login(user, password):
            if 'next' in request.args:
                return redirect(request.args['next'])
            return redirect(url_for('protected'))
        flash('Invalid Login Details!')
    return render_template("login.html")

#Dashboard
@app.route('/protected-route')
@login_required
def protected_route():
    '''
    Sample protected route, change it to your test
    '''
    return render_template('protected.html')


#Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('protected_route'))

#A Simple 404 error page
@app.errorhandler(404)
def page404(e):
    return render_template('404.html')
        """

web_blueprint_app = """
'''
    app
    --------------
    Main app initializer.
'''
#Basic Flask Requirements
from flask import Flask, request, render_template, url_for, redirect, session, flash, Response, make_response, send_file, send_from_directory, make_response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

import os

from **project.model import db

#instance of app
app = Flask(__name__)

#cookie generator
app.secret_key = os.urandom(24)

#configs
app.config.from_pyfile('config.cfg')

db.init_app(app)

from **project import filters
from **project.model import User
from **project.methods import do_login

#Flask Login Setup
LOGINMANAGER = LoginManager()
LOGINMANAGER.init_app(app)
LOGINMANAGER.login_view = 'index'

#Loading Users to Flask-Login
@LOGINMANAGER.user_loader
def load_user(username):
    '''
    Queries and loads all users from the db module.
    '''
    #Getting all users from the database
    return User.query.get(username)

#TODO: Register more blueprints like this
# Check the blueprint folder for more info
from **project.**my_blueprint.routes import **my_blueprint
app.register_blueprint(**my_blueprint)

@app.context_processor
def app_wide_variables():
    '''
    Function takes no argument,
    returns variables that are accessible everywhere in the app

    #TODO: pass *kwargs to dict
    '''
    return dict()

#Index Route or Login Route
@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    Index function takes no argument,
    routes to the '/' page and holds the login logic.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('protected_route'))
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        if do_login(user, password):
            if 'next' in request.args:
                return redirect(request.args['next'])
            return redirect(url_for('protected'))
        flash('Invalid Login Details!')
    return render_template("login.html")

#Dashboard
@app.route('/protected-route')
@login_required
def protected_route():
    '''
    Sample protected route, change it to your test
    '''
    return render_template('protected.html')


#Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('protected_route'))

#A Simple 404 error page
@app.errorhandler(404)
def page404(e):
    return render_template('404.html')
        """

basic_blueprint_app = """
'''
API APP
--------------
API BASED APP INITIALIZER.
'''
#Basic Flask Requirements
from flask import Flask, request, render_template, url_for, redirect, session, flash

import os

#instance of app
app = Flask(__name__)

#cookie generator
app.secret_key = os.urandom(24)

#configs
app.config.from_pyfile('config.cfg')

#TODO: 
# Modify this import to reflect your desired blueprint
# Check blue print folder for more
from **project.**my_blueprint.routes import **my_blueprint

# TODO: 
# You can register more blueprints here
app.register_blueprint(**my_blueprint)

@api.route('/')
def index():
    return render_template('index.html')
        """
    
basic_blueprint_setup = """
'''
MY BLUEPRINT
--------------
MY BLUEPRINT INITIALIZER.
'''
from flask import Blueprint, request, render_template, redirect, url_for

**my_blueprint = Blueprint('**my_blueprint', __name__, url_prefix='/**my_blueprint')

@**my_blueprint.route('/')
def index():
    return render_template('**my_blueprint/index.html')
        """

web_blueprint_setup = """
'''
MY BLUEPRINT
--------------
MY BLUEPRINT INITIALIZER.
'''
from flask import Blueprint, request, render_template, redirect, url_for

from **project.marshmallow import UserSchema

from **project.model import User

**my_blueprint = Blueprint('**my_blueprint', __name__)

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(exclude=['password'], many=True)

@**my_blueprint.route('/users')
def teacher_():
    users = User.query.all()
    # return {'result':users_schema.dump(users)}
    return users_schema.jsonify(users)
        """

web_model = """
'''
MY MODEL
--------------
'''
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash as gph, check_password_hash as cph

db = SQLAlchemy()

#Model Sample
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    def set_password(self, password):
        self.password = gph(password)
        return True
    def is_verified(self, password):
        return cph(self.password, password)
        """

web_marshmallow = """
'''
MY MARSHMALLOW
--------------
'''
from **project.model import *

from flask_marshmallow import Marshmallow

from **project import app

ma = Marshmallow(app)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        """

web_methods = """
'''
MY METHODS
--------------
'''
import arrow

#MODELS
from **project.model import *
from **project import login_user

#EXAMPLE METHOD
def do_login(phone, password):
    user = User.query.filter_by(phone=phone).first()
    if user and user.is_verified(password):
        return True
    return False

def returnTrue():
    return True
        """

web_filters = """
'''
MY FILTERS
--------------
'''
from **project import app
from **project.methods import returnTrue

#HERE THERE ARE TWO WAYS OF USING FILTERS

#EITHER BY USING DEFINED FUNCTIONS
app.jinja_env.filters['returnTrue'] = returnTrue

#OUR DEFINING THE FUNCTION WITH A FILTER DECORATOR
@app.template_filter()
def roundit(number, point=1):
    return round(number, point)
        """