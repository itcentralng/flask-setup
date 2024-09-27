import os

from flask_setup.methods import read_logs


def run_start_command():
    """
    Start the project
    """
    port = read_logs()['config']['port']
    entry = read_logs()['config']['entry-point']
    os.system(f'flask --app {entry} --debug run -p ' + str(port))