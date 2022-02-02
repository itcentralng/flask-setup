import os, subprocess
import shutil

from flask_setup.config import args

from flask_setup.methods import get_project_name, install, uninstall

from distutils.dir_util import copy_tree

def generate_blueprint():
    project = get_project_name()
    blueprint_name = args.blueprint
    content = ""
    try:
        # make blueprint folder
        os.mkdir(f"{project}/{blueprint_name}")
        path = os.path.dirname(os.path.realpath(__file__))
        # copy blueprint files
        copy_tree(f"{path}/generators/blueprint", f"{project}/{blueprint_name}")
        # rename templates folder
        os.rename(f"{project}/{blueprint_name}/templates/blueprintname", f"{project}/{blueprint_name}/templates/{blueprint_name}")
        # replace blueprint name
        with open(f"{project}/{blueprint_name}/routes.py", "r") as blueprint:
            content = blueprint.read()
            content = content.replace("blueprintname", blueprint_name)
        with open(f"{project}/{blueprint_name}/routes.py", "w") as blueprint:
            blueprint.write(content)
        # add blueprint to __init__.py
        with open(f"{project}/__init__.py", "r") as main_app:
            # check if there is already a blueprint and add this after it
            content = main_app.read()
            if "app.register_blueprint" in main_app:
                # find the last blueprint
                last_blueprint = content.rfind(".register_blueprint")
                # add the new blueprint
                content = content.replace(content[last_blueprint:], f"\nfrom {project}.{blueprint_name}.routes import {blueprint_name}\napp.register_blueprint({blueprint_name})\n")
            else:
                # add the new blueprint
                content = content.replace("app = Flask(__name__)", f"app = Flask(__name__)\n\nfrom {project}.{blueprint_name}.routes import {blueprint_name}\napp.register_blueprint({blueprint_name})\n")
            with open(f"{project}/__init__.py", "w") as main_app:
                main_app.write(content)
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
        with open(f"{project}/__init__.py", "r") as main_app:
            content = main_app.read()
        content = content.replace(f"from {project}.{blueprint_name}.routes import {blueprint_name}\n", "")
        content = content.replace(f"app.register_blueprint({blueprint_name})\n", "")
        with open(f"{project}/__init__.py", "w") as main_app:
            main_app.write(content)
        print(f'Blueprint: "{blueprint_name}" successfully destroyed')
        return True
    except Exception as e:
        print(e)
        return False

def generate_marshmallow():
    project = get_project_name()
    try:
        req = ['flask-marshmallow', 'marshmallow-sqlalchemy']
        path = os.path.dirname(os.path.realpath(__file__))
        # copy marshmallow files
        shutil.copyfile(f"{path}/generators/marshmallow.py", f"{project}/marshmallow.py")
        # replace project name
        with open(f"{project}/marshmallow.py", "r") as marsh:
            content = marsh.read()
        content = content.replace("projectname", project)
        with open(f"{project}/marshmallow.py", "w") as marsh:
            marsh.write(content)
        install(req)
        print(f'Marshmallow successfully generated')
        return True

    except Exception as e:
        print(e)
        return False

def destroy_marshmallow():
    project = get_project_name()
    try:
        subprocess.call(f"rm {project}/marshmallow.py", shell=True)
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
        # get the original path to this file even when imported from another file
        path = os.path.dirname(os.path.realpath(__file__))
        # copy model files
        shutil.copyfile(f"{path}/generators/model.py", f"{project}/model.py")
        # replace project name
        with open(f"{project}/model.py", "r") as model:
            content = model.read()
        content = content.replace("projectname", project)
        with open(f"{project}/model.py", "w") as model:
            model.write(content)
        # add model to __init__.py
        with open(f"{project}/__init__.py", "r") as main_app:
            content = main_app.read()
            if f"from {project}.model import db" in content:
                pass
            else:
                content = content.replace("app.config.from_object('config')", f"app.config.from_object('config')\n\nfrom {project}.model import db\ndb.init_app(app)\n")
            with open(f"{project}/__init__.py", "w") as main_app:
                main_app.write(content)
        install(req)
        print(f'Model successfully generated')
        return True

    except Exception as e:
        print(e)
        return False

def destroy_model():
    project = get_project_name()
    try:
        subprocess.call(f"rm {project}/model.py", shell=True)
        req = ['flask-sqlalchemy']
        with open(f"{project}/__init__.py", "r") as main_app:
            content = main_app.read()
        content = content.replace(f"\n\nfrom {project}.model import db\ndb.init_app(app)\n", "")
        with open(f"{project}/__init__.py", "w") as main_app:
            main_app.write(content)
        uninstall(req)
        print(f'Model successfully destroyed')
        return True
    except Exception as e:
        print(e)
        return False