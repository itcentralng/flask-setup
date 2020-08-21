from fs.file_strings import configuration, standard_app, basic_app, standard_filters, basic_blueprint_app, basic_blueprint_setup, standard_blueprint_app, standard_blueprint_setup, standard_methods, standard_filters

from fs.methods import install, uninstall, get_project_name

from fs.config import args

import os

def build_basic_app(api=None):
    try:
        project = get_project_name()
        blueprint_name = args.blueprint if args.blueprint else api
        req = ["flask"] #requirements
        blueprint_name = args.blueprint
        os.mkdir(project)
        templates = f"{project}/templates"
        os.makedirs(templates)
        static = f"{project}/static"
        os.makedirs(static)
        config = f"{project}/config"
        os.makedirs(config)
        with open(f"{templates}/index.html", "w") as _app:
            _app.write('<h1>Welcome to index page</h1>')
        with open(f"{templates}/404.html", "w") as _app:
            _app.write('<h1>Welcome to 404 page</h1>')
        with open(f"{config}/dev.py", "w") as _config:
            _config.write(configuration)
        with open(f"{config}/prod.py", "w") as _config:
            _config.write(configuration)
        if blueprint_name:
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
                _app.write(basic_app.replace("**project", project))
        install(req)
        print('App built successfully')
        return True
    except Exception as e:
        print(e)
        print(f'Perhaps the project: "{project}" already exists')
    return False


def build_standard_app():
    try:
        project = get_project_name()
        req = ["flask", "flask-sqlalchemy", "flask-login", "flask-migrate", "flask-script", "flask-wtf", "arrow"] #requirements
        blueprint_name = args.blueprint
        os.mkdir(project)
        templates = f"{project}/templates"
        os.makedirs(templates)
        static = f"{project}/static"
        os.makedirs(static)
        config = f"{project}/config"
        os.makedirs(config)
        with open(f"{templates}/index.html", "w") as _app:
            _app.write('<h1>Welcome to index page</h1>')
        with open(f"{templates}/login.html", "w") as _app:
            _app.write('<h1>Welcome to login page</h1>')
        with open(f"{templates}/protected.html", "w") as _app:
            _app.write('<h1>Welcome to protected page</h1>')
        with open(f"{templates}/404.html", "w") as _app:
            _app.write('<h1>Welcome to 404 page</h1>')
        with open(f"{config}/dev.py", "w") as _config:
            _config.write(configuration)
        with open(f"{config}/prod.py", "w") as _config:
            _config.write(configuration)
        with open(f"{project}/model.py", "w") as _app:
                _app.write(standard_model.replace("**project", project))
        with open(f"{project}/methods.py", "w") as _app:
            _app.write(standard_methods.replace("**project", project))
        with open(f"{project}/filters.py", "w") as _app:
            _app.write(standard_filters.replace("**project", project))
        if blueprint_name:
            blueprint = f"{project}/{blueprint_name}"
            blueprint_templates = f"{blueprint}/templates/{blueprint_name}"
            os.makedirs(blueprint)
            os.makedirs(blueprint_templates)
            with open(f"{project}/__init__.py", "w") as _app:
                _app.write(standard_blueprint_app.replace('**project', project).replace("**my_blueprint", blueprint_name))
            with open(f"{blueprint}/__init__.py", "w") as _app:
                _app.write('')
            with open(f"{blueprint}/routes.py", "w") as _app:
                _app.write(standard_blueprint_setup.replace("**my_blueprint", blueprint_name).replace("**project", project))
            with open(f"{blueprint_templates}/index.html", "w") as _app:
                _app.write('<h1>Welcome to index page from blueprint</h1>')
            with open(f"{project}/marshmallow.py", "w") as _app:
                _app.write(standard_marshmallow.replace("**project", project))
        else:
            with open(f"{project}/__init__.py", "w") as _app:
                _app.write(standard_app.replace("**project", project))
        install(req)
        print('App built successfully')
        return True
    except Exception as e:
        print(e)
        print(f'Perhaps the project: "{project}" already exists')
        return False

def build_app(_type):
    allowed_apps = ['api', 'basic', 'standard']
    if _type in allowed_apps:
        if _type == 'basic':
            return build_basic_app()
        elif _type == 'standard':
            return build_standard_app()
        return build_basic_app(_type)
    return False