import os
import subprocess
from flask_setup.commands.add import do_post_add_logs
import typer
from flask_setup.commands.install import install_defaults, manage_dependencies
from flask_setup.methods import manage_modules, project_is_v6_down, write_log_file
from shutil import copytree
from rich.progress import track

def run_build_command(project, name, email, path):
    """
    Build a new project from scratch
    """
    if os.path.exists(project):
        typer.echo("Project already exists")
        return
    
    for _ in track(range(1), description="Creating project folder..."):
            
        # Create project folder
        os.mkdir(project)
        # move to project folder
        os.chdir(project)
        
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

    for _ in track(range(1), description="Upgrading pip..."):
        PIP = "venv/bin/pip" if os.name == 'posix' else  "venv\\Scripts\\pip"

        # upgrade pip
        subprocess.run([PIP, 'install', '--upgrade', 'pip'], stdout=subprocess.PIPE, text=True)

    write_log_file(project, name, email)

    install_defaults(PIP)

    default_module = {
         "name":"user",
         "fields":[
              "username:str",
              "password:str"
              ]
        }

    do_post_add_logs(default_module['name'], default_module["fields"])

    typer.echo('Project built successfully')

def run_init_command(project, name, email):
    """
    Initialize flask-setup in an existing project
    """

    write_log_file(project, name, email)

    manage_dependencies()

    typer.echo('fs initialized successfully')

def run_migrate_command():
    """
    Migrate an older flask-setup project to latest version
    """

    if project_is_v6_down():
        project = typer.prompt('Name of this project')
        author_name = typer.prompt('Your name')
        author_email = typer.prompt('Your email')
        write_log_file(project, author_name, author_email)

    manage_dependencies()

    manage_modules()

    typer.echo('Project migrated successfully')