import os, typer

from functools import wraps

def before_command(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not os.path.isfile('.fs'):
            typer.echo('.fs file is missing and is required to run this command!')
            return
        return f(*args, **kwargs)
    return decorated