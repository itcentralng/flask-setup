# flask-setup #
Flask Setup Tool

# INSTALLATION #
`$ pip install flask-setup`

# USAGE #

1. create a virtual environment and activate it:
   `$ python -m venv venv`
   `$ source venv/bin/activate`
   `$ fs --flag argument`

# USAGE DETAILS #

1. --init or -i: Intialize Flask-Setup in project folder; this makes sure you dont need to pass
   project name each time you call flask_setup
    `$ fs --init project_name` OR `$ fs -i project_name`

2. --build or -b: Takes flask app type to build; currently support ['api', 'standard', 'basic']
    `$ fs --build api` OR `$ fs -b api`

3. --generate or -g: Takes generator type; currently supports ['model', 'marshmallow', 'blueprint'] e.g.
    `$ fs --generate blueprint -blueprint api` this will generate a blueprint with the name 'api'
    OR 
    `$ fs --generate model`

4.  --destroy or -d: pass this alongside a generator ['marshmallow', 'blueprint', 'model'] e.g.:
    `$ fs -d blueprint -blueprint myblueprintname`
    OR 
    `$ fs -d model`
5.  --add or -a: pass this alongside a module e.g.:
    `$ fs -install flask` this will install flask and freeze to requirements file
6.  --remove or -r: pass this alongside a module e.g.:
    `$ fs -remove flask` this will uninstall flask and freeze to requirements file