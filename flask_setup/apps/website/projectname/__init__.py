
'''
projectname
--------------
'''
#Basic Flask Requirements
from flask import Flask, render_template

import os

#instance of app
app = Flask(__name__)

#cookie generator
app.secret_key = os.urandom(24)

#configs
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')
        