#!/usr/bin/env python
import os
from shutil import copytree
import typer

from flask_setup.decorators import before_command, new_project_command
from flask_setup.methods import do_add_log, do_freeze

app = typer.Typer()

@app.command()
@new_project_command
def init():
    """
    Initialize .fs
    """
    do_add_log(".fs file created")

@app.command()
@new_project_command
def build(project: str):

    if os.path.exists(project):
        typer.echo("Project already exists")
        return
    
    # Create project folder
    os.mkdir(project)
    # move to project folder
    os.chdir(project)
    do_add_log("Project folder created")

    path = os.path.dirname(os.path.realpath(__file__))
    # copy relevant app files to project directory
    copytree(f'{path}/starter', '.', dirs_exist_ok=True)
    
    # create virtual environment
    os.system('python3 -m venv venv') if os.name == 'posix' else os.system('py -m venv venv')

    # install requirements
    os.system(f'pip install -r requirements.txt')
    log = 'Project built successfully'
    do_add_log(log)
    typer.echo(log)

@app.command()
@before_command
def destroy():
    typer.echo('Are you sure you want to destroy this project?')
    if typer.confirm('y/n'):
        typer.echo('Destroying project...')
        os.system('rm -rf *')
        typer.echo('Project destroyed successfully')

@app.command()
@before_command
def install(*packages):
    """
    Install packages
    """
    if 'all' in packages:
        os.system('pip install -r requirements.txt')
        log = 'All packages installed successfully'
    else:
        os.system(f'pip install {" ".join(packages)}')
        log = f"Installed packages: {', '.join(packages)}"
    do_freeze()
    typer.echo(log)
    do_add_log(log)

@app.command()
@before_command
def uninstall(package: str):
    if package == 'all':
        os.system('pip uninstall -r requirements.txt')
        log = 'All packages uninstalled successfully'
    else:
        log = f'Package: {package} uninstalled successfully'
        os.system(f'pip uninstall {package}')
    do_freeze()
    typer.echo(log)
    do_add_log(log)

@app.command()
@before_command
def add(name: str):
    name = name.lower()
    # check if a folder with the name exists
    log = f'Blueprint {name} already exists'
    if not os.path.isdir(f'app/{name}'):
        path = os.path.dirname(os.path.realpath(__file__))
        copytree(f'{path}/generators/blueprint', f'app/{name}', dirs_exist_ok=True)
        # rename sample blueprint to name
        with open(f'app/{name}/controller.py', 'r') as f:
            content = f.read()
        content = content.replace('__blueprint__', name)
        with open(f'app/{name}/controller.py', 'w') as f:
            f.write(content)
        # register the blueprint to the app
        with open("app/__init__.py", "r") as main_app:
            # check if there is already a blueprint and add this after it
            content = main_app.read()
            # check if 'app.register_blueprint' is in content
            if "app.register_blueprint" in content:
                # find the last blueprint
                last_blueprint = content.rfind(".register_blueprint")
                # find the immediate line after the last blueprint
                next_line = content.find("\n", last_blueprint)
                # add the new blueprint after the last blueprint
                content = content[:next_line] + f"\nfrom app.{name}.controller import bp as {name}_bp\napp.register_blueprint({name}_bp)" + content[next_line:]
            elif "Register controllers" in content:
                # find the last blueprint
                last_blueprint = content.rfind("Register controllers")
                # find the immediate line after the last blueprint
                next_line = content.find("\n", last_blueprint)
                # add the new blueprint after the last blueprint
                content = content[:next_line] + f"\nfrom app.{name}.controller import bp as {name}_bp\napp.register_blueprint({name}_bp)" + content[next_line:]
            else:
                # add the new blueprint
                content = content.replace("migrate = Migrate(app, db)", f"migrate = Migrate(app, db)\n\n\nfrom app.{name}.controller import bp as {name}_bp\napp.register_blueprint({name}_bp)\n")
            with open(f"app/__init__.py", "w") as main_app:
                main_app.write(content)
        log = f'Blueprint {name} added successfully'
        do_add_log(log)
    typer.echo(log)

@app.command()
@before_command
def remove(name: str):
    name = name.lower()
    # check if a folder with the name exists
    log = f'Blueprint {name} does not exist'
    if os.path.isdir(f'app/{name}'):
        log = ''
        typer.echo("Are you sure you want to remove this blueprint?")
        if typer.confirm('y/n'):
                # remove the blueprint
            os.system(f'rm -rf app/{name}')
            # unregister the blueprint to the app
            with open("app/__init__.py", "r") as main_app:
                content = main_app.read()
                content = content.replace(f"\nfrom app.{name}.controller import bp as {name}_bp", "")
                content = content.replace(f"\napp.register_blueprint({name}_bp)", "")
            with open("app/__init__.py", "w") as main_app:
                main_app.write(content)
            log = f'Blueprint {name} removed successfully'
            do_add_log(log)
    typer.echo(log)

def run():
    app()