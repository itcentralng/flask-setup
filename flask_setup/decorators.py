import os, typer

from functools import wraps

def before_command(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not os.environ.get('VIRTUAL_ENV'):
            typer.echo('Please run this command in a virtual environment')
        elif not os.path.isfile('.fs'):
            typer.echo('Project not initialized')
        return f(*args, **kwargs)
    return decorated