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

0. init: Intialize Flask-Setup in project folder; this makes sure you dont need to pass
   project name each time you call flask_setup
    `$ flask_setup init --project_name`

1. -basic: Builds a basic flask app
    `$ flask_setup -basic`

2. -standard: Builds a full web flask app
    `$ flask_setup -standard`

3. b or -blueprint: this depends on the first two above. Adds
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

6.  -g or -generate: pass this alongside b or -blueprint flag to generate
    blueprint on existing project. e.g.:
    `$ flask_setup --myproject g -blueprint myblueprintname`
    or if you've called the `init` arg you can simply do:
    `$ flask_setup g -blueprint myblueprintname`

7.  -d or -destroy: pass this alongside b or -blueprint flag to remove a
    blueprint from existing project. e.g.:
    `$ flask_setup --myproject d -blueprint myblueprintname`
    or if you've called the `init` arg you can simply do:
    `$ flask_setup d -blueprint myblueprintname`

8.  -g or -generate: pass this alongside m or -marshmallow flag to generate
    marshmallow on existing project. e.g.:
    `$ flask_setup --myproject g -marshmallow`
    or if you've called the `init` arg you can simply do:
    `$ flask_setup g -marshmallow`

9.  -d or -destroy: pass this alongside m or -marshmallow flag to remove a
    marshmallow setup from existing project. e.g.:
    `$ flask_setup --myproject d -marshmallow`
    or if you've called the `init` arg you can simply do:
    `$ flask_setup d -marshmallow`
10.  -g or -generate: pass this alongside -model flag to generate
    model on existing project. e.g.:
    `$ flask_setup --myproject g -model`
    or if you've called the `init` arg you can simply do:
    `$ flask_setup g -model`

11.  -d or -destroy: pass this alongside -model flag to remove a
    model setup from existing project. e.g.:
    `$ flask_setup --myproject d -model`
    or if you've called the `init` arg you can simply do:
    `$ flask_setup d -model`