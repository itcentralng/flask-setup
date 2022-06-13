#!/usr/bin/env python
import os
from shutil import copytree
import typer

from flask_setup.decorators import before_command
from flask_setup.methods import do_add_log, do_freeze

app = typer.Typer()

@app.command()
def init():
    """
    Initialize .fs
    """
    if os.path.exists(".fs"):
        typer.echo("File .fs already exists")
        return
    do_add_log(".fs file created")

@app.command()
@before_command
def build():
    path = os.path.dirname(os.path.realpath(__file__))
    # copy relevant app files to project directory
    copytree(f'{path}/starter', '.', dirs_exist_ok=True)
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
def install(package: str):
    if package == 'all':
        os.system('pip install -r requirements.txt')
        log = 'All packages installed successfully'
    else:
        log = f'Package: {package} installed successfully'
        os.system(f'pip install {package}')
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