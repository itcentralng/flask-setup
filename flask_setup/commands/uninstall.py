import subprocess
import typer

from flask_setup.commands.install import get_installed_packages
from flask_setup.methods import read_logs, write_logs

def run_uninstall_command(package):
    if package == 'all':
        typer.echo("Are you sure you want to uninstall all packages?")
        if typer.confirm('y/n'):
            try:
                installed_packages = get_installed_packages()
                for package, _ in installed_packages:
                    if package != 'flask-setup':
                        run_uninstall_command(package)
            except Exception as e:
                typer.echo(f'An error occurred: {e}')
    else:
        try:
            result = subprocess.run(['pip', 'uninstall', '-y', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            do_post_uninstall_logs(package)
            if result.returncode == 0:
                typer.echo(f'{package} successfully uninstalled')
            else:
                typer.echo(f'Error uninstalling {package}: {result.stderr}')
        except Exception as e:
            typer.echo(f'An error occurred: {e}')

def do_post_uninstall_logs(package):
    logs = read_logs()
    for index, item in enumerate(logs['packages']):
        if item['name'].lower() == package.lower():
            logs['packages'].pop(index)
            write_logs(logs)
            break