import os, typer

from functools import wraps

def before_command(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not os.environ.get('VIRTUAL_ENV'):
            typer.echo('Please run this command in a virtual environment')
            return
        elif not os.path.isfile('.fs'):
            typer.echo('Project not initialized')
            return
        return f(*args, **kwargs)
    return decorated

def new_project_command(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if os.path.isfile('.fs'):
            typer.echo('Project already initialized')
            return
        return f(*args, **kwargs)
    return decorated