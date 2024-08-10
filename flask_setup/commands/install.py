import platform
import subprocess
from typing import List, Optional
from typing_extensions import Annotated
from flask_setup.methods import do_add_log, read_logs, write_config
from rich.progress import track

LOG_TYPE = 'packages'

def run_install_command(packages: Annotated[Optional[List[str]], None] = None, PIP='pip'):
    """
    Install packages
    """
    if packages == ["all"] or packages == None:
        install_all(PIP='pip')
    else:
        for package_name in track(packages, description="Installing packages..."):
            # Install the package
            install_package(package_name, PIP)

            do_post_install_logs(package_name, PIP)

def install_all(PIP='pip'):
    logs = read_logs()
    packages = [f"{package['name']}=={package['version']}" for package in logs['packages']]
    for package in track(packages, description="Installing packages..."):
        install_package(package, PIP)

def install_defaults(PIP):
    packages = [
        "flask-setup==0.6.1",
        "Flask==3.0.3",
        "Flask-Cors==4.0.1",
        "Flask-Migrate==4.0.7",
        "flask-marshmallow==1.2.1",
        "marshmallow-sqlalchemy==1.0.0",
        "Flask-SQLAlchemy==3.1.1",
        "bcrypt==4.2.0",
        "Flask-JWT-Extended==4.6.0",
        "celery==5.4.0",
        "gunicorn==22.0.0",
        "psycopg2-binary==2.9.9",
        "python-dotenv==1.0.1",
        "redis==5.0.8",
        "requests==2.32.3",
        ]
    run_install_command(packages, PIP)

    set_configs()

def install_package(package, PIP='pip'):
    subprocess.run([PIP, 'install', package], stdout=subprocess.PIPE, text=True)

def show_package(package, PIP='pip'):
    result = subprocess.run([PIP, 'show', package], stdout=subprocess.PIPE, text=True)
    # Get the installed package version
    output = result.stdout
    version = None
    dependencies = []
    
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

    for package, _ in track(installed_packages, description="Managing packages..."):
    # for package, _ in installed_packages:
        do_post_install_logs(package)
    
    set_configs()

def get_installed_packages(PIP='pip'):
    # Run `pip list` command
    result = subprocess.run([PIP, 'list', '--format=freeze'], stdout=subprocess.PIPE, text=True)
    
    # Capture the output
    output = result.stdout
    
    # Parse the output to extract package names and versions
    packages = []
    for line in output.splitlines():
        if '==' in line:
            package, version = line.split('==')
            packages.append((package, version))
    
    return packages

def do_post_install_logs(package_name, PIP='pip'):
    package_name = package_name.split('==')[0]
            
    version, dependencies = show_package(package_name, PIP)

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

def set_configs(PIP='pip'):
    python_version = platform.python_version()
    pip_version, _ = show_package('pip', PIP)
    fs_version, _ = show_package('flask-setup', PIP)

    write_config(python_version, pip_version, fs_version)