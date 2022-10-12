import os
import typer

from flask_setup.methods import do_add_log

def run_remove_command(name, existing_blueprint):
    # check if a folder with the name exists
    log = f'Blueprint {name} does not exist'
    if existing_blueprint:
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