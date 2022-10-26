import os
import typer
from flask_setup.methods import do_add_log
from shutil import copytree

def run_build_command(project, path):
    if os.path.exists(project):
            typer.echo("Project already exists")
            return
        
    # Create project folder
    os.mkdir(project)
    # move to project folder
    os.chdir(project)
    do_add_log("Project folder created")

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

    # install requirements into the virtual environment
    os.system('venv/bin/pip install -r requirements.txt') if os.name == 'posix' else os.system('venv\Scripts\pip install -r requirements.txt')

    log = 'Project built successfully'
    do_add_log(log)
    typer.echo(log)