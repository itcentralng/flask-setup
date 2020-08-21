# flask-setup #
Flask Setup Tool

# INSTALLATION #
`$ pip install flask-setup`

# USAGE #

1. create a virtual environment and activate it:
   `$ python -m venv venv`
   `$ source venv/bin/activate`
   `$ flask_setup --flag argument`

# FLAGS #

1. --init or -i: Intialize Flask-Setup in project folder; this makes sure you dont need to pass
   project name each time you call flask_setup
    `$ flask_setup --init project_name` OR `$ flask_setup -i project_name`

2. --build or -b: Takes flask app type to build; currently support ['api', 'standard', 'basic']
    `$ flask_setup --build api` OR `$ flask_setup -b api`

3. --generate or -g: Takes generator type; currently supports ['model', 'marshmallow', 'blueprint'] e.g.
    `$ flask_setup --generate blueprint -blueprint api` this will generate a blueprint with the name 'api'
    OR 
    `$ flask_setup --generate model`

4.  --destroy or -d: pass this alongside a generator ['marshmallow', 'blueprint', 'model'] e.g.:
    `$ flask_setup -d blueprint -blueprint myblueprintname`
    OR 
    `$ flask_setup -d model`