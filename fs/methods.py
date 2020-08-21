from fs.app_builder import build_basic_app, build_standard_app, build_api_app

from fs.config import args

import subprocess

def install(packages):
    for p in packages:
        print("\n new package: ", p)
        subprocess.check_call(["pip", "install", p])
    return True

def uninstall(packages):
    for p in packages:
        subprocess.check_call(["pip", "uninstall", "-y", p])
    return True

def freeze():
    #send a pip freeze command to shell and hold returned value
    req = subprocess.check_output(["pip", "freeze"])
    with open("requirements.txt", "w") as _app:
        req = req.decode("utf-8") #convert returned byte value to string
        _app.write(req)
    return True

def initialize_setup():
    project = args.init
    try:
        print(f"Initializing flask_setup in {project}")
        with open(".flask_setup", "w") as _app:
            _app.write(f"# Flask Setup Initialization File.\n# Please do not delete this file!\n# If necessary, add it to your .gitinore file to remove it from tracking.\n\nPROJECT: {project}")
        print("flask-setup is ready!")
        return True
    except Exception as e:
        print(e)
        return False

def get_project_name():
    project = None
    try:
        with open('.flask_setup', 'r') as _file:
            lines = _file.readlines()
            for line in lines:
                if line.startswith('PROJECT:'):
                    project = line.split(': ')[-1]
    except Exception:
        print('It seems you have not intialized flask-setup or you are working outside root of project folder.\nGo to project root and try again.')
    return project

def build_app(_type):
    allowed_apps = ['api', 'basic', 'standard']
    if _type in allowed_apps:
        if _type == 'basic':
            return build_basic_app()
        elif _type == 'standard':
            return build_standard_app()
        return build_basic_app(_type)
    return False