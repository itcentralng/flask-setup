from random import randint
import os


def run_start_command():
    """
    Start the project
    """
    is_not_running = True
    port = 5000
    while is_not_running:
        try:
            is_not_running = False
            os.system('export FLASK_APP=main && export FLASK_DEBUG=True && flask run -p ' + str(port))
        except:
            is_not_running = True
            port = randint(4999, 6000)