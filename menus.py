# menus.py

import questionary
from questionary import Style
from cli_utils import typed_out_print
from setting import ADVANCED_SETTINGS
import sys, time

QUESTIONARY_STYLE = Style([
    ("qmark", "fg:#E91E63 bold"),
    ("question", "fg:#673AB7 bold"),
    ("answer", "fg:#2196f3 bold"),
    ("pointer", "fg:#00BCD4 bold"),
    ("highlighted", "fg:#FF5722 bold"),
    ("selected", ""),
    ("separator", "fg:#cc5454"),
    ("instruction", "fg:#9E9E9E italic"),
    ("text", ""),
    ("disabled", "fg:#858585 italic")
])

def main_menu() -> str:
    typed_out_print("Use arrow keys and Enter to select an action.\n", 0.002)
    return questionary.select(
        "Main Menu:",
        choices=[
            "Generate Single Essay",
            "Generate Multiple Essays (Batch)",
            "Compare Two Essays",
            "Advanced Settings",
            "Exit"
        ],
        style=QUESTIONARY_STYLE
    ).ask()

def advanced_settings_menu():
    ADVANCED_SETTINGS["style"] = questionary.select(
        "Select a writing style:",
        choices=["Formal", "Creative", "Casual"],
        style=QUESTIONARY_STYLE
    ).ask()

    ADVANCED_SETTINGS["language"] = questionary.select(
        "Select a language:",
        choices=["English", "Spanish", "French", "German"],
        style=QUESTIONARY_STYLE
    ).ask()

    ADVANCED_SETTINGS["audience"] = questionary.select(
        "Select an audience:",
        choices=["Academic", "Business", "General"],
        style=QUESTIONARY_STYLE
    ).ask()

    auto_save_choice = questionary.select(
        "Enable auto-save?",
        choices=["Yes", "No"],
        style=QUESTIONARY_STYLE
    ).ask()
    ADVANCED_SETTINGS["auto_save"] = (auto_save_choice == "Yes")

    ADVANCED_SETTINGS["export_format"] = questionary.select(
        "Select export format:",
        choices=["txt", "pdf"],
        style=QUESTIONARY_STYLE
    ).ask()

    outline_choice = questionary.select(
        "Generate outline after essay?",
        choices=["Yes", "No"],
        style=QUESTIONARY_STYLE
    ).ask()
    ADVANCED_SETTINGS["outline_requested"] = (outline_choice == "Yes")

    summary_choice = questionary.select(
        "Generate summary after essay?",
        choices=["Yes", "No"],
        style=QUESTIONARY_STYLE
    ).ask()
    ADVANCED_SETTINGS["summary_requested"] = (summary_choice == "Yes")

    plag_choice = questionary.select(
        "Run a plagiarism check? (Placeholder)",
        choices=["Yes", "No"],
        style=QUESTIONARY_STYLE
    ).ask()
    ADVANCED_SETTINGS["plagiarism_check"] = (plag_choice == "Yes")
