configuration = "SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/db'"

app_run = """
from **project import app
if __name__ =='__main__':
    app.run()
        """

sample_marshmallow_schema = """
class **modelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = **model
    include_fk = True
    include_relationship = True\n"""

sample_model = """
class **model(db.Model):
    id = db.Column(db.Integer, primary_key=True)\n"""

help_string = """"
# USAGE #

1. create a virtual environment and activate it:
   `$ python -m venv venv`
   `$ source venv/bin/activate`
   `$ flask_setup --flag argument`

# FLAGS #

1. --init or -i: Intialize Flask-Setup in project folder;
    `$ fs --init project_name` OR `$ fs -i project_name`

2. --build or -b: Takes flask app type to build; currently support ['api', 'basic', 'website']
    `$ fs --build api` OR `$ fs -b api`

3. --generate or -g: Takes generator type; currently supports ['model', 'marshmallow', 'blueprint'] e.g.
    `$ fs --generate blueprint --blueprint api` this will generate a blueprint with the name 'api'
    OR 
    `$ fs --generate model`

4.  --destroy or -d: pass this alongside a generator ['marshmallow', 'blueprint', 'model'] e.g.:
    `$ fs -d blueprint -blueprint myblueprintname`
    OR 
    `$ fs-d model`
5.  --add or -install: pass this alongside a module e.g.:
    `$ fs -a flask` this will install flask and freeze to requirements file
6.  --remove or -r: pass this alongside a module e.g.:
    `$ flask_setup -r flask` this will uninstall flask and freeze to requirements file
"""