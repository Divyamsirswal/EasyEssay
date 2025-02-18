# cli_utils.py

import sys
import os
import time
from rich.console import Console

console = Console()

def clear_screen():
    """Cross-platform screen clear."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def typed_out_print(text: str, delay: float = 0.01, style: str = None):
    """
    Prints text char-by-char with an optional Rich style,
    but no bracket markup in the text itself.
    """
    for char in text:
        console.print(char, end="", style=style, markup=False)
        sys.stdout.flush()
        time.sleep(delay)
    console.print()  # newline

def log_error(msg: str):
    console.print(f"ERROR: {msg}", style="bold red")
