import os
import typer

from flask_setup.methods import do_add_log, do_freeze, read_logs, write_logs

PIP = 'venv/bin/pip' if os.name == 'posix' else 'venv\Scripts\pip'

def run_uninstall_command(package):
    if package == 'all':
        os.system(f'{PIP} freeze --exclude-editable | xargs pip uninstall -y')
        logs = read_logs()
        logs = logs['packages'] = []
        write_logs(logs)
    else:
        os.system(f'{PIP} uninstall {package}')
        logs = read_logs()
        for index, item in enumerate(logs['packages']):
            if item['name'].lower() == package.lower():
                logs['packages'].pop(index)
                write_logs(logs)
                break