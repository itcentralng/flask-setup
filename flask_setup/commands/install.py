import platform
import subprocess
import sys
from typing import List, Optional, Tuple
from typing_extensions import Annotated
from flask_setup.methods import do_add_log, read_logs, write_config
from rich.progress import track
from rich import print as rich_print

LOG_TYPE = 'packages'

def run_install_command(packages: Annotated[Optional[List[str]], None] = None, PIP='pip'):
    """
    Install packages
    """
    if packages == ["all"] or packages == None:
        install_all(PIP='pip')
    else:
        for package_name in track(packages, description="Installing packages..."):
            # Check if version is specified, if not, install latest
            if '==' not in package_name:
                # Install the package (latest version)
                success, message = install_package(package_name, PIP)
            else:
                # Version is already specified, install as is
                success, message = install_package(package_name, PIP)
            
            # Only log successful installations
            if success:
                rich_print(f"[green]Successfully installed {package_name}[/green]")
                try:
                    # package_name could be without version, do_post_install_logs will get the version
                    do_post_install_logs(package_name, PIP)
                except Exception as e:
                    rich_print(f"[yellow]Warning: Could not log package information for {package_name}. Error: {e}[/yellow]")
            else:
                rich_print(f"[red]Failed to install {package_name}[/red]")

def install_all(PIP='pip'):
    logs = read_logs()
    packages = [f"{package['name']}=={package['version']}" for package in logs['packages']]
    for package in track(packages, description="Installing packages..."):
        success, message = install_package(package, PIP)
        if success:
            rich_print(f"[green]Successfully installed {package}[/green]")
            try:
                do_post_install_logs(package.split('==')[0], PIP)
            except Exception as e:
                rich_print(f"[yellow]Warning: Could not log package information for {package}. Error: {e}[/yellow]")
        else:
            rich_print(f"[red]Failed to install {package}[/red]")

def install_defaults(PIP):
    try:
        fs_version, _ = show_package('flask-setup')
        packages = [
            f"flask-setup=={fs_version}",
            "Flask==3.0.3",
            "Flask-Cors==4.0.1",
            "Flask-Migrate==4.0.7",
            "flask-marshmallow-1.3.0",
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
        failed_packages = []
        
        for package in track(packages, description="Installing default packages..."):
            success, message = install_package(package, PIP)
            
            if success:
                rich_print(f"[green]Successfully installed {package}[/green]")
                try:
                    do_post_install_logs(package.split('==')[0], PIP)
                except Exception as e:
                    rich_print(f"[yellow]Warning: Could not log package information for {package}. Error: {e}[/yellow]")
            else:
                failed_packages.append(package)
                rich_print(f"[red]Failed to install {package}[/red]")
        
        # Show summary of any failed packages
        if failed_packages:
            rich_print(f"[yellow]Warning: {len(failed_packages)} package(s) failed to install.[/yellow]")
            rich_print("[yellow]Failed packages: " + ", ".join(failed_packages) + "[/yellow]")
        
        set_configs()
    except Exception as e:
        rich_print(f"[red]Error during installation of default packages: {str(e)}[/red]")

def install_package(package, PIP='pip'):
    """
    Install a package and handle potential errors.
    
    Args:
        package: The package name (and optionally version) to install
        PIP: The pip command to use
        
    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        # Check if the package exists in PyPI
        package_name = package.split('==')[0]
        
        # Run pip install with capture_output to get both stdout and stderr
        process = subprocess.run(
            [PIP, 'install', package],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False  # Don't raise exception on error
        )
        
        # Check if installation was successful
        if process.returncode == 0:
            return True, f"Successfully installed {package}"
        else:
            # Check for common errors
            if "No matching distribution found" in process.stderr:
                rich_print(f"[red]Error: Package '{package}' not found. Check the package name or version.[/red]")
            elif "Could not find a version that satisfies the requirement" in process.stderr:
                rich_print(f"[red]Error: No compatible version found for '{package}'.[/red]")
            else:
                rich_print(f"[red]Error installing '{package}': {process.stderr}[/red]")
            
            return False, process.stderr
    except Exception as e:
        rich_print(f"[red]Error: {str(e)}[/red]")
        return False, str(e)

def show_package(package, PIP='pip'):
    result = subprocess.run([PIP, 'show', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Get the installed package version
    output = result.stdout
    error = result.stderr
    version = None
    dependencies = []
    
    # Check if the package information was successfully retrieved
    if result.returncode != 0:
        rich_print(f"[yellow]Warning: Cannot get information for package '{package}'. The package might be installed but pip can't find its metadata.[/yellow]")
        # Try to get version using pip list as a fallback
        list_result = subprocess.run([PIP, 'list'], stdout=subprocess.PIPE, text=True)
        if list_result.returncode == 0:
            for line in list_result.stdout.splitlines():
                parts = line.split()
                if len(parts) >= 2 and parts[0].lower() == package.lower():
                    version = parts[1]
                    break
        return version, dependencies
    
    # Parse the output to find the version and dependencies
    for line in output.split('\n'):
        if line.startswith('Version:'):
            version = line.split()[1]
        elif line.startswith('Requires:'):
            dependencies = line.split(': ')[1].split(', ') if len(line.split(': ')) > 1 and line.split(': ')[1] else []
    
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
    
    # If version is None, we could not get package info, so we skip logging
    if version is None:
        rich_print(f"[yellow]Warning: Could not log package information for '{package_name}' because version info is not available.[/yellow]")
        return
    
    # Get versions for all dependencies
    dependency_info = []
    for dependency in dependencies:
        if dependency:
            dep_name = dependency.split('[')[0]  # Handle extras like package[extra]
            dep_version, _ = show_package(dep_name, PIP)
            
            if dep_version:
                dependency_info.append({
                    "name": dep_name,
                    "version": dep_version
                })
            else:
                # If we can't get the version, just store the name
                dependency_info.append({
                    "name": dep_name
                })
    
    log = {
        "name": package_name,
        "version": version,
        "dependencies": dependency_info
    }
    
    do_add_log(LOG_TYPE, log)

def set_configs(PIP='pip'):
    python_version = platform.python_version()
    pip_version, _ = show_package('pip', PIP)
    fs_version, _ = show_package('flask-setup', PIP)

    # If versions couldn't be found, use default values
    if pip_version is None:
        pip_version = "unknown"
        rich_print(f"[yellow]Warning: Could not determine pip version.[/yellow]")
    
    if fs_version is None:
        fs_version = "unknown"
        rich_print(f"[yellow]Warning: Could not determine flask-setup version.[/yellow]")

    write_config(python_version, pip_version, fs_version)