# flask-setup #
Flask Setup Tool

# INSTALLATION #
`$ pip install flask-setup`

# USAGE #

1. create a virtual environment and activate it:
   `$ python -m venv venv`
   `$ source venv/bin/activate`
   `$ flask_setup help`

# FLAGS #

1. -basic: Builds a basic flask app
    `$ flask_setup -basic`

2. -standard: Builds a full web flask app
    `$ flask_setup -standard`

3. -blueprint: this depends on the first two above. Adds
    blueprint to the project: e.g.
    `$ flask_setup -basic -blueprint`
    `$ flask_setup -standard -blueprint`

4. -api: this adds flask-marshmallow and
    marshmallow-sqlalchemy to the project
    to help serialize your models e.g.:
    `$ flask_setup -standard -blueprint -api`

5.  --project_name: you pass a double flag non-spaced 
    name to name your project default is 'project'. e.g.:
    `$ flask_setup --myproject -basic -blueprint`

6.  -g or -generate: pass this alongside -blueprint flag to generate
    blueprint on existing project. e.g.:
    `$ flask_setup --myproject g -blueprint myblueprintname`

7.  -d or -destroy: pass this alongside -blueprint flag to remove a
    blueprint from existing project. e.g.:
    `$ flask_setup --myproject d -blueprint myblueprintname`

8.  -g or -generate: pass this alongside -marshmallow flag to generate
    marshmallow on existing project. e.g.:
    `$ flask_setup --myproject g -marshmallow`

9.  -d or -destroy: pass this alongside -marshmallow flag to remove a
    marshmallow setup from existing project. e.g.:
    `$ flask_setup --myproject d -marshmallow`