import os, subprocess

from fs.config import args

from fs.methods import get_project_name, install, uninstall

from fs.file_strings import standard_blueprint_setup, standard_marshmallow, standard_model

def generate_blueprint():
    project = get_project_name()
    blueprint_name = args.blueprint
    try:
        blueprint = f"{project}/{blueprint_name}"
        os.makedirs(blueprint)
        templates = f"{blueprint}/templates"
        os.makedirs(templates)
        static = f"{blueprint}/static"
        os.makedirs(static)
        with open(f"{blueprint}/__init__.py", "w") as _app:
            _app.write('')
        with open(f"{blueprint}/routes.py", "w") as _app:
            _app.write(standard_blueprint_setup.replace("**my_blueprint", blueprint_name).replace("**project", project))
        with open(f"{project}/__init__.py", "r") as _app:
            _main = _app.read()
        if "app.register_blueprint" in _main:
            _main = _main.replace("app.register_blueprint", f"from {project}.{blueprint_name}.routes import {blueprint_name}\napp.register_blueprint({blueprint_name})\napp.register_blueprint", 1)
        
        elif "#Blueprints" in _main:
            _main = _main.replace("#Blueprints", f"#Blueprints\nfrom {project}.{blueprint_name}.routes import {blueprint_name}\napp.register_blueprint({blueprint_name})", 1)
        
        else:
            _main = _main.replace("@app.", f"#Blueprints\nfrom {project}.{blueprint_name}.routes import {blueprint_name}\napp.register_blueprint({blueprint_name})\n\n@app.", 1)
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(_main)
        print(f'Blueprint: "{blueprint_name}" successfully generated')
        return True
    except Exception as e:
        print(e)
        return False

def destroy_blueprint():
    project = get_project_name()
    blueprint_name = args.blueprint
    try:
        blueprint = f"{project}/{blueprint_name}"
        subprocess.call(f"rm -r {blueprint}", shell=True)
        with open(f"{project}/__init__.py", "r") as _app:
            _main = _app.read()
        _main = _main.replace(f"from {project}.{blueprint_name}.routes import {blueprint_name}\n", "")
        _main = _main.replace(f"app.register_blueprint({blueprint_name})\n", "")
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(_main)
        print(f'Blueprint: "{blueprint_name}" successfully destroyed')
        return True
    except Exception as e:
        print(e)
        return False

def generate_marshmallow():
    project = get_project_name()
    try:
        req = ['flask-marshmallow', 'marshmallow-sqlalchemy']
        with open(f"{project}/marshmallow.py", "w") as _app:
            _app.write(standard_marshmallow.replace("**project", project))

        install(req)
        print(f'Marshmallow successfully generated')
        return True

    except Exception as e:
        print(e)
        return False

def destroy_marshmallow():
    project = get_project_name()
    try:
        subprocess.call(f"rm r {project}/marshmallow.py", shell=True)
        req = ['flask-marshmallow', 'marshmallow-sqlalchemy']
        uninstall(req)
        print(f'Marshmallow successfully destroyed')
        return True
    except Exception as e:
        print(e)
        return False

def generate_model():
    project = get_project_name()
    try:
        req = ['flask-sqlalchemy']
        config = f"{project}/config"
        with open(f"{project}/model.py", "w") as _app:
            _app.write(standard_model.replace("**project", project))
        
        with open(f"{project}/__init__.py", "r") as _app:
            _main = _app.read()
        _main = _main.replace("app = Flask(__name__, instance_relative_config=False)", f"app = Flask(__name__, instance_relative_config=False)\n\nfrom {project}.model import *\ndb.init_app(app)", 1)
        
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(_main)
        
        with open(f"{config}/dev.py", "r") as _app:
            _main = _app.read()
        _main += "\nSQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' #REPLACE WITH YOUR ACTUAL DB URI"
        with open(f"{config}/prod.py", "r") as _app:
            _main = _app.read()
        _main += "\nSQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' #REPLACE WITH YOUR ACTUAL DB URI"
        
        install(req)
        print(f'Model successfully generated')
        return True

    except Exception as e:
        print(e)
        return False

def destroy_model():
    project = get_project_name()
    try:
        subprocess.call(f"rm r {project}/model.py", shell=True)
        req = ['flask-sqlalchemy']
        with open(f"{project}/__init__.py", "r") as _app:
            _main = _app.read()
        _main = _main.replace(f"from {project}.model import *\ndb.init_app(app)", "")
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(_main)
        uninstall(req)
        print(f'Model successfully generated')
        return True
    except Exception as e:
        print(e)
        return False