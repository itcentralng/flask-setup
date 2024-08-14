import datetime
import os
import re
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

def project_is_v6_down():
    try:
        with open('.fs', 'r') as file:
            data = file.read()
            json.loads(data)
        return False
    except (ValueError, json.JSONDecodeError):
        if os.path.exists('.fs'):
            os.system('rm .fs') if os.name == 'posix' else os.system('del .fs')
        return True

def manage_modules():
    LOG_TYPE = "modules"
    model_field_types = {
       "String":"str",
        "Integer":"int",
        "DateTime":"date",
        "Float":"float",
        "Boolean":"bool",
        "ForeignKey":"fk",
        "relationship":"rel",
    }
    modules = []
    app_dir = 'app'
    dirs = os.listdir(app_dir)
    for dir in dirs:
        if os.path.isdir(os.path.join(app_dir, dir)):
            files = os.listdir(os.path.join(app_dir, dir))
            for filename in files:
                if filename == 'model.py':
                    with open(os.path.join(app_dir, dir, filename), 'r') as file:
                        file_content = file.read()
                        class_name, fields_matches = get_class_name_and_fields_from_model_string(file_content)

                        if class_name and fields_matches:

                            modules.append(
                                {
                                    'name':class_name.lower(),
                                    'fields':[
                                        {
                                            "name":field[0].lower(),
                                            "type":model_field_types[extract_column_type(field[-1])]
                                        }
                                        for field in fields_matches if extract_column_type(field[-1]) in model_field_types
                                    ]
                                }
                            )
    for module in modules:
        do_add_log(LOG_TYPE, module)

def get_class_name_and_fields_from_model_string(model_string):
    # Regular expression to extract class name
    class_name_pattern = re.compile(r'class (\w+)\(db.Model\):')
    class_name_match = class_name_pattern.search(model_string)
    class_name = class_name_match.group(1) if class_name_match else None

    # Regular expression to extract field names and types
    fields_pattern = re.compile(r'(\w+)\s*=\s*db\.(Column|relationship)\(([^)]*)\)')
    fields_matches = fields_pattern.findall(model_string)

    return class_name, fields_matches

def extract_column_type(field_args):
    column_type_match = re.search(r'db\.(\w+)', field_args)
    if column_type_match:
        return column_type_match.group(1)
    return ''