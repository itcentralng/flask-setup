#!/usr/bin/env python
import os
from flask_setup.commands.add import run_add_command
from flask_setup.commands.build import run_build_command
from flask_setup.commands.copy import run_copy_command
from flask_setup.commands.destroy import run_destroy_command
from flask_setup.commands.install import run_install_command
from flask_setup.commands.remove import run_remove_command
from flask_setup.commands.start import run_start_command
from flask_setup.commands.uninstall import run_uninstall_command
import typer

from flask_setup.decorators import before_command, new_project_command
from flask_setup.methods import do_add_log

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
    path = os.path.dirname(os.path.realpath(__file__))
    return run_build_command(project, path)
    

@app.command()
@before_command
def destroy():
    return run_destroy_command()

@app.command()
@before_command
def install(package):
    return run_install_command(package)

@app.command()
@before_command
def uninstall(package: str):
    return run_uninstall_command(package)

@app.command()
@before_command
def add(name: str, *args):
    name = name.lower()
    existing_blueprint = os.path.isdir(f'app/{name}')
    path = os.path.dirname(os.path.realpath(__file__))
    return run_add_command(path, name, existing_blueprint, *args)

@app.command()
@before_command
def remove(name: str):
    """
    The remove command removes a blueprint from the project:
        it requires the name of the blueprint to be removed
    """
    name = name.lower()
    existing_blueprint = os.path.isdir(f'app/{name}')
    return run_remove_command(name, existing_blueprint)

@app.command()
@before_command
def copy(blueprint_to_copy: str, new_blueprint_name: str):
    """
    The copy command copies a blueprint from the project:
        it requires the name of the blueprint to be copied and the new name of the blueprint
    """
    blueprint_to_copy = blueprint_to_copy.lower()
    new_blueprint_name = new_blueprint_name.lower()
    existing_blueprint = os.path.isdir(f'app/{blueprint_to_copy}')
    return run_copy_command(blueprint_to_copy, new_blueprint_name, existing_blueprint)

@app.command()
@before_command
def start():
    return run_start_command()



def run():
    app()