import datetime
import subprocess

def do_freeze():
    #send a pip freeze command to shell and hold returned value
    req = subprocess.check_output(["pip", "freeze"])
    with open("requirements.txt", "w") as _app:
        req = req.decode("utf-8") #convert returned byte value to string
        _app.write(req)
    return True


def do_add_log(log):
    try:
        with open(".fs", "r") as file:
            # create a datetime string
            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d %H:%M:%S")
            oldcontent = file.read()
        with open(".fs", "w") as newcontent:
            # add the log to the end of the file
            newcontent.write(f"{oldcontent}\n{date}: {log}")
    except FileNotFoundError:
        with open(".fs", "w") as content:
            # create a datetime string
            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d %H:%M:%S")
            # add the log to the file
            content.write(f"FLASK SETUP LOG\n{date}: {log}")