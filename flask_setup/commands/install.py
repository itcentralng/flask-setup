import os
import typer
from flask_setup.methods import do_add_log, do_freeze

def run_install_command(package):
    """
    Install packages
    """
    if package == 'all':
        os.system('pip install -r requirements.txt')
        log = 'All packages installed successfully'
    else:
        os.system(f'pip install {package}')
        log = f'{package} installed successfully'
    do_freeze()
    typer.echo(log)
    do_add_log(log)