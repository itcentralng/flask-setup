import os
import typer

from flask_setup.methods import do_add_log, do_freeze

def run_uninstall_command(package):
    if package == 'all':
        os.system('pip uninstall -r requirements.txt')
        log = 'All packages uninstalled successfully'
    else:
        log = f'Package: {package} uninstalled successfully'
        os.system(f'pip uninstall {package}')
    do_freeze()
    typer.echo(log)
    do_add_log(log)