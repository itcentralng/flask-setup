import os
import typer
from shutil import copytree
from flask_setup.methods import do_add_log


def run_copy_command(blueprint_to_copy, new_blueprint_name, existing_blueprint):
    # check if a folder with the name exists
    log = f'Blueprint {blueprint_to_copy} does not exist'
    if existing_blueprint:
        log = ''
        typer.echo("Are you sure you want to copy this blueprint?")
        if typer.confirm('y/n'):
            # copy the blueprint
            copytree(f'app/{blueprint_to_copy}', f'app/{new_blueprint_name}', dirs_exist_ok=True)
            # rename the blueprint
            with open(f'app/{new_blueprint_name}/controller.py', 'r') as f:
                content = f.read()
            content = content.replace(f'__blueprint__ = "{blueprint_to_copy}"', f'__blueprint__ = "{new_blueprint_name}"')
            with open(f'app/{new_blueprint_name}/controller.py', 'w') as f:
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
                    content = content[:next_line] + f"\nfrom app.{new_blueprint_name}.controller import bp as {new_blueprint_name}_bp\napp.register_blueprint({new_blueprint_name}_bp)" + content[next_line:]
                elif "Register controllers" in content:
                    # find the last blueprint
                    last_blueprint = content.rfind("Register controllers")
                    # find the immediate line after the last blueprint
                    next_line = content.find("\n", last_blueprint)
                    # add the new blueprint after the last blueprint
                    content = content[:next_line] + f"\nfrom app.{new_blueprint_name}.controller import bp as {new_blueprint_name}_bp\napp.register_blueprint({new_blueprint_name}_bp)" + content[next_line:]
                else:
                    # add the new blueprint
                    content = content.replace("migrate = Migrate(app, db)", f"migrate = Migrate(app, db)\n\n\nfrom app.{new_blueprint_name}.controller import bp as {new_blueprint_name}_bp\napp.register_blueprint({new_blueprint_name}_bp)\n")
                with open(f"app/__init__.py", "w") as main_app:
                    main_app.write(content)
                # Read the content of the controller file and replace the blueprint name
                with open(f'app/{new_blueprint_name}/controller.py', 'r') as f:
                    content = f.read()
                content = content.replace(blueprint_to_copy, new_blueprint_name)
                content = content.replace(blueprint_to_copy.title(), new_blueprint_name.title())
                content = content.replace(blueprint_to_copy.upper(), new_blueprint_name.upper())
                with open(f'app/{new_blueprint_name}/controller.py', 'w') as f:
                    f.write(content)
                # Read the content of the model file and replace the blueprint name
                with open(f'app/{new_blueprint_name}/model.py', 'r') as f:
                    content = f.read()
                content = content.replace(blueprint_to_copy, new_blueprint_name)
                content = content.replace(blueprint_to_copy.title(), new_blueprint_name.title())
                content = content.replace(blueprint_to_copy.upper(), new_blueprint_name.upper())
                with open(f'app/{new_blueprint_name}/model.py', 'w') as f:
                    f.write(content)
                # Read the content of the schema file and replace the blueprint name
                with open(f'app/{new_blueprint_name}/schema.py', 'r') as f:
                    content = f.read()
                content = content.replace(blueprint_to_copy, new_blueprint_name)
                content = content.replace(blueprint_to_copy.title(), new_blueprint_name.title())
                content = content.replace(blueprint_to_copy.upper(), new_blueprint_name.upper())
                with open(f'app/{new_blueprint_name}/schema.py', 'w') as f:
                    f.write(content)
            log = f'Blueprint {blueprint_to_copy} copied successfully'
            do_add_log(log)
    typer.echo(log)