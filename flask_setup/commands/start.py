import os
import socket
import typer
from rich.console import Console

from flask_setup.methods import read_logs


def is_port_in_use(port):
    """
    Check if a port is already in use
    
    Args:
        port: The port number to check
        
    Returns:
        bool: True if the port is in use, False otherwise
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
            return False
        except socket.error:
            return True


def run_start_command():
    """
    Start the project
    
    If the specified port is in use, increment it until we find an available one
    """
    console = Console()
    logs = read_logs()
    initial_port = logs['config']['port']
    port = initial_port
    entry = logs['config']['entry-point']
    
    # Find an available port
    while is_port_in_use(port):
        console.print(f"[yellow]Port {port} is already in use. Trying port {port + 1}...[/yellow]")
        port += 1
    
    if port != initial_port:
        console.print(f"[green]Found available port: {port}[/green]")
    
    console.print(f"[green]Starting server on port {port}...[/green]")
    os.system(f'flask --app {entry} --debug run -p {port}')