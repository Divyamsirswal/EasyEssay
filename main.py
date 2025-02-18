
import sys
import time
from cli_utils import clear_screen, typed_out_print
from ascii_art import ascii_logo
from menus import main_menu, advanced_settings_menu
from setting import ADVANCED_SETTINGS
from generation import generate_and_display, compare_two_essays
from cli_utils import typed_out_print

def run_advanced_settings():
    clear_screen()
    ascii_logo()
    typed_out_print("Advanced Settings\n", 0.002)
    advanced_settings_menu()
    typed_out_print("Settings updated!", 0.01, style="green")
    typed_out_print("Press Enter to continue...")
    input()

def run_single_essay():
    from menus import QUESTIONARY_STYLE
    import questionary

    clear_screen()
    ascii_logo()
    typed_out_print("Generate Single Essay\n", 0.002)

    topic = questionary.text(
        "Topic:",
        default="Artificial Intelligence",
        style=QUESTIONARY_STYLE
    ).ask()
    word_input = questionary.text(
        "Word Limit:",
        default="500",
        style=QUESTIONARY_STYLE
    ).ask()
    try:
        word_limit = int(word_input)
    except ValueError:
        typed_out_print("Invalid limit, using 500.", 0.01, style="yellow")
        word_limit = 500

    generate_and_display(topic, word_limit)
    typed_out_print("Press Enter to return to menu...")
    input()

def run_batch_essays():
    from menus import QUESTIONARY_STYLE
    import questionary

    clear_screen()
    ascii_logo()
    typed_out_print("Batch Essay Generation\n", 0.002)

    typed_out_print("Enter multiple topics, comma-separated.\n", 0.003)
    topics_raw = questionary.text("Topics:", style=QUESTIONARY_STYLE).ask().strip()
    if not topics_raw:
        typed_out_print("No topics given, returning...", 0.01, style="yellow")
        time.sleep(1)
        return

    word_input = questionary.text("Word Limit:", default="500", style=QUESTIONARY_STYLE).ask()
    try:
        word_limit = int(word_input)
    except ValueError:
        typed_out_print("Invalid. Using 500.", 0.01, style="yellow")
        word_limit = 500

    topics = [t.strip() for t in topics_raw.split(",") if t.strip()]
    typed_out_print(f"Generating essays for {len(topics)} topics...\n", 0.005)

    for i, topic in enumerate(topics, start=1):
        typed_out_print(f"({i}/{len(topics)}) Topic: {topic}", 0.01, style="dim")
        generate_and_display(topic, word_limit)

    typed_out_print("All done. Press Enter to continue.", 0.002)
    input()

def run_compare_essays():
    from menus import QUESTIONARY_STYLE
    import questionary

    clear_screen()
    ascii_logo()
    typed_out_print("Compare Two Essays\n", 0.002)

    typed_out_print("Pick how to get the two essays:\n", 0.003)
    method = questionary.select(
        "Method:",
        choices=["Generate Both Now", "Paste Two Essays"],
        style=QUESTIONARY_STYLE
    ).ask()

    if method == "Generate Both Now":
        typed_out_print("Essay #1", 0.003)
        topic1 = questionary.text("Topic #1:", default="AI", style=QUESTIONARY_STYLE).ask()
        wl1_str = questionary.text("Word limit #1:", default="200", style=QUESTIONARY_STYLE).ask()
        try:
            wl1 = int(wl1_str)
        except ValueError:
            wl1 = 200
        e1 = generate_and_display(topic1, wl1)

        typed_out_print("Essay #2", 0.003)
        topic2 = questionary.text("Topic #2:", default="Blockchain", style=QUESTIONARY_STYLE).ask()
        wl2_str = questionary.text("Word limit #2:", default="200", style=QUESTIONARY_STYLE).ask()
        try:
            wl2 = int(wl2_str)
        except ValueError:
            wl2 = 200
        e2 = generate_and_display(topic2, wl2)

        if e1 and e2:
            typed_out_print("Side-by-Side Comparison:\n", 0.002)
            from generation import compare_two_essays
            compare_two_essays(e1, e2)
            typed_out_print("Press Enter to return...", 0.002)
            input()

    else:
        typed_out_print("Paste your essays below.\n", 0.003)
        e1 = questionary.text("Essay #1:", style=QUESTIONARY_STYLE).ask()
        e2 = questionary.text("Essay #2:", style=QUESTIONARY_STYLE).ask()
        typed_out_print("Side-by-Side Comparison:\n", 0.002)
        from generation import compare_two_essays
        compare_two_essays(e1, e2)
        typed_out_print("Press Enter to return...", 0.002)
        input()

def main():
    while True:
        clear_screen()
        ascii_logo()
        choice = main_menu()
        if choice == "Exit":
            typed_out_print("Goodbye!", 0.005, style="magenta")
            sys.exit(0)
        elif choice == "Advanced Settings":
            run_advanced_settings()
        elif choice == "Generate Single Essay":
            run_single_essay()
        elif choice == "Generate Multiple Essays (Batch)":
            run_batch_essays()
        elif choice == "Compare Two Essays":
            run_compare_essays()

if __name__ == "__main__":
    try:
        if not ADVANCED_SETTINGS or "style" not in ADVANCED_SETTINGS:
            # In case user has some custom config logic
            ADVANCED_SETTINGS["style"] = "Formal"
        main()
    except KeyboardInterrupt:
        typed_out_print("\nKeyboard Interrupt. Exiting gracefully...", 0.005, style="red")
        sys.exit(0)
