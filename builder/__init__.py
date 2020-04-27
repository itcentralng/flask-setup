#!/usr/bin/env python

import subprocess
import sys
import os
from builder.file_strings import *

project, with_blueprint, blueprint_name = 'project', False, 'my_blueprint'

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def build_basic_app(project='project', with_blueprint=False, blueprint_name='my_blueprint'):
    os.mkdir(project)
    templates = f"{project}/templates"
    os.makedirs(templates)
    static = f"{project}/static"
    os.makedirs(static)
    with open(f"{templates}/index.html", "w") as _app:
        _app.write('<h1>Welcome to index page</h1>')
    with open(f"{templates}/404.html", "w") as _app:
        _app.write('<h1>Welcome to 404 page</h1>')
    with open(f"{project}/config.cfg", "w") as config:
        config.write(configuration)
    if with_blueprint:
        blueprint = f"{project}/{blueprint_name}"
        blueprint_templates = f"{blueprint}/templates/{blueprint_name}"
        os.makedirs(blueprint)
        os.makedirs(blueprint_templates)
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(basic_blueprint_app.replace('**project', project).replace("**my_blueprint", blueprint_name))
        with open(f"{blueprint}/__init__.py", "w") as _app:
            _app.write('')
        with open(f"{blueprint}/routes.py", "w") as _app:
            _app.write(basic_blueprint_setup.replace("**my_blueprint", blueprint_name))
        with open(f"{blueprint_templates}/index.html", "w") as _app:
            _app.write('<h1>Welcome to index page from blueprint</h1>')
    else:
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(basic_app)

def build_web_app(project='project', with_blueprint=False, blueprint_name='my_blueprint'):
    os.mkdir(project)
    templates = f"{project}/templates"
    os.makedirs(templates)
    static = f"{project}/static"
    os.makedirs(static)
    with open(f"{templates}/index.html", "w") as _app:
        _app.write('<h1>Welcome to index page</h1>')
    with open(f"{templates}/login.html", "w") as _app:
        _app.write('<h1>Welcome to login page</h1>')
    with open(f"{templates}/protected.html", "w") as _app:
        _app.write('<h1>Welcome to protected page</h1>')
    with open(f"{templates}/404.html", "w") as _app:
        _app.write('<h1>Welcome to 404 page</h1>')
    with open(f"{project}/config.cfg", "w") as config:
        config.write(configuration)
    with open(f"{project}/model.py", "w") as _app:
            _app.write(web_model.replace("**project", project))
    with open(f"{project}/methods.py", "w") as _app:
        _app.write(web_methods.replace("**project", project))
    with open(f"{project}/filters.py", "w") as _app:
        _app.write(web_filters.replace("**project", project))
    if with_blueprint:
        blueprint = f"{project}/{blueprint_name}"
        blueprint_templates = f"{blueprint}/templates/{blueprint_name}"
        os.makedirs(blueprint)
        os.makedirs(blueprint_templates)
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(web_blueprint_app.replace('**project', project).replace("**my_blueprint", blueprint_name))
        with open(f"{blueprint}/__init__.py", "w") as _app:
            _app.write('')
        with open(f"{blueprint}/routes.py", "w") as _app:
            _app.write(web_blueprint_setup.replace("**my_blueprint", blueprint_name).replace("**project", project))
        with open(f"{blueprint_templates}/index.html", "w") as _app:
            _app.write('<h1>Welcome to index page from blueprint</h1>')
        with open(f"{project}/marshmallow.py", "w") as _app:
            _app.write(web_marshmallow.replace("**project", project))
    else:
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(web_app.replace("**project", project))

def generate_blueprint(project=None, blueprint_name='blue'):
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
            _app.write(web_blueprint_setup.replace("**my_blueprint", blueprint_name).replace("**project", project))
        with open(f"{project}/__init__.py", "r") as _app:
            _main = _app.read()
        if "app.register_blueprint" in _main:
            _main = _main.replace("app.register_blueprint", f"from {project}.{blueprint_name}.routes import {blueprint_name}\napp.register_blueprint({blueprint_name})\napp.register_blueprint", 1)
        else:
            _main = _main.replace("@app.", f"from {project}.{blueprint_name}.routes import {blueprint_name}\napp.register_blueprint({blueprint_name})\n@app.", 1)
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(_main)
    except Exception as e:
        print(e)

def destroy_blueprint(project=None, blueprint_name='blue'):
    try:
        blueprint = f"{project}/{blueprint_name}"
        subprocess.call(f"rm -r {blueprint}", shell=True)
        with open(f"{project}/__init__.py", "r") as _app:
            _main = _app.read()
        _main = _main.replace(f"from {project}.{blueprint_name}.routes import {blueprint_name}\n", "")
        _main = _main.replace(f"app.register_blueprint({blueprint_name})\n", "")
        with open(f"{project}/__init__.py", "w") as _app:
            _app.write(_main)
    except Exception as e:
        print(e)

def build_package():
    global project, with_blueprint, blueprint_name
    project = [a for a in sys.argv if a.startswith('--')]
    project = 'project' if not project else project[0][2:]
    
    #Check for generate request first
    if "g" in sys.argv or "generate" in sys.argv:
        if "-blueprint" in sys.argv:
            if not sys.argv[-1].startswith('-'):
                blueprint_name = sys.argv[-1]
            generate_blueprint(project, blueprint_name)
    
    #Check for destroy request next
    elif "d" in sys.argv or "destroy" in sys.argv:
        if "-blueprint" in sys.argv:
            if not sys.argv[-1].startswith('-'):
                blueprint_name = sys.argv[-1]
            destroy_blueprint(project, blueprint_name)
    else:
        res = input("Please ensure you have created a virtual environment and have activated,\n do you have a virtual environment activate? \nProceed? y/n?")
        if res == 'y':
            req = ["flask"]
            print(f'Building your {project} environment please wait....')

            if "-basic" in sys.argv:
                if "-blueprint" in sys.argv:
                    with_blueprint = True
                try:
                    build_basic_app(project, with_blueprint, blueprint_name)
                except Exception as e:
                    print(e)
                    print('Project already exist, removing and reinitializing')
                    subprocess.call(f"rm -r {project}", shell=True)
                    build_basic_app(project, with_blueprint, blueprint_name)

            elif "-web" in sys.argv:
                req += ["flask-sqlalchemy", "flask-login", "flask-migrate", "flask-script", "flask-wtf", "arrow"]
                if "-blueprint" in sys.argv:
                    with_blueprint = True
                    if "-api" in sys.argv:
                        req+= ["flask-marshmallow", "marshmallow-sqlalchemy"]
                        blueprint_name = 'api'
                try:
                    build_web_app(project, with_blueprint, blueprint_name)
                except Exception as e:
                    print(e)
                    print('Project already exist, removing and reinitializing')
                    subprocess.call(f"rm -r {project}", shell=True)
                    build_web_app(project, with_blueprint, blueprint_name)
            for r in req:
                install(r)
            with open("run.py", "w") as _app:
                _app.write(app_run.replace("**project", project))
            with open("requirements.txt", "w") as _app:
                _app.write("\n".join(req))
            print('All done!!!')
        else:
            print('Restart flask_starter when you have an active virtualenv')