import subprocess
import sys
import json
from typing import List

from rich.table import Table
from rich.console import Console

console = Console()

def get_outdated_packages() -> List[dict]:
    """
    Retrieves a list of outdated packages using pip's JSON output format.
    
    Returns:
        A list of dictionaries, where each dictionary represents an outdated package.
        
    Raises:
        SystemExit: If pip command fails or is not found.
    """
    try:
        # Use pip's JSON format for reliable parsing
        command = [sys.executable, "-m", "pip", "list", "--outdated", "--format=json"]
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            console.print(f"[bold red]Error running pip:[/bold red]\n{stderr}")
            raise SystemExit(1)
        
        # If stdout is empty, no packages are outdated
        if not stdout.strip():
            return []
            
        # Pip's JSON output might be a single line or multiple lines of JSON objects
        return [json.loads(line) for line in stdout.strip().split('\n')]

    except FileNotFoundError:
        console.print("[bold red]Fatal Error:[/bold red] `pip` is not installed or not in your PATH.")
        raise SystemExit(1)
    except json.JSONDecodeError:
        console.print("[bold red]Fatal Error:[/bold red] Could not parse pip's output. Your pip version might be too old.")
        raise SystemExit(1)

def generate_packages_table(packages: List[dict], title: str) -> Table:
    """
    Generates a Rich Table to display package information.

    Args:
        packages: A list of package dictionaries.
        title: The title for the table.

    Returns:
        A Rich Table object ready for printing.
    """
    table = Table(
        title=title,
        caption=f"{len(packages)} packages selected",
        show_header=True,
        header_style="bold magenta",
    )
    table.add_column("Package Name", style="cyan", no_wrap=True)
    table.add_column("Current Version", style="yellow")
    table.add_column("Latest Version", style="green")

    for pkg in packages:
        table.add_row(pkg.get('name'), pkg.get('version'), pkg.get('latest_version'))
    return table