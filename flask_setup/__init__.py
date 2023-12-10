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
from typing import List

from flask_setup.decorators import before_command, new_project_command
from flask_setup.methods import do_add_log

app = typer.Typer()

@app.command()
@new_project_command
def init():
    """
    run `fs init` => This create a .fs file in the current directory
    """
    do_add_log(".fs file created")

@app.command()
@new_project_command
def build(project: str):
    """
    run `fs build project` => This create a new directory `project` and build your app in it.
    """
    path = os.path.dirname(os.path.realpath(__file__))
    return run_build_command(project, path)
    

@app.command()
@before_command
def destroy():
    """
    run `fs destroy` => This remove all files and folders from the current project.
    """
    return run_destroy_command()

@app.command()
@before_command
def install(package):
    """
    run `fs install package` => This uses pip in the backgroun to install and freeze `package`
    """
    return run_install_command(package)

@app.command()
@before_command
def uninstall(package: str):
    """
    run `fs uninstall package` => This uses pip in the background to uninstall and freeze `package`.
    """
    return run_uninstall_command(package)

@app.command()
@before_command
def add(name: str, fields: List[str]):
    """
    run `fs add module ...fields` => This create a new module with the defined fields. 

    e.g. fs add game name description => This then creates a new module in your app with
    model that contains the defined fields `name` and `description`.
    """
    name = name.lower()
    existing_blueprint = os.path.isdir(f'app/{name}')
    path = os.path.dirname(os.path.realpath(__file__))
    return run_add_command(path, name, existing_blueprint, fields)

@app.command()
@before_command
def remove(name: str):
    """
    run `fs remove module` => The remove command removes a module from the project:
    """
    name = name.lower()
    existing_blueprint = os.path.isdir(f'app/{name}')
    return run_remove_command(name, existing_blueprint)

@app.command()
@before_command
def copy(blueprint_to_copy: str, new_blueprint_name: str):
    """
    run `fs copy existing new` => The copy command copies a blueprint from the project:
        it requires the name of the blueprint to be copied and the new name of the blueprint
    """
    blueprint_to_copy = blueprint_to_copy.lower()
    new_blueprint_name = new_blueprint_name.lower()
    existing_blueprint = os.path.isdir(f'app/{blueprint_to_copy}')
    return run_copy_command(blueprint_to_copy, new_blueprint_name, existing_blueprint)

@app.command()
@before_command
def start():
    """
    run `fs start` => This runs the project.
    """
    return run_start_command()



def run():
    app()