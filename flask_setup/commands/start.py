import os

from flask_setup.methods import read_logs


def run_start_command():
    """
    Start the project
    """
    port = read_logs()['config']['port']
    os.system('flask --app main --debug run -p ' + str(port))