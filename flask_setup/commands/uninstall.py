import subprocess
import typer

from flask_setup.commands.install import get_installed_packages
from flask_setup.methods import read_logs, write_logs
from rich.progress import track

def run_uninstall_command(package):
    if package == 'all' or package == None:
        typer.echo("Are you sure you want to uninstall all packages?")
        if typer.confirm('y/n'):
            try:
                installed_packages = get_installed_packages()
                for package, _ in track(installed_packages, description="Uninstalling packages..."):
                    if package != 'flask-setup':
                        run_uninstall_command(package)
            except Exception as e:
                typer.echo(f'An error occurred: {e}')
    else:
        try:
            subprocess.run(['pip', 'uninstall', '-y', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            do_post_uninstall_logs(package)
        except Exception as e:
            typer.echo(f'An error occurred: {e}')

def do_post_uninstall_logs(package):
    logs = read_logs()
    for index, item in enumerate(logs['packages']):
        if item['name'].lower() == package.lower():
            logs['packages'].pop(index)
            write_logs(logs)
            break