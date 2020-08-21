from builder.file_strings import configuration, standard_app, basic_app, standard_filters, basic_blueprint_app, basic_blueprint_setup, standard_blueprint_app, standard_blueprint_setup, standard_methods, standard_filters

from builder.methods import install, uninstall, get_project_name

from builder.config import args

def build_basic_app(api=None):
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
    with open(f"{project}/dev.py", "w") as config:
        config.write(configuration)
    with open(f"{project}/prod.py", "w") as config:
        config.write(configuration)
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
    return True


def build_standard_app(project='project', with_blueprint=False, blueprint_name='my_blueprint'):
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
    with open(f"{project}/dev.py", "w") as config:
        config.write(configuration)
    with open(f"{project}/prod.py", "w") as config:
        config.write(configuration)
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
    return True