from random import randint
import os


def run_start_command():
    """
    Start the project
    """
    port = randint(4999, 6000)
    os.system('flask --app main --debug run -p ' + str(port))