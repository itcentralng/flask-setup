#!/usr/bin/env python
import os
from typing_extensions import Annotated
from flask_setup.commands.add import run_add_command
from flask_setup.commands.build import run_build_command, run_init_command
from flask_setup.commands.install import run_install_command
from flask_setup.commands.remove import run_remove_command
from flask_setup.commands.start import run_start_command
from flask_setup.commands.uninstall import run_uninstall_command

import typer
from typing import List

from flask_setup.decorators import before_command

app = typer.Typer()

@app.command()
def init(
    project: Annotated[str, typer.Argument(help="The name to give this project")] = None,
    author_name: Annotated[str, typer.Argument(help="Your name to associate with this project")] = None,
    author_email: Annotated[str, typer.Argument(help="Yout email to associate with this project")] = None,
):
    """
    run `fs init` => This create a .fs file in the current directory
    """
    project = project or typer.prompt('Name of this project')
    author_name = author_name or typer.prompt('Your name')
    author_email = author_email or typer.prompt('Your email')
    run_init_command(project, author_name, author_email)

@app.command()
def build(
    project: Annotated[str, typer.Argument(help="The name to give this project")] = None,
    author_name: Annotated[str, typer.Argument(help="Your name to associate with this project")] = None,
    author_email: Annotated[str, typer.Argument(help="Yout email to associate with this project")] = None,
):
    """
    run `fs build project` => This create a new directory `project` and build your app in it.
    """
    path = os.path.dirname(os.path.realpath(__file__))
    project = project or typer.prompt('Name of this project')
    author_name = author_name or typer.prompt('Your name')
    author_email = author_email or typer.prompt('Your email')
    return run_build_command(project, author_name, author_email, path)
    

@app.command()
@before_command
def install(packages: Annotated[List[str], typer.Argument(help="space separated packages or 'all' e.g. fs install 'flask arrow'")] = None):
    """
    run `fs install package` => This uses pip in the background to install `package`. Packages can be passed as space separated.
    """
    return run_install_command(packages)

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
def start():
    """
    run `fs start` => This runs the project.
    """
    return run_start_command()



def run():
    app()