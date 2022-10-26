import os
import typer
from shutil import copytree
from flask_setup.methods import do_add_log


def run_add_command(path, name, existing_blueprint):
    # check if a folder with the name exists
    log = f'Blueprint {name} already exists'
    if not existing_blueprint:
        copytree(f'{path}/generators/blueprint', f'app/{name}', dirs_exist_ok=True)
        # rename sample blueprint to name
        # IN CONTROLLER
        with open(f'app/{name}/controller.py', 'r') as f:
            content = f.read()
        content = content.replace('__blueprint__', name)
        with open(f'app/{name}/controller.py', 'w') as f:
            f.write(content)
        # IN MODEL
        with open(f'app/{name}/model.py', 'r') as f:
            content = f.read()
        content = content.replace('__blueprint__', name)
        with open(f'app/{name}/model.py', 'w') as f:
            f.write(content)
        # IN SCHEMA
        with open(f'app/{name}/schema.py', 'r') as f:
            content = f.read()
        content = content.replace('__blueprint__', name)
        with open(f'app/{name}/schema.py', 'w') as f:
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