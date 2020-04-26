# flask-setup #
Flask Setup Tool

# INSTALLATION #
$ pip install flask-setup

# USAGE #

1. create a virtual environment and activate it:
   $ python -m venv venv
   $ source venv/bin/activate
   $ flask_setup help

# FLAGS #

1. -basic: Builds a basic flask app
    $ flask_setup -basic
    
2. -web: Builds a full web flask app
    $ flask_setup -web

3. -blueprint: this depends on the first two above. Adds
    blueprint to the project: e.g.
    $ flask_setup -basic -blueprint
    $ flask_setup -web -blueprint

4. -api: this adds flask-marshmallow and
    marshmallow-sqlalchemy to the project
    to help serialize your models e.g.:
    $ flask_setup -web -blueprint -api

5.  --project_name: you pass a double flag non-spaced 
    name to name your project default is 'project'. e.g.:
    $ flask_setup --myproject -basic -blueprint