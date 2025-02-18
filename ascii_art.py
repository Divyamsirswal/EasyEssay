# ascii_art.py

import time
from rich.console import Console

console = Console()

try:
    import pyfiglet
    PYFIGLET_AVAILABLE = True
except ImportError:
    PYFIGLET_AVAILABLE = False

def ascii_logo():
    """
    Displays a small ASCII logo using PyFiglet (if installed),
    printing each line in bold cyan WITHOUT bracket markup.
    """
    if PYFIGLET_AVAILABLE:
        ascii_text = pyfiglet.figlet_format("Easy Essay", font="small").rstrip()
        for line in ascii_text.split("\n"):
            console.print(line, style="bold cyan", markup=False)
            time.sleep(0.02)
    else:
        console.print("Easy Essay", style="bold cyan", markup=False)
