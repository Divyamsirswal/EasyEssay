# generation.py

from typing import Optional
from rich.table import Table
from rich.console import Console
from cohere_api import (
    cohere_generate_essay,
    generate_outline,
    generate_summary,
    run_plagiarism_check
)
from cli_utils import typed_out_print
from setting import ADVANCED_SETTINGS
from menus import QUESTIONARY_STYLE
import questionary

from fpdf import FPDF

console = Console()

def save_txt(topic: str, content: str) -> str:
    from datetime import datetime
    filename = f"essay_{topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def save_pdf(topic: str, content: str) -> str:
    from datetime import datetime
    filename = f"essay_{topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)
    pdf.output(filename)
    return filename

def compare_two_essays(essay1: str, essay2: str):
    table = Table(box=None)
    table.add_column("Essay #1", style="cyan", overflow="fold")
    table.add_column("Essay #2", style="magenta", overflow="fold")
    short1 = essay1[:300] + ("..." if len(essay1) > 300 else "")
    short2 = essay2[:300] + ("..." if len(essay2) > 300 else "")
    table.add_row(short1, short2)
    console.print(table)

def generate_and_display(topic: str, word_limit: int) -> Optional[str]:
    style = ADVANCED_SETTINGS["style"]
    language = ADVANCED_SETTINGS["language"]
    audience = ADVANCED_SETTINGS["audience"]

    essay = cohere_generate_essay(topic, word_limit, style, language, audience)
    if not essay:
        typed_out_print("No essay returned or generation failed.", 0.01, style="yellow")
        return None

    # Show in a minimal table
    table = Table(box=None)
    table.add_column("Topic", style="cyan", justify="center")
    table.add_column("Essay", style="white", overflow="fold")
    table.add_row(topic, essay)
    console.print(table)
    console.print()

    if ADVANCED_SETTINGS["outline_requested"]:
        outline = generate_outline(essay)
        if outline:
            typed_out_print("Outline:\n", 0.002)
            console.print(outline + "\n")

    if ADVANCED_SETTINGS["summary_requested"]:
        summary = generate_summary(essay)
        if summary:
            typed_out_print("Summary:\n", 0.002)
            console.print(summary + "\n")

    if ADVANCED_SETTINGS["plagiarism_check"]:
        run_plagiarism_check(essay)

    if ADVANCED_SETTINGS["auto_save"]:
        if ADVANCED_SETTINGS["export_format"] == "pdf":
            filename = save_pdf(topic, essay)
        else:
            filename = save_txt(topic, essay)
        typed_out_print(f"Auto-saved essay as {filename}\n", 0.01, style="green")
    else:
        save_choice = questionary.select(
            "💾 Do you want to save the essay?",
            choices=["Yes", "No"],
            style=QUESTIONARY_STYLE
        ).ask()
        if save_choice == "Yes":
            if ADVANCED_SETTINGS["export_format"] == "pdf":
                filename = save_pdf(topic, essay)
            else:
                filename = save_txt(topic, essay)
            typed_out_print(f"Essay saved as {filename}\n", 0.01, style="green")

    return essay
