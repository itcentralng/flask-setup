import os
import platform
import subprocess
import typer
from flask_setup.methods import do_add_log, do_freeze, read_logs, write_config

LOG_TYPE = 'packages'

PIP = 'venv/bin/pip' if os.name == 'posix' else 'venv\Scripts\pip'

def run_install_command(packages: list[str]):
    """
    Install packages
    """
    if packages == 'all':
        install_all()
    else:
        for package_name in packages:
            # Install the package
            install_package(package_name)

            do_post_install_logs(package_name)

def install_all():
    logs = read_logs()
    packages = " ".join([f"{package['name']}=={package['version']}" for package in logs['packages']])
    install_package(packages)

def install_defaults():
    packages = [
        "flask-setup==0.6.1",
        "Flask-JWT-Extended==4.6.0",
        "bcrypt==4.2.0",
        "Flask==3.0.3",
        "Flask-Cors==4.0.1",
        "celery==5.4.0",
        "marshmallow==3.21.3",
        "marshmallow-sqlalchemy==1.0.0",
        "Flask-Migrate==4.0.7",
        "Flask-SQLAlchemy==3.1.1",
        "gunicorn==22.0.0",
        "psycopg2-binary==2.9.9",
        "python-dotenv==1.0.1",
        "redis==5.0.8",
        "boto3==1.34.151",
        "requests==2.32.3",
        ]
    run_install_command(packages)

    set_configs()

def install_package(package):
    subprocess.run([PIP, 'install', package])

def show_package(package):
    result = subprocess.run([PIP, 'show', package], stdout=subprocess.PIPE, text=True)
    # Get the installed package version
    output = result.stdout
    version = None
    
    # Parse the output to find the version and dependencies
    for line in output.split('\n'):
        if line.startswith('Version:'):
            version = line.split()[1]
        elif line.startswith('Requires:'):
            dependencies = line.split(': ')[1].split(', ') if line.split(': ')[1] else []
    return version, dependencies

def manage_dependencies():
    # Get the list of installed packages
    installed_packages = get_installed_packages()

    # Print the list of packages
    for package, _ in installed_packages:
        do_post_install_logs(package)
    
    set_configs()

def get_installed_packages():
    # Run `pip list` command
    result = subprocess.run(['pip', 'list', '--format=freeze'], stdout=subprocess.PIPE, text=True)
    
    # Capture the output
    output = result.stdout
    
    # Parse the output to extract package names and versions
    packages = []
    for line in output.splitlines():
        if '==' in line:
            package, version = line.split('==')
            packages.append((package, version))
    
    return packages

def do_post_install_logs(package_name):
    package_name = package_name.split('==')[0]
            
    version, dependencies = show_package(package_name)

    log = {
        "name":package_name.split('==')[0],
        "version":version,
        "dependencies":[
            {
                "name":dependency
            }
            for dependency in dependencies
        ],
        }
    do_add_log(LOG_TYPE, log)

def set_configs():
    python_version = platform.python_version()
    pip_version, _ = show_package('pip')
    fs_version, _ = show_package('flask-setup')

    write_config(python_version, pip_version, fs_version)