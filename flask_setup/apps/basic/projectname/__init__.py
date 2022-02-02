
'''
projectname
--------------
'''
#Basic Flask Requirements
from flask import Flask

import os

#instance of app
app = Flask(__name__)

#cookie generator
app.secret_key = os.urandom(24)

#configs
app.config.from_object('config')

@app.route('/')
def index():
    return {'name': 'projectname', 'version': '0.0.1', 'status': 'OK'}
        