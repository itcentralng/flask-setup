import os
import subprocess
import typer

from flask_setup.commands.install import get_installed_packages
from flask_setup.methods import do_add_log, do_freeze, read_logs, write_logs

PIP = 'venv/bin/pip' if os.name == 'posix' else 'venv\Scripts\pip'

def run_uninstall_command(package):
    if package == 'all':
        if input('Are you sure you want to uninstall all packages?\nY/n').lower().strip() == 'y':
            try:
                installed_packages = get_installed_packages()
                for package, _ in installed_packages:
                    if package != 'flask-setup':
                        run_uninstall_command(package)
            except Exception as e:
                print(f'An error occurred: {e}')
    else:
        try:
            result = subprocess.run([PIP, 'uninstall', '-y', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            logs = read_logs()
            for index, item in enumerate(logs['packages']):
                if item['name'].lower() == package.lower():
                    logs['packages'].pop(index)
                    write_logs(logs)
                    break
            if result.returncode == 0:
                print(f'{package} successfully uninstalled')
            else:
                print(f'Error uninstalling {package}: {result.stderr}')
        except Exception as e:
            print(f'An error occurred: {e}')