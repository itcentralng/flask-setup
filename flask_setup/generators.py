import os, subprocess
import re
import shutil

from flask_setup.config import args

from flask_setup.methods import get_project_name, install, uninstall
from flask_setup.file_strings import sample_marshmallow_schema, sample_model

from distutils.dir_util import copy_tree

def generate_blueprint():
    project = get_project_name()
    blueprint_name = args.name if args.name else 'api'
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
            # check if 'app.register_blueprint' is in content
            if "app.register_blueprint" in content:
                # find the last blueprint
                last_blueprint = content.rfind(".register_blueprint")
                # find the immediate line after the last blueprint
                next_line = content.find("\n", last_blueprint)
                # add the new blueprint after the last blueprint
                content = content[:next_line] + f"\nfrom {project}.{blueprint_name}.routes import {blueprint_name}\napp.register_blueprint({blueprint_name})" + content[next_line:]
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
    blueprint_name = args.name
    try:
        blueprint = f"{project}/{blueprint_name}"
        subprocess.call(f"rm -r {blueprint}", shell=True)
        with open(f"{project}/__init__.py", "r") as main_app:
            content = main_app.read()
        content = content.replace(f"\nfrom {project}.{blueprint_name}.routes import {blueprint_name}", "")
        content = content.replace(f"\napp.register_blueprint({blueprint_name})", "")
        with open(f"{project}/__init__.py", "w") as main_app:
            main_app.write(content)
        print(f'Blueprint: "{blueprint_name}" successfully destroyed')
        return True
    except Exception as e:
        print(e)
        return False

def generate_marshmallow():
    project = get_project_name()
    name = args.name if args.name else None
    try:
        # check if marshmallow.py already exists
        if not os.path.isfile(f"{project}/marshmallow.py"):
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
            if name:
                # check if model of the same name exists in model.py
                with open(f"{project}/model.py", "r") as model:
                    content = model.read()
                    if not f'class {name.capitalize()}' in content:
                        print(f"Please create a db model named: {name.capitalize()} first")
                        return False
                print(f'Adding {name}Schema to marshamallow.py')
                # open marshmallow.py and sample_marshmallow_schema
                with open(f"{project}/marshmallow.py", "a") as marsh:
                    marsh.write(sample_marshmallow_schema.replace('**model', name.capitalize()))
                print(f'Done!')
            return True
        if name:
            # check if model of the same name exists in model.py
            with open(f"{project}/model.py", "r") as model:
                content = model.read()
                if not f'class {name.capitalize()}' in content:
                    print(f"Please create a db model named: {name.capitalize()} first")
                    return False
            # check if the schema already exists
            with open(f"{project}/marshmallow.py", "r") as marsh:
                content = marsh.read()
            if f"{name.capitalize()}Schema" in content:
                print(f'{name.capitalize()}Schema already exists')
                return False
            print(f'Adding {name}Schema to marshamallow.py')
            # open marshmallow.py and sample_marshmallow_schema
            with open(f"{project}/marshmallow.py", "a") as marsh:
                marsh.write(sample_marshmallow_schema.replace('**model', name.capitalize()))
            print(f'Done!')
        else:
            print('No model provided or marshmallow.py already exists')
        return True

    except Exception as e:
        print(e)
        return False

def destroy_marshmallow():
    project = get_project_name()
    name = args.name if args.name else None
    try:
        if name:
            name = f'class {name.capitalize()}Schema'
            with open(f"{project}/marshmallow.py", "r") as marsh:
                content = marsh.read()
            # use regex to find the line with the schema
            schema_line = re.search(f'\n{name}', content)
            if schema_line:
                # get the line number of the schema
                start_line = schema_line.start()
                # get the line number of the end of the schema
                end_line = content.find("\n\n", start_line)
                # remove the schema
                content = content[:start_line-1] + content[end_line:]
                with open(f"{project}/marshmallow.py", "w") as marsh:
                    marsh.write(content)
                    print(f'{name} removed')
            else:
                print(f'{name} not found')
        else:
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
    name = args.name if args.name else None
    try:
        # check if model.py already exists
        if not os.path.isfile(f"{project}/model.py"):
            req = ['flask-sqlalchemy', 'flask-migrate']
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
                    content = content.replace("app.config.from_object('config')", f"app.config.from_object('config')\n\nfrom {project}.model import db\ndb.init_app(app)\nfrom flask_migrate import Migrate\nmigrate = Migrate(app, db)\n")
                with open(f"{project}/__init__.py", "w") as main_app:
                    main_app.write(content)
            install(req)
            print(f'Model successfully generated')
            if name:
                print(f'Adding {name} to model.py')
                # open model.py and sample_model
                with open(f"{project}/model.py", "a") as model:
                    model.write(sample_model.replace('**model', name.capitalize()))
                print(f'Done!')
            return True
        if name:
            # check if the model already exists
            with open(f"{project}/model.py", "r") as model:
                content = model.read()
            if f"class {name.capitalize()}" in content:
                print(f'{name.capitalize()} already exists')
                return False
            print(f'Adding {name} to model.py')
            # open model.py and sample_model
            with open(f"{project}/model.py", "a") as model:
                model.write(sample_model.replace('**model', name.capitalize()))
            print(f'Done!')
        else:
            print('No model provided or model.py already exists')
        return True

    except Exception as e:
        print(e)
        return False

def destroy_model():
    project = get_project_name()
    name = args.name if args.name else None
    try:
        if name:
            name = f'class {name.capitalize()}'
            with open(f"{project}/model.py", "r") as model:
                content = model.read()
            # use regex to find the line with the model
            model_line = re.search(f'\n{name}', content)
            if model_line:
                # get the line number of the model
                start_line = model_line.start()
                # get the line number of the end of the model
                end_line = content.find("\n\n", start_line)
                # remove the model
                content = content[:start_line-1] + content[end_line:]

                with open(f"{project}/model.py", "w") as model:
                    model.write(content)
                    print(f'{name} removed')
            else:
                print(f'{name} not found')
        else:
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