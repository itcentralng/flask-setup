import os
import typer

def run_destroy_command():
    typer.echo('Are you sure you want to destroy this project?')
    if typer.confirm('y/n'):
        typer.echo('Destroying project...')
        os.system('rm -rf *')
        typer.echo('Project destroyed successfully')