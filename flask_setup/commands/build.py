import os
from flask_setup.commands.add import do_post_add_logs
import typer
from flask_setup.commands.install import install_defaults, manage_dependencies
from flask_setup.methods import do_add_log, write_config, write_log_file
from shutil import copytree

def run_build_command(project, name, email, path):
    """
    Build a new project from scratch
    """
    if os.path.exists(project):
            typer.echo("Project already exists")
            return
        
    # Create project folder
    os.mkdir(project)
    # move to project folder
    os.chdir(project)
    # do_add_log("Project folder created")

    # copy relevant app files to project directory
    copytree(f'{path}/starter', '.', dirs_exist_ok=True)
    
    # rename __project__ in app/main.py
    with open("main.py", "r") as main_app:
        content = main_app.read()
        content = content.replace("__project__", project)
        with open("main.py", "w") as main_app:
            main_app.write(content)
    # create virtual environment
    os.system('python3 -m venv venv') if os.name == 'posix' else os.system('py -m venv venv')

    # upgrade pip
    os.system('venv/bin/pip install --upgrade pip') if os.name == 'posix' else os.system('venv\\Scripts\\pip install --upgrade pip')

    write_log_file(project, name, email)

    install_defaults()

    default_module = {
         "name":"user",
         "fields":[
              "username:str",
              "password:str"
              ]
        }

    do_post_add_logs(default_module['name'], default_module["fields"])

    typer.echo('Project built successfully')

def run_init_command(project, name, email):
    """
    Initialize flask-setup in an existing project
    """

    write_log_file(project, name, email)

    manage_dependencies()

    typer.echo('fs initialized successfully')