import datetime
import subprocess
import json

def do_add_log(type, data):
    # create a datetime string
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")

    data['timestamp'] = date

    logs = read_logs()

    logs[type].append(data)

    write_logs(logs)

def read_logs():
    try:
        with open(".fs", "r", encoding='utf-8') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        raise Exception('.fs file is missing or damaged.')

def write_logs(content):
    try:
        with open(".fs", "w", encoding='utf-8') as file:
            # add the log to the end of the file
            json.dump(content, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        raise Exception('.fs file is missing or damaged.')

def write_log_file(project, name, email):
    try:
        content = {
        "project":project,
        "author":name,
        "email":email,
        "config":{},
        "packages":[],
        "modules":[]
        }

        with open(".fs", "w", encoding='utf-8') as file:
            # add the log to the end of the file
            json.dump(content, file, ensure_ascii=False, indent=4)
    except Exception as e:
        raise Exception('.fs file is missing or damaged.')

def write_config(python_version, pip_version, fs_version):
    config = {
        "environment":"venv",
        "python":python_version,
        "pip":pip_version,
        "fs":fs_version,
        "port":5000
        }
    
    logs = read_logs()

    logs['config'] = config

    write_logs(logs)