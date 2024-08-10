import os
import typer

from flask_setup.methods import read_logs, write_logs

def run_remove_command(name, existing_blueprint):
    """
    Remove existing module(blueprint) from the project
    """
    # check if a folder with the name exists
    if existing_blueprint:
        typer.echo(f"Are you sure you want to remove this blueprint ({name})?")
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
            do_post_remove_logs(name)
            typer.echo(f'Blueprint {name} removed successfully')
    else:
        typer.echo(f'Blueprint {name} does not exist')

def do_post_remove_logs(module):
    logs = read_logs()
    for index, item in enumerate(logs['modules']):
        if item['name'].lower() == module.lower():
            logs['modules'].pop(index)
            write_logs(logs)
            break