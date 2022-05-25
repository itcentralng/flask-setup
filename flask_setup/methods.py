import subprocess

from flask_setup.file_strings import help_string, app_run

def install(packages):
    for p in packages:
        print("\n new package: ", p)
        subprocess.check_call(["pip", "install", p])
    freeze()
    return True

def uninstall(packages):
    for p in packages:
        subprocess.check_call(["pip", "uninstall", "-y", p])
    freeze()
    return True

def freeze():
    #send a pip freeze command to shell and hold returned value
    req = subprocess.check_output(["pip", "freeze"])
    with open("requirements.txt", "w") as _app:
        req = req.decode("utf-8") #convert returned byte value to string
        _app.write(req)
    return True

def initialize_setup(project):
    invalids = "!@#$%^&*()+=~?><,./\|-){[}]("
    for i in invalids:
        project = project.replace(i, '_')
    try:
        print(f"Initializing Flask Setup in {project}")
        with open(".fs", "w") as _app:
            _app.write(f"# Flask Setup Initialization File.\n# Please do not delete this file!\n# If necessary, add it to your .gitinore file to remove it from tracking.\n\nPROJECT: {project}")
            gitignore()
        print(f"{project} is ready!")
        return True
    except Exception as e:
        print(e)
        return False

def gitignore():
    ignore_flask_setup = "\n#FLASK SETUP\n.fs"
    try:
        with open(".gitignore", "r+") as content:
            new_content = content.read()+ignore_flask_setup
            content.write(new_content)
    except Exception:
        with open(".gitignore", "w") as content:
            content.write(ignore_flask_setup)

def get_project_name():
    project = None
    try:
        with open('.fs', 'r') as _file:
            lines = _file.readlines()
            for line in lines:
                if line.startswith('PROJECT:'):
                    project = line.split(': ')[-1]
    except Exception:
        print('It seems you have not intialized flask-setup or you are working outside root of project folder.\nGo to project root and try again.\nHowever if you are working inside project folder, consider renaming your .flask_setup file to .fs')
    return project

def set_app_runner():
    project = get_project_name()
    with open("run.py", "w") as content:
        content.write(app_run.replace('**project', project))
    with open(".env", "w") as content:
        install(['python-dotenv'])
        content.write('config=config.dev')
    return True

def destroy_project():
    try:
        project = get_project_name()
        subprocess.check_call(["rm", "-r", project])
        subprocess.check_call(["rm", "-r", 'config'])
    except:
        pass
    return True


def helper():
    print(help_string)
    return True