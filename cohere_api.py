# cohere_api.py

import cohere
import time
from typing import Optional
from config import COHERE_API_KEY
from cli_utils import typed_out_print, log_error
from rich.console import Console

console = Console()

def get_cohere_client() -> cohere.Client:
    return cohere.Client(COHERE_API_KEY)

def build_prompt(topic: str, word_limit: int, style: str, language: str, audience: str) -> str:
    return (
        f"Write a {word_limit}-word, {style.lower()} essay in {language} on the topic '{topic}', "
        f"tailored to a(n) {audience.lower()} audience. Make it professional, insightful, and well-structured.\n\n"
    )

def cohere_generate_essay(topic: str, word_limit: int, style: str, language: str, audience: str, max_retries=3) -> Optional[str]:
    co = get_cohere_client()
    max_tokens = word_limit * 4
    prompt = build_prompt(topic, word_limit, style, language, audience)

    for attempt in range(1, max_retries + 1):
        typed_out_print(f"Generating essay (Attempt {attempt}/{max_retries}) for '{topic}'...", 0.02, style="dim")
        try:
            resp = co.generate(
                model="command-xlarge-nightly",
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.7
            )
            if resp and resp.generations:
                typed_out_print("Essay generated successfully!\n", 0.02, style="green")
                return resp.generations[0].text
            else:
                console.print("No text returned by Cohere.", style="red")
                return None
        except Exception as e:
            log_error(str(e))
            if attempt == max_retries:
                return None
            typed_out_print("Retrying in 2 seconds...", 0.02, style="yellow")
            time.sleep(2)
    return None

def generate_outline(essay: str) -> Optional[str]:
    co = get_cohere_client()
    sub_prompt = f"Create a concise, bulleted outline:\n\n{essay}\n\nOutline:"
    try:
        resp = co.generate(
            model="command-xlarge-nightly",
            prompt=sub_prompt,
            max_tokens=200,
            temperature=0.5
        )
        if resp and resp.generations:
            return resp.generations[0].text.strip()
    except Exception as e:
        log_error(f"Outline error: {e}")
    return None

def generate_summary(essay: str) -> Optional[str]:
    co = get_cohere_client()
    sub_prompt = f"Summarize this essay in a few bullet points:\n\n{essay}\n\nSummary:"
    try:
        resp = co.generate(
            model="command-xlarge-nightly",
            prompt=sub_prompt,
            max_tokens=200,
            temperature=0.5
        )
        if resp and resp.generations:
            return resp.generations[0].text.strip()
    except Exception as e:
        log_error(f"Summary error: {e}")
    return None

def run_plagiarism_check(essay: str):
    typed_out_print("Running plagiarism check (placeholder)...", 0.03, style="yellow")
    time.sleep(1.5)
    typed_out_print("No significant matches found. (Placeholder only.)\n", 0.02, style="green")
