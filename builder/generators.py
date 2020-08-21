from builder.config import args
from builder.file_strings import standard_blueprint_setup, standard_marshmallow, standard_model

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
        freeze()
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
        freeze()
        return True
    except Exception as e:
        print(e)
        return False

def generate_model():
    project = get_project_name()
    try:
        req = ['flask-sqlalchemy']
        with open(f"{project}/model.py", "w") as _app:
            _app.write(standard_model.replace("**project", project))
        
        with open(f"{project}/__init__.py", "r") as _app:
            _main = _app.read()
        _main = _main.replace("app = Flask(__name__)", f"app = Flask(__name__)\n\nfrom {project}.model import *\ndb.init_app(app)", 1)
        
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(_main)
        
        with open(f"{project}/dev.py", "r") as _app:
            _main = _app.read()
        with open(f"{project}/prod.py", "r") as _app:
            _main = _app.read()
        _main += "\nSQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' #REPLACE WITH YOUR ACTUAL DB URI"
        
        with open(f"{project}/dev.py", "r") as _app:
            _main = _app.read()
        with open(f"{project}/prod.py", "r") as _app:
            _main = _app.read()

        install(req)
        freeze()
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
        _main = _main.replace(f"from {project}.model import *\ndb.init_app(app)", 1)
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(_main)
        uninstall(req)
        freeze()
        return True
    except Exception as e:
        print(e)
        return False